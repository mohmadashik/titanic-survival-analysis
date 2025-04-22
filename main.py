# main.py
import os
from scripts.data_loader import load_titanic_data
from scripts.preprocessing import fill_missing_age
from scripts.analysis import calculate_survival_rate
from scripts.visualization import plot_survival_rate

DATA_PATH = 'data/titanic.csv'
RESULTS_DIR = 'results'
PLOT_FILE = os.path.join(RESULTS_DIR, 'survival_rate_plot.png')

def main():
    # Ensure results directory exists
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Data pipeline
    df = load_titanic_data(DATA_PATH)
    df = fill_missing_age(df)
    survival_df = calculate_survival_rate(df)
    
    # Plot and save output
    plot_survival_rate(survival_df, output_path=PLOT_FILE)

if __name__ == "__main__":
    main()
