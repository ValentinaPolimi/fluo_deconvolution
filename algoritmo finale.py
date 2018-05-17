
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
from skimage.feature import peak_local_max
from skimage import color, data, restoration




# In[3]:


#Path del file da deconvolvere:
file1=tiff.imread("/Users/Abel/Desktop/progetto di tesi/PSFlarge.tif")

#Path del file del campione da cui estrarre la psf:
file2=tiff.imread("/Users/Abel/Desktop/progetto di tesi/PSFlarge.tif")


dimensioni_stack=np.shape(file1)
dimensioni_stack=np.array(dimensioni_stack)
xmax_stack=dimensioni_stack[2]-1
ymax_stack=dimensioni_stack[1]-1
zmax_stack=dimensioni_stack[0]-1
piano_visualizzato=27
#Porzione di stack che si vuole deconvolvere:
x_iniziale=1000
x_finale=1600#xmax_stack

y_iniziale=0
y_finale=ymax_stack

z_iniziale=0
z_finale=100#zmax_stack

img=file1[z_iniziale:z_finale,y_iniziale:y_finale,x_iniziale:x_finale]


#Dimensioni della psf che si vuole acquisire:
semilarghezza_psf=15
semialtezza_psf=15
semiprofondita_psf=15
dimensioni_psf=[semilarghezza_psf,semialtezza_psf,semiprofondita_psf]
dimensione_maggiore_psf=np.amax(dimensioni_psf)

valoremax=np.amax(file2)

#Valore minimo per cui un pixel può essere ritenuto un picco di psf:
valore_soglia=valoremax/100


# In[4]:


#ricerca delle coordinate dei centri di ogni psf:
coordinates = peak_local_max(file2,threshold_abs=valore_soglia, 
                             min_distance=dimensione_maggiore_psf,exclude_border=dimensione_maggiore_psf)

#verifica del numero di psf trovate:
dimensioni_coord=np.shape(coordinates)
dim_coord=np.array(dimensioni_coord)
numero_psf=dim_coord[0]

#creazione della psf mediata
psf=np.zeros((semiprofondita_psf*2+1,semialtezza_psf*2+1,semilarghezza_psf*2+1))
for j in range(0,numero_psf):
    psf_j=file2[coordinates[j,0]-semiprofondita_psf:coordinates[j,0]+semiprofondita_psf+1,
                coordinates[j,1]-semialtezza_psf:coordinates[j,1]+semialtezza_psf+1,
                coordinates[j,2]-semilarghezza_psf:coordinates[j,2]+semilarghezza_psf+1]
    
    #ad ogni psf viene tolto il suo valore minimo per portare il rumore a zero:
    psf_j_min=np.amin(psf_j)
    psf_j=psf_j-psf_j_min
    
    #normalizzazione della jesima psf:
    M=np.sum(psf_j)
    psf_j_norm=psf_j/M
    psf=psf+psf_j_norm
    
psf_mediata=psf/numero_psf

np.sum(psf_mediata)


# In[8]:


#Visualizzazione della psf nelle tre viste:

fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10,10))


for ii in (ax[0], ax[1], ax[2]):
    ii.axis('off')
psf_xy=psf_mediata[semiprofondita_psf,:,:]
ax[0].imshow(psf_xy, vmin=psf_mediata.min(), vmax=psf_mediata.max(), cmap="gray")
ax[0].set_title('Vista XY')

psf_xz=psf_mediata[:,semialtezza_psf,:]
ax[1].imshow(psf_xz, vmin=psf_mediata.min(), vmax=psf_mediata.max(), cmap="gray") 
ax[1].set_title('Vista XZ')

psf_yz=psf_mediata[:,:,semilarghezza_psf]
ax[2].imshow(psf_yz, vmin=psf_mediata.min(), vmax=psf_mediata.max(), cmap="gray") 
ax[2].set_title('Vista YZ')

fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)

plt.show()

print ("immagini ottenute mediando %d psf"%numero_psf)


# In[9]:


#deconvoluzione dei dati con richardson-lucy:
img_restaurata= restoration.richardson_lucy(img, psf_mediata, iterations=30,clip=False)
estratto_originario=img[:,piano_visualizzato,:]
estratto_restaurato=img_restaurata[:,piano_visualizzato,:]
a=plt.imshow(estratto_restaurato,vmin=0,vmax=255, cmap="gray")


# In[11]:


type(estratto_originario[2,4])

