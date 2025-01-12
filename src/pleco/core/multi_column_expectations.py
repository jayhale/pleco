from typing import Any, List, Set, Tuple

from ..expectation import CountExpectation, ValueExpectation


class ExpectColumnPairValuesAToBeGreaterThanB(CountExpectation):
    """Expect values in column A to be greater than column B"""

    column_a: str
    column_b: str


class ExpectColumnPairValuesToBeEqual(CountExpectation):
    """Expect values in column A to be equal to column B"""

    column_a: str
    column_b: str


class ExpectColumnPairValuesToBeInSet(CountExpectation):
    """Expect pair values in column A and B to be in a set"""

    column_a: str
    column_b: str
    value_set: Set[Tuple[Any, Any]]


class ExpectCompoundColumnsToBeUnique(CountExpectation):
    """Expect a compound set of columns to be unique together"""

    columns: List[str]


class ExpectMultiColumnSum(ValueExpectation):
    """Expect the sum of values from a set of columns"""

    columns: List[str]


class ExpectMultiColumnValuesToBeUnique(CountExpectation):
    """Expect values from multiple columns to be unique"""

    columns: List[str]


class ExpectMultiColumnValuesToBeUniqueWithinRecord(CountExpectation):
    """Expect the values from specified columns to be unique within the row"""

    columns: List[str]
