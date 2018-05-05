
# coding: utf-8

# In[40]:


import numpy as np
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt

from PIL import Image 
import glob
from skimage.external import tifffile as tiff
area=25*25

img = tiff.imread('/Users/Abel/Desktop/PSF_test.tif')
neighborhood_size = 4
matrice=img[:,23,:]
maxi = np.amax(matrice)
for x in range (0,199):
    for y in range (0,49):
        if matrice[x,y]== maxi:
            print ("[%s,%s]",x,y)
            a=x
            b=y
maxi


# In[41]:


psf = matrice[a-13:a+12,b-12:b+13]
somma=0
for x in range (0,25):
    for y in range (0,25):
        temp=psf[x,y]
        somma=somma+temp
threshold=somma/area
plt.imshow(psf, cmap="gray")


# In[42]:


data_max = filters.maximum_filter(psf, neighborhood_size)
maxima = (psf == data_max)
data_min = filters.minimum_filter(psf, neighborhood_size)
diff = ((data_max - data_min) > threshold)

labeled, num_objects = ndimage.label(maxima)
slices = ndimage.find_objects(labeled)
x, y = [], []
for dy,dx in slices:
    x_center = (dx.start + dx.stop - 1)/2
    x.append(x_center)
    y_center = (dy.start + dy.stop - 1)/2    
    y.append(y_center)

plt.imshow(psf, cmap="gray")


plt.autoscale(False)
plt.plot(x,y, 'ro')

