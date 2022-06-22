# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:42:47 2022

@author: ZonaGamerLS
"""

import sqlite3 
# Con el comando connect buscara la base de datos
# que tenga ese nombre, de lo contrario lo creara...
conexion = sqlite3.connect("bdbiblioteca.db")
conexion.close()