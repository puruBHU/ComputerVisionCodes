# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 19:41:24 2021

@author: Purnendu Mishra
"""

import numpy as np

# create a random image

M  = 9 # rows
N  = 7 # cols


img  = np.zeros((M, N), dtype = np.int16)

r    = np.random.randint(0, M)
c    = np.random.randint(0, N)

img[r,c]   = 1

# idx        = N * r + c

linear_img = img.reshape(-1)

# print('IDx :',idx)
# print(np.where(linear_img == 1)[0])

idx = np.where(linear_img == 1)[0][0]

c_ = idx % N
r_ = np.int16((idx - r) / N)

