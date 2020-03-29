#!/usr/bin/env python
# coding: utf-8

# In[19]:

#Paso 1: Crear el campo eléctrico para una sola carga en el origen¶
#importar librerías
import numpy as np
import matplotlib.pyplot as plt
import math
plt.style.use('ggplot')


# In[20]:

#Definir el dominio del eje 1
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
x = np.linspace(grid_minX,grid_maxX,N)
y = np.linspace(grid_minY,grid_maxY,N)


# In[22]:

#Se crea cuadrícula
X,Y = np.meshgrid(x,y)


# In[54]:


print(X,Y)
plt.plot(X,Y)


# In[23]:

#configuración de la constante
eps_0 = 8.8542*(10**-12)
k_e = 1/(4*math.pi*eps_0)

# definamos también un valor para la carga, 
# por el momento podemos definirlo como 20e-6 
# pero puedes cambiarlo después para experimentar
q = 20e-6

#Para sacar los ángulos se usaran los rangos y dominios de y y x que serán los catetos opuestos y adyacentes respecitvamente
angles = np.arctan(y/x)

#Sacar r a partir de x y y
r = math.sqrt((x**2)+(y**2))

#Ahora que tienes los ángulos, ya puedes calcular las componentes para cada punto en la cuadrícula del campo eléctrico
Ex = k_e*((q/r)**2)*np.cos(angles)
Ey = k_e*((q/r)**2)*np.sin(angles)


# Creamos una figura y eje con plt.subplots()
fig, ax = plt.subplots(figsize = (7,7))

# Agregamos al eje (ax) las flechas de los vectores con plt.quiver()
ax.quiver(X,Y,Ex,Ey)
# Dibujamos en el eje (ax) la carga puntual usando plt.scatter()
ax.scatter(0,0,c='red',s=1000)
#Configuramos las dimensiones del eje y el aspecto
ax.axis([-2,2,-2,2])
ax.set_aspect('equal','box')

#magnitud de los vectores pero sólo en eje X
mags = np.linalg.norm(X)






