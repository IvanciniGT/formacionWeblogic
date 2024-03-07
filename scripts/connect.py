import sys
import os

def crear_propiedad(ruta, propiedad):
    cd(ruta)
    cmo.createProperty(propiedad)
    

def asignar_propiedad(ruta, propiedad, valor):
    cd(ruta)
    set(propiedad,valor)


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
    
    asignar_propiedad('/JDBCSystemResources/'+nombre, 'Targets',jarray.array([ObjectName('com.bea:Name='+servidor+',Type=Server')], ObjectName))


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

def inicializar_dato(valor_fichero, valor_codigo):
    if valor_codigo is not None:
        return valor_codigo
    return valor_fichero

def super_connect(_usuario=None, _password=None, _protocolo=None, _host=None, _puerto=None):
    global usuario, password, protocolo, host, puerto
    usuario = inicializar_dato(usuario, _usuario)
    password = inicializar_dato(password, _password)
    protocolo = inicializar_dato(protocolo, _protocolo)
    host = inicializar_dato(host, _host)
    puerto = inicializar_dato(puerto, _puerto)

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

super_connect(_usuario="Weblogic", _protocolo="t3s", _host="localhost", _puerto=9002) 

edit()
startEdit()
try:
    crear_datasource("Mi Mysql", 
                     "jdbc/mysql", 
                     "jdbc:mysql://mysql:3306/basedatos", 
                     "com.mysql.jdbc.Driver", 
                     "usuario", 
                     "password", 
                     "AdminServer")
        
    save()
    activate()
except:
    print("Ocurrio un error:")
    import traceback
    apply(traceback.print_exception, sys.exc_info())
    stopEdit('y')
    
disconnect()