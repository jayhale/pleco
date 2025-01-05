from typing import List

from pydantic import BaseModel

from .expectation import RecordCountExpectation


class Suite(BaseModel):
    """A suite of expectations"""

    name: str
    expectations: List[RecordCountExpectation]

    def append(self, expectation: RecordCountExpectation) -> None:
        self.expectations.append(expectation)
