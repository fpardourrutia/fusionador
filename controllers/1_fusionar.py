# -*- coding: utf-8 -*-
import os

def index():
    
    #Creando una forma para que se suban los archivos CSV múltiples,
    #que contienen la información de cada base de datos enviada a CONAFOR

    Campos_forma = [
        INPUT(_name='archivos_csv',_type='file',requires=[IS_NOT_EMPTY()],
              multiple=True), #tipo: csv
    ]
    
    forma = FORM(*Campos_forma)
    
    if forma.accepts(request.vars,formname='formaHTML'):
        
    	################Procesando los archivos múltiples#################################
    	
    	archivos = forma.vars['archivos_csv']
    	if not isinstance(archivos, list):
            
            archivos = [archivos]
    		
        for aux in archivos:
            
            #Guardando el archivo en la carpeta adecuada
            archivoCSV = db.Archivo_csv.archivo.store(aux, aux.filename)
    		
            datosArchivoCSV = {}
            datosArchivoCSV['archivo'] = archivoCSV
            datosArchivoCSV['archivo_nombre_original'] = aux.filename
    	
    		#Insertando el registro en la base de datos:
            
            db.Archivo_csv.insert(**datosArchivoCSV)
            
            #Importando el contenido del archivo en la base de datos:
            
            nombre_archivo = os.path.join(request.folder,'uploads',archivoCSV)
            
            db.import_from_csv_file(open(nombre_archivo,'r'))
	
        response.flash = 'Éxito'
        
    elif forma.errors:
        
       response.flash = 'Por favor, introduzca archivos del tipo CSV'
       
    else:
    	response.flash ='Por favor, introduzca los archivos CSV a fusionar'
        
    return dict()
