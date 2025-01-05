import pandas as pd

import pleco


def expect_multi_column_sum(
    expectation: pleco.ExpectMultiColumnSum, data: pd.DataFrame
) -> pleco.ValueResult:
    data_frame = data[expectation.columns]
    observation_count = data_frame.shape[0] * data_frame.shape[1]
    observed_value = data_frame.sum().sum()
    return expectation.build_result(observation_count, observed_value)
