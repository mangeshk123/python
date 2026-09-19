from PIL import Image
import numpy as np

img = Image.open("color.png")
img = img.resize((28,28))

pixels = np.array(img)
print("Image information : ")
print("Image shape ", pixels.shape)
print("height : ", pixels.shape[0])
print("Width : ", pixels.shape[1])
print("Channels : ", pixels.shape[2])

total  = pixels.shape[0] * pixels.shape[1] * pixels.shape[2]

print("Total pixels : ", total)
print(" Single pixel meaning")
r = pixels[10][10][0]
g = pixels[10][10][1]
b = pixels[10][10][2]

print(" Pixels details are ")
print("R",r)
print("G",g)
print("B",b)