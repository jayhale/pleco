from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectColumnValuesToBeUnique


def test_expect_column_values_to_be_unique_succeeds(runner: PandasRunner):
    expectation = ExpectColumnValuesToBeUnique(column="a")
    data = DataFrame({"a": [1, 2, 3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 3
    assert result.failure_count == 0
    assert result.failure_percent == 0.0


def test_expect_column_values_to_be_unique_fails(runner: PandasRunner):
    expectation = ExpectColumnValuesToBeUnique(column="a")
    data = DataFrame({"a": [1, 2, 2]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 3
    assert result.failure_count == 2
    assert result.failure_percent == 2.0 / 3 * 100
