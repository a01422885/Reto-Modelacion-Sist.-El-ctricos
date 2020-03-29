#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import matplotlib.pyplot as plt
import math
plt.style.use('ggplot')


# In[20]:


ej_1 = np.linspace(0,10,100)
print(ej_1)
plt.plot(ej_1)


# In[36]:



# El tamaño de la cuadrícula
N = 9
#El rango
grid_minX = -2
grid_maxX = 2
grid_minY = -2
grid_maxY = 2

# Ahora crea tus arreglos, te sugerimos usar los valores grid_min y grid_max para el rango
# Y N para el tamaño del arreglo pero también te invitamos a experimentar con tamaños distintos
# una vez que haya funcionado tu código.
X = np.linspace(grid_minX,grid_maxX,N)
Y = np.linspace(grid_minY,grid_maxY,N)


# In[22]:


X,Y = np.meshgrid(X,Y)


# In[54]:


print(X,Y)
plt.plot(X,Y)


# In[23]:


eps_0 = 8.8542*(10**-12)
k_e = 1/(4*math.pi*eps_0)

# definamos también un valor para la carga, 
# por el momento podemos definirlo como 20e-6 
# pero puedes cambiarlo después para experimentar

q = 20e-6


# In[ ]:




