from typing import List, Set

from ..expectation import CountExpectation, Expectation, ValueExpectation


class ExpectColumnToExist(Expectation):
    """Expect the data source to have a column"""

    column: str


class ExpectTableColumnCount(ValueExpectation):
    """Expect the count of columns in a table"""


class ExpectTableColumnsToMatchOrderedList(CountExpectation):
    """Expect the columns of a table to match an ordered list"""

    columns: List[str]


class ExpectTableColumnsToBeInSet(CountExpectation):
    """Expect the columns of a table to match"""

    columns: Set[str]


class ExpectTableRowCount(ValueExpectation):
    """Expect the number of rows in a table"""
