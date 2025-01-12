from enum import IntEnum
from typing import List, Optional, Union

from pydantic import BaseModel, confloat, conint, model_validator
from typing_extensions import Self

from .constraint import Constraint


class Severity(IntEnum):
    """The severity of an expectation failure"""

    WARN = 10
    """An expectation failure is tolerable, but should be visible"""

    ERROR = 20
    """An expectation failure is not tolerable"""

    RAISE = 30
    """An expectation failure should raise an exception, immediately stopping
    processing"""


class Result(BaseModel):
    """The result of an expectation evaluation.

    Most commonly, a :class:`Result` instance will be constructed by
    :meth:`Expectation.build_result` with the requisite values from evaluating the
    expectation.
    """

    expectation: "Expectation"
    """The expectation that was evaluated to generate the result"""

    success: bool
    """Whether the expectation was met"""

    observation_count: conint(ge=0)
    """The number of entities (e.g., values, columns, tables) observed to evaluate the
    expectation"""


class CountResult(Result):
    """The result of an expectation evaluation that counts records"""

    failure_count: Optional[conint(ge=0)] = None
    """The number of observations that failed to satisfy the expectation"""

    failure_percent: Optional[confloat(ge=0)] = None
    """The percentage of observations that failed to satisfy the expectation"""


class ValueResult(Result):
    """The result of an expectation evaluation that computes a value"""

    observed_value: Optional[Union[int, float]] = None
    """The actual value observed to evaluate the expectation"""


class Expectation(BaseModel):
    """A generic expectation"""

    severity: Severity = Severity.WARN

    def build_result(self, success: bool, observation_count: int) -> Result:
        """Build a result after the expectation has been evaluated"""
        return Result(
            expectation=self, success=success, observation_count=observation_count
        )


class Results(BaseModel):
    """A collection of associated expectation evaluation results, commonly from a
    :class:`Suite`"""

    success: bool
    """Whether all expectations in the collection were met"""

    results: List[Result] = []
    """The individual expectation evaluation results"""

    def append(self, result: Result) -> None:
        """Add a result to the collection"""

        self.results.append(result)

        if not result.success:
            self.success = False


class CountExpectation(Expectation):
    """A generic observation-count expectation. Count expectations can be constrained
    by either or both the count and percentage of failing observations."""

    failure_count_constraint: Optional[Constraint] = Constraint(eq=0)
    """A constraint on the number of observations that fail to satisfy the
    expectation"""

    failure_percent_constraint: Optional[Constraint] = None
    """A constraint on the percent of observations that fail to satisfy the
    expectation"""

    @model_validator(mode="after")
    def validate_at_least_one_constraint(self) -> Self:
        if self.failure_count_constraint is not None:
            return self
        if self.failure_percent_constraint is not None:
            return self
        raise ValueError(
            "At least one of failure_count_constraint or failure_percent_constraint"
            "must be specified"
        )

    def build_result(self, observation_count: int, failure_count: int) -> CountResult:
        """Build a result from observation and failure counts"""

        failure_percent = failure_count / observation_count * 100
        success = True

        if self.failure_count_constraint is not None:
            if not self.failure_count_constraint.test(failure_count):
                success = False

        if self.failure_percent_constraint is not None:
            if not self.failure_percent_constraint.test(failure_percent):
                success = False

        return CountResult(
            expectation=self,
            success=success,
            observation_count=observation_count,
            failure_count=failure_count,
            failure_percent=failure_percent,
        )


class ValueExpectation(Expectation):
    """An expectation that assesses and aggregated value describing the observed
    data."""

    constraint: Constraint = Constraint(le=0)
    """A constraint on the observed value"""

    def build_result(
        self, observation_count: int, value: Union[int, float]
    ) -> ValueResult:
        success = self.constraint.test(value)

        return ValueResult(
            expectation=self,
            success=success,
            observation_count=observation_count,
            observed_value=value,
        )
