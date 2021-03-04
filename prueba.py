# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:05:20 2021

@author: LUIS
"""

#esto es una prueba. 

print("Hola vatos")

import numpy as np
import matplotlib.pyplot as plt
nb = 100**3

#vamos a graficar una distribución exponencial
x = np.random.exponential(0.5,nb)
plt.hist(x)

y = np.random.standard_normal(100**3)
plt.hist(y)