#!/usr/bin/env python
# coding: utf-8

# Esto es una celda de markdown (texto)
# 
# # Solución analítica de posición del mecanismo manivela corredera
# 
# ## Objetivo
# 
# Hallar las variables que definen la posición del mecanismo estudiado
# 
# ## Contexto

# ![IMG_20210209_151540834.jpg](attachment:IMG_20210209_151540834.jpg)

# ## Diagrama cinemático y vectorial
# 
# ![ManivelaCorrederaJupyterG3.png](attachment:ManivelaCorrederaJupyterG3.png)

# [Usar este enlace para escribir las ecuaciones en formáto LaTeX: https://codecogs.com/latex/eqneditor.php]
# 
# Parámetros: $r2$, $r3$, $\theta_{4}$
# 
# Variable de entrada: $\theta_{2}$
# 
# Variables secundarias: $\theta_{3}$, $r_4$
# 
# Partiendo del diagrama vectorial, planetamos la siguiente ecuación vectorial
# 
# $\overrightarrow{r_2}-\overrightarrow{r_3}-\overrightarrow{r_4}=0$ (1)
# 
# cuyas ecuaciones escalares son
# 
# $r2\cdot cos(\theta_{2})-r3\cdot cos(\theta_{3})-r4\cdot cos(\theta_{4})=0$, (2)
# 
# $r2\cdot sin(\theta_{2})-r3\cdot sin(\theta_{3})-r4\cdot sin(\theta_{4})=0$ (3)
# 
# Vamos a encontrar $\theta_3$ y $r_4$ en términos de $\theta_2$
# 
# resolviendo el sistema de ecuaciones (2) y (3) obtenemos
# 
# $\theta_3 = sin^{-1}(k_1)$ (4) o
# 
# $\theta_3 = \pi + sin^{-1}(-k_1)$ (5)
# 
# donde $k_1 = \frac{r_2sin(\theta _2))}{r_3}$ (6), y
# 
# $r4 = r_2cos(\theta _2) - r_3cos(\theta_3)$ (7)
# 

# ### Solución
# 
# tareas: 
# - implementar las ecuaciones (4), (5) y (7)
# - usar funciones trigonométricas
# 
# Para esto debo importar (incluir en mi programa) un módulo (librería) que me permita hacer esto

# In[17]:


import numpy as np 
# esto es un comentario
# las funciones trigonométricas hacen parte del módulo Numpy. Se llaman np."Nombre de la funcion" sin las comillas


# las funciones trigonométricas hacen parte del módulo Numpy. Se llaman np."Nombre de la funcion" sin las comillas.
# 
# Ahora definamos los parámetros y le damos un valor a la variable de entrada

# In[18]:


r2 = 2.5
r3 = 8.75
th4 = 0
print("los parámetros son ")
print(r2,r3,th4)
# pendiente: solicitar datos al usuario

th2 = np.deg2rad(135)
print("la variable de entrada es ")
print(th2)


# Ahora vamos a definir las ecuaciones (4) y (5).
# 
# Nota: la función trigonomética $sin^{-1}$ es np.arcsin()

# In[21]:


k1 = r2*np.sin(th2)/r3
th3a = np.arcsin(k1)
print(np.rad2deg(th3a))
th3b = np.pi + np.arcsin(-k1)
print(np.rad2deg(th3b))


# tomamos el resultado de (5) de acuerdo al contexto.
# 
# ahora evaluamos este valor de $\theta_3$ en (7)

# In[24]:


r4 = r2*np.cos(th2) - r3*np.cos(th3b)
print(r4)


# En conclusión, obtuvimos que para $\theta_2=135$°,
# 
# $r_4 = 6.801$ y $\theta_3 = 168$°

# In[25]:


print("Hola Mundo")

