#Extrae para facturas de Funeraria la Paz

import re
import os
from datetime import datetime

# ---------------------------------------------------------------------
def buscar_archivos(ruta):
        lista_archivos = []
        archivos_carpeta = os.listdir(ruta)
        for archivo in archivos_carpeta:
           if archivo[-4:] == '.xml':          #acepta los xml directamente
              lista_archivos.append(archivo)
        return lista_archivos

def ordenar_filas(c1, c2, c3, c4, c5, cfall):
    #Ordena las filas de acuerdo al formato de cargue de Adasys
    now = datetime.now()
    hoy = str(now.day)+"/"+str(now.month)+"/"+str(now.year)
    csv_salida = hoy+"|"+c1+"|"+""+"|"+c2+"|"+c3+"|"+c4+"|"+cfall+"|"+c5+"|"+""+"\n"
    return csv_salida

def leer_archivos_escribir_csv(ruta):

    archivos = buscar_archivos(ruta_carpeta)
    print(archivos)

    encabezado = "fecha factura|fac|n orden|nit/cc|proveedor|scpa|fallecido|valor|observaciones\n"
    csv_total = [encabezado]
    for archivo in archivos:
        with open(ruta_carpeta + '/' + archivo, 'r') as f:
            content = f.read()
            uno, dos, cinco = extraer_fac_nitcc_valor(content)
            tres = extraer_proveedor(content)
            cuatro = extraer_scpa(content)
            n_fallecido = extraer_fallecido(content)
            csv_total.append(ordenar_filas(uno, dos, tres, cuatro, cinco, n_fallecido))
    print(csv_total)
    creador_csv = open(os.path.join(ruta_carpeta,"csv_total.txt"), "w")
    creador_csv.writelines(csv_total)
    creador_csv.close()
# ---------------------------------------------------------------------

def extraer_fac_nitcc_valor(datos_txt):
    #Saca el FAC, NIT/CC y VALOR de la factura
    try:
        parte_ = re.split("</?sts:QRCode>", datos_txt)
        parte = parte_[1]  #Nos quedamos con el contenido en el tag del QR
    except:
        fac = ". . ."
        nitcc = ". . ."
        valor = ". . ."

    try:
        fac = re.search("NumFac:\w+", parte)
        fac = fac.group()[7:-1]
    except:
        fac = ". . ."

    try:
        nitcc = re.search("NitFac:\w+", parte)
        nitcc = nitcc.group()[7:-1]
    except:
        nitcc = ". . ."

    try:
        valor = re.search("ValTolFac:\w+", parte)
        valor = valor.group()[10:]
    except:
        valor = ". . ."

    return fac, nitcc, valor

def extraer_proveedor(datos_txt):

    try:
        parte__ = re.split("</?cac:PartyName>", datos_txt)
        parte_ = re.split("</?cbc:Name>", parte__[1])

        proveedor = parte_[1]
    except:
        proveedor = ". . ."

    return proveedor

def extraer_scpa(datos_txt):

    try:
        parte_ = re.split("</?cbc:Note>", datos_txt)
        parte = parte_[1]

        scpa1 = re.search("AUT N.{0,2} (SC|PA)", parte)
        scpa2 = re.search("AUT N.{0,2} (SC|PA)[\. ]{0,2}\d{6}", parte)

        #AUT N° SC. 775574
        scpa1 = scpa1.group()[-2:]
        scpa2 = scpa2.group()[-6:]
        scpa = scpa1+scpa2
    except:
        scpa = ". . ."

    return scpa

def extraer_fallecido(datos_txt):

    try:
        parte_ = re.split("</?cbc:Note>", datos_txt)
        parte = parte_[1]
        fallecido = re.search("\+\+[\w ]*", parte)
        fallecido = fallecido.group()[2:]
        #print(fallecido)
    except:
        fallecido = ". . ."

    return fallecido

"""
Esta otra forma pide la direccion de la carpeta:
    print("Hola. Script para el prov Funeraria Inversiones y Planes de la Paz.\n")
    ruta_carpeta = input("Pegue la dirección de la carpeta con las facturas en XML: \n->")
    ruta_carpetas = "/".join(ruta_carpeta.split("\\"))
"""


# ---------------------------------------------------------------------
#Pegar la ruta de la carpeta con los XMLs, los "\" se cambian solos por "/"
#ruta_carpeta = r"C:\Users\ANALISTADECOSTOS\Desktop\xmls"
print("Script para el prov Funeraria Inversiones y Planes de la Paz.\n")
ruta_carpeta = input("Pegue la dirección de la carpeta con las facturas en XML: \n->")
# ---------------------------------------------------------------------



#Funciona para las facturas de Funeraria Inversiones y Planes La Paz
#ruta_arreglada = "/".join(ruta_carpeta.split("\\"))
leer_archivos_escribir_csv(ruta_carpeta)
