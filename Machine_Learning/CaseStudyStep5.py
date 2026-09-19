import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

Border = "_"*30
########################################################
#      Step 1 load the dat set
########################################################

print(Border)
print("Step 1 : load the dat set")
print(Border)
Datapath = "iris.csv"

df = pd.read_csv(Datapath)
print("Dataet loaded successfully")
print("Initial data is ")
print(df.head())

########################################################
#      Step 2 Data analysis (EDA)
########################################################
print(Border)
print("Step 2 Data analysis (EDA)")
print(Border)
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
print(Border)
print("Step 3 Decide independent and dependent variable")
print(Border)
# X : independent variable / Features
# Y : dependent variable / labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    ]

X = df[feature_cols]
Y = df["species"]

print("X.Shape : ",X.shape)
print("Y.Shape : ",Y.shape)

########################################################
#      Step 4 Visualization of dataset
########################################################
print(Border)
print("Step 4 Visualization of dataset")
print(Border)

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
print(Border)
print("Step 5 split the data for training")
print(Border)

X_train,Y_train,X_test,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
print("Dataset splitting done")
print("X", X.shape) # 
print("Y", Y.shape)
print("X_train : ",X_train.shape) # 75,4
print("X_Test : ",X_test.shape) # 75,4
print("Y_train : ",Y_train.shape) # 75,
print("Y_Test : ",Y_test.shape) # 75,