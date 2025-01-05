from typing import Any, Optional, Set

from ..expectation import RecordCountExpectation, ValueExpectation


class ExpectColumnValuesToBeInSet(RecordCountExpectation):
    """Expect column distinct values to be in set"""

    column: str
    value_set: Set[Any]


class ExpectColumnValuesToContainSet(RecordCountExpectation):
    """Expect column distinct values to contain set"""

    column: str
    value_set: Set[Any]


class ExpectColumnValuesToEqualSet(RecordCountExpectation):
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


class ExpectColumnValueLengthsToBeBetween(RecordCountExpectation):
    """Expect the length of values in a column to fall in a specified range"""

    column: str
    length_min: Optional[int] = None
    length_max: Optional[int] = None


class ExpectColumnValueLengthsToEqual(RecordCountExpectation):
    """Expect the length of values in a column"""

    column: str
    length: int


class ExpectColumnValueZScoresToBeBetween(RecordCountExpectation):
    """Expect the Z-score for values in a column to be in a specified range"""

    column: str
    zscore_max: Optional[float]
    zscore_min: Optional[float]


class ExpectColumnValuesToBeBetween(RecordCountExpectation):
    """Expect the values in a column to be in a specified range"""

    column: str
    value_min: Optional[float]
    value_max: Optional[float]


class ExpectColumnValuesToBeDecreasing(RecordCountExpectation):
    """Expect the values in a column to be decreasing"""

    column: str


class ExpectColumnValuesToBeInTypeSet(RecordCountExpectation):
    """Expect the values in a column to be of a specified set of types"""

    column: str
    type_set: Set[Any]


class ExpectColumnValuesToBeIncreasing(RecordCountExpectation):
    """Expect the values in a column to be increasing"""

    column: str


class ExpectColumnValuesToBeJsonParseable(RecordCountExpectation):
    """Expect the values in a column to be valid JSON"""

    column: str


class ExpectColumnValuesToBeNull(RecordCountExpectation):
    """Expect the values in a column to be null"""

    column: str


class ExpectColumnValuesToBeOfType(RecordCountExpectation):
    """Expect the values in a column to be of a specified type"""

    column: str
    type: Any


class ExpectColumnValuesToBeUnique(RecordCountExpectation):
    """Expect column values to be unique"""

    column: str


class ExpectColumnValuesToMatchJsonSchema(RecordCountExpectation):
    """Expect values in a column to conform to a specified JSON schema"""

    column: str
    json_schema: str


class ExpectColumnValuesToMatchLikePattern(RecordCountExpectation):
    """Expect values in a column to match a LIKE pattern"""

    column: str
    pattern: str


class ExpectColumnValuesToMatchLikePatternSet(RecordCountExpectation):
    """Expect values in a column to match a set of LIKE patterns"""

    column: str
    patterns: Set[str]


class ExpectColumnValuesToMatchRegex(RecordCountExpectation):
    """Expect values in a column to match a RegEx pattern"""

    column: str
    pattern: str


class ExpectColumnValuesToMatchRegexSet(RecordCountExpectation):
    """Expect values in a column to match a set of RegEx patterns"""

    column: str
    patterns: Set[str]


class ExpectColumnValuesToMatchStrftimeFormat(RecordCountExpectation):
    """Expect values in a column to match a strftime format"""

    column: str
    format: str


class ExpectColumnValuesToNotBeInSet(RecordCountExpectation):
    """Expect values in a column to not be in a specified set"""

    column: str
    value_set: Set[Any]


class ExpectColumnValuesToNotBeNull(RecordCountExpectation):
    """Expect column values to not be null"""

    column: str


class ExpectColumnValuesToNotMatchLikePattern(RecordCountExpectation):
    """Expect values in a column to not match a LIKE pattern"""

    column: str
    pattern: str


class ExpectColumnValuesToNotMatchLikePatternSet(RecordCountExpectation):
    """Expect values in a column to not match a set of LIKE patterns"""

    column: str
    patterns: Set[str]


class ExpectColumnValuesToNotMatchRegex(RecordCountExpectation):
    """Expect values in a column to not match a RegEx pattern"""

    column: str
    pattern: str


class ExpectColumnValuesToNotMatchRegexList(RecordCountExpectation):
    """Expect values in a column to not match a set of RegEx patterns"""

    column: str
    patterns: Set[str]
