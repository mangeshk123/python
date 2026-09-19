from PIL import Image
import numpy as np

img = Image.open("digit_28x28.png")
img = img.convert("L")
img = img.resize((28,28))
pixel = np.array(img)
print("Image size : ",pixel.shape)
print("Pixel values : ")
print(pixel)

# 0   pure nlack
# 255 pure white
# 50 Dark gray
# 120 medium gray
# 200 light gray