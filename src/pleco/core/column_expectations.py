from typing import Any, Optional, Set

from ..expectation import CountExpectation, ValueExpectation


class ExpectColumnValuesToBeInSet(CountExpectation):
    """Expect column distinct values to be in set"""

    column: str
    value_set: Set[Any]


class ExpectColumnValuesToContainSet(CountExpectation):
    """Expect column distinct values to contain set"""

    column: str
    value_set: Set[Any]


class ExpectColumnValuesToEqualSet(CountExpectation):
    """Expect column distinct values to equal set"""

    column: str
    value_set: Set[Any]


class ExpectColumnKLDivergence(ValueExpectation):
    """Expect column Kullback-Leibler divergence"""

    column: str


class ExpectColumnMax(ValueExpectation):
    """Expect column maximum value"""

    column: str


class ExpectColumnMean(ValueExpectation):
    """Expect column mean value"""

    column: str


class ExpectColumnMedian(ValueExpectation):
    """Expect column median value"""

    column: str


class ExpectColumnMin(ValueExpectation):
    """Expect column minimum value"""

    column: str


class ExpectColumnMode(ValueExpectation):
    """Expect column mode (most common) value"""

    column: str


class ExpectColumnProportionOfUniqueValues(ValueExpectation):
    """Expect a proportion of unique values in a column"""

    column: str


class ExpectColumnQuantile(ValueExpectation):
    """Expect a specific quantile of a column"""

    column: str
    quantile: float


class ExpectColumnStandardDeviation(ValueExpectation):
    """Expect the standard deviation of a column"""

    column: str


class ExpectColumnSum(ValueExpectation):
    """Expect a sum of a column"""

    column: str


class ExpectColumnUniqueValueCount(ValueExpectation):
    """Expect a count of unique values in a column"""

    column: str


class ExpectColumnValueLengthsToBeBetween(CountExpectation):
    """Expect the length of values in a column to fall in a specified range"""

    column: str
    length_min: Optional[int] = None
    length_max: Optional[int] = None


class ExpectColumnValueLengthsToEqual(CountExpectation):
    """Expect the length of values in a column"""

    column: str
    length: int


class ExpectColumnValueZScoresToBeBetween(CountExpectation):
    """Expect the Z-score for values in a column to be in a specified range"""

    column: str
    zscore_max: Optional[float]
    zscore_min: Optional[float]


class ExpectColumnValuesToBeBetween(CountExpectation):
    """Expect the values in a column to be in a specified range"""

    column: str
    value_min: Optional[float]
    value_max: Optional[float]


class ExpectColumnValuesToBeDecreasing(CountExpectation):
    """Expect the values in a column to be decreasing"""

    column: str


class ExpectColumnValuesToBeInTypeSet(CountExpectation):
    """Expect the values in a column to be of a specified set of types"""

    column: str
    type_set: Set[Any]


class ExpectColumnValuesToBeIncreasing(CountExpectation):
    """Expect the values in a column to be increasing"""

    column: str


class ExpectColumnValuesToBeJsonParseable(CountExpectation):
    """Expect the values in a column to be valid JSON"""

    column: str


class ExpectColumnValuesToBeNull(CountExpectation):
    """Expect the values in a column to be null"""

    column: str


class ExpectColumnValuesToBeOfType(CountExpectation):
    """Expect the values in a column to be of a specified type"""

    column: str
    type: Any


class ExpectColumnValuesToBeUnique(CountExpectation):
    """Expect column values to be unique"""

    column: str


class ExpectColumnValuesToMatchJsonSchema(CountExpectation):
    """Expect values in a column to conform to a specified JSON schema"""

    column: str
    json_schema: str


class ExpectColumnValuesToMatchLikePattern(CountExpectation):
    """Expect values in a column to match a LIKE pattern"""

    column: str
    pattern: str


class ExpectColumnValuesToMatchLikePatternSet(CountExpectation):
    """Expect values in a column to match a set of LIKE patterns"""

    column: str
    patterns: Set[str]


class ExpectColumnValuesToMatchRegex(CountExpectation):
    """Expect values in a column to match a RegEx pattern"""

    column: str
    pattern: str


class ExpectColumnValuesToMatchRegexSet(CountExpectation):
    """Expect values in a column to match a set of RegEx patterns"""

    column: str
    patterns: Set[str]


class ExpectColumnValuesToMatchStrftimeFormat(CountExpectation):
    """Expect values in a column to match a strftime format"""

    column: str
    format: str


class ExpectColumnValuesToNotBeInSet(CountExpectation):
    """Expect values in a column to not be in a specified set"""

    column: str
    value_set: Set[Any]


class ExpectColumnValuesToNotBeNull(CountExpectation):
    """Expect column values to not be null"""

    column: str


class ExpectColumnValuesToNotMatchLikePattern(CountExpectation):
    """Expect values in a column to not match a LIKE pattern"""

    column: str
    pattern: str


class ExpectColumnValuesToNotMatchLikePatternSet(CountExpectation):
    """Expect values in a column to not match a set of LIKE patterns"""

    column: str
    patterns: Set[str]


class ExpectColumnValuesToNotMatchRegex(CountExpectation):
    """Expect values in a column to not match a RegEx pattern"""

    column: str
    pattern: str


class ExpectColumnValuesToNotMatchRegexSet(CountExpectation):
    """Expect values in a column to not match a set of RegEx patterns"""

    column: str
    patterns: Set[str]
