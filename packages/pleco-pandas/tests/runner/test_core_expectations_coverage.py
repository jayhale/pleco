import inspect
from typing import Any

from pleco_pandas import PandasRunner

import pleco


def is_core_expectation(m: Any) -> bool:
    if not inspect.isclass(m):
        return False
    if not issubclass(m, pleco.Expectation):
        return False
    if m is pleco.Expectation:
        return False
    if m is pleco.CountExpectation:
        return False
    if m is pleco.ValueExpectation:
        return False
    return True


def test_core_expectations_coverage(runner: PandasRunner):
    core_expectations = inspect.getmembers(pleco, is_core_expectation)
    supported_expectations = [e for e in core_expectations if runner.supports(e[1])]
    unsupported_expectations = [
        e for e in core_expectations if not runner.supports(e[1])
    ]
    print(
        "Yet to be supported:\n"
        + "\n".join(f" - {e[0]}" for e in unsupported_expectations)
    )
    supported_percent = len(supported_expectations) * 100.0 / len(core_expectations)
    assert supported_percent >= 50.0
