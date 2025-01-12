from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import Constraint, ExpectColumnSum


def test_expect_column_sum_succeeds(runner: PandasRunner):
    expectation = ExpectColumnSum(column="a", constraint=Constraint(eq=15))
    data = DataFrame({"a": [1, 2, 3, 4, 5]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 5
    assert result.observed_value == 15


def test_expect_column_sum_fails(runner: PandasRunner):
    expectation = ExpectColumnSum(column="a", constraint=Constraint(eq=15))
    data = DataFrame({"a": [1, 2, 3, 4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 4
    assert result.observed_value == 10
