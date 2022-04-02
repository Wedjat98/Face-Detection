import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('img/cat0.png')
# path split
b, g, r = cv.split(img)
plt.imshow(b)
# path merge
img = cv.merge((b, g, r))
plt.imshow(img[:, :, ::-1])
plt.title('plt_cat'), plt.xticks([]), plt.yticks([])
plt.show()
