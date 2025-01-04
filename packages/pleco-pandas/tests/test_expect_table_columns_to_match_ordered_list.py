from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import CountThreshold, ExpectTableColumnsToMatchOrderedList


def test_expect_table_columns_to_match_ordered_list_succeeds(runner: PandasRunner):
    expectation = ExpectTableColumnsToMatchOrderedList(
        threshold=CountThreshold(count_eq=0), columns=["a", "b", "c"]
    )
    data = DataFrame({"a": [1], "b": [2], "c": [3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 3
    assert result.failure_count == 0
    assert result.failure_percent == 0


def test_expect_table_columns_to_match_ordered_list_fails(runner: PandasRunner):
    expectation = ExpectTableColumnsToMatchOrderedList(
        threshold=CountThreshold(count_eq=0), columns=["a", "b", "c"]
    )
    data = DataFrame({"a": [1], "b": [4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 2
    assert result.failure_count == 1
    assert result.failure_percent == 1.0 / 2 * 100
