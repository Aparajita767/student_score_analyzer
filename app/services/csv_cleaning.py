import pandas as pd
from pathlib import Path
import os

def handle_date_column(df):
    '''
    Converts 'date' column to datetime if exists.

    Returns : 
        tuple : (cleaned_df, invalid_date_count)
    '''
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        invalid_dates = df['date'].isnull().sum()
    else:
        invalid_dates = 'N/A'
    return df, invalid_dates

def clean_column_names(df):
    '''
    Standardize column names by converting to lowercase and stripping whitespace
    
    Parameters : Dataframe

    Returns : Dataframe with normalized column names
    '''
    df.columns = [col.strip().lower() for col in df.columns]
    return df

def is_numeric_like(value):
    '''
    Check if single value can be interpreted as a numeric value.
    Supports integers, floats and negatives
    '''
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def is_mostly_numeric(series, threshold = 0.7):
    '''
    Checks if an object type column has numeric values above a defined threshold

    Parameters : 
        series (pd.Series) : column to check.
        threshold (float) : Proportion of values that must be numeric-like

    Returns : 
        bool : True if mostly numeric, False if otherwise.
    '''
    non_null = series.dropna()
    if non_null.empty:
        return False
    numeric_count = non_null.apply(is_numeric_like).sum()
    return ((numeric_count/len(non_null)) >= threshold)

def convert_numeric_columns( df , exclude_columns = None , threshold = 0.7):
    '''
    Converts object columns that are mostly numeric to numeric type

    Parameters : 
        df (pd.Dataframe) : The DataFrame to modify
        exclude_columns(list): Columns to exclude from conversion.

    Returns : 
        tuple : (updated_df, converted_columns)
    '''
    if exclude_columns is None:
        exclude_columns = []
    
    converted_columns = []

    object_columns = df.select_dtypes(include = 'object').columns

    for col in object_columns:
        if col not in exclude_columns and is_mostly_numeric(df[col],threshold):
            df[col] = pd.to_numeric(df[col],errors='coerce')
            converted_columns.append(col)
    
    return df, converted_columns

def clean_csv(filename):
    '''
    Main cleaning function for a CSV file.

    Parameters : 
        filename (str) : The CSV file name inside the data folder

    Returns :
    '''
    # Extract filename using path and filepath using os.join
    file_name = Path(filename).name
    file_path = os.join('data', file_name)

    # Load the file
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return {'error' : f'File {file_name} not found'}
    except pd.errors.ParserError:
        return {'error': f'Failed to parse file {file_name}'}
    except Exception as e:
        return {'error' : f'Unexpected error {str(e)}'}
    
    # Logging initial info
    initial_info = {
        'Initial Shape' : df.shape(),
        'Missing Values' : df.isnull().sum().to_dict()
    }

    # Normalize column names
    df = clean_column_names(df)

    # Convert date column if present
    df, invalid_dates = handle_date_column(df)

    # Remove date column to avoid accidental conversion
    exclude = ['date'] if 'date' in df.columns else []
    #Convert mostly numeric columns to numeric
    df , numeric_converted = convert_numeric_columns(df, exclude_columns= exclude)

    #Final Summary
    return df