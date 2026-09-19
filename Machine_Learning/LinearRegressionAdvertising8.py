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
    print("Step 6 : Saperate Dependent and Independent variables")
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

    # Step 7 : Split the dataset into training and testing sets
    print(Border)
    print("Step 7 : Split the dataset into training and testing sets")
    print(Border)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print("Training set:")
    print(f"X_train: {X_train.shape} samples")
    print(f"Y_train: {Y_train.shape} samples")
    print("Testing set:")
    print(f"X_test: {X_test.shape} samples")    
    print(f"Y_test: {Y_test.shape} samples")
    print(Border)  

    #Step 8: Create and train model
    print(Border)
    print("Step 8 : Create and train model")
    print(Border)
    model = LinearRegression()
    model = model.fit(X_train, Y_train)
    print("Model trained successfully!")

    # Step 9: Test the model
    print(Border)
    print("Step 9 : Test the model")
    print(Border)
    Y_pred = model.predict(X_test)
    print("Predictions:")
    print("Expected Answers:")
    print(Y_test[:3])
    print("Predicted Answers:")
    print(Y_pred[:3])

    # Step 10: Evaluate the model
    print(Border)
    print("Step 10 : Evaluate the model")
    print(Border)
    MSE = mean_squared_error(Y_test, Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test, Y_pred)
    print(f"Mean Squared Error: {MSE}")
    print(f"Root Mean Squared Error: {RMSE}")
    print(f"R-squared: {R2}")
    print(Border)

    #Step 11: Display the coefficients and intercept of the model
    print(Border)
    print("Step 11 : Display the coefficients and intercept of the model")
    print(Border)
    print(f"TV Coefficient: {model.coef_[0]}")
    print(f"Radio Coefficient: {model.coef_[1]}")
    print(f"Newspaper Coefficient: {model.coef_[2]}")
    print(f"Intercept: {model.intercept_}")

def main():
    marvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()