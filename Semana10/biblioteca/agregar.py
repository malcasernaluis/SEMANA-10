# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:43:54 2022

@author: ZonaGamerLS
"""

import sqlite3 
conexion = sqlite3.connect("bdbiblioteca.db")
# REcordemos al insertar que el id es autoincrement
consulta = """ INSERT INTO 
                            PAIS(NOMBRE, ESTADO)
                            VALUES('Brasil','A')
           """
           
cursor = conexion.cursor()
cursor.execute(consulta)

#Nunca olvidar hacer commit ....

conexion.commit()
conexion.close()