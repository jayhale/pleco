from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectColumnValueLengthsToBeBetween


def test_expect_column_value_lengths_to_be_between_succeeds(runner: PandasRunner):
    expectation = ExpectColumnValueLengthsToBeBetween(
        column="a", length_min=0, length_max=3
    )
    data = DataFrame({"a": ["", "1", "_3_"]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 3
    assert result.failure_count == 0
    assert result.failure_percent == 0.0


def test_expect_column_value_lengths_to_be_between_fails(runner: PandasRunner):
    expectation = ExpectColumnValueLengthsToBeBetween(
        column="a", length_min=0, length_max=3
    )
    data = DataFrame({"a": ["", "1", "__5__"]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 3
    assert result.failure_count == 1
    assert result.failure_percent == 1.0 / 3 * 100
