import os
import shutil

import os
import shutil
import pandas as pd
from docx.shared import Mm
import docxtpl

########################## Configuracion del usuario###################################

# Ruta de salida
OUTPUT_PATH = '..\Outputs'

# Ruta fichero word
WORD_PATH="..\inputs\Templates\plantilla.docx"
# Ruta fichero word
EXCEL_PATH = "..\inputs\Templates\plantilla.xlsx"

########################## /Configuracion del usuario###################################

########################## Funciones ###################################

def EliminarCrearCarpetas(path):
    #verificar si la carpeta existe y eliminarla
    if(os.path.exists(path)):
        shutil.rmtree(path)
    
    #Crear carpeta de salida
    os.mkdir(OUTPUT_PATH)
    


########################## /Funciones ###################################

def main():
    EliminarCrearCarpetas(OUTPUT_PATH)

if __name__ == '__main__':
    main()
