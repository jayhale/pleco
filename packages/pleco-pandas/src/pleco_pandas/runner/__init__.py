from inspect import isclass
from typing import Callable, Type, Union
from weakref import WeakKeyDictionary

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
    expect_column_sum,
    expect_column_values_to_be_unique,
    expect_column_values_to_not_be_null,
)
from .table_expectations import (
    expect_table_column_count,
    expect_table_columns_to_be_in_set,
    expect_table_columns_to_match_ordered_list,
    expect_table_row_count,
)

PandasHandler = Callable[[Expectation, DataFrame], Result]


class HandlerAlreadyRegistered(RuntimeError):
    """An expectation has already been registered with the runner"""

    pass


class PandasRunner(Runner):
    """Run expectations against a Pandas DataFrame"""

    _handlers = WeakKeyDictionary(
        {
            pleco.ExpectColumnDistinctValuesToBeInSet: expect_column_distinct_values_to_be_in_set,
            pleco.ExpectColumnDistinctValuesToContainSet: expect_column_distinct_values_to_contain_set,
            pleco.ExpectColumnDistinctValuesToEqualSet: expect_column_distinct_values_to_equal_set,
            pleco.ExpectColumnMax: expect_column_max,
            pleco.ExpectColumnMean: expect_column_mean,
            pleco.ExpectColumnMedian: expect_column_median,
            pleco.ExpectColumnMin: expect_column_min,
            pleco.ExpectColumnMode: expect_column_mode,
            pleco.ExpectColumnQuantile: expect_column_quantile,
            pleco.ExpectColumnSum: expect_column_sum,
            pleco.ExpectColumnValuesToBeUnique: expect_column_values_to_be_unique,
            pleco.ExpectColumnValuesToNotBeNull: expect_column_values_to_not_be_null,
            pleco.ExpectTableColumnCount: expect_table_column_count,
            pleco.ExpectTableColumnsToBeInSet: expect_table_columns_to_be_in_set,
            pleco.ExpectTableColumnsToMatchOrderedList: expect_table_columns_to_match_ordered_list,
            pleco.ExpectTableRowCount: expect_table_row_count,
        }
    )

    def run_expectation(self, expectation: Expectation, data: DataFrame) -> Result:
        if expectation.__class__ not in self._handlers:
            raise ExpectationNotSupportedByRunner(
                f"expectation {type(expectation)} is not supported by PandasRunner"
            )

        handler = self._handlers[expectation.__class__]
        return handler(expectation, data)

    def supports(self, expectation: Union[Expectation, Type[Expectation]]) -> bool:
        if isclass(expectation):
            return expectation in self._handlers
        return expectation.__class__ in self._handlers

    def add_handler(
        self, expectation: Union[Expectation, Type[Expectation]], handler: PandasHandler
    ) -> None:
        klass = expectation if isclass(expectation) else type(expectation)
        if klass in self._handlers:
            raise HandlerAlreadyRegistered(
                f"{klass} already registered in PandasRunner"
            )
        self._handlers[klass] = handler

    def remove_handler(
        self, expectation: Union[Expectation, Type[Expectation]]
    ) -> None:
        klass = expectation if isclass(expectation) else type(expectation)
        if klass in self._handlers:
            del self._handlers[klass]

    def replace_handler(
        self, expectation: Union[Expectation, Type[Expectation]], handler: PandasHandler
    ) -> None:
        self.remove_handler(expectation)
        self.add_handler(expectation, handler)
