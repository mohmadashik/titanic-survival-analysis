# scripts/preprocessing.py
import pandas as pd

def fill_missing_age(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing Age values with median age."""
    df['Age'] = df['Age'].fillna(df['Age'].median())
    return df
