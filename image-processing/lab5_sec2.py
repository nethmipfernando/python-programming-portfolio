# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 11:44:53 2025

@author: eia23npf
"""

from pylab import *
img = imread("che.png")
(rows, cols, d3) = img.shape
for row in range(rows):
    for col in range(cols):
        for i in range(d3):
            if img[row, col, i] < 0.5:
                img[row, col] = (.0, .0, .0)
            elif img[row, col, i] > 0.5:
                img[row, col] = (1, 1, 1)
# imshow(img)
# show()
            

from pylab import *
img = imread("che.png")
img2=array(img)
(rows, cols, d3)= img2.shape
for row in range(rows):
    for col in range(cols):
        pixel = img2[row, col]
        if sum(pixel) > 0.5:
            img2[row, col] = (1, .0, .0)
# imshow(img2)
# show()


from pylab import *
img = imread("che.png")
img3=array(img)
(rows, cols, d3) = img3.shape
for row in range(rows):
    for col in range(cols):
        pixel = img3[row, col]
        if 60<row<160 and 55<col<140:
            if sum(pixel) > 1.5:
                img3[row, col] = (1, 1, 1)
        if (60<=row>=160 or 55<=col>=140) or (160>=row and col<=55) or (40>=row and col<=140):
            if sum(pixel) >1.5:
                img3[row, col] = (1, .0, .0)    
imshow(img3)
show()


from pylab import *
img = imread("che.png")
img4=array(img)
(rows, cols, d3)= img4.shape
for row in range(rows):
    for col in range(cols):
        pixel = img4[row, col]
        if sum(pixel) > 0.5:
            img4[row, col] = (1, .0, .0)



