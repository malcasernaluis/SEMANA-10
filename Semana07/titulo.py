# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:37:34 2022

@author: ZonaGamerLS
"""
# Importamos la libreria

import camelcase

# Tenemos una cadena llamada nombre y se desea 
# que se muestre en formato titulo
nombre= "luis Alejandro Serna malca"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# Imprimimos el nombre en formato título
# Utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto cam2
# Al definir el objeto incluimos los argumentos 
# 'luis' y 'malca'

cam2 = camelcase.CamelCase('luis','malca')
print(cam2.hump(nombre))
