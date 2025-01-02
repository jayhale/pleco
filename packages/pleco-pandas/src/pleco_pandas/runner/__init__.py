from inspect import isclass
from typing import Callable, Dict, Type, Union

from pandas import DataFrame

import pleco
from pleco import (
    Expectation,
    ExpectationNotSupportedByRunner,
    Result,
    Runner,
)

from .column_expectations import (
    expect_column_distinct_values_to_be_in_set,
    expect_column_distinct_values_to_contain_set,
    expect_column_distinct_values_to_equal_set,
    expect_column_max,
    expect_column_mean,
    expect_column_median,
    expect_column_min,
    expect_column_mode,
    expect_column_quantile,
    expect_column_values_to_be_unique,
    expect_column_values_to_not_be_null,
)
from .table_expectations import expect_table_column_count


class PandasRunnerBase(Runner):
    """Run expectations against a Pandas DataFrame"""

    _handler_registry: Dict[str, Callable[[Expectation, DataFrame], Result]] = {}

    def run_expectation(self, expectation: Expectation, data: DataFrame) -> Result:
        if expectation.__class__.__name__ not in self._handler_registry:
            raise ExpectationNotSupportedByRunner(
                f"expectation {type(expectation)} is not supported by PandasRunner"
            )

        handler = self._handler_registry[expectation.__class__.__name__]
        return handler(expectation, data)

    def supports(self, expectation: Union[Expectation, Type[Expectation]]) -> bool:
        if isclass(expectation):
            return expectation.__name__ in self._handler_registry
        return expectation.__class__.__name__ in self._handler_registry


class PandasRunnerBuilder:
    """Construct a PandasRunner from expectation handlers"""

    def __init__(self):
        self._handler_registry = {}

    def build(self) -> Type[Runner]:
        class C(PandasRunnerBase):
            _handler_registry = self._handler_registry

        return C

    def register(
        self,
        expectation_class: Type[Expectation],
        handler: Callable[[Expectation, DataFrame], Result],
    ):
        if expectation_class.__name__ in self._handler_registry:
            raise RuntimeError(
                f"expectation {expectation_class.__name__} already registered"
            )
        self._handler_registry[expectation_class.__name__] = handler


builder = PandasRunnerBuilder()
builder.register(
    pleco.ExpectColumnDistinctValuesToBeInSet,
    expect_column_distinct_values_to_be_in_set,
)
builder.register(
    pleco.ExpectColumnDistinctValuesToContainSet,
    expect_column_distinct_values_to_contain_set,
)
builder.register(
    pleco.ExpectColumnDistinctValuesToEqualSet,
    expect_column_distinct_values_to_equal_set,
)
builder.register(pleco.ExpectColumnMax, expect_column_max)
builder.register(pleco.ExpectColumnMean, expect_column_mean)
builder.register(pleco.ExpectColumnMedian, expect_column_median)
builder.register(pleco.ExpectColumnMin, expect_column_min)
builder.register(pleco.ExpectColumnMode, expect_column_mode)
builder.register(pleco.ExpectColumnQuantile, expect_column_quantile)
builder.register(pleco.ExpectColumnValuesToBeUnique, expect_column_values_to_be_unique)
builder.register(
    pleco.ExpectColumnValuesToNotBeNull, expect_column_values_to_not_be_null
)
builder.register(pleco.ExpectTableColumnCount, expect_table_column_count)
PandasRunner = builder.build()
