import os
import shutil
import panda as pd
from docx.shared import Mm
import docxtpl
import csv

import Carta
import Directivo
import Estudiante


########################## Configuracion del usuario ###################################

# Ruta de salida
OUTPUT_PATH = '..\Outputs'

# Ruta fichero word
WORD_PATH="..\inputs\Templates\plantilla.docx"
# Ruta fichero word
EXCEL_PATH = "..\inputs\Templates\plantilla.xlsx"

########################## /Configuracion del usuario###################################

########################## Funciones ###################################

''''Crear carpeta de salidas'''
def EliminarCrearCarpetas(path):
    #verificar si la carpeta existe y eliminarla
    if(os.path.exists(path)):
        shutil.rmtree(path)
    
    #Crear carpeta de salida
    os.mkdir(OUTPUT_PATH)
 
'''Crear Csv para plantilla de datos de las cartas'''
def CrearCsV():

    headers =['ID','Name','Last Name','Sexo','Email']
    Users =[
        ['2012-0990', 'Adrian','Peralta','M', 'user1@pywombat.com'],
        ['2011-1516', 'Pamela','Peralta','F', 'user2@pywombat.com'],
        ['2022-2203', 'John','Peralta','M','user3@pywombat.com'],
        ['2023-5569', 'Josefa','Peralta','F', 'user3@pywombat.com'],
    ]

    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers) # Creamos las columnas

    for user in Users:
        writer.writerow(user)

########################## /Funciones ###################################

def main():
    EliminarCrearCarpetas(OUTPUT_PATH)

if __name__ == '__main__':
    main()
