
# coding: utf-8

# In[64]:


import matplotlib.pyplot as plt
from PIL import Image 
import numpy as np
import glob
from skimage.external import tifffile as tiff
from skimage import img_as_float
from scipy.signal import convolve as conv
from skimage import color, data, restoration
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt

sfondo=np.zeros((100,100,100))
for x in range (24,32):
    for y in range (80,88):
        for z in range (80,88):
            sfondo[x,y,z]=10
for x in range (67,72):
    for y in range (40,45):
        for z in range (80,85):
            sfondo[x,y,z]=10
        
for x in range (87,89):
    for y in range (35,37):
        for z in range (80,82):
            sfondo[x,y,z]=10

sfondo[46,52,80]=10
img = tiff.imread("/Users/Abel/Desktop/PSFlarge.tif")
for z in range (0,43):
    matrice = img[:,z,:]
    maxi = np.amax(matrice)
    for x in range (0,199):
        for y in range (0,1239):
            if matrice[x,y]== maxi:
                a=x
                b=y
matrice = img[:,6,:]
maxi = np.amax(matrice)
for x in range (0,199):
    for y in range (0,1239):
        if matrice[x,y] == maxi:
            a=x
            b=y
psf=img[a-10:a+12,0:12,b-7:b+7]
somma=0
for x in range (0,22):
    for y in range (0,12):
        for z in range (0,14):
            temp=psf[x,y,z]
            somma=somma+temp
psf=psf/somma


fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10,10))


for ii in (ax[0], ax[1], ax[2]):
    ii.axis('off')
xy=sfondo[:,:,80]
ax[0].imshow(xy, vmin=0, vmax=10, cmap="gray")
ax[0].set_title('Vista XY')

xz=sfondo[:,80,:]
ax[1].imshow(xz, vmin=0, vmax=10, cmap="gray") 
ax[1].set_title('Vista XZ')

yz=sfondo[30,:,:]
ax[2].imshow(yz, vmin=0, vmax=10, cmap="gray") 
ax[2].set_title('Vista YZ')

fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)

plt.show()


# In[76]:


image = conv(sfondo+0.0001, psf)
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10,10))

for ii in (ax[0], ax[1], ax[2]):
    ii.axis('off')
xy=image[:,:,90]
ax[0].imshow(xy, vmin=image.min(), vmax=image.max(), cmap="gray")
ax[0].set_title('Vista XY')

xz=image[:,90,:]
ax[1].imshow(xz, vmin=image.min(), vmax=image.max(), cmap="gray") 
ax[1].set_title('Vista XZ')

yz=image[30,:,:]
ax[2].imshow(yz, vmin=image.min(), vmax=image.max(), cmap="gray") 
ax[2].set_title('Vista YZ')

fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)

plt.show()
np.shape(image)


# In[75]:


deconv = restoration.richardson_lucy(image, psf, iterations=20,clip=False)
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10,10))

for ii in (ax[0], ax[1], ax[2]):
    ii.axis('off')
xy=deconv[:,:,90]
ax[0].imshow(xy, vmin=image.min(), vmax=image.max(), cmap="gray")
ax[0].set_title('Vista XY')

xz=deconv[:,90,:]
ax[1].imshow(xz, vmin=image.min(), vmax=image.max(), cmap="gray") 
ax[1].set_title('Vista XZ')

yz=deconv[35,:,:]
ax[2].imshow(yz, vmin=image.min(), vmax=image.max(), cmap="gray") 
ax[2].set_title('Vista YZ')

fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)

plt.show()
  
    
#le immagini finali hanno le beats shiftate poichè la deconvoluzione 3D sul bordo "inventa" dei 
#pixel nelle 3 dimensioni delle dimensioni della PSF dove svolge la deconvoluzione
# la posizione finale della bead è la stessa +7


# In[ ]:


#le bead piü piccole vengono riassorbite all'interno della convoluzione

