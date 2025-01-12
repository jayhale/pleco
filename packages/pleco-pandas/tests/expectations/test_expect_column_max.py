from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import Constraint, ExpectColumnMax


def test_expect_column_max_succeeds(runner: PandasRunner):
    expectation = ExpectColumnMax(column="a", constraint=Constraint(gt=3, lt=5))
    data = DataFrame({"a": [1, 2, 3, 4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 4
    assert result.observed_value == 4


def test_expect_column_max_fails(runner: PandasRunner):
    expectation = ExpectColumnMax(column="a", constraint=Constraint(gt=3, lt=5))
    data = DataFrame({"a": [1, 2, 3, 3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 4
    assert result.observed_value == 3
