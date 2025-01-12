from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import Constraint, ExpectColumnStandardDeviation


def test_expect_column_standard_deviation_succeeds(runner: PandasRunner):
    expectation = ExpectColumnStandardDeviation(
        column="a", constraint=Constraint(gt=1, lt=2)
    )
    data = DataFrame({"a": [1, 2, 3, 4, 5]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 5
    assert result.observed_value >= 1.58
    assert result.observed_value <= 1.59


def test_expect_column_standard_deviation_fails(runner: PandasRunner):
    expectation = ExpectColumnStandardDeviation(column="a", constraint=Constraint(eq=1))
    data = DataFrame({"a": [1, 2, 3, 4, 5]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 5
    assert result.observed_value >= 1.58
    assert result.observed_value <= 1.59
