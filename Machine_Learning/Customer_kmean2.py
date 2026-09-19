import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def main():
    # Load the dataset
    csv = "Mall_Customers.csv"
    df = pd.read_csv(csv)
    print("Dataset loaded successfully!")
    print(df.head())
    print("Missing values")
    print(df.isnull().sum())

    # Step 2 :Feature selection
    X = df[["AnnualIncome","SpendingScore"]]
    print("Selected features:")
    print(X.head())

    

if __name__ == "__main__":
    main()