# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 18:00:13 2022

@author: Senku
"""


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten

import cv2
import numpy as np
from getData import obtenerDatos
from random import shuffle


model = Sequential()

model.add(Convolution2D(32, (3,3), input_shape = (1000, 1000, 3), activation = "relu"))
model.add(MaxPooling2D(pool_size=((2,2)) ))
model.add(Flatten())

#------------------------------------------------------------------------------------------------------
#   CAPA DE ENTRADA
#------------------------------------------------------------------------------------------------------

model.add(Dense(640, activation = "relu"))
model.add(Dense(512, activation = "relu"))
model.add(Dense(382, activation = "relu"))
model.add(Dense(256, activation = "relu"))

model.add(Dense(120, activation = "relu"))

model.compile(optimizer = "adam", loss="binary_crossentropy", metrics=['accuracy'])


x_train = []
y_train = []
x_test = []
y_test = []

dataTrain = []

#-----------------------------------------------------------------------------------------------------------------
#   LECTURA DE DATOS PARA EL ENTRENAMIENTO
#-----------------------------------------------------------------------------------------------------------------

datos, etiquetas = obtenerDatos()

for dato in datos:
    for 
    




