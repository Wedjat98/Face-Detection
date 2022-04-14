import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1 read
img = cv.imread("img/letter.png")
# 2 core
kernel = np.ones((5, 5), np.uint8)

# 3 erosion  dilate
erosion = cv.erode(img, kernel)  # erosion
dilate = cv.dilate(img, kernel)  # dilate

# 4 img show
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 8), dpi=100)
axes[0].imshow(img)
axes[0].set_title("Origin")
axes[1].imshow(erosion)
axes[1].set_title("erosion result")
axes[2].imshow(dilate)
axes[2].set_title("dilate result")
plt.show()
