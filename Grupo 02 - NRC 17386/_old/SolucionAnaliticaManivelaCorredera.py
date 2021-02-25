#!/usr/bin/env python
# coding: utf-8

# Esto es una celda Markdown (de texto)
# # Solución analítica de la posición del mecanismo manivela corredera
# 
# ## Objetivo
# 
# Encontrar las variables que definen la posición del mecanismo manivela corredera
# 
# ## Contexto
# 

# ![ManivelaCorrederaJupyter.png](attachment:ManivelaCorrederaJupyter.png)

# [Usar este enlace para escribir las ecuaciones en formáto LaTeX: https://codecogs.com/latex/eqneditor.php]
# 
# Parámetros: $r2$, $r3$, $\theta_{4}$
# 
# Variable de entrada: $\theta_{2}$
# 
# Variables secundarias: $\theta_{3}$, $\theta_{4}$
# 
# Partiendo de este diagrama vectorial, podemos obtener la siguiente ecuación vectorial
# 
# $\overrightarrow{r_{2}}-\overrightarrow{r_{3}}-\overrightarrow{r_{4}}=0$ (1)
# 
# cuyas ecuaciones escalares correspondientes son
# 
# $r2\cdot cos(\theta_{2})-r3\cdot cos(\theta_{3})-r4\cdot cos(\theta_{4})=0$, (2)
# 
# $r2\cdot sin(\theta_{2})-r3\cdot sin(\theta_{3})-r4\cdot sin(\theta_{4})=0$ (3)
# 
# Vamos a encontrar $\theta_{3}$ y $\theta_{4}$ en términos de $\theta_{2}$
# 
# Resolviendo el sistema de ecuaciones escalares (2) y (3) obtenemos
# 
# $\theta _3 = sin^{-1}(r_2sin( \theta _2)/r_3)$ (4a) o
# 
# $\theta _3 = \pi + sin^{-1}(-r_2sin( \theta _2)/r_3)$ (4b) y
# 
# $r_4 = r2cos(\theta_{2})-r3cos(\theta_{3})$ (5).
# 
# Usamos 4b y 5.

# ### Solución
# 
# Primero hay que importar los módulos necesarios para resolver el problema
# por ejemplo para funciones matemáticas se importa Numpy

# In[16]:


import numpy as np


# ahora definamos los parámetros y un valor para la variable de entrada

# In[17]:


r2 = 2.5
r3 = 8.75
th4 = 0

th2 = np.deg2rad(90)
print(th2)


# luego definimos las ecuaciones (4) y (5) y calculamos para th2 = 90°
# voy a crear parámetros internos tal que
# 
# $k_1 = r_2sin( \theta _2)/r_3$
# 
# luego $\theta _3 = sin^{-1}(k_1)$
# 
# nota: seno inverso se implementa usando la función arcsin de numpy

# In[21]:


k1 = r2*np.sin(th2)/r3
th3 = np.pi + np.arcsin(-k1)
print(np.rad2deg(th3)) #revisar


# In[19]:


r4 = r2*np.cos(th2) - r3*np.cos(th3)
print(r4)


# En conclusión obtuvimos
# 
# $r_4 = 8.38$ cm y
# $\theta_3 = 163.39$°

# In[1]:


print("Hola mundo")

