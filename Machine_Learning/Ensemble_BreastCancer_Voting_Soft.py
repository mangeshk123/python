import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier


#---------------------------------------------------------
# Step 1: Read from csv
#---------------------------------------------------------
df = pd.read_csv("breast_cancer.csv")
print("Shape of dataset :", df.shape)
print(df.head())

#---------------------------------------------------------
# Step 2: Separate features and labels
#---------------------------------------------------------
X = df.drop("target", axis=1)
Y = df["target"]
print("X shape: ", X.shape)
print("Y shape: ", Y.shape)

#---------------------------------------------------------
# Step 3: Split dataset
#---------------------------------------------------------
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#---------------------------------------------------------
# Step 4: Scale the features
#---------------------------------------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#---------------------------------------------------------
# Step 5.1: Create the individual models
#---------------------------------------------------------
model_log = LogisticRegression(max_iter=1000)
model_det = DecisionTreeClassifier(random_state=42)
model_knn = KNeighborsClassifier(n_neighbors=5)

#---------------------------------------------------------
# Step 5.2: Create the voting model
#---------------------------------------------------------
model = VotingClassifier(estimators=[
    ("logistics",model_log),
    ("decision_tree",model_det),
    ("knn",model_knn)],
    voting="soft"
    )

#---------------------------------------------------------
# Step 6: Train model
#---------------------------------------------------------
model.fit(X_train, Y_train)

#---------------------------------------------------------
# Step 7: Test model
#---------------------------------------------------------
Y_pred = model.predict(X_test)

#---------------------------------------------------------
# Step 8: Evaluate model
#---------------------------------------------------------
print("Accuracy : ", accuracy_score(Y_test, Y_pred))
print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
