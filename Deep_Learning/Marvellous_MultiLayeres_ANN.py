import numpy as np
import math
#-----------------------------------------
# Step 1 :Input layer 
#-----------------------------------------
x1 = 2.0
x2 = 3.0
print("Step 1 : Input layer")
print(" Input Features : X ")
print("X1 = ", x1)
print("X2 = ", x2)

#-----------------------------------------
# Step 2  hidden layer 
#-----------------------------------------
print("Step 2 : Hidden layer")
print("-------------------- Hidden neuron 1--------------------------")
w11 = 0.5
w12 = -0.2
b1 = 0.1

print("Weights")
print(f"W11 is {w11}")
print(f"W12 is {w12}")

print("Bias is")
print(f"b1 is {b1}")

print("Weighted sum is ")
print("z1")
z1 = (x1*w11) + (x2*w12) + b1
print("Weighted sum is : z1 ", z1)
h1 = max(0,z1)
print("Output of neuron is ", h1)

###################
print("------------------------ Hidden neuron 2---------------------")
w21 = 0.8
w22 = 0.4
b2 = -0.1

print("Weights")
print(f"W21 is {w21}")
print(f"W22 is {w22}")

print("Bias is")
print(f"b2 is {b2}")

print("Weighted sum is ")
print("z2")
z2 = (x1*w21) + (x2*w22) + b2
print("Weighted sum is : z2 ", z2)
h2 = max(0,z2)
print("Output of neuron is ", h2)

#-----------------------------------------
# Step 3  Output layer 
#-----------------------------------------
w_out1 = 1.0
w_out2 = -1.5
b_out = 0.2

print("weights :")
print(f"w_out1 : {w_out1}")
print(f"w_out2 : {w_out2}")

z_out = h1* w_out1 + h2 * w_out2 + b_out
print("Weighted sum :", z_out)
# Sigmoid
z = 1/(1 + math.exp(-z_out))
print("------------------------------")
print("----Neural network summary----")
print("------------------------------")
print("Input layer")
print(f"x1 : {x1}")
print(f"x1 : {x2}")

print("Hidden layer")
print(f"h1 : {h1}")
print(f"h2 : {h2}")

print("output layer")
print(f"z : {z}")

print("predixtion of neural network")
if(z>= 0.5):
    print("predicted as positive class")
else:
    print("predicted as negative class")