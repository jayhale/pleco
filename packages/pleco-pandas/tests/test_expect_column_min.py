from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectColumnMin, ValueThreshold


def test_expect_column_min_succeeds(runner: PandasRunner):
    expectation = ExpectColumnMin(column="a", threshold=ValueThreshold(gt=0, lt=2))
    data = DataFrame({"a": [1, 2, 3, 4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 4
    assert result.observed_value == 1


def test_expect_column_min_fails(runner: PandasRunner):
    expectation = ExpectColumnMin(column="a", threshold=ValueThreshold(gt=0, lt=2))
    data = DataFrame({"a": [2, 2, 3, 2]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 4
    assert result.observed_value == 2
