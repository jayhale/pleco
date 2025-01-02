import pandas as pd

import pleco


def expect_table_column_count(
    expectation: pleco.ExpectTableColumnCount, data: pd.DataFrame
) -> pleco.Result:
    observed_count = data.shape[1]
    return expectation.build_result(observed_count, observed_count)
