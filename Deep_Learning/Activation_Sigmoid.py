import numpy as np
import math

def sigmoid(z):
    return 1/ (1+ math.exp(-z))

def marvellous_neuron_forword(inputs, weights, bias):
    print(" inputs are ", inputs)
    print(" weights are ", weights)
    print(" bias is ", bias)
    z = 0
    for i in range(len(inputs)):
        z = z + (inputs[i]* weights[i])

    z = z + bias
    
    # z = sum(w*x for w,x in zip(weights, inputs)) + bias
    print(" weighted sum = ", z)

    y = sigmoid(z)
    return y

def main():
    print(" Marvellous neural network")
    inputs = [1.0,2.0,3.0]
    weights = [0.6, 0.4,-0.2]
    bias = 0.5
    result = marvellous_neuron_forword(inputs, weights, bias)
    print("Predicted result is ", result)

if __name__ == "__main__":
    main()