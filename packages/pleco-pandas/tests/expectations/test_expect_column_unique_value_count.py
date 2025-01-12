from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import Constraint, ExpectColumnUniqueValueCount


def test_expect_column_values_to_be_unique_succeeds(runner: PandasRunner):
    expectation = ExpectColumnUniqueValueCount(column="a", constraint=Constraint(eq=3))
    data = DataFrame({"a": [1, 2, 3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 3
    assert result.observed_value == 3


def test_expect_column_values_to_be_unique_fails(runner: PandasRunner):
    expectation = ExpectColumnUniqueValueCount(column="a", constraint=Constraint(eq=3))
    data = DataFrame({"a": [1, 2, 2]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 3
    assert result.observed_value == 2
