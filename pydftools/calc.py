import pandas as pd


class CalcDf(pd.DataFrame):
    def add_columns(self, func, stats, colnames):
        rlt = func(self[stats])
        self.loc[:, colnames] = rlt
