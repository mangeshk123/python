import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def marvellousPredictor():
    # Load the data
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]
    print("Values of independent vars X :", X)
    print("Values of dependent vars Y :", Y)

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("Mean_X is : ",mean_X)
    print("Mean_Y is : ",mean_Y)
    
def main():
    marvellousPredictor()
if __name__ == "__main__":
    main()