#Extrae para facturas del proveedor Sociedad Hermanos de la Caridad

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

def leer_archivos_escribir_csv(ruta):

    archivos = buscar_archivos(ruta_carpeta)
    print(archivos)

    encabezado = "fecha factura|fac|n orden|nit/cc|proveedor|scpa|fallecido|valor|observaciones\n"
    csv_total = [encabezado]
    for archivo in archivos:
        with open(ruta_carpeta + '/' + archivo, 'r') as f:
            content = f.read()
            Cfac = extraer_factura(content)
            Cnitcc = extraer_nitcc(content)
            Cprov = extraer_proveedor(content)
            Cscpa = extraer_scpa(content)
            Cfall = extraer_fallecido(content)
            Cval = extraer_valor(content)
            csv_total.append(ordenar_filas(Cfac, Cnitcc, Cprov, Cscpa, Cfall, Cval))
    print(csv_total)
    #Excribe el csv
    creador_csv = open(os.path.join(ruta_carpeta,"csv_total.txt"), "w")
    creador_csv.writelines(csv_total)
    creador_csv.close()

def ordenar_filas(Cfac, Cnitcc, Cprov, Cscpa, Cfall, Cval):
    # Ordena las filas de acuerdo al formato de cargue de Adasys
    now = datetime.now()
    hoy = str(now.day) + "/" + str(now.month) + "/" + str(now.year)
    csv_salida = hoy + "|" + Cfac + "|" + "" + "|" + Cnitcc + "|" + Cprov + "|" + Cscpa + "|" + Cfall + "|" + Cval + "|" + "" + "\n"
    return csv_salida

# ---------------------------------------------------------------------
"""
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
"""

def extraer_factura(datos_txt):
    try:
        parte_ = re.split("</?cbc:ID>", datos_txt)
        #print(parte_[1])
        factura = parte_[1]
    except:
        factura = ". . ."

    return factura

def extraer_nitcc(datos_txt):
    try:
        parte_ = re.split("</?cbc:CompanyID[^>]*>", datos_txt)
        nitcc = parte_[1]
    except:
        nitcc = ". . ."

    return nitcc

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
        parte__ = re.split("</?cbc:Note>", datos_txt)
        parte_ = parte__[1]
        parte = re.search("FALLECIDO: (CC\.{0,1} )?[\d]* [\w ]*- CSE", parte_)
        fallecido = parte.group()[:-6]
        print(fallecido)
        #print(fallecido)
    except:
        fallecido = ". . ."

    return fallecido

def extraer_valor(datos_txt):

    try:
        parte_ = re.split("</?cbc:PriceAmount[^>]*>", datos_txt)
        valor = parte_[1]
    except:
        valor = ". . ."

    return valor


"""
Esta otra forma pide la direccion de la carpeta:
    print("Hola. Script para el prov Funeraria Inversiones y Planes de la Paz.\n")
    ruta_carpeta = input("Pegue la dirección de la carpeta con las facturas en XML: \n->")
    ruta_carpetas = "/".join(ruta_carpeta.split("\\"))
"""


# ---------------------------------------------------------------------
#Pegar la ruta de la carpeta con los XMLs, los "\" se cambian solos por "/"
#ruta_carpeta = r"C:\Users\ANALISTADECOSTOS\Desktop\xmls"
print("Script para el prov ______________________.\n")
ruta_carpeta = input("Pegue la dirección de la carpeta con las facturas en XML: \n->")
# ---------------------------------------------------------------------



#Funciona para las facturas del proveedor Sociedad Hermanos de la Caridad

#ruta_arreglada = "/".join(ruta_carpeta.split("\\"))
leer_archivos_escribir_csv(ruta_carpeta)
