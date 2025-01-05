from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectColumnValuesToEqualSet


def test_expect_column_values_to_equal_set_succeeds(runner: PandasRunner):
    expectation = ExpectColumnValuesToEqualSet(column="a", value_set={1, 2, 3})
    data = DataFrame({"a": [1, 2, 3, 3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 3
    assert result.failure_count == 0
    assert result.failure_percent == 0.0


def test_expect_column_values_to_equal_set_fails(runner: PandasRunner):
    expectation = ExpectColumnValuesToEqualSet(column="a", value_set={1, 2, 3})
    data = DataFrame({"a": [1, 2, 4, 4]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 3
    assert result.failure_count == 2
    assert result.failure_percent == 2.0 / 3 * 100
