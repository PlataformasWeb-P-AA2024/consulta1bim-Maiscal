import pymongo
from pymongo import MongoClient


ruta = 'atp_tennis.csv'


archivo = open(ruta, 'r', encoding='utf-8')
lineas = archivo.readlines()
archivo.close()

lineas = [linea.strip().split(',') for linea in lineas]
encabezado = lineas[0]
datos = lineas[1:]

# Convertir las líneas en diccionarios usando el encabezado
lista_datos = []
for linea in datos:
    diccionario = {encabezado[i]: linea[i] for i in range(len(encabezado))}
    lista_datos.append(diccionario)

# Conectar a MongoDB
cliente = MongoClient('localhost', 27017)
bd = cliente['consulta_b1']
coleccion = bd['atp_tennis']

coleccion.insert_many(lista_datos)

# Realizar una consulta en MongoDB para verificar los datos ingresados
resultado_consulta = coleccion.find()

# Presentar la información por consola
for documento in resultado_consulta:
    print(documento)