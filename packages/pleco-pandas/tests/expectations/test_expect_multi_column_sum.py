from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import Constraint, ExpectMultiColumnSum


def test_expect_column_sum_succeeds(runner: PandasRunner):
    expectation = ExpectMultiColumnSum(columns=["a", "b"], constraint=Constraint(eq=15))
    data = DataFrame({"a": [1, 2, 3], "b": [4, 5, None], "c": [6, 7, 8]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 6
    assert result.observed_value == 15


def test_expect_column_sum_fails(runner: PandasRunner):
    expectation = ExpectMultiColumnSum(
        columns=["a", "b", "c"], constraint=Constraint(eq=15)
    )
    data = DataFrame({"a": [1, 2, 3], "b": [4, 5, None], "c": [6, 7, 8]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 9
    assert result.observed_value == 36
