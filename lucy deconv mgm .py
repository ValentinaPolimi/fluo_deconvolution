
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
from PIL import Image 
import numpy as np
import glob
from skimage.external import tifffile as tiff
from skimage import img_as_float


img = tiff.imread('/Users/Abel/Desktop/PSFlarge.tif')
img= img_as_float(img)
print (type (img[1,1,1]))

matrice=img[:, 11,:]
plt.imshow(matrice, cmap="gray")





# In[43]:



import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import convolve2d as conv2

from skimage import color, data, restoration

psf = np.matrix([[ 251,  229,  270,  249,  234,  266,  267,  263,  257,  278,  241,
         274,  337,  335,  274,  257,  260,  248,  287,  303,  394,  393,
         318,  318,  377],
       [ 269,  305,  266,  328,  286,  286,  288,  266,  269,  256,  305,
         327,  427,  415,  284,  242,  283,  265,  282,  291,  395,  384,
         287,  323,  365],
       [ 274,  293,  298,  274,  291,  254,  251,  253,  288,  296,  274,
         376,  491,  469,  316,  278,  323,  304,  270,  325,  352,  383,
         269,  280,  359],
       [ 219,  270,  273,  293,  270,  290,  263,  257,  293,  292,  320,
         456,  648,  550,  373,  279,  292,  304,  281,  351,  405,  351,
         300,  313,  359],
       [ 267,  277,  260,  277,  248,  304,  226,  275,  289,  331,  289,
         479,  860,  766,  433,  275,  304,  284,  270,  303,  372,  390,
         307,  320,  351],
       [ 298,  252,  278,  325,  261,  273,  278,  271,  314,  294,  319,
         602,  963,  867,  474,  304,  296,  303,  223,  282,  409,  416,
         309,  276,  356],
       [ 247,  283,  283,  262,  258,  285,  306,  255,  369,  305,  305,
         665, 1171,  977,  534,  299,  291,  316,  286,  356,  382,  374,
         322,  271,  272],
       [ 269,  305,  288,  299,  286,  291,  292,  262,  339,  330,  320,
         765, 1415, 1207,  620,  318,  315,  302,  257,  293,  349,  370,
         336,  274,  295],
       [ 247,  350,  318,  292,  262,  265,  265,  303,  306,  292,  376,
         855, 1577, 1454,  725,  359,  344,  310,  323,  279,  354,  328,
         262,  271,  275],
       [ 291,  347,  310,  268,  239,  290,  283,  277,  394,  358,  408,
         976, 1809, 1752,  915,  355,  328,  358,  262,  279,  284,  306,
         296,  265,  247],
       [ 281,  279,  342,  293,  272,  317,  267,  282,  402,  364,  408,
        1033, 1987, 1989,  920,  373,  328,  375,  309,  308,  352,  315,
         260,  285,  323],
       [ 270,  318,  274,  313,  315,  347,  306,  326,  369,  355,  389,
        1302, 2257, 2121, 1019,  392,  338,  333,  254,  287,  295,  304,
         277,  258,  224],
       [ 312,  270,  315,  292,  306,  306,  329,  309,  362,  372,  431,
        1319, 2361, 2352, 1073,  349,  357,  364,  320,  291,  299,  295,
         296,  269,  266],
       [ 307,  329,  321,  361,  279,  289,  309,  354,  417,  355,  444,
        1335, 2435, 2316, 1062,  393,  313,  335,  294,  311,  295,  269,
         266,  310,  268],
       [ 334,  337,  395,  353,  317,  327,  298,  335,  361,  336,  484,
        1320, 2385, 2266, 1079,  359,  349,  365,  292,  244,  270,  302,
         260,  248,  274],
       [ 321,  326,  330,  381,  294,  295,  283,  319,  370,  386,  440,
        1095, 2010, 2112, 1083,  407,  328,  329,  285,  265,  277,  276,
         246,  290,  263],
       [ 318,  334,  343,  338,  304,  294,  281,  313,  377,  345,  407,
        1033, 1974, 1761,  974,  405,  301,  297,  297,  297,  264,  266,
         305,  287,  251],
       [ 294,  369,  347,  331,  291,  289,  292,  272,  338,  308,  360,
         859, 1513, 1621,  816,  326,  307,  299,  287,  289,  279,  292,
         306,  254,  264],
       [ 277,  315,  316,  308,  300,  282,  283,  275,  311,  290,  318,
         844, 1371, 1266,  717,  354,  325,  275,  267,  269,  268,  268,
         282,  241,  269],
       [ 272,  310,  330,  339,  299,  290,  293,  273,  328,  282,  359,
         635,  963,  984,  615,  306,  271,  293,  263,  271,  254,  286,
         253,  264,  270],
       [ 260,  306,  350,  275,  290,  281,  286,  272,  273,  274,  305,
         483,  754,  736,  473,  274,  265,  243,  252,  266,  263,  263,
         259,  253,  236],
       [ 276,  279,  315,  299,  258,  262,  237,  271,  291,  326,  277,
         368,  502,  597,  423,  232,  273,  233,  271,  228,  270,  278,
         237,  289,  277],
       [ 300,  298,  277,  259,  239,  260,  263,  290,  275,  290,  273,
         331,  458,  399,  295,  228,  255,  251,  223,  244,  271,  243,
         252,  246,  284],
       [ 289,  252,  316,  265,  242,  254,  239,  269,  311,  269,  264,
         313,  330,  356,  276,  259,  235,  207,  237,  221,  254,  232,
         260,  237,  297],
       [ 297,  293,  292,  281,  256,  264,  211,  289,  314,  260,  246,
         281,  311,  257,  256,  251,  235,  245,  243,  238,  250,  253,
         235,  236,  389]])
psf=img_as_float(psf)
somma=0
for x in range (0,24):
    for y in range (0,24):
        temp=psf[x,y]
        somma=somma+temp
        
somma
psf=psf/somma
# Restore Image using Richardson-Lucy algorithm
a= restoration.richardson_lucy(matrice, psf, iterations=40,clip=False)
#a= restoration.wiener(matrice, psf, balance=0.01,clip=False)
b=a[xmin:xmax,ymin:ymax]
plt.imshow(b, vmin=b.min(), vmax=(b.max()),cmap='gray')


# In[44]:



fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(100,400))

xmin=50
xmax=150
ymin=600
ymax=700

for ii in (ax[0], ax[1]):
    ii.axis('off')
c=matrice[xmin:xmax,ymin:ymax]
ax[0].imshow(c, vmin=b.min(), vmax=(b.max()), cmap="gray")
ax[0].set_title('Original Data')


ax[1].imshow(b, vmin=b.min(), vmax=(b.max()), cmap="gray") 
ax[1].set_title('Restoration using\nRichardson-Lucy')

fig.subplots_adjust(wspace=0.02, hspace=0.2,
                    top=0.9, bottom=0.05, left=0, right=1)

plt.show()


# In[30]:


plt.imshow(a[xmin:xmax,ymin:ymax],cmap='gray')
