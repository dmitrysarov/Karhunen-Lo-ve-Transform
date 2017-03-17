# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:22:51 2017

@author: temp
"""
from scipy.misc import imread
import numpy as np
import matplotlib.pylab as plt
image = imread(r'testImage.jpg')
blocksByTwo = np.reshape(image, (2,np.size(image)/2), order = 'F')
blocksByTwo_subMean = blocksByTwo.T - np.mean(blocksByTwo, axis = 1)
corMatOfBlockByTwo = np.dot(blocksByTwo_subMean.T,blocksByTwo_subMean)
#%%
plt.plot(blocksByTwo[0,:], blocksByTwo[1,:], '.')
alfa = 45*np.pi/180
rotationMat = np.array([[np.cos(alfa), -np.sin(alfa)],[np.sin(alfa), np.cos(alfa)]])
rotatedBlocksByTwo = np.dot(rotationMat.T,blocksByTwo)
plt.plot(rotatedBlocksByTwo[0,:], rotatedBlocksByTwo[1,:], '.')
rotatedblocksByTwo_subMean = rotatedBlocksByTwo.T - np.mean(rotatedBlocksByTwo, axis = 1)
corMatOfRotatedBlockByTwo = np.dot(rotatedblocksByTwo_subMean.T,rotatedblocksByTwo_subMean)
#%%
image_rotated = np.reshape(rotatedBlocksByTwo,(image.shape[0],image.shape[1]))
plt.matshow(image_rotated,cmap = 'gray')
plt.figure()
plt.matshow(image, cmap='gray')