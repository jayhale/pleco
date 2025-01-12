from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import Constraint, ExpectColumnQuantile


def test_expect_column_quantile_succeeds(runner: PandasRunner):
    expectation = ExpectColumnQuantile(
        column="a", quantile=0.2, constraint=Constraint(gt=1, lt=2)
    )
    data = DataFrame({"a": [1, 2, 3, 4, 5]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 5
    assert result.observed_value == 1.8


def test_expect_column_quantile_fails(runner: PandasRunner):
    expectation = ExpectColumnQuantile(
        column="a", quantile=0.2, constraint=Constraint(gt=1, lt=2)
    )
    data = DataFrame({"a": [0, 1, 2, 3, 4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 5
    assert result.observed_value == 0.8
