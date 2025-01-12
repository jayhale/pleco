from typing import List

from pydantic import BaseModel

from .expectation import CountExpectation


class Suite(BaseModel):
    """A suite of expectations"""

    name: str
    expectations: List[CountExpectation]

    def append(self, expectation: CountExpectation) -> None:
        self.expectations.append(expectation)
