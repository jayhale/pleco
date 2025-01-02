from abc import ABC, abstractmethod
from typing import Any, Type, Union

from pydantic import BaseModel

from .expectation import Expectation, Result, Results
from .suite import Suite


class Runner(BaseModel, ABC):
    """A generic expectation runner"""

    @abstractmethod
    def run_expectation(self, expectation: Expectation, data: Any) -> Result:
        """Run a single expectation"""
        pass

    def run_suite(self, suite: Suite, data: Any) -> Results:
        """Run a suite of expectations"""
        results = Results(success=True)
        for expectation in suite.expectations:
            results.append(self.run_expectation(expectation, data))
        return results

    @abstractmethod
    def supports(self, expectation: Union[Expectation, Type[Expectation]]) -> bool:
        """Report whether the runner supports a specific expectation"""
        pass
