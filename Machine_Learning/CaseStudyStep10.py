import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay)



########################################################
#      Step 1 load the dat set
########################################################

def addBorder(Border, Text):
    print(Border)
    print(Text)
    print(Border)


def loadDataset(Datapath, Border):
    addBorder(Border, "Step 1 : load the data set")
    df = pd.read_csv(Datapath)
    print("Dataet loaded successfully")
    print("Initial data is ")
    print(df.head())
    return df


########################################################
#      Step 2 Data analysis (EDA)
########################################################
def dataAnalysis(df, Border):
    addBorder(Border,"Step 2 Data analysis (EDA)")
    
    print("Shape fo dataset: " , df.shape)
    print("Column names", list(df.columns))
    print("Missing values per columns : ")
    print(df.isnull().sum())

    print("Class distribution (species count) ")
    print(df["species"].value_counts())

    print("Statistical report of dataset : ")
    print(df.describe())

########################################################
#      Step 3 Decide independent and dependent variable
########################################################
def splitDataInLabelsAndFetures(df, Border):
    addBorder(Border, "Step 3 Decide independent and dependent variable")
    feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]
    X = df[feature_cols]
    Y = df["species"]
    return X,Y


########################################################
#      Step 4 Visualization of dataset
########################################################
def renderdataset(df, Border):
    addBorder(Border,"Step 4 Visualization of dataset")
    # Scatter 
    plt.figure(figsize=(7,5))

    for sp in df[ "species"].unique():
        temp = df[df[ "species"] == sp]
        plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"], label =sp)

    plt.title("Iris case study")
    plt.xlabel("Petal length")
    plt.xlabel("Petal width")
    plt.legend()
    plt.grid()
    plt.show()


########################################################
#      Step 5 split the data for training
########################################################
def splitTrainingData(X, Y, Border):
    addBorder(Border, "Step 5 split the data for training")
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)
    print("Dataset splitting done")
    return X_train, X_test, Y_train, Y_test


########################################################
#      Step 6 Build model
########################################################
def buildModel(Border):
    addBorder(Border, "Step 6 Build model")
    model = DecisionTreeClassifier(max_depth= 8)
    print("Model gets created succesfully")
    return model


########################################################
#      Step 7 Train model
########################################################
def trainModel(model,X_train,Y_train,Border):
    addBorder(Border,"Step 7 Train model")    
    model.fit(X_train, Y_train)
    print("Model trained successfully")



########################################################
#      Step 8 Evaluate model
########################################################
def testModel(model, X_test, Y_test, Border):
    addBorder(Border, "Step 8 Evaluate model")
    Y_pred = model.predict(X_test)
    print("Model testing done")
    return Y_pred


########################################################
#      Step 9 Evaluate model
########################################################
def accuracyCheckForModel(model, Y_test, Y_pred, Border):
    addBorder(Border,"Step 8 Evaluate model")
  
    accuracy = accuracy_score(Y_test, Y_pred)
    print("accuracy_score ",accuracy*100)
    cm = confusion_matrix(Y_test, Y_pred)
    print("confusion_matrix :",cm)

    showConfusionMatrix(model, cm)

def showConfusionMatrix(model, cm):
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=model.classes_)

    fig, ax = plt.subplots(figsize=(6,6))
    disp.plot(cmap="Blues", ax=ax, values_format="d")
    plt.title("Confusion Matrix - Iris Classification")
    plt.show()


def main():
    Border = "-"*30
    Datapath = "iris.csv"

    df = loadDataset(Datapath, Border)
    dataAnalysis(df, Border)
    X, Y = splitDataInLabelsAndFetures(df,Border)
    X_train, X_test, Y_train, Y_test = splitTrainingData(X,Y, Border)
    renderdataset(df, Border)    
    model = buildModel(Border)
    trainModel(model,X_train,Y_train,Border)
    Y_pred = testModel(model, X_test,Y_test,Border)
    accuracyCheckForModel(model, Y_test, Y_pred, Border)
    
if __name__ == "__main__":
    main()
