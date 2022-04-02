import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# 1 img read
img1 = cv.imread("img/view.jpg")
img2 = cv.imread("img/rain.jpg")

# 2 add
img3 = cv.add(img1, img2)
img4 = img1 + img2

# 3.1 show
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 8), dpi=100)
axes[0].imshow(img3[:, :, ::-1])
# axes[0].set_title("openCV_add")
axes[1].imshow(img4[:, :, ::-1])
# axes[1].set_title("Straight_add")

img5 = cv.addWeighted(img1, 0.7, img2, 0.3, 0)  # mix    dst = α⋅img1 + β⋅img2 + γ

# 3.2 show
plt.figure(figsize=(8, 8))
plt.imshow(img5[:, :, ::-1])
plt.show()

