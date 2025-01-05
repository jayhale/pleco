from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectTableRowCount, ValueThreshold


def test_expect_table_column_count_succeeds(runner: PandasRunner):
    expectation = ExpectTableRowCount(threshold=ValueThreshold(eq=3))
    data = DataFrame({"a": [1, 2, 3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 3
    assert result.observed_value == 3


def test_expect_table_column_count_fails(runner: PandasRunner):
    expectation = ExpectTableRowCount(threshold=ValueThreshold(eq=3))
    data = DataFrame({"a": [1, 2, 3, 4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 4
    assert result.observed_value == 4
