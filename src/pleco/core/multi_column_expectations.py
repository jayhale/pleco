from typing import Any, List, Set, Tuple

from ..expectation import RecordCountExpectation, ValueExpectation


class ExpectColumnPairValuesAToBeGreaterThanB(RecordCountExpectation):
    """Expect values in column A to be greater than column B"""

    column_a: str
    column_b: str


class ExpectColumnPairValuesToBeEqual(RecordCountExpectation):
    """Expect values in column A to be equal to column B"""

    column_a: str
    column_b: str


class ExpectColumnPairValuesToBeInSet(RecordCountExpectation):
    """Expect pair values in column A and B to be in a set"""

    column_a: str
    column_b: str
    value_set: Set[Tuple[Any, Any]]


class ExpectCompoundColumnsToBeUnique(RecordCountExpectation):
    """Expect a compound set of columns to be unique together"""

    columns: List[str]


class ExpectMultiColumnSum(ValueExpectation):
    """Expect the sum of values from a set of columns"""

    columns: List[str]


class ExpectMultiColumnValuesToBeUnique(RecordCountExpectation):
    """Expect values from multiple columns to be unique"""

    columns: List[str]


class ExpectMultiColumnValuesToBeUniqueWithinRecord(RecordCountExpectation):
    """Expect the values from specified columns to be unique within the row"""

    columns: List[str]
