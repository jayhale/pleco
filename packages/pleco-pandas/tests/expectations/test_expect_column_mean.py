from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectColumnMean, ValueThreshold


def test_expect_column_mean_succeeds(runner: PandasRunner):
    expectation = ExpectColumnMean(column="a", threshold=ValueThreshold(gt=2, lt=3))
    data = DataFrame({"a": [1, 2, 3, 4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 4
    assert result.observed_value == 2.5


def test_expect_column_mean_fails(runner: PandasRunner):
    expectation = ExpectColumnMean(column="a", threshold=ValueThreshold(gt=2, lt=3))
    data = DataFrame({"a": [1, 2, 3, 2]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 4
    assert result.observed_value == 2
