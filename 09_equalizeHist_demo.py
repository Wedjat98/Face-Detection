import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 1. grayscale
img = cv.imread('img/cat2.jpeg', 0)
# 2. equalize
dst = cv.equalizeHist(img)
# 3. show
# plt.imshow(img, cmap=plt.cm.gray)
# plt.imshow(dst, cmap=plt.cm.gray)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img, cmap=plt.cm.gray)
axes[0].set_title("origin")
axes[1].imshow(dst, cmap=plt.cm.gray)
axes[1].set_title("result")
plt.show()
