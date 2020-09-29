def add_columns(df, func, stats, colnames):
    rlt = func(df[stats])
    df.loc[:, colnames] = rlt
    return(df)
