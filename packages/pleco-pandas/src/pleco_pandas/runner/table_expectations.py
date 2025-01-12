from typing import Any, Iterable, Optional

import pandas as pd

import pleco


def expect_column_to_exist(
    expectation: pleco.ExpectColumnToExist, data: pd.DataFrame
) -> pleco.Result:
    observation_count = data.shape[1]
    success = expectation.column in data.columns
    return expectation.build_result(success, observation_count)


def expect_table_column_count(
    expectation: pleco.ExpectTableColumnCount, data: pd.DataFrame
) -> pleco.ValueResult:
    observation_count = data.shape[1]
    return expectation.build_result(observation_count, observation_count)


def expect_table_columns_to_be_in_set(
    expectation: pleco.ExpectTableColumnsToBeInSet, data: pd.DataFrame
) -> pleco.CountResult:
    observation_count = data.shape[1]
    observed_columns = set(data.columns)
    failure_count = len(observed_columns.difference(expectation.columns))
    return expectation.build_result(observation_count, failure_count)


def expect_table_columns_to_match_ordered_list(
    expectation: pleco.ExpectTableColumnsToMatchOrderedList, data: pd.DataFrame
) -> pleco.CountResult:
    observation_count = data.shape[1]
    observed_columns = data.columns
    failure_count = 0

    for expected_column, observed_column in zip_longest(
        expectation.columns, observed_columns
    ):
        if not expected_column == str(observed_column):
            failure_count += 1

    return expectation.build_result(observation_count, failure_count)


def expect_table_row_count(
    expectation: pleco.ExpectTableRowCount, data: pd.DataFrame
) -> pleco.ValueResult:
    observation_count = data.shape[0]
    return expectation.build_result(observation_count, observation_count)


def zip_longest(*iterables: Iterable, pad_with: Optional[Any] = None) -> Iterable:
    class _ZipLongestSentinel:
        pass

    iterators = tuple(iter(i) for i in iterables)
    sentinel = _ZipLongestSentinel()
    while True:
        new = tuple(next(i, sentinel) for i in iterators)
        if all(n is sentinel for n in new):
            return
        yield tuple(pad_with if n is sentinel else n for n in new)
