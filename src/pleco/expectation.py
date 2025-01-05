from enum import IntEnum
from typing import List, Optional, Union

from pydantic import BaseModel, confloat, conint

from .threshold import RecordCountThreshold, ValueThreshold


class Severity(IntEnum):
    """The severity of an expectation failure"""

    WARN = 10
    ERROR = 20
    RAISE = 30


class Result(BaseModel):
    """The result of an expectation evaluation"""

    expectation: "Expectation"
    success: bool
    observation_count: conint(ge=0)


class RecordCountResult(Result):
    """The result of an expectation evaluation that counts records"""

    failure_count: Optional[conint(ge=0)] = None
    failure_percent: Optional[confloat(ge=0)] = None


class ValueResult(Result):
    """The result of an expectation evaluation that computes a value"""

    observed_value: Optional[Union[int, float]] = None


class Expectation(BaseModel):
    """A generic expectation"""

    severity: Severity = Severity.WARN

    def build_result(self, success: bool, observation_count: int) -> Result:
        """Build a result after the expectation has been evaluated"""
        return Result(
            expectation=self, success=success, observation_count=observation_count
        )


class Results(BaseModel):
    success: bool
    results: List[Result] = []

    def append(self, result: Result) -> None:
        """Add a result"""

        self.results.append(result)

        if not result.success:
            self.success = False


class RecordCountExpectation(Expectation):
    """A generic observation-count expectation"""

    threshold: RecordCountThreshold = RecordCountThreshold(count_le=0)

    def build_result(
        self, observation_count: int, failure_count: int
    ) -> RecordCountResult:
        """Build a result from observation and failure counts"""

        failure_percent = failure_count / observation_count * 100
        success = self.threshold.test(failure_count, failure_percent)

        return RecordCountResult(
            expectation=self,
            success=success,
            observation_count=observation_count,
            failure_count=failure_count,
            failure_percent=failure_percent,
        )


class ValueExpectation(Expectation):
    """A generic value expectation"""

    threshold: ValueThreshold = ValueThreshold(le=0)

    def build_result(
        self, observation_count: int, value: Union[int, float]
    ) -> ValueResult:
        success = self.threshold.test(value)

        return ValueResult(
            expectation=self,
            success=success,
            observation_count=observation_count,
            observed_value=value,
        )
