# Script-Facturacion-Electronica
He creado este Script en Python para procesar de forma masiva facturas electronicas de un mismo proveedor. Este script lo he empleado como herramienta de ayuda en mi trabajo actual para automatizar pasos de un proceso en auditoria de costos, devolviendome los datos necesitados en un archivo CSV el cual facilmente se carga a excel.

La estructura del Script se puede reaprovechar para proveedores distintos cambiando el patron de busqueda **RegEx**, dado que distintos proveedores manejan estructuras distintas en sus facturas para mostrar una informacion de una compra, con algunas que otras variaciones u otros datos adicionales. El script esta estructurado de forma que se ayuda a comprender y se puede reaprovechar mas facil, tiene funciones para cada paso como: deteccion de los XML en una carpeta cuya direccion se ingresa, apertura de cada XML y guardado de su contenido, busqueda de cada uno de los segmentos de texto en este contenido, ordenacion de estos segmentos en una tabla en un archivo CSV y su creacion. Adicionalmente tambien maneja los errores en caso de que los segmentos necesitados no se encuentre.

![pdf-to-xml2](https://github.com/jairo-andres-a-m/Script-Facturacion-Electronica/assets/124465699/d9915d31-70bb-4b7b-9cf3-c96aafbe7a86)


El Script funciona basado en que La Facturacion Electronica proporciona de forma estandar un documento PDF y un archivo XML (el cual "construye" el PDF como tal). El formato XML (Extensible Markup Language) es un formato muy extendio, usado para transmitir informacion de forma estructurada entre aplicaciones, paginas web o bases de datos, este formato puede leerse como un arhivo plano de texto, el cual contiene etiquetas y tabulado que ayuda a representar la estructura.

