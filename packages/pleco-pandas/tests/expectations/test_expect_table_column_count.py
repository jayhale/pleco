from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectTableColumnCount, ValueThreshold


def test_expect_table_column_count_succeeds(runner: PandasRunner):
    expectation = ExpectTableColumnCount(threshold=ValueThreshold(eq=1))
    data = DataFrame({"a": [1, 2, 3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 1
    assert result.observed_value == 1


def test_expect_table_column_count_fails(runner: PandasRunner):
    expectation = ExpectTableColumnCount(threshold=ValueThreshold(eq=1))
    data = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 2
    assert result.observed_value == 2
