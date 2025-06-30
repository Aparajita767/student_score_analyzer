import pandas as pd
from app.utils import normalize_columns
print('csv_validation loaded successfully')

def validate_csv(file_path: str) -> dict:
    #Read file
    df = pd.read_csv(file_path)

    REQUIRED_COLUMNS = ['student_id','name','score','date']

    #Normalize column names before validation check
    df = normalize_columns(df)

    #Check for missing columns
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    
    if missing_cols:
        raise ValueError(f'Missing columns : {missing_cols}')
    
    #Try to coerce numeric columns
    temp_score = pd.to_numeric(df['score'], errors='coerce')
    nan_ratio = temp_score.isna().sum() / len (temp_score)

    if nan_ratio > 0.2 : 
        raise ValueError(f'Too many invalid scores : {nan_ratio : .0%} are not numeric')
    
    #Try to parse date column
    try:
        pd.to_datetime(df['date'],format='%Y-%m-%d')
    except Exception:
        raise ValueError('Invalid date format in "date" column')
    
    #Check value range for scores
    if temp_score.min() < 0 or temp_score.max() > 100:
        raise ValueError('Scores must be between 0 and 100')
    
    #If validation successful return info
    return {
        'rows' : len(df),
        'columns' : df.columns.tolist(),
        'invalid_score_ratio': nan_ratio
    }
    