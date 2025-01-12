from inspect import isclass
from typing import Callable, Type, Union, overload, override
from weakref import WeakKeyDictionary

from pandas import DataFrame

import pleco

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
    expect_column_standard_deviation,
    expect_column_sum,
    expect_column_unique_value_count,
    expect_column_value_lengths_to_be_between,
    expect_column_value_lengths_to_equal,
    expect_column_values_to_be_between,
    expect_column_values_to_be_null,
    expect_column_values_to_be_unique,
    expect_column_values_to_not_be_in_set,
    expect_column_values_to_not_be_null,
)
from .multi_column_expectations import expect_multi_column_sum
from .table_expectations import (
    expect_column_to_exist,
    expect_table_column_count,
    expect_table_columns_to_be_in_set,
    expect_table_columns_to_match_ordered_list,
    expect_table_row_count,
)

PandasHandler = Callable[[pleco.Expectation, DataFrame], pleco.Result]


class HandlerAlreadyRegistered(RuntimeError):
    """An expectation has already been registered with the runner"""

    pass


class PandasRunner(pleco.Runner):
    """Run expectations against a Pandas DataFrame"""

    _handlers = WeakKeyDictionary(
        {
            pleco.ExpectColumnValuesToBeInSet: expect_column_distinct_values_to_be_in_set,  # noqa: E501
            pleco.ExpectColumnValuesToContainSet: expect_column_distinct_values_to_contain_set,  # noqa: E501
            pleco.ExpectColumnValuesToEqualSet: expect_column_distinct_values_to_equal_set,  # noqa: E501
            pleco.ExpectColumnMax: expect_column_max,
            pleco.ExpectColumnMean: expect_column_mean,
            pleco.ExpectColumnMedian: expect_column_median,
            pleco.ExpectColumnMin: expect_column_min,
            pleco.ExpectColumnMode: expect_column_mode,
            pleco.ExpectColumnQuantile: expect_column_quantile,
            pleco.ExpectColumnStandardDeviation: expect_column_standard_deviation,
            pleco.ExpectColumnSum: expect_column_sum,
            pleco.ExpectColumnToExist: expect_column_to_exist,
            pleco.ExpectColumnUniqueValueCount: expect_column_unique_value_count,
            pleco.ExpectColumnValueLengthsToBeBetween: expect_column_value_lengths_to_be_between,  # noqa: E501
            pleco.ExpectColumnValueLengthsToEqual: expect_column_value_lengths_to_equal,
            pleco.ExpectColumnValuesToBeBetween: expect_column_values_to_be_between,
            pleco.ExpectColumnValuesToBeNull: expect_column_values_to_be_null,
            pleco.ExpectColumnValuesToBeUnique: expect_column_values_to_be_unique,
            pleco.ExpectColumnValuesToNotBeInSet: expect_column_values_to_not_be_in_set,
            pleco.ExpectColumnValuesToNotBeNull: expect_column_values_to_not_be_null,
            pleco.ExpectMultiColumnSum: expect_multi_column_sum,
            pleco.ExpectTableColumnCount: expect_table_column_count,
            pleco.ExpectTableColumnsToBeInSet: expect_table_columns_to_be_in_set,
            pleco.ExpectTableColumnsToMatchOrderedList: expect_table_columns_to_match_ordered_list,  # noqa: E501
            pleco.ExpectTableRowCount: expect_table_row_count,
        }
    )

    @overload
    def run_expectation(
        self, expectation: pleco.CountExpectation, data: DataFrame
    ) -> pleco.CountResult:
        pass

    @overload
    def run_expectation(
        self, expectation: pleco.ValueExpectation, data: DataFrame
    ) -> pleco.ValueResult:
        pass

    @override
    def run_expectation(
        self, expectation: pleco.Expectation, data: DataFrame
    ) -> pleco.Result:
        if expectation.__class__ not in self._handlers:
            raise pleco.ExpectationNotSupportedByRunner(
                f"expectation {type(expectation)} is not supported by PandasRunner"
            )

        handler = self._handlers[expectation.__class__]
        result = handler(expectation, data)

        if expectation.severity >= pleco.Severity.RAISE and not result.success:
            raise pleco.ExpectationFailed(result)

        return handler(expectation, data)

    @override
    def supports(
        self, expectation: Union[pleco.Expectation, Type[pleco.Expectation]]
    ) -> bool:
        if isclass(expectation):
            return expectation in self._handlers
        return expectation.__class__ in self._handlers

    def add_handler(
        self,
        expectation: Union[pleco.Expectation, Type[pleco.Expectation]],
        handler: PandasHandler,
    ) -> None:
        """Add an expectation handler to the runner instance"""
        klass = expectation if isclass(expectation) else type(expectation)
        if klass in self._handlers:
            raise HandlerAlreadyRegistered(
                f"{klass} already registered in PandasRunner"
            )
        self._handlers[klass] = handler

    def remove_handler(
        self, expectation: Union[pleco.Expectation, Type[pleco.Expectation]]
    ) -> None:
        """Remove an expectation handler from a runner instance"""
        klass = expectation if isclass(expectation) else type(expectation)
        if klass in self._handlers:
            del self._handlers[klass]

    def replace_handler(
        self,
        expectation: Union[pleco.Expectation, Type[pleco.Expectation]],
        handler: PandasHandler,
    ) -> None:
        """Replace an expectation handler in the runner instance"""
        self.remove_handler(expectation)
        self.add_handler(expectation, handler)
