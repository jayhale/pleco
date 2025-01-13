.. py:currentmodule:: pleco

=================
Core Expectations
=================

Pleco provides a set of tested and well-supported expectations that cover many common
data validation needs.

Column Aggregate Expectations
-----------------------------

.. list-table::
   :header-rows: 1

   * - Expectation
     - Implementations
   * - :class:`ExpectColumnKLDivergence`
     -
   * - :class:`ExpectColumnMax`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnMean`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnMedian`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnMin`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnMode`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnProportionOfUniqueValues`
     -
   * - :class:`ExpectColumnQuantile`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnStandardDeviation`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnSum`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnUniqueValueCount`
     - .. impl-icon:: pandas

Column Value Expectations
-------------------------

.. list-table::
   :header-rows: 1

   * - Expectation
     - Implementations
   * - :class:`ExpectColumnValueLengthsToBeBetween`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnValueLengthsToEqual`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnValuesToBeBetween`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnValuesToBeDecreasing`
     -
   * - :class:`ExpectColumnValuesToBeIncreasing`
     -
   * - :class:`ExpectColumnValuesToBeInSet`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnValuesToBeInTypeSet`
     -
   * - :class:`ExpectColumnValuesToBeJsonParseable`
     -
   * - :class:`ExpectColumnValuesToBeNull`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnValuesToBeOfType`
     -
   * - :class:`ExpectColumnValuesToBeUnique`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnValuesToContainSet`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnValuesToEqualSet`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnValuesToMatchJsonSchema`
     -
   * - :class:`ExpectColumnValuesToMatchLikePattern`
     -
   * - :class:`ExpectColumnValuesToMatchLikePatternSet`
     -
   * - :class:`ExpectColumnValuesToMatchRegex`
     -
   * - :class:`ExpectColumnValuesToMatchRegexSet`
     -
   * - :class:`ExpectColumnValuesToMatchStrftimeFormat`
     -
   * - :class:`ExpectColumnValuesToNotBeInSet`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnValuesToNotBeNull`
     - .. impl-icon:: pandas
   * - :class:`ExpectColumnValuesToNotMatchLikePattern`
     -
   * - :class:`ExpectColumnValuesToNotMatchLikePatternSet`
     -
   * - :class:`ExpectColumnValuesToNotMatchRegex`
     -
   * - :class:`ExpectColumnValuesToNotMatchRegexList`
     -
   * - :class:`ExpectColumnValueZScoresToBeBetween`
     -

Multi-Column Expectations
-------------------------

.. list-table::
   :header-rows: 1

   * - Expectation
     - Implementations
   * - :class:`ExpectColumnPairValuesAToBeGreaterThanB`
     -
   * - :class:`ExpectColumnPairValuesToBeEqual`
     -
   * - :class:`ExpectColumnPairValuesToBeInSet`
     -
   * - :class:`ExpectCompoundColumnsToBeUnique`
     -
   * - :class:`ExpectMultiColumnSum`
     - .. impl-icon:: pandas
   * - :class:`ExpectMultiColumnValuesToBeUnique`
     -
   * - :class:`ExpectMultiColumnValuesToBeUniqueWithinRecord`
     -

Table Expectations
------------------

.. list-table::
   :header-rows: 1

   * - Expectation
     - Implementations
   * - :class:`ExpectColumnToExist`
     - .. impl-icon:: pandas
   * - :class:`ExpectTableColumnCount`
     - .. impl-icon:: pandas
   * - :class:`ExpectTableColumnsToBeInSet`
     - .. impl-icon:: pandas
   * - :class:`ExpectTableColumnsToMatchOrderedList`
     - .. impl-icon:: pandas
   * - :class:`ExpectTableRowCount`
     - .. impl-icon:: pandas
