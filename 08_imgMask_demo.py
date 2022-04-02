import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 1. img in grayscale
img = cv.imread('img/cat2.jpeg', 0)
# 2. mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[400:650, 200:500] = 255
# 3. mask img
masked_img = cv.bitwise_and(img, img, mask=mask)
# 4. calculate
mask_hist = cv.calcHist([img], [0], mask, [256], [1, 256])
# 5. show
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].imshow(img, cmap=plt.cm.gray)
axes[0, 0].set_title("origin")
axes[0, 1].imshow(mask, cmap=plt.cm.gray)
axes[0, 1].set_title("Mask")
axes[1, 0].imshow(masked_img, cmap=plt.cm.gray)
axes[1, 0].set_title("Masked")
axes[1, 1].plot(mask_hist)
axes[1, 1].grid()
axes[1, 1].set_title("grayscale")
plt.show()
