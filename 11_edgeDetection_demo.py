import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 1 img read
img = cv.imread('img/sleep cat.jpeg', 0)
# 2 calculate Sobel convolution result
x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=-1)  # sobel don't has ksize
y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=-1)  # Scharr ksize=-1
# 3 data reverse
Scale_absX = cv.convertScaleAbs(x)  # convert 转换  scale 缩放
Scale_absY = cv.convertScaleAbs(y)
# 4 compose the result
result = cv.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
# 5 img show
plt.figure(figsize=(10, 8), dpi=100)
plt.subplot(121), plt.imshow(img, cmap=plt.cm.gray), plt.title('origin')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(result, cmap=plt.cm.gray), plt.title('result')
plt.xticks([]), plt.yticks([])
plt.show()
