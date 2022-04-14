import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1 read img and reverse to gary mode
img = cv.imread('img/mosaic.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 2 corner detection
# 2.1 inputted img must be float32
gray = np.float32(gray)
# 2.2 last arg is between 0.04 and 0.05
dst = cv.cornerHarris(gray, 2, 3, 0.04)
# 3 set a max value,draw to the img
img[dst > 0.001 * dst.max()] = [0, 0, 255]
# 4 img show
plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(img[:, :, ::-1]), plt.title('Harris')
plt.xticks([]), plt.yticks([])
plt.show()
