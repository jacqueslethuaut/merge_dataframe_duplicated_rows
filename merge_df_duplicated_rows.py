# merge_df_duplicated_rows.py

import pandas as pd


def merge_duplicated_rows_with_col_as_key(df:pd.DataFrame, col:str)->pd.DataFrame:
    """_summary_
        Merge duplicated rows of a DataFrame
        'col' will be the key to find out duplicated rows

    Args:
        df (pd.DataFrame): the DataFrame to operate in
        col (str): the key for finding duplicated rows

    Returns:
        pd.DataFrame: a DataFrame without duplicated rows
    """    
    lmbd = lambda x: ''.join if np.dtype(x)=='str' else x.max()
    
    numeric_columns = df.select_dtypes(include=['number']).columns
    non_numeric_columns = df.select_dtypes(exclude=['number']).columns
    print(non_numeric_columns)
    df[numeric_columns] = df[numeric_columns].fillna(0)
    df[non_numeric_columns] = df[non_numeric_columns].fillna('')

    return df.replace('None','').groupby(col, as_index=False).agg(lmbd)