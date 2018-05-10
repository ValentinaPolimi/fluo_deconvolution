
# coding: utf-8

# In[179]:


import numpy as np
import scipy
import scipy.ndimage as ndimage
import scipy.ndimage.filters as filters
import matplotlib.pyplot as plt
from PIL import Image 
import glob
from skimage.external import tifffile as tiff
from skimage import color, data, restoration
from skimage.feature import peak_local_max
img= tiff.imread("/Users/Abel/Desktop/progetto di tesi/PSFlarge.tif")
# ATTENZIONE: le coordinate dell'immagine e della psf vengono lette come (z,y,x)
xmin=200
xmax=600
zmin=50
zmax=150
piano_y=35
semilarghezza=12        #rinominare parametri
semialtezza=12      
semiprofondita=12    
dimensioni_psf=[semilarghezza,semialtezza,semiprofondita]
dimensione_maggiore_psf=np.amax(dimensioni_psf)

valoremax=np.amax(img)
valore_soglia=valoremax/10

#ricerca delle coordinate dei centri di ogni psf:
coordinates = peak_local_max(img,threshold_abs=valore_soglia, 
                             min_distance=dimensione_maggiore_psf,exclude_border=dimensione_maggiore_psf)

#verifica del numero di psf trovate:
dimensioni_coord=np.shape(coordinates)
dim_coord=np.array(dimensioni_coord)
numero_psf=dim_coord[0]

#creazione della psf mediata
psf=np.zeros((semiprofondita*2+1,semialtezza*2+1,semilarghezza*2+1))
for j in range(0,numero_psf):
    psf_j=img[coordinates[j,0]-semiprofondita:coordinates[j,0]+semiprofondita+1,coordinates[j,1]-semialtezza:
              coordinates[j,1]+semialtezza+1,coordinates[j,2]-semilarghezza:coordinates[j,2]+semilarghezza+1]
    psf_j_min=np.amin(psf_j)
    psf_j=psf_j-psf_j_min
    M=sum(psf_j)
    M=sum(M)
    M=sum(M)
    psf_j_norm=psf_j/M
    psf=(psf+psf_j_norm)
psf_mediata=psf/numero_psf

#estratto di img
img2=img[zmin:zmax,:,xmin:xmax]
### da fare calcolo valore psf, img, img restaurata



# In[187]:


img_restaurata= restoration.richardson_lucy(img2, psf_mediata, iterations=30,clip=False)
estratto_originario=img2[:,piano_y,:]
estratto_restaurato=img_restaurata[:,piano_y,:]
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20,20))
for ii in (ax[0], ax[1]):
    ii.axis('off')

ax[0].imshow(estratto_originario, vmin=estratto_originario.min(), vmax=estratto_originario.max(), cmap="gray")
ax[0].set_title('Original Data')


ax[1].imshow(estratto_restaurato, vmin=estratto_originario.min(), vmax=estratto_originario.max(), cmap="gray") 
ax[1].set_title('Restoration using\nRichardson-Lucy')

fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)

plt.show()
### da vedere contrasto 

