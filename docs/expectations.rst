.. py:currentmodule:: pleco

======================
Expectations Reference
======================

Pleco provides a set of tested and well-supported expectations that cover many common
data validation needs.

Column Aggregate Expectations
-----------------------------

.. toctree::
   :hidden:

   expectations/expect_column_kl_divergence
   expectations/expect_column_max
   expectations/expect_column_mean
   expectations/expect_column_median
   expectations/expect_column_min
   expectations/expect_column_mode
   expectations/expect_column_proportion_of_unique_values
   expectations/expect_column_quantile
   expectations/expect_column_standard_deviation
   expectations/expect_column_sum
   expectations/expect_column_unique_value_count

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

.. toctree::
   :hidden:

   expectations/expect_column_value_lengths_to_be_between
   expectations/expect_column_value_lengths_to_equal
   expectations/expect_column_values_to_be_between
   expectations/expect_column_values_to_be_decreasing
   expectations/expect_column_values_to_be_increasing
   expectations/expect_column_values_to_be_in_set
   expectations/expect_column_values_to_be_in_type_set
   expectations/expect_column_values_to_be_json_parseable
   expectations/expect_column_values_to_be_null
   expectations/expect_column_values_to_be_of_type
   expectations/expect_column_values_to_be_unique
   expectations/expect_column_values_to_contain_set
   expectations/expect_column_values_to_equal_set
   expectations/expect_column_values_to_match_json_schema
   expectations/expect_column_values_to_match_like_pattern
   expectations/expect_column_values_to_match_like_pattern_set
   expectations/expect_column_values_to_match_regex
   expectations/expect_column_values_to_match_regex_set
   expectations/expect_column_values_to_match_strftime_format
   expectations/expect_column_values_to_not_be_in_set
   expectations/expect_column_values_to_not_be_null
   expectations/expect_column_values_to_not_match_like_pattern
   expectations/expect_column_values_to_not_match_like_pattern_set
   expectations/expect_column_values_to_not_match_regex
   expectations/expect_column_values_to_not_match_regex_set
   expectations/expect_column_value_z_scores_to_be_between

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
   * - :class:`ExpectColumnValuesToNotMatchRegexSet`
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
