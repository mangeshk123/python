import numpy as np
import pandas as pd
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Load the dataset
#------------------------------------------------------------------------------------------
# Function name LoadData
# Description : This function is used to load the data from csv file
# Input : Path of csv file
# Output : Dataframe
# Author : Mangesh Kulkarni
# Date : 16/08/2026
#------------------------------------------------------------------------------------------
def LoadData(DataPath):
    Border = "-" * 50
    print(f"Loading data from {DataPath}...")
    df = pd.read_csv(DataPath)
    print(Border)
    print("Data loaded successfully!")
    print(df.head())
    print(Border)
    return df

# Step 2: Preprocess the data
#------------------------------------------------------------------------------------------
# Function name preprocessData
# Description : This function is used to preprocess the loaded data
# Input : Dataframe
# Output : Updated Dataframe
# Author : Mangesh Kulkarni
# Date : 16/08/2026
#------------------------------------------------------------------------------------------
def preprocessData(df):
    Border = "-" * 50
    print("Preprocessing data...")
    print(Border)

    df = df.drop(columns=['Passengerid', 'zero'])
    print("Columns dropped successfully!")
    # Handle missing values
    print(Border)
    print("Checking for missing values...") 
    print(Border)
    print("Total missing values:")
    print(df.isnull().sum())
    print(Border)

    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    print("Missing values handled successfully!")

    # Convert categorical to numeric data
    df = pd.get_dummies(df, columns=['Embarked'], drop_first=True, dtype=int)

    print(df.head())

    return df


#------------------------------------------------------------------------------------------
# Function name Main
# Description : This function is the main entry point of the program. It calls the LoadData function to load the Titanic dataset and performs logistic regression analysis.
# Input : none
# Output : none
# Author : Mangesh Kulkarni
# Date : 16/08/2026
#------------------------------------------------------------------------------------------
def main():
    df = LoadData("MarvellousTitanicDataset.csv")
    df = preprocessData(df)

if __name__ == "__main__":
    main()