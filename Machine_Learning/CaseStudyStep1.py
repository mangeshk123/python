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