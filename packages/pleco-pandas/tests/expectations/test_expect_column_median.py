from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import Constraint, ExpectColumnMedian


def test_expect_column_median_succeeds(runner: PandasRunner):
    expectation = ExpectColumnMedian(column="a", constraint=Constraint(gt=2, lt=4))
    data = DataFrame({"a": [2, 2, 3, 4, 4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 5
    assert result.observed_value == 3


def test_expect_column_median_fails(runner: PandasRunner):
    expectation = ExpectColumnMedian(column="a", constraint=Constraint(gt=2, lt=4))
    data = DataFrame({"a": [1, 2, 3, 2, 1]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 5
    assert result.observed_value == 2
