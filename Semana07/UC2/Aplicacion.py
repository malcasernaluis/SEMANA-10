# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:43:01 2022

@author: Luis Serna Malca
"""

import gestion_archivos

def menu():
    print("*** MENU PRINCIPAL ****")
    print("1. Crear Archivo")
    print("2. Eliminar Archivo")
    print("3. Agregar Archivo")
    print("4. Mostrar contenido de Archivo")
    print("5. Salir")
    
def crear():
    print("*** CREAR ARCHIVO ***")
    archivo = input("Crear archivo: ")
    contenido = input ("Contenido del archivo: ")
    gestion_archivos.crear_archivo(archivo, contenido)
    
def eliminar():
    print("*** ELIMINAR ARCHIVO***")
    archivo = input ("Quiero eliminar el archivo: ")
    gestion_archivos.eliminar_archivo(archivo)
    
def Agregar():
    print("***AGREGAR CONTENIDO***")
    archivo = input ("Quiero agregar contenido al archivo: ")
    contenido = input (" El contenido adicional del archivo será: ")
    gestion_archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print(" *** MOSTRAR CONTENIDO DE UN ARCHIVO ***")
    archivo = input ("Quiero mostrar el contenido del archivo: ")
    print(gestion_archivos.leer_archivo(archivo))
    
def salir():
    print("Gracias ... VUELVA PRONTO")

def error():
    print("Opcion invalida")
    
    
#La logica para el menu de opciones
    
opcion = 1 
while opcion!=5:
    menu()
    opcion = int(input("Seleccione una opcion [1-5]: "))
    if opcion==1:
        crear()
    elif opcion==2:
        eliminar()
    elif opcion == 3 :
        Agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        error()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        