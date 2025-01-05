class ExpectationNotSupportedByRunner(Exception):
    """A runner was passed an exception that it does not support"""


class ExpectationFailed(RuntimeError):
    """An expectation failed with a severity of `RAISE`"""
