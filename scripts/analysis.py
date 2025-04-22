# scripts/analysis.py
import pandas as pd

def calculate_survival_rate(df: pd.DataFrame) -> pd.DataFrame:
    """Group by Sex and Pclass to calculate survival rate."""
    survival = df.groupby(['Sex', 'Pclass'])['Survived'].mean().reset_index()
    survival.rename(columns={'Survived': 'SurvivalRate'}, inplace=True)
    return survival
