import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1 img read
img1 = cv.imread("img/letter-open.png")
img2 = cv.imread("img/letter-close.png")
# 2 create kernel
kernel = np.ones((10, 10), np.uint8)
# 3 MORPH_OPEN & MORPH_CLOSE
# cvOpen = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel)  # open
# cvClose = cv.morphologyEx(img2, cv.MORPH_CLOSE, kernel)  # close

cvOpen = cv.morphologyEx(img1, cv.MORPH_TOPHAT, kernel)  # TOPHAT
cvClose = cv.morphologyEx(img2, cv.MORPH_BLACKHAT, kernel)  # BLACKHAT
# 4 show
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes[0, 0].imshow(img1)
axes[0, 0].set_title("origin")
axes[0, 1].imshow(cvOpen)
axes[0, 1].set_title("MORPH_OPEN")
axes[1, 0].imshow(img2)
axes[1, 0].set_title("origin")
axes[1, 1].imshow(cvClose)
axes[1, 1].set_title("MORPH_CLOSE")
plt.show()
