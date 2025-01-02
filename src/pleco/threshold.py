from typing import Optional, Union

from pydantic import BaseModel, confloat, conint, model_validator
from typing_extensions import Self


class CountThreshold(BaseModel):
    """Threshold for deciding if an expectation should succeed or fail base on observation counts"""

    count_gt: Optional[conint(ge=0)] = None
    count_ge: Optional[conint(ge=0)] = None
    count_lt: Optional[conint(ge=0)] = None
    count_le: Optional[conint(ge=0)] = None
    percent_gt: Optional[confloat(ge=0)] = None
    percent_ge: Optional[confloat(ge=0)] = None
    percent_lt: Optional[confloat(ge=0)] = None
    percent_le: Optional[confloat(ge=0)] = None

    @model_validator(mode="after")
    def validate_at_least_one_constraint(self) -> Self:
        if self.count_gt is not None:
            return self
        if self.count_ge is not None:
            return self
        if self.count_lt is not None:
            return self
        if self.count_le is not None:
            return self
        if self.percent_gt is not None:
            return self
        if self.percent_ge is not None:
            return self
        if self.percent_lt is not None:
            return self
        if self.percent_le is not None:
            return self
        raise ValueError(
            "At least one of count_gt, count_ge, count_lt, count_le, percent_gt, percent_ge, percent_lt, or percent_le"
            "must be specified"
        )

    def test(self, failure_count: int, failure_percent: float) -> bool:
        if self.count_gt is not None:
            if not failure_count > self.count_gt:
                return False
        if self.count_ge is not None:
            if not failure_count >= self.count_ge:
                return False
        if self.count_lt is not None:
            if not failure_count < self.count_lt:
                return False
        if self.count_le is not None:
            if not failure_count <= self.count_le:
                return False
        if self.percent_gt is not None:
            if not failure_percent > self.percent_gt:
                return False
        if self.percent_ge is not None:
            if not failure_percent >= self.percent_ge:
                return False
        if self.percent_lt is not None:
            if not failure_percent < self.percent_lt:
                return False
        if self.percent_le is not None:
            if not failure_percent <= self.percent_le:
                return False
        return True


class ValueThreshold(BaseModel):
    """Threshold for deciding if an expectation should succeed or fail base on values"""

    eq: Optional[Union[int, float]] = None
    gt: Optional[Union[int, float]] = None
    ge: Optional[Union[int, float]] = None
    lt: Optional[Union[int, float]] = None
    le: Optional[Union[int, float]] = None

    @model_validator(mode="after")
    def validate_at_least_one_constraint(self) -> Self:
        if self.eq is not None:
            return self
        if self.gt is not None:
            return self
        if self.ge is not None:
            return self
        if self.lt is not None:
            return self
        if self.le is not None:
            return self
        raise ValueError("At least one of eq, gt, ge, lt, or le must be specified")

    def test(self, value: Union[int, float]) -> bool:
        if self.eq is not None:
            if not value == self.eq:
                return False
        if self.gt is not None:
            if not value > self.gt:
                return False
        if self.ge is not None:
            if not value >= self.ge:
                return False
        if self.lt is not None:
            if not value < self.lt:
                return False
        if self.le is not None:
            if not value <= self.le:
                return False
        return True
