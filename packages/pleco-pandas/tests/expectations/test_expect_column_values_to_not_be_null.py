from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectColumnValuesToNotBeNull


def test_expect_column_values_to_not_be_null_succeeds(runner: PandasRunner):
    expectation = ExpectColumnValuesToNotBeNull(column="a")
    data = DataFrame({"a": [1, 2, 3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 3
    assert result.failure_count == 0
    assert result.failure_percent == 0.0


def test_expect_column_values_to_not_be_null_fails(runner: PandasRunner):
    expectation = ExpectColumnValuesToNotBeNull(column="a")
    data = DataFrame({"a": [1, 2, None]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 3
    assert result.failure_count == 1
    assert result.failure_percent == 1.0 / 3 * 100
