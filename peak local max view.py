
# coding: utf-8

# In[6]:


import numpy as np
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt
from PIL import Image 
import glob
from skimage.external import tifffile as tiff
from skimage.feature import peak_local_max
from skimage import color, data, restoration


# In[11]:


file2=tiff.imread("/Users/Abel/Desktop/progetto di tesi/PSFlarge.tif")
semilarghezza_psf=17
semialtezza_psf=17
semiprofondita_psf=17
dimensioni_psf=[semilarghezza_psf,semialtezza_psf,semiprofondita_psf]
dimensione_maggiore_psf=np.amax(dimensioni_psf)

valoremax=np.amax(file2)
valore_soglia=valoremax/50
coordinates = peak_local_max(file2,threshold_abs=valore_soglia, 
                             min_distance=dimensione_maggiore_psf,exclude_border=dimensione_maggiore_psf)
dimensioni_coord=np.shape(coordinates)
dim_coord=np.array(dimensioni_coord)
numero_psf=dim_coord[0]


# In[10]:


piano1=21
piano2=17
piano3=19


fig, axes = plt.subplots(1, 3, figsize=(50, 20), sharex=True, sharey=True)
ax = axes.ravel()
contatore=0
for K in range (0,numero_psf):
    if coordinates[K,1]==piano1:
        contatore=contatore+1
J=np.zeros((contatore,2))
U=0
for K in range (0,numero_psf):
    if coordinates[K,1]==piano1:
        J[U,0]=coordinates[K,0]
        J[U,1]=coordinates[K,2]
        U=U+1

ax[0].imshow(file2[:,piano1,:], cmap="gray")
ax[0].autoscale(False)
ax[0].plot(J[:,1],J[:,0], 'r.')
ax[0].axis('off')
ax[0].set_title('Peak local max')

contatore=0
for K in range (0,numero_psf):
    if coordinates[K,1]==piano2:
        contatore=contatore+1
J=np.zeros((contatore,2))
U=0
for K in range (0,numero_psf):
    if coordinates[K,1]==piano2:
        J[U,0]=coordinates[K,0]
        J[U,1]=coordinates[K,2]
        U=U+1

ax[1].imshow(file2[:,piano2,:], cmap="gray")
ax[1].autoscale(False)
ax[1].plot(J[:,1],J[:,0], 'r.')
ax[1].axis('off')
ax[1].set_title('Peak local max')

contatore=0
for K in range (0,numero_psf):
    if coordinates[K,1]==piano3:
        contatore=contatore+1
J=np.zeros((contatore,2))
U=0
for K in range (0,numero_psf):
    if coordinates[K,1]==piano3:
        J[U,0]=coordinates[K,0]
        J[U,1]=coordinates[K,2]
        U=U+1
ax[2].imshow(file2[:,piano3,:], cmap="gray")
ax[2].autoscale(False)
ax[2].plot(J[:,1],J[:,0], 'r.')
ax[2].axis('off')
ax[2].set_title('Peak local max')

fig.tight_layout()

plt.show()


# ### 
