from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectColumnValuesToBeNull


def test_expect_column_values_to_be_null_succeeds(runner: PandasRunner):
    expectation = ExpectColumnValuesToBeNull(column="a")
    data = DataFrame({"a": [None, None, None]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 3
    assert result.failure_count == 0
    assert result.failure_percent == 0.0


def test_expect_column_values_to_be_null_fails(runner: PandasRunner):
    expectation = ExpectColumnValuesToBeNull(column="a")
    data = DataFrame({"a": [1, None, None]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 3
    assert result.failure_count == 1
    assert result.failure_percent == 1.0 / 3 * 100
