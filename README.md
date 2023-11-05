# Script de extracción de datos de Facturacion Electrónica :page_with_curl:  
He creado este Script en Python para procesar de forma masiva facturas electrónicas de un mismo proveedor. Ver codigo en este repositorio (↑ arriba).
Este script lo he empleado como herramienta de ayuda en mi trabajo actual para automatizar pasos de un proceso en auditoria de costos, devolviéndome los datos necesitados en un archivo CSV el cual fácilmente se carga a Excel.

- El script se puede reaprovechar para distintos proveedores cambiando los patrones de búsqueda **RegEx** en las funciones de búsqueda de cada dato.
- El script está estructurado en bloques de funciones. Esto para más fácil comprensión, prueba o reutilización. Las partes son:
  - Detección de los XML en una carpeta cuya dirección se ingresa.
  - Apertura de cada XML y guardado de su contenido.
  - Búsqueda de cada uno de los segmentos de texto necesitados (los datos a extraer, una funcion por dato) en el contenido.
  - Ordenación de estos segmentos en una tabla en un archivo CSV y su creación.
  - Adicionalmente también maneja los errores en caso de que los segmentos necesitados no se encuentre.

-------------------------------------------------------------------------------------------------------

![pdf-to-xml2](https://github.com/jairo-andres-a-m/Script-Facturacion-Electronica/assets/124465699/d9915d31-70bb-4b7b-9cf3-c96aafbe7a86)


El Script funciona basado en que La Facturacion Electronica proporciona de forma estándar un documento PDF y un archivo XML (el cual "construye" el PDF como tal). El formato XML (Extensible Markup Language) es un formato muy extendió, usado para transmitir información de forma estructurada entre aplicaciones, páginas web o bases de datos, este formato puede leerse como un archivo plano de texto, el cual contiene etiquetas y tabulado que ayuda a representar la estructura del contenido de la factura.
