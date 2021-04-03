from tsfresh.utilities.dataframe_functions import roll_time_series
from tsfresh import extract_features
import pandas as pd


def test_features_on_btc():
    
    df = pd.DataFrame({
        "id": [1, 1, 1, 1, 2, 2],
        "time": [1, 2, 3, 4, 8, 9],
        "x": [1, 2, 3, 4, 10, 11],
        "y": [5, 6, 7, 8, 12, 13],
        })

    df_rolled = roll_time_series(df, column_id="id", column_sort="time")
    assert df_rolled['id'].nunique() == 6
    df_features = extract_features(df_rolled, column_id="id", column_sort="time")
    assert df_features.shape[0] == 6
