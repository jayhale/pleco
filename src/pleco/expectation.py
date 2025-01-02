from abc import ABC, abstractmethod
from enum import IntEnum
from typing import List, Optional, Union

from pydantic import BaseModel, confloat, conint

from .threshold import CountThreshold, ValueThreshold


class Severity(IntEnum):
    WARN = 10
    ERROR = 20
    RAISE = 30


class Expectation(BaseModel, ABC):
    """A generic expectation"""

    severity: Severity = Severity.WARN

    @abstractmethod
    def build_result(self, *args, **kwargs) -> "Result":
        """Build a result after the expectation has been evaluated"""
        pass


class Result(BaseModel):
    expectation: Expectation
    success: bool
    observation_count: conint(ge=0)
    observed_value: Optional[Union[int, float]] = None
    failure_count: Optional[conint(ge=0)] = None
    failure_percent: Optional[confloat(ge=0)] = None


class Results(BaseModel):
    success: bool
    results: List[Result] = []

    def append(self, result: Result) -> None:
        """Add a result"""

        self.results.append(result)

        if not result.success:
            self.success = False


class CountExpectation(Expectation):
    """A generic observation-count expectation"""

    threshold: CountThreshold = CountThreshold(count_le=0)

    def build_result(self, observation_count: int, failure_count: int) -> Result:
        """Build a result from observation and failure counts"""

        failure_percent = failure_count / observation_count * 100
        success = self.threshold.test(failure_count, failure_percent)

        return Result(
            expectation=self,
            success=success,
            observation_count=observation_count,
            failure_count=failure_count,
            failure_percent=failure_percent,
        )


class ValueExpectation(Expectation):
    """A generic value expectation"""

    threshold: ValueThreshold = ValueThreshold(le=0)

    def build_result(self, observation_count: int, value: Union[int, float]) -> Result:
        success = self.threshold.test(value)

        return Result(
            expectation=self,
            success=success,
            observation_count=observation_count,
            observed_value=value,
        )
