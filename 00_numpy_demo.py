from PIL import Image

import numpy as np

a1 = np.array([1, 2, 3, 4, 5])
# a2 = np.zeros(4)
a2 = np.zeros((3, 2))  # 3rows 2columns all zero && (a2.shape) = (3, 2)
a3 = np.ones((2, 4))  # 2rows 4columns all one
a4 = np.arange(3, 7)  # [3 4 5 6]
a5 = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ]
a6 = np.random.rand(2, 2)  # random array
# a6.dtype = float64
a7 = np.zeros((3, 3), dtype=np.int8)  # use dtype to define the type of array
'''
type of array
np.int8/16/32/64
np.uint8/16/32/64
np.float32/64
bool
str
'''
aa1 = np.array([1, 2, 3])
aa2 = np.array([4, 5, 6])
aa3 = aa1 + aa2  # [5 7 9]
aa4 = aa1 / aa2  # [0.25 0.4  0.5 ]
aa5 = np.dot(aa1, aa2)  # dot is 32
aa1 = np.array([[1, 2],
                [3, 4]])
aa2 = np.array([[2, 0],
                [0, 2]])
aa6 = aa1 @ aa2  # same to np.matmul()
'''
[[2 4]
 [6 8]]
'''
a8 = np.array([1, 2, 3])  # np.sin(a8) = [0.84147098 0.90929743 0.14112001]
# a8 * 5 = [ 5 10 15] Broadcasting
'''
np.sqrt
np.sin
np.cos
np.log
np.power
'''
# min() & max() is the value,argmin()&argmax() is the index of the array
# same sum(), mean(), median(), var(), std()
a9 = np.array([1, 2, 3, 4, 5, 6, 7])  # [::-1] is [7 6 5 4 3 2 1]
img = Image.open('img/sleep cat.jpeg')
