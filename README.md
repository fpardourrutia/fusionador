fusionador
==========

###Introducción

El fusionador es una aplicación de Web2py, que recibe archivos CSV (generados por los clientes de captura a partir de sus bases de datos), y guarda la información en su base de datos asociada (SQLite ó PostgreSQL). Adicionalmente, permite exportar el contenido de esta base de datos a formato CSV, de tal forma que se pueda iterar en el proceso de integración de datos. Por ejemplo: fusionar las bases individuales de cada cliente de captura (SQLite) a bases parciales (SQLite), y fusionar éstas a la base final (PostgreSQL).


###Caracteristicas

1. El fusionador tiene un modelo análogo al del cliente de captura, con una tabla adicional: ‘Archivo_csv’, donde se guardarán los archivos a fusionar.

2. El fusionador tiene un controlador y una vista inicial análogos a los del cliente de captura.

###Funcionamiento

El fusionador tiene 4 controladores:

"1_fusionar_f":
Lee los archivos CSV
Para cada archivo CSV:
	Lo registra en la base de datos y lo inserta en uploads
	Borra los catálogos (paso que hay que ver si es necesario)
	Al final inserta los catálogos otra vez.

"2_revisar_f": Implementa las pantallas de revisión con ayuda de la SQLFORM.grid
Se instancian los requerimientos de los campos asociados a catálogos (para poder elegir de los catálogos mediante combobox)
Se generan las smartgrids para la edición.

"3_revisar_f": Revisión de fotografías insertadas en la tabla “Archivo_camara”, implementada como en el cliente.

"4_exportar_f": Exporta la base de datos (incluyendo tabla ‘Archivo_csv’) a un archivo CSV.

###Observaciones
1. Para evitar cualquier problema de incopatibilidad de esquemas de datos, el modelo de los clientes de captura con los que se creó el CSV debe ser el mismo que el del fusionador que lo recibe.
2. El fusionador únicamente se ocupa de las bases de datos, para fusionar los archivos hay que hacer un procedimiento adicional.
