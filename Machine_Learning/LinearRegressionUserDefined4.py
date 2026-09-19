import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def marvellousPredictor():
    # Load the data
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]
    print("Values of independent vars X :", X)
    print("Values of dependent vars Y :", Y)
    sum_X = 0
    sum_Y = 0
    for i in range(len(X)):
        sum_X = sum_X + X[i]
        sum_Y = sum_Y + Y[i]
    mean_X = sum_X / len(X)
    mean_Y = sum_Y / len(Y)

    print("Mean_X is : ",mean_X)
    print("Mean_Y is : ",mean_Y)
    n = len(X)
    numerator = 0
    denomerator = 0
    # Calculate slope ie. m
    for i in range(n):
        numerator = numerator + ((X[i] - mean_X)*(Y[i]-mean_Y))
        denomerator = denomerator + ((X[i] - mean_X)**2)
    m  = numerator / denomerator
    print("Slope of line is ", m)
    
    
def main():
    marvellousPredictor()
if __name__ == "__main__":
    main()