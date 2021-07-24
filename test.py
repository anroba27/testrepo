# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
from random import randint,uniform
import pandas as pd
import numpy as np

def llenar_matriz(m,n):
    matriz = []
    
    for i in range(m):
        fila = []
        
        for j in range(n):
            fila.append(round(uniform(1,100),2))
        matriz.append(fila)
    
    return matriz


resultado = llenar_matriz(10,7)

media = np.mean(resultado)
desv_tip = np.std(resultado)

matriz_N = (resultado-media)/desv_tip

print(matriz_N)

#df = pd.DataFrame(resultado)

#df.columns = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

Resultado2 = llenar_matriz (1,10)
Resultado3 = str(llenar_matriz(1,10))
A = [Resultado2,Resultado3]



