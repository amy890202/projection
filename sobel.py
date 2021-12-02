# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:53:19 2021

@author: USER
"""

import numpy as np
from PIL import Image
from scipy import signal

I = Image.open('CO.jpg')
data = np.asarray(I)
data2 = np.zeros((225,225)).astype('uint8')
R = data[:,:,0].astype('float')
G = data[:,:,1].astype('float')
B = data[:,:,2].astype('float')
data3 = ((R+G+B)/3).astype('uint8')
Sx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
Sy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
Ix = signal.convolve2d(data3,Sx,boundary='symm',mode='same')
Iy = signal.convolve2d(data3,Sy,boundary='symm',mode='same')
data4 = (Ix**2)+(Iy**2)
data4_1D = np.sort(data4.reshape((-1,1))[:,0])
threshold = data4_1D[int(len(data4_1D)*0.8)]
data2[data4<threshold] = 255
I2 = Image.fromarray(data2)
I2.show()
