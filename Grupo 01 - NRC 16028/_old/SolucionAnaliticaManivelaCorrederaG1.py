#!/usr/bin/env python
# coding: utf-8

# Esto es una celda Markdown (texto)
# 
# # Análisis de posición del mecanismo manivela corredera por método analítico
# 
# ## Objetivo
# 
# Encontrar valores de las variables del mecanismo que me permitan posicionar sus barras, usando método analítico.
# 
# ## Contexto

# ![IMG_20210209_151540834.jpg](attachment:IMG_20210209_151540834.jpg)

# ## Diagrama cinemático y vectorial
# 
# ![ManivelaCorrederaJupyterG1.png](attachment:ManivelaCorrederaJupyterG1.png)

# Usar este enlace para escribir las ecuaciones en formáto LaTeX: https://codecogs.com/latex/eqneditor.php
# 
# Parámetros: $r2$, $r3$, $\theta_4$
# 
# Variable de entrada: $\theta_2$
# 
# Variables secundarias: $\theta_3$ y $r_4$
# 
# A partir del diagrama vectorial, se puede plantear una ecuación vectorial que represente al mecanismo:
# 
# $\overrightarrow{r_{2}}-\overrightarrow{r_{3}}-\overrightarrow{r_{4}} = 0$ (1)
# 
# cuyas ecuaciones escalares son
# 
# $r2\cdot cos(\theta_{2})-r3\cdot cos(\theta_{3})-r4\cdot cos(\theta_{4})=0$, (2)
# 
# $r2\cdot sin(\theta_{2})-r3\cdot sin(\theta_{3})-r4\cdot sin(\theta_{4})=0$ (3).
# 
# Vamos a encontrar $\theta_3$ y $r_4$ en términos de $\theta_2$.
# 
# Resolviendo el sistema de ecuaciones (2) y (3), obtenemos
# 
# $\theta_{3}=sin^{-1}(k_{1})$ (4) o
# 
# $\theta_{3}=\pi + sin^{-1}(-k_{1})$ (5),
# 
# donde $k_{1} = \frac{r_{2}sin(\theta_2)}{r_3}$ (6), y
# 
# $r_4=r_2cos(\theta_2)-r_3cos(\theta_3)$ (7).
# 

# ## Solución
# 
# tareas:
# 
# - implementar las ecuaciones (4), (5) y (7)
# - usar funciones trigonométricas
# 
# para hacer esto debo importar (incluir en el programa) un módulo que me lo permita

# In[33]:


import numpy as np
# esto es un comentario
# las funciones trigonométricas hacen parte del módulo Numpy. Se llaman np."Nombre de la funcion" sin las comillas


# ahora definamos los parámetros y le damos un valor a la variable de entrada.

# In[34]:


r2 = 5
r3 = 17.5
th4 = 0
print("los parámetros son: ")
print(r2,r3,th4)

th2 = np.deg2rad(270)


# Ahora vamos a definir las ecuaciones (4) y (5)
# 
# Nota: la función trigonomética $sin^{-1}$ es np.arcsin()

# In[35]:


k1 = r2*np.sin(th2)/r3

th3a = np.arcsin(k1)
th3b = np.pi + np.arcsin(-k1)

print(np.rad2deg(th3a),np.rad2deg(th3b))


# utilizaremos la ecuación (5), porque corresponde al mecanismo físico estudiado.
# 
# Luego calculamos $r_4$ evaluando el último resultado en (7)

# In[36]:


r4 = r2*np.cos(th2) - r3*np.cos(th3b)
print(r4)


# En conclusión, obtuvimos que para $\theta_2=270°$,
# 
# $r_4 = 16.77$ y $\theta_3 = 196.6°$
