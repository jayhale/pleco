from typing import Optional, Union

from pydantic import BaseModel, model_validator
from typing_extensions import Self


class Constraint(BaseModel):
    """Threshold for deciding if an expectation should succeed or fail base on values.
    Constraints can be defined with any combination of attributes."""

    eq: Optional[Union[int, float]] = None
    """Equality constraint"""

    gt: Optional[Union[int, float]] = None
    """Greater than constraint"""

    ge: Optional[Union[int, float]] = None
    """Greater than or equal constraint"""

    lt: Optional[Union[int, float]] = None
    """Less than constraint"""

    le: Optional[Union[int, float]] = None
    """Less than or equal constraint"""

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
