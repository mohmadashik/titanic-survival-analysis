# tests/test_preprocessing.py
import pandas as pd
from scripts.preprocessing import fill_missing_age

def test_fill_missing_age():
    df = pd.DataFrame({'Age': [22, None, 35, None, 28]})
    result = fill_missing_age(df)
    assert result['Age'].isnull().sum() == 0
    assert result['Age'].iloc[1] == 28  # Median of [22, 35, 28] = 28
