# scripts/visualization.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_survival_rate(df: pd.DataFrame, output_path: str = None):
    """Plots a bar chart of survival rate by Sex and Pclass."""
    plt.figure(figsize=(8, 6))
    sns.barplot(data=df, x='Pclass', y='SurvivalRate', hue='Sex')

    plt.title('Survival Rate by Class and Gender')
    plt.ylabel('Survival Rate')
    plt.xlabel('Passenger Class')

    if output_path:
        plt.savefig(output_path)
        print(f"Plot saved to {output_path}")
    else:
        plt.show()
