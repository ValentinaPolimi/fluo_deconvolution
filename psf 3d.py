
# coding: utf-8

# In[2]:


import numpy as np
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt

from PIL import Image 
import glob
from skimage.external import tifffile as tiff


img = tiff.imread("/Users/Abel/Desktop/PSFlarge.tif")
for z in range (0,43):
    matrice = img[:,z,:]
    maxi = np.amax(matrice)
    for x in range (0,199):
        for y in range (0,1239):
            if matrice[x,y]== maxi:
                a=x
                b=y


# In[6]:


matrice = img[:,6,:]
maxi = np.amax(matrice)
for x in range (0,199):
    for y in range (0,1239):
        if matrice[x,y] == maxi:
            a=x
            b=y
psf=img[a-10:a+10,0:12,b-7:b+7]

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10,10))


for ii in (ax[0], ax[1], ax[2]):
    ii.axis('off')
psf_xy=psf[:,:,7]
ax[0].imshow(psf_xy, vmin=300, vmax=4000, cmap="gray")
ax[0].set_title('Vista XY')

psf_xz=psf[:,6,:]
ax[1].imshow(psf_xz, vmin=300, vmax=4000, cmap="gray") 
ax[1].set_title('Vista XZ')

psf_yz=psf[11,:,:]
ax[2].imshow(psf_yz, vmin=300, vmax=4000, cmap="gray") 
ax[2].set_title('Vista YZ')

fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)

plt.show()
np.shape(psf)

