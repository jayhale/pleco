from pleco_pandas import PandasRunner
from pytest import fixture


@fixture
def runner() -> PandasRunner:
    return PandasRunner()
