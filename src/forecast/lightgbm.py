from tsfresh.utilities.dataframe_functions import roll_time_series
from tsfresh import extract_features


class lgbm:
    def __init__(self, df, id, column_sort):
        self.df = df
        self.id = id
        self.column_sort = column_sort

    def get_rolling_windows(self):
        self.df_rolled = roll_time_series(self.df, column_id=self.id, 
                                          column_sort=self.column_sort)
    
    def get_rolling_features(self):
        self.get_rolling_windows()
        self.df_features = extract_features(df_rolled, column_id=self.id, 
                                            column_sort=self.column_sort)
        return(self.features)
    
