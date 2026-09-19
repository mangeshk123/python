import numpy as np
from sklearn.linear_model import LinearRegression
def main():
    X = np.array([[1], [2], [3], [4], [5]])
    Y = np.array([50,55,60,65,70])
    model = LinearRegression()
    model = model.fit(X,Y)
    print("Prediction for x=6 is ", model.predict([[6]]))
    print("Slope of line is ", model.coef_)

if __name__ == "__main__":
    main()