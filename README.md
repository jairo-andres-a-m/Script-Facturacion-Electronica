# Script-Facturacion-Electronica
He creado este Script en Python para procesar de forma masiva facturas electronicas de un mismo proveedor. Este script lo he empleado como herramienta de ayuda en mi trabajo actual para automatizar pasos de un proceso en auditoria de costos, devolviendome los datos necesitados en un archivo CSV el cual facilmente se carga a excel.

La estructura del Script se puede reaprovechar con proveedores distintos cambiando el patron de busqueda (dado que distintos proveedores manejan estructuras distintas en sus facturas)

El Script funciona basado en que La Facturacion Electronica proporciona de forma estandar un documento PDF y un archivo XML (el cual "construye" el PDF como tal). El formato XML (Extensible Markup Language) es un formato muy extendio, usado para transmitir informacion de forma estructurada entre aplicaciones, paginas web o bases de datos, este formato puede leerse como un arhivo plano de texto, el cual contiene etiquetas y tabulado que ayuda a representar la estructura.

Quien conozca una factura sabra que de acuerdo a quien emita la factura, esta tiene una presentacion y estructura distinta a la hora de representar los datos de una compra. Por esta razon, el script requiere de un mecanismo de busqueda o patron distinto de acuerdo.

por esto es necesario una busqueda distinta dado cada proveedor, pero la estructura 
