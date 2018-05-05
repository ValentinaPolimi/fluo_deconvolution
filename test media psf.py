
# coding: utf-8

# In[27]:


import numpy as np
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt

from PIL import Image 
import glob
from skimage.external import tifffile as tiff
from skimage.feature import peak_local_max
img = tiff.imread('/Users/Abel/Desktop/PSF_test.tif')

psf=np.zeros((25,25))
contatore_psf=0
g=np.size(psf)
np.shape(img)


# In[42]:


contatore_psf=0
for i in range (0,45):
    matrice=np.matrix(img[:,i,:])
    maxi = np.amax(matrice)
    for x in range (0,199):
        for y in range (0,49):
            if matrice[x,y]== maxi:
                a=x-12
                b=y-12
                if a>0 or a<29 and b>0 or b<175:
                    psf_i[0:25,0:25]=matrice[a:a+25,b:b+25]
                    plt.imshow(psf_i)
                    #psf=psf+psf_i
                    #for X in range (a-13,a+12):
                        #for Y in range (b-13,b+12):
                            #psf=np.matrix(psf[X,Y])+np.matrix(matrice[X,Y])
                    #contatore_psf=contatore_psf+1
                    #psf=psf+immagine      
plt.imshow(psf_i, cmap="gray")


# In[48]:


xy = peak_local_max(psf, min_distance=3, exclude_border=False, threshold_abs=100)


# In[49]:


xy


# In[50]:


plt.imshow(psf, cmap="gray")
plt.plot(xy[:, 1], xy[:, 0], 'ro')


# In[65]:


v=np.size(xy)
v


# In[43]:




