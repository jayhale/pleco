from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectColumnValuesToBeBetween


def test_expect_column_values_to_be_unique_succeeds(runner: PandasRunner):
    expectation = ExpectColumnValuesToBeBetween(column="a", value_min=0, value_max=3)
    data = DataFrame({"a": [1, 2, 3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 3
    assert result.failure_count == 0
    assert result.failure_percent == 0.0


def test_expect_column_values_to_be_unique_fails(runner: PandasRunner):
    expectation = ExpectColumnValuesToBeBetween(column="a", value_min=0, value_max=3)
    data = DataFrame({"a": [1, 2, 4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 3
    assert result.failure_count == 1
    assert result.failure_percent == 1.0 / 3 * 100
