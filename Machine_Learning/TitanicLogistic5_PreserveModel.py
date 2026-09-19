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


# Step 3: Performs splitting activity
#------------------------------------------------------------------------------------------
# Function name splitDataset
# Description : This function is used to perform splitting activity on the preprocessed data
# Input : Dataframe
# Output : 4 sets of data (X_train, X_test, Y_train, Y_test)
# Author : Mangesh Kulkarni
# Date : 16/08/2026
#------------------------------------------------------------------------------------------
def splitDataset(df):
    Border = "-" * 50
    print("Splitting dataset into training and testing sets...")
    print(Border)

    X = df.drop('Survived', axis=1)
    Y = df['Survived']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("Dataset split successfully!")
    print(Border)
    print(f"Training set size: {X_train.shape[0]} samples")
    print(f"Testing set size: {X_test.shape[0]} samples")
    print(Border)

    return X_train, X_test, Y_train, Y_test


# Step 4: Performs Model training activity
#------------------------------------------------------------------------------------------
# Function name trainModel
# Description : This function is used to train the logistic regression model
# Input : Training data (X_train, Y_train)
# Output : Trained model
# Author : Mangesh Kulkarni
# Date : 16/08/2026
#------------------------------------------------------------------------------------------
def trainModel(X_train, Y_train):
    Border = "-" * 50
    print("Training Logistic Regression model...")
    print(Border)

    model = LogisticRegression(max_iter=1000)
    model = model.fit(X_train, Y_train)
    print("Model trained successfully!")
    return model

# Step 4: Performs evaluation of the model
#------------------------------------------------------------------------------------------
# Function name evaluateModel
# Description : This function is used to evaluate the model on the test data and print the accuracy, confusion matrix, and classification report
# Input : Trained model, Test data (X_test, Y_test)
# Output : Evaluation metrics
# Author : Mangesh Kulkarni
# Date : 16/08/2026
#------------------------------------------------------------------------------------------
def evaluateModel(model, X_test, Y_test):
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)
    print(f"Model Accuracy: {accuracy}")
    print("Confusion Matrix:")
    print(confusion_matrix(Y_test, Y_pred)) 

# Step 6: Preserves the model
#------------------------------------------------------------------------------------------
# Function name preserveModel
# Description : This function is used to preserve the trained model to a file
# Input : Trained model, Filename
# Output : None
# Author : Mangesh Kulkarni
# Date : 16/08/2026
#------------------------------------------------------------------------------------------
def preserveModel(model,fileName):
    joblib.dump(model, fileName)
    print(f"Model preserved successfully to {fileName}!")
    
#------------------------------------------------------------------------------------------
# Function name Main
# Description : This function is the main entry point of the program. It calls the LoadData function to load the Titanic dataset and performs logistic regression analysis.
# Input : none
# Output : none
# Author : Mangesh Kulkarni
# Date : 16/08/2026
#------------------------------------------------------------------------------------------
def main():
    # Step 1: Load the dataset
    df = LoadData("MarvellousTitanicDataset.csv")
    # Step 2: Preprocess the data
    df = preprocessData(df)
    # Step 3: Split the dataset into training and testing sets
    X_train, X_test, Y_train, Y_test = splitDataset(df)
    # Step 4: Train the logistic regression model
    model = trainModel(X_train, Y_train)
    # Step 5: Evaluate the model
    evaluateModel(model, X_test, Y_test)
    # Step 6: Preserve the model
    preserveModel(model, "MarvellousTitanic.pkl")

if __name__ == "__main__":
    main()