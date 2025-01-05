from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectColumnValueLengthsToEqual


def test_expect_column_value_lengths_to_equal_succeeds(runner: PandasRunner):
    expectation = ExpectColumnValueLengthsToEqual(column="a", length=3)
    data = DataFrame({"a": ["_3_", "___", "333"]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 3
    assert result.failure_count == 0
    assert result.failure_percent == 0.0


def test_expect_column_value_lengths_to_equal_fails(runner: PandasRunner):
    expectation = ExpectColumnValueLengthsToEqual(column="a", length=3)
    data = DataFrame({"a": ["_3_", "___", "__5__"]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 3
    assert result.failure_count == 1
    assert result.failure_percent == 1.0 / 3 * 100
