import sys
import os

def crear_propiedad(ruta, propiedad):
    cd(ruta)
    cmo.createProperty(propiedad)
    

def asignar_propiedad(ruta, propiedad, valor):
    cd(ruta)
    cmo.set(propiedad,valor)
    

def crear_datasource(nombre, jndi, url, driver, usuario, password, servidor):
    cd('/')
    cmo.createJDBCSystemResource(nombre)
    
    ruta_recurso = '/JDBCSystemResources/'+nombre+'/JDBCResource/'+nombre
    
    asignar_propiedad(ruta_recurso, "Name", nombre)
    asignar_propiedad(ruta_recurso, "DatasourceType", "GENERIC")

    asignar_propiedad(ruta_recurso+'/JDBCDataSourceParams/'+nombre, 'JNDINames', jarray.array([jndi], String))
    asignar_propiedad(ruta_recurso+'/JDBCDataSourceParams/'+nombre, 'GlobalTransactionsProtocol', 'None')

    asignar_propiedad(ruta_recurso+'/JDBCDriverParams/'+nombre, "Url", url)
    asignar_propiedad(ruta_recurso+'/JDBCDriverParams/'+nombre, "DriverName", driver)
    asignar_propiedad(ruta_recurso+'/JDBCDriverParams/'+nombre, "Password", password)
    crear_propiedad(  ruta_recurso+'/JDBCDriverParams/'+nombre+'/Properties/'+nombre, 'user')
    asignar_propiedad(ruta_recurso+'/JDBCDriverParams/'+nombre+'/Properties/'+nombre+'/Properties/user', 'Value', usuario)
    
    asignar_propiedad(ruta_recurso+'/JDBCConnectionPoolParams/'+nombre, 'TestTableName', 'SQL SELECT 1')
    
    asignar_propiedad('/JDBCSystemResources/'+nombre, 'Targets',jarray.array([ObjectName('com.bea:Name='+servidor,Type=Server)], ObjectName))
    

def pedir_dato_por_consola(mensaje, valor_por_defecto):
    dato = raw_input(mensaje + " [" + valor_por_defecto + "]: ")  
    if len(dato) == 0:
        dato = valor_por_defecto
    return dato

def obtener_datos_conexion(usuario, password, protocolo, host, puerto):
    # Miro a ver si me han pasado algunos datos de conexión mediante argumentos del script
    # sys.argv =  [ "redimensionarPoolBBDD.py", "mysql", "25", "--port", "9002", "--user", "Weblogic", "-h", "localhost" ]
    for indice in range(1, len(sys.argv)): 
        parametro = sys.argv[indice]
        if parametro == "--user" or parametro == "-u":
            usuario = sys.argv[indice + 1]
        elif parametro == "--password" or parametro == "-p":
            password = sys.argv[indice + 1]
        elif parametro == "--host" or parametro == "-h":
            host = sys.argv[indice + 1]
        elif parametro == "--protocol" or parametro == "-t":
            protocolo = sys.argv[indice + 1]
        elif parametro == "--port" or parametro == "-P":
            puerto = sys.argv[indice + 1]

    # Para aquellos datos de conexión que no tengan valor, miro a ver si están definidos en variables de entorno
    if usuario is None:
        usuario = os.environ.get("WEBLOGIC_USER_NAME")
    if password is None:
        password = os.environ.get("WEBLOGIC_PASSWORD")
    if protocolo is None:
        protocolo = os.environ.get("WEBLOGIC_PROTOCOL")
    if host is None:
        host = os.environ.get("WEBLOGIC_HOST")
    if puerto is None:
        puerto = os.environ.get("WEBLOGIC_PORT")
        
    # Para aquellos datos de conexión que no tengan valor, se los pido al usuario
    if usuario is None:
        usuario = pedir_dato_por_consola("Usuario con el que conectar a Weblogic","weblogic")
    if password is None:
        password = pedir_dato_por_consola("Password con el que conectar a Weblogic","password")
    if protocolo is None:
        protocolo = pedir_dato_por_consola("Protocolo con el que conectar a Weblogic","t3")
    if host is None:
        host = pedir_dato_por_consola("Host con el que conectar a Weblogic","localhost")
    if puerto is None:
        puerto = pedir_dato_por_consola("Puerto con el que conectar a Weblogic","7001")
    
    return (usuario, password, protocolo, host, puerto)


def super_connect(usuario=None, password=None, protocolo=None, host=None, puerto=None):

    (usuario, password, protocolo, host, puerto) = obtener_datos_conexion(usuario, password, protocolo, host, puerto)

    url = protocolo + "://" + host + ":" + str(puerto)
    print("Conectando al servidor weblogic:")
    print(" URL: %s" % url)
    print(" Usuario: %s" % usuario)
    print(" Password: %s" % password)
    try:
        connect(usuario, password, url) # Llamo al weblogic
        print("Conectados al servidor")
    except:
        print("Error: No ha sido posible conectarse con el servidor.")
        exit(1)

try:
    usuario
except NameError: # No me han pasado el usuario en un fichero properties
    usuario = None
try:
    password
except NameError: # No me han pasado el password en un fichero properties
    password = None
try:
    protocolo
except NameError: # No me han pasado el protocolo en un fichero properties
    protocolo = None
try:
    host
except NameError: # No me han pasado el host en un fichero properties
    host = None
try:
    puerto
except NameError: # No me han pasado el puerto en un fichero properties
    puerto = None
    
usuario = "Weblogic"
protocolo = "t3s"
host = "localhost"
puerto = 9002
    
super_connect(usuario, password, protocolo, host, puerto ) # Se cargan del properties

crear_datasource("Mi Mysql", 
                 "jdbc/mysql", 
                 "jdbc:mysql://mysql:3306/basedatos", 
                 "com.mysql.jdbc.Driver", 
                 "usuario", 
                 "password", 
                 "AdminServer")

disconnect()