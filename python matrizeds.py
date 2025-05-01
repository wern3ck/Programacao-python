# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 19:37:51 2025

@author: lucas
"""
import numpy as np
matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])
matriz 
matriz.shape

soma = 0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma += matriz[i][j]
        print('soma: ', soma)
