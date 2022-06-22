# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:47:17 2022

@author: ZonaGamerLS
"""

#DAdo el subtotal, 

import financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVSubTotal(subtotal): .2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal): .2f}")
