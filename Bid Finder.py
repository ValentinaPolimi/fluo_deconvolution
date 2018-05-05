
# coding: utf-8

# In[2]:



# coding: utf-8

import matplotlib.pyplot as plt
from PIL import Image 
import numpy as np
import glob
from skimage.external import tifffile as tiff


img = tiff.imread('/Users/Abel/Desktop/PSF_test.tif')

matrice=img[:, 34,:]
plt.imshow(matrice)



# In[3]:





# In[71]:



# coding: utf-8

import matplotlib.pyplot as plt
from PIL import Image 
import numpy as np
import glob
from skimage.external import tifffile as tiff


img = tiff.imread('/Users/Abel/Desktop/PSF_test.tif')
for i in range (1,46):
    matrice=img[$$$$:, i,:]
    max = np.amax(matrice)
    for x in range (0,199):
        for y in range (0,49):
            if matrice[x,y]== max:
                a=x
                b=y
                     
                print (x,y,"Intensità: %s"% matrice[x,y])
                 

