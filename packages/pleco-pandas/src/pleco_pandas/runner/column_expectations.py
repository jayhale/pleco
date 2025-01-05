import numpy as np
import pandas as pd

import pleco


def expect_column_distinct_values_to_be_in_set(
    expectation: pleco.ExpectColumnValuesToBeInSet, data: pd.DataFrame
) -> pleco.RecordCountResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    failure_count = (~series.isin(expectation.value_set)).sum()
    return expectation.build_result(observation_count, failure_count)


def expect_column_distinct_values_to_contain_set(
    expectation: pleco.ExpectColumnValuesToContainSet, data: pd.DataFrame
) -> pleco.RecordCountResult:
    series = data[expectation.column]
    observed_set = series.unique()
    observation_count = observed_set.shape[0]
    failure_count = np.setdiff1d(
        list(expectation.value_set), observed_set, assume_unique=True
    ).shape[0]
    return expectation.build_result(observation_count, failure_count)


def expect_column_distinct_values_to_equal_set(
    expectation: pleco.ExpectColumnValuesToEqualSet, data: pd.DataFrame
) -> pleco.RecordCountResult:
    series = data[expectation.column]
    observed_set = series.unique()
    observation_count = observed_set.shape[0]
    left_failure_count = np.setdiff1d(
        list(expectation.value_set), observed_set, assume_unique=True
    ).shape[0]
    right_failure_count = np.setdiff1d(
        observed_set, list(expectation.value_set), assume_unique=True
    ).shape[0]
    return expectation.build_result(
        observation_count, left_failure_count + right_failure_count
    )


def expect_column_max(
    expectation: pleco.ExpectColumnMax, data: pd.DataFrame
) -> pleco.ValueResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    observed_value = series.max()
    return expectation.build_result(observation_count, observed_value)


def expect_column_mean(
    expectation: pleco.ExpectColumnMean, data: pd.DataFrame
) -> pleco.ValueResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    observed_value = series.mean()
    return expectation.build_result(observation_count, observed_value)


def expect_column_median(
    expectation: pleco.ExpectColumnMedian, data: pd.DataFrame
) -> pleco.ValueResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    observed_value = series.median()
    return expectation.build_result(observation_count, observed_value)


def expect_column_min(
    expectation: pleco.ExpectColumnMin, data: pd.DataFrame
) -> pleco.ValueResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    observed_value = series.min()
    return expectation.build_result(observation_count, observed_value)


def expect_column_mode(
    expectation: pleco.ExpectColumnMode, data: pd.DataFrame
) -> pleco.ValueResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    observed_value = series.mode().min()
    return expectation.build_result(observation_count, observed_value)


def expect_column_quantile(
    expectation: pleco.ExpectColumnQuantile, data: pd.DataFrame
) -> pleco.ValueResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    observed_value = series.quantile(expectation.quantile)
    return expectation.build_result(observation_count, observed_value)


def expect_column_standard_deviation(
    expectation: pleco.ExpectColumnStandardDeviation, data: pd.DataFrame
) -> pleco.ValueResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    observed_value = series.std()
    return expectation.build_result(observation_count, observed_value)


def expect_column_sum(
    expectation: pleco.ExpectColumnSum, data: pd.DataFrame
) -> pleco.ValueResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    observed_value = series.sum()
    return expectation.build_result(observation_count, observed_value)


def expect_column_unique_value_count(
    expectation: pleco.ExpectColumnUniqueValueCount, data: pd.DataFrame
) -> pleco.ValueResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    observed_value = series.unique().shape[0]
    return expectation.build_result(observation_count, observed_value)


def expect_column_value_lengths_to_be_between(
    expectation: pleco.ExpectColumnValueLengthsToBeBetween, data: pd.DataFrame
) -> pleco.RecordCountResult:
    series = data[expectation.column].astype(str)
    observation_count = series.shape[0]
    failure_count = (
        ~series.str.len().between(expectation.length_min, expectation.length_max)
    ).sum()
    return expectation.build_result(observation_count, failure_count)


def expect_column_value_lengths_to_equal(
    expectation: pleco.ExpectColumnValueLengthsToEqual, data: pd.DataFrame
) -> pleco.RecordCountResult:
    series = data[expectation.column].astype(str)
    observation_count = series.shape[0]
    failure_count = (series.str.len() != expectation.length).sum()
    return expectation.build_result(observation_count, failure_count)


def expect_column_values_to_be_between(
    expectation: pleco.ExpectColumnValuesToBeBetween, data: pd.DataFrame
) -> pleco.RecordCountResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    failure_count = (
        ~series.between(expectation.value_min, expectation.value_max)
    ).sum()
    return expectation.build_result(observation_count, failure_count)


def expect_column_values_to_be_null(
    expectation: pleco.ExpectColumnValuesToBeNull, data: pd.DataFrame
) -> pleco.RecordCountResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    failure_count = (~series.isnull()).sum()
    return expectation.build_result(observation_count, failure_count)


def expect_column_values_to_be_unique(
    expectation: pleco.ExpectColumnValuesToBeUnique, data: pd.DataFrame
) -> pleco.RecordCountResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    failure_count = series.duplicated(keep=False).sum()
    return expectation.build_result(observation_count, failure_count)


def expect_column_values_to_not_be_in_set(
    expectation: pleco.ExpectColumnValuesToNotBeInSet, data: pd.DataFrame
) -> pleco.RecordCountResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    failure_count = series.isin(expectation.value_set).sum()
    return expectation.build_result(observation_count, failure_count)


def expect_column_values_to_not_be_null(
    expectation: pleco.ExpectColumnValuesToNotBeNull, data: pd.DataFrame
) -> pleco.RecordCountResult:
    series = data[expectation.column]
    observation_count = series.shape[0]
    failure_count = series.isnull().sum()
    return expectation.build_result(observation_count, failure_count)
