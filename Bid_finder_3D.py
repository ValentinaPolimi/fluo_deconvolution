
# coding: utf-8

# In[35]:


import numpy as np
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt

from PIL import Image 
import glob
from skimage.external import tifffile as tiff


img = tiff.imread('C:/Users/User/Downloads/PSFlarge.tif')
for z in range (0,43):
    matrice = img[:,z,:]
    maxi = np.amax(matrice)
    for x in range (0,199):
        for y in range (0,1239):
            if matrice[x,y]== maxi:
                print ("[%s,%s]",x,y)
                a=x
                b=y

             
               
                 


# In[48]:



matrice = img[:,6,:]
maxi = np.amax(matrice)
for x in range (0,199):
    for y in range (0,1239):
        if matrice[x,y] == maxi:
            a=x
            b=y
for z in range (3,10):
    matrice2 = img[:,z,:]
    psf=matrice2[a-20:a+20,b-10:b+10]
    plt.imshow(psf, cmap='gray')  
    plt.show()

                

