# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:53:00 2022

@author: ZonaGamerLS
"""

#Dado el total, calcular el IGV  y el subtotal

import financieros
total = 1000.49
print(f"SubTotal: {financieros.obtenerSubTotalconTotal(total): .2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total): .2f}")
print(f"Total: {total}")