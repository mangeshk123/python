
#-----------------------------------------------------
# Deep learning pipeline
#-----------------------------------------------------
#1.  Read the data from csv
#2.  Data analysis 
#3.  Preprocessing
#4.  Train test split
#5.  Feature scaling
#6.  FNN model scaling
#7.  Model Evaluation
#8.  Graphical representation
#9.  Model preserve 
#10. Model loading and preserve
#11. test unseen data
#----------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Read fromcsv

data =pd.read_csv("placement_data.csv")
print("Data is",data.head())
print("Column names : ")
print(data.columns)
print("Shape of data is :", data.shape)
print("Desc is : ")
print(data.describe())
# Step 3 Preprocessing
print("3. Preprocessing ")
X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]

Y = data[['Placed']]

print("Input features")
print(X.head())
print("Target ")
print(Y.head())
# Step 4 train test split
print("4. train test split")
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3, random_state=42)
print("Training input shape",X_train.shape)
print("Testing input shape",X_test.shape)
print("Training output shape",Y_train.shape)
print("Testing output shape",Y_test.shape)

# 5 feature scaling
print("feature scaling")
scalar = StandardScaler()
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)
print("Scaled training data ")
print(X_train_scaled[:5])
print(X_test_scaled[:5])

# 6 FNN model training
print("6. FNN model training")
model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver='adam',
    random_state=42,
    max_iter=1000
)

print(model)
print("Train the model")

model.fit(X_train_scaled,Y_train)
print("Model is trained")

# 7 Model evaluation
print("Model Evaluation")
Y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy is ", accuracy)
cm  = confusion_matrix(Y_test,Y_pred)
print('Predict rhe probability ')
Y_prob = model.predict_proba(X_test_scaled)
print("Y_prob")
print(Y_prob[:5])
#Step 9 Model preserve
#joblib.dump(model,"placementModel.pkl")
#joblib.dump(scalar,"placement_scalar.pkl")

print("Model gets dumped successfully")

# 10 Model loading and preserve
print("10 Model loading and preserve")
loaded_model = joblib.load("placementModel.pkl")
loaded_scalar = joblib.load("placement_scalar.pkl")

print("Model is loaded successfully")
# 11. Test unseen data
# Aptitude: 70
# Coding : 75
# Communication: 80
# Acadenics: 85
# Internship: 1
new_Student = pd.DataFrame([[70,75,80,85,1]], columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_Student_scaled = loaded_scalar.transform(new_Student)
new_pred = loaded_model.predict(new_Student_scaled)
new_prob = loaded_model.predict_proba(new_Student_scaled)

print("new Student data")
print(new_Student)
print("Probablity is ", new_prob)
if(new_pred[0] == 1):
    print("placed")
else:
    print("not placed")


