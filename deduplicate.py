# deduplicate.py

import pandas as pd
import numpy as np

from pandas.api.types import is_datetime64_any_dtype

def merge_rows(df:pd.DataFrame, col_key:str) -> pd.DataFrame:
    if df[col_key].dtype != 'object':
        raise ValueError('The key column should contain strings.')
    
    lmbd = lambda x: ''.join if np.dtype(x)=='str' else x.max()
    
    numeric_columns = df.select_dtypes(include=['number']).columns
    non_numeric_columns = df.select_dtypes(exclude=['number']).columns
    print(non_numeric_columns)
    df[numeric_columns] = df[numeric_columns].fillna(0)
    df[non_numeric_columns] = df[non_numeric_columns].fillna('')

    return df.replace('None','').groupby(col_key, as_index=False).agg(lmbd)


def remove_duplicates(df:pd.DataFrame, col_key:str, col_date:str) -> pd.DataFrame:
    if df[col_key].dtype != 'object':
        raise ValueError('The key column should contain strings.')
    
    if not is_datetime64_any_dtype(df[col_date]): 
        raise ValueError('The datetime column should be of datetime type.')
    
    df = df.sort_values(col_date, ascending=False)
    df = df.drop_duplicates(subset=col_key, keep='first')
    
    return df
