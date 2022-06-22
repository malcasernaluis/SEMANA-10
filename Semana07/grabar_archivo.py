# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:47:55 2022

@author: ZonaGamerLS
"""

archivo=open("archivo_de_prueba.txt","wt")
contenido= "Linea1 hola amigos ¿Cómo están? \nLínea2 Bienvenido a la Untels. "
archivo.write(contenido)
archivo.close()