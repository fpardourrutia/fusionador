fusionador
==========

El fusionador es una aplicación de Web2py, que recibe archivos CSV (generados por los clientes de captura a partir de sus bases de datos), y guarda la información en una base de datos interna a éste (SQLite ó PostgreSQL). Consta de 4 funcionalidades distintas:

1. Fusio

###Observaciones:
1. Para evitar cualquier problema de incopatibilidad de esquemas de datos, el modelo de los clientes de captura con los que se creó el CSV debe ser el mismo que el del fusionador que lo recibe.
