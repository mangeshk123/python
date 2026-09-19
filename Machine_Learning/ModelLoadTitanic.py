import pandas as pd
import joblib

def load_model(model_path):
    # Load the model from the specified path
    model = joblib.load(model_path)
    print(f"Model loaded successfully from {model_path}!")
    print(model.feature_names_in_)  # Print the feature names used in the model
    return model

def predict_survival(model):
    print("Enter the following details to predict survival:")
    pclass = int(input("Passenger Class (1, 2, or 3): "))
    sex = int(input("Sex (male(0) or female(1)): "))
    Age = float(input("Age: "))
    sibsp = int(input("Number of Siblings/Spouses Aboard: "))
    parch = int(input("Number of Parents/Children Aboard: "))
    fare = float(input("Fare: "))
    embarked = int(input("Port of Embarkation (0, 1, or 2): "))
    # Make prediction
    input_data = {"pclass":pclass,"sex":sex,"Age":Age,"sibsp":sibsp,"parch":parch,"fare":fare,"embarked":embarked}
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    return prediction

def main():
    model_path = "MarvellousTitanic.pkl"  # Path to the saved model
    model = load_model(model_path)
    prediction = predict_survival(model)
    print(f"Predicted Survival: {'Survived' if prediction[0] == 1 else 'Did not survive'}")

if __name__ == "__main__":
    main()