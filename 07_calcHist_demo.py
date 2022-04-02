import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 1 in grayscale
img = cv.imread('img/cat1.png', 0)
# 2 calculate
hist = cv.calcHist([img], [0], None, [256], [0, 256])
# 3 draw
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(hist)
plt.grid()
plt.show()
