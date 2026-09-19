import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
#---------------------------------------------------------
# Step 1: Read from csv
#---------------------------------------------------------
df = pd.read_csv("breast_cancer.csv")
print("Shape of dataset :", df.shape)
print(df.head)

#---------------------------------------------------------
# Step 2: saperate feature and labels
#---------------------------------------------------------
X = df.drop("target",axis = 1)
Y = df["target"]
print("X shape: ", X.shape)
print("Y shape: ", Y.shape)

#---------------------------------------------------------
# Step 3: split dataset 
#---------------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2, random_state=42)

#---------------------------------------------------------
# Step 4: scale the features 
#---------------------------------------------------------

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.fit_transform(X_test)

#---------------------------------------------------------
# Step 5: Create model 
#---------------------------------------------------------
model = DecisionTreeClassifier(random_state=42)

#---------------------------------------------------------
# Step 6: train model 
#---------------------------------------------------------
model = model.fit(X_train,X_test)
#---------------------------------------------------------
# Step 7: tEST model 
#---------------------------------------------------------

Y_pred = model.predict(Y_test)
#---------------------------------------------------------
# Step 8: Evaluate model 
#---------------------------------------------------------
print("Accuracy : ", accuracy_score(Y_test,Y_pred))

