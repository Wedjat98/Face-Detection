import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('img/cat0.png')
# path split
b, g, r = cv.split(img)
# path merge
img = cv.merge((b, g, r))
cv.imshow('cv_cat', img)
cv.waitKey(0)
cv.destroyAllWindows()
