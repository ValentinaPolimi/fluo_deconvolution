
# coding: utf-8

# In[100]:


import numpy as np
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt

from PIL import Image 
import glob
from skimage.external import tifffile as tiff
from skimage.feature import peak_local_max
img= tiff.imread("/Users/Abel/Desktop/progetto prof.BASSI/PSFlarge.tif")



semilarghezza=10
semialtezza=10
semiprofondita=14
dimensioni_psf=[semilarghezza,semialtezza,semiprofondita]
dimensione_maggiore_psf=np.amax(dimensioni_psf)

valoremax=np.amax(img)
valore_soglia=valoremax/100

#ricerca delle coordinate dei centri di ogni psf:
coordinates = peak_local_max(img,threshold_abs=valore_soglia, min_distance=dimensione_maggiore,exclude_border=dimensione_maggiore)

#verifica del numero di psf trovate:
dimensioni_coord=np.shape(coordinates)
dim_coord=np.array(dimensioni_coord)
numero_psf=dim_coord[0]

psf=np.zeros((semiprofondita*2+1,semialtezza*2+1,semilarghezza*2+1))
for j in range(0,numero_psf-1):
    psf_j=img[coordinates[j,0]-semiprofondita:coordinates[j,0]+semiprofondita+1,coordinates[j,1]-semialtezza:coordinates[j,1]+semialtezza+1,coordinates[j,2]-semilarghezza:coordinates[j,2]+semilarghezza+1]
    psf=psf+psf_j
psf_mediata=psf/numero_psf

# ATTENZIONE: le coordinate dell'immagine e della psf vengono lette come (z,y,x)


# In[101]:



#Visualizzazione della psf nelle tre viste:

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10,10))


for ii in (ax[0], ax[1], ax[2]):
    ii.axis('off')
psf_xy=psf_mediata[semiprofondita+1,:,:]
ax[0].imshow(psf_xy, vmin=psf_mediata.min(), vmax=psf_mediata.max(), cmap="gray")
ax[0].set_title('Vista XY')

psf_xz=psf_mediata[:,semialtezza,:]
ax[1].imshow(psf_xz, vmin=psf_mediata.min(), vmax=psf_mediata.max(), cmap="gray") 
ax[1].set_title('Vista XZ')

psf_yz=psf_mediata[:,:,semilarghezza]
ax[2].imshow(psf_yz, vmin=psf_mediata.min(), vmax=psf_mediata.max(), cmap="gray") 
ax[2].set_title('Vista YZ')

fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)

plt.show()

print ("immagini ottenute mediando %d psf"%numero_psf)

