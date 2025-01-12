from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import Constraint, ExpectColumnMode


def test_expect_column_mode_succeeds(runner: PandasRunner):
    expectation = ExpectColumnMode(column="a", constraint=Constraint(eq=3))
    data = DataFrame({"a": [1, 2, 3, 3, 4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 5
    assert result.observed_value == 3


def test_expect_column_mode_fails(runner: PandasRunner):
    expectation = ExpectColumnMode(column="a", constraint=Constraint(eq=3))
    data = DataFrame({"a": [2, 2, 3, 2, 2]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 5
    assert result.observed_value == 2
