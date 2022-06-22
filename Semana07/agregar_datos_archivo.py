# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:57:33 2022

@author: ZonaGamerLS
"""

archivo = open("noticia.txt", "at")
#\n es para agregar el contenido en una línea final 
contenido = "\nFuente: RPP Noticias"

archivo.write(contenido)
archivo.close()