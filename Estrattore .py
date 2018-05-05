
# coding: utf-8

# In[4]:



# coding: utf-8

import matplotlib.pyplot as plt
from PIL import Image 
import numpy as np
import glob
from skimage.external import tifffile as tiff


img = tiff.imread('/Users/Abel/Desktop/PSF_test.tif')
for i in range (0,46)
    matrice=img[:, i,:]
    plt.imshow(matrice)
    max = np.amax(matrice)
    for x in range (0,199):
        for y in range (0,49):
            if matrice[x,y]== max:
                a=x
                b=y
                



# In[5]:






# In[6]:



# coding: utf-8



# In[7]:


max = np.amax(matrice)
max


# In[8]:



for x in range (0,199):
    for y in range (0,49):
        if matrice[x,y]== max:
            a=x
            b=y
            print ("[%s,%s]",x,y)
        


# In[27]:


psf = matrice[a-13:a+12,b-12:b+13]
psf


# In[28]:


plt.imshow(psf,cmap="gray")

