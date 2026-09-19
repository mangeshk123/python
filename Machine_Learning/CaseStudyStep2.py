import pandas as pd

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