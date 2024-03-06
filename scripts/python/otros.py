#print()
#range
#len
# Algunas de esas funciones se agrupan en paquetes
# Hay un paquete llamado os, que permite interactuar con el Sistema Operativo

import os # Quiero usar las funciones de Sistema Operativo de python

print( os.environ )

mi_diccionario = {"primero": 1,"segundo": "texto", "tercero": True}
print( mi_diccionario )

print( os.environ["PATH"] )

try:
    print( mi_diccionario["cuarto"] )
except: # Caso que te hayas encontrado con un error
    print("UPS, parece que no está la clave 'cuarto'")
    
print("pero el programa sigue ejecutándose")

print( mi_diccionario.get("tercero","dar un valor por defecto, caso que no exista") )
print( mi_diccionario.get("cuarto","dar un valor por defecto, caso que no exista") )


nombre = "Felipe"
print ( "Hola "+ nombre)
print ( "Hola %s" % nombre)

# El lunes que viene nos vamos a entibar
# El lunes que viene nos vamos a comer
print("Felipe")


cd('/Servers/AdminServer')
cmo.setListenPortEnabled(true)
cmo.set("ListenPortEnabled",true)
# CMO = Current managed object... Si cd nos permite movernos por "carpetas"
                                # El cmo es como si en la bash usamos el .

cmo.setClientCertProxyEnabled(false)
cmo.setListenPort(7003)
cmo.set("ListenPort",7003)
cmo.setJavaCompiler('javac')

cd('/Servers/AdminServer/SSL/AdminServer')
cmo.setEnabled(true)
cmo.setListenPort(7002)

cd('/Servers/AdminServer/ServerDiagnosticConfig/AdminServer')
cmo.setWLDFDiagnosticVolume('Low')

activate()







connect(...)
edit() # bloquear
startEdit() #Editar

cd('/JDBCSystemResources/Mi MySQL/JDBCResource/Mi MySQL/JDBCConnectionPoolParams/Mi MySQL')
cmo.setMaxCapacity(15)

save() #Guardar
activate() # Activar cambios
disconnect()