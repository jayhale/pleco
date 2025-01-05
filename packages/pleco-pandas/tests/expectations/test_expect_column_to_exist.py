from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectColumnToExist


def test_expect_column_to_exist_succeeds(runner: PandasRunner):
    expectation = ExpectColumnToExist(column="a")
    data = DataFrame({"a": [1, 2, 3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True
    assert result.observation_count == 1


def test_expect_column_to_exist_fails(runner: PandasRunner):
    expectation = ExpectColumnToExist(column="a")
    data = DataFrame({"b": [4, 5, 6]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False
    assert result.observation_count == 1
