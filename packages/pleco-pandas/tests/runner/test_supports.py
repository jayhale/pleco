from pleco_pandas import PandasRunner

from pleco import CountExpectation, ExpectColumnValuesToBeUnique


def test_supports_class_succeeds(runner: PandasRunner):
    supported_expectation_class = ExpectColumnValuesToBeUnique
    assert runner.supports(supported_expectation_class)


def test_supports_class_fails(runner: PandasRunner):
    class UnsupportedExpectation(CountExpectation):
        pass

    assert not runner.supports(UnsupportedExpectation())


def test_supports_instance_succeeds(runner: PandasRunner):
    supported_expectation = ExpectColumnValuesToBeUnique(column="a")

    assert runner.supports(supported_expectation)


def test_supports_instance_fails(runner: PandasRunner):
    class UnsupportedExpectation(CountExpectation):
        pass

    assert not runner.supports(UnsupportedExpectation())
