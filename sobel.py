# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:10:29 2021

@author: user
"""
import numpy as np
from PIL import Image
from scipy import signal

I = Image.open('co.jpg')#225*225*3 讀圖
data = np.asarray(I)
data2 = np.zeros((225,225)).astype('uint8')#uint只能做整數#255,255為你的照片大小
#data2[:,:,2] = data[:,:,2]#只copy藍色那一層(if 0->Red那一層)
#data2 = 255-data
#I2 = Image.fromarray(data2,'RGB')#data2塞進I2的image
#I2.show()#I2就會是底片

#M = np.ones((10,10))/100#一百個點的平均(20,20,400->400個點平均 比較糊)
#M = np.ones((1,50))/50#會橫著跑(橫向模糊)
#M = np.array([[1,1,1],[1,9,1],[1,1,1]])/17#中間會凸顯 旁邊會模糊   [-1 0 1 ]
R = data[:,:,0].astype('float')#int不能做除法 ，所以強制轉成float
G = data[:,:,1].astype('float')
B = data[:,:,2].astype('float')
data3 = ((R+G+B)/3).astype('uint8')#把RGB混起來一起處理
Sx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
Sy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])#設計filter
Ix = signal.convolve2d(data3,Sx,boundary='symm',mode='same')
Iy = signal.convolve2d(data3,Sy,boundary='symm',mode='same')
data4 = (Ix**2)+(Iy**2)#平方相加
data4_1D = np.sort(data4.reshape((-1,1))[:,0])
threshold = data4_1D[int(len(data4_1D)*0.75)]#0.85調小一點可以留多一點edge
#data5 = data4.copy()
data2[data4<threshold] = 255
I2 = Image.fromarray(data2)
I2.show()#模仿素描

# =============================================================================
# R2 = signal.convolve2d(R,M,boundary='symm',mode='same')
# G2 = signal.convolve2d(G,M,boundary='symm',mode='same')
# B2 = signal.convolve2d(B,M,boundary='symm',mode='same')
# data2[:,:,0] = R2
# data2[:,:,1] = G2
# data2[:,:,2] = B2
# =============================================================================
I2 = Image.fromarray(data2,'RGB')
I2.show()


