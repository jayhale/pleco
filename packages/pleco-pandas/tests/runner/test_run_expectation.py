import pytest
from pandas import DataFrame
from pleco_pandas import PandasRunner

from pleco import ExpectationFailed, ExpectColumnValuesToBeUnique, Severity


def test_run_expectation_succeeds(runner: PandasRunner):
    expectation = ExpectColumnValuesToBeUnique(column="a")
    data = DataFrame({"a": [1, 2, 3]})
    result = runner.run_expectation(expectation, data)
    assert result.success is True


def test_run_expectation_fails_warn(runner: PandasRunner):
    expectation = ExpectColumnValuesToBeUnique(column="a", severity=Severity.WARN)
    data = DataFrame({"a": [1, 2, 2]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False


def test_run_expectation_fails_error(runner: PandasRunner):
    expectation = ExpectColumnValuesToBeUnique(column="a", severity=Severity.ERROR)
    data = DataFrame({"a": [1, 2, 2]})
    result = runner.run_expectation(expectation, data)
    assert result.success is False


def test_run_expectation_fails_raise(runner: PandasRunner):
    expectation = ExpectColumnValuesToBeUnique(column="a", severity=Severity.RAISE)
    data = DataFrame({"a": [1, 2, 2]})

    with pytest.raises(ExpectationFailed):
        runner.run_expectation(expectation, data)
