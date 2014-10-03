# -*- coding: utf-8 -*-

Campos_Archivo_csv = [

    Field('archivo_nombre_original',required=True),
    Field('archivo','upload',autodelete=True,required=True)

    ]

db.define_table('Archivo_csv',*Campos_Archivo_csv)
