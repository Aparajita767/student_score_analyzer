'''
A file for general purpose helper functions
'''
import pandas as pd

def normalize_columns(df : pd.DataFrame) -> pd.DataFrame:
    '''
    Helper function to normalize column names

    Parameters : pd.DataFrame

    Returns : pd.DataFrame
    '''
    df.columns = (
        df.columns.str.strip().str.lower().str.replace(' ','_')
    )
    return df