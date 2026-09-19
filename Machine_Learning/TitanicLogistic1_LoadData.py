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

#------------------------------------------------------------------------------------------
# Function name Main
# Description : This function is the main entry point of the program. It calls the LoadData function to load the Titanic dataset and performs logistic regression analysis.
# Input : none
# Output : none
# Author : Mangesh Kulkarni
# Date : 16/08/2026
#------------------------------------------------------------------------------------------
def main():
    LoadData("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()