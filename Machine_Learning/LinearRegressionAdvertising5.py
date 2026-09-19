import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def marvellousRegression(DataPath):
    Border = "-" * 50
    # Load the dataset
    print(f"Loading data from {DataPath}...")
    df = pd.read_csv(DataPath)

    print(df)
    # Define features and target
    # Remove unwanted columns
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    print(Border)
    print(df.head())

    #Step 3
    # Check missing values
    print(Border)
    print("Checking for missing values...")
    print(Border)
    print("Total missing values:")
    print(df.isnull().sum())
    print(Border)

    # Step 4 Statstical summary of data
    print(Border)
    print("Step 4 : Statistical summary of data:")
    print(Border)
    print(df.describe())
    print(Border)

    # Step 5 : Correlation between features and target
    print(Border)
    print("Step 5 : Correlation between features and target")
    print(Border)
    print(df.corr())
    print(Border)

    # Step 6 : Saperate Dependent and Independent variables
    print(Border)
    print("Step 6 : Split Dependent and Independent variables")
    print(Border)
    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']
    print(Border)
    print("Independent variables (X):")
    print(X.head())
    print(Border)
    print("Dependent variable (Y):")
    print(Y.head())
    print(Border)

def main():
    marvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()