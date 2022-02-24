# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 19:40:01 2022

@author: Senku
"""

import mysql.connector
import glob
import os
import cv2


conexion = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd= '',
    db = 'animales'
)



def poblarBD():
    listaDirectorios = os.listdir("images/Images")
    print(listaDirectorios)
    
#---------------------------------------------------------------------------------------------------------
#   INSERCIÓN DE RAZAS DE PERROS
#---------------------------------------------------------------------------------------------------------
    for directorio in listaDirectorios:
        data = directorio.split("-")
        ID = data[0]
        descripcion = data[1].replace("_", " ")
        print("ID de raza: " + ID + " raza: " + descripcion)
        try:
            
            cur = conexion.cursor()
            add_raza = ("INSERT INTO RAZA (ID_RAZA, DESCRIPCION) VALUES(%s, %s)")
            data_raza = (ID, descripcion)
            cur.execute(add_raza, data_raza)
            
            conexion.commit()
        except mysql.connector.Error as err:
            if(err.errno == 1062):
                print("El registro ya existe en la base de datos: {}".format(err))
        
        imgs = os.listdir("images/Images/" + directorio)
        for imagen in imgs:
            path = "images/Images/" + str(directorio) + "/" + str(imagen)
            
            try:
                cur = conexion.cursor()
                add_data = ("INSERT INTO PERRO (ID_RAZA, IMAGEN) VALUES (%s, %s)")
                data_perro = (ID, path)
                cur.execute(add_data, data_perro)
                
                conexion.commit()
            except mysql.connector.Error as err:
                if(err.errno == 1062):
                    print("El registro ya existe en la base de datos: {}".format(err))
        
        



def obtenerDatos():
    
    datos = []
    
    cur = conexion.cursor()
    
    query = ("SELECT R.DESCRIPCION, P.IMAGEN FROM RAZA R, PERRO P WHERE P.ID_RAZA = R.ID_RAZA ORDER BY R.DESCRIPCION")
    cur.execute(query)
    
    for (descripcion, imagen)in cur:
        datos.append([descripcion, cv2.imread(imagen)])
    
    return datos

datos = obtenerDatos()