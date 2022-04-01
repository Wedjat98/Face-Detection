import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1 cv2 read
img = cv.imread('img/cat0.png')
# img = cv.imread('img/cat0.png', 0)
cv.imshow('cv_cat', img)
cv.waitKey(0)
cv.destroyAllWindows()
# cv.imwrite('img/cat0_gray.png', img)

# 2 plt read
# plt.imshow(img) BGR need reverse to RBG
# plt.imshow(img, cmap=plt.cm.gray)  plt read needs 'cmap=plt.cm.gray'
# plt.imshow(img[:, :, ::-1])
# plt.title('plt_cat'), plt.xticks([]), plt.yticks([])
# plt.show()

