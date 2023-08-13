'''
Created on Aug 12 23

@author: Anjali Patel
'''
import numpy as np
from matplotlib import pyplot as plt
import cv2


#To read the images
img1=cv2.imread("C:\\Users\\DC\\Downloads\\Assignment_2\\images\\ECE.png", 0)
img2=cv2.imread("C:\\Users\\DC\\Downloads\\Assignment_2\\images\\IIScMain.png", 0)

#To find max  values
max_img1=np.max(img1)
print("Max value of img1 :",max_img1)
max_img2=np.max(img2)
print("Max value of img2 :",max_img2)

#To find min values
min_img1=np.min(img1)
print("Min value of img1 :",min_img1)
min_img2=np.min(img2)
print("Min value of img2 :",min_img2)

#To apply contrast stretch formula
str_img1=255*((img1-min_img1)/(max_img1-min_img1))
str_img2=255*((img2-min_img2)/(max_img2-min_img2))


#To find value of bins for histogram
bins1=max_img1-min_img1
bins2=max_img2-min_img2


#To show subplots of original image1 and stretched image1
plt.subplot(241)
plt.title("Original Image 1")
plt.imshow(img1,cmap='gray')

plt.subplot(242)
plt.title("Stretched Image 1")
plt.imshow(str_img1,cmap='gray')

#To plot histogram of original image1 and stretched image1
plt.subplot(243)
plt.title(" Histogram of Original Image 1")
plt.hist(img1.ravel(),bins=87,range=(1,img1.ravel().max()))

plt.subplot(244)
plt.title("Histogram of Stretched Image 1")
plt.hist(img2.ravel(),bins=255,range=(1,str_img1.ravel().max()))

#To show subplots of original image1 and stretched image1
plt.subplot(245)
plt.title("Original Image 2")
plt.imshow(img2,cmap='gray')

plt.subplot(246)
plt.title("Stretched Image 2")
plt.imshow(str_img2,cmap='gray')

#To plot histogram of original image1 and stretched image1
plt.subplot(247)
plt.title(" Histogram of Original Image 2")
plt.hist(img2.ravel(),bins=255,range=(1,img2.ravel().max()))

plt.subplot(248)
plt.title("Histogram of Stretched Image 2")
plt.hist(img2.ravel(),bins=255,range=(1,str_img2.ravel().max()))

















