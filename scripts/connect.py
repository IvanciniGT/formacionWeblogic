# docker exec -it -w /scripts miwl wlst.sh connect.py -loadProperties datos-conexion.properties -d datasources
import sys
import os
import weblogic

def imprimir_mensaje_importante(mensaje):
    line = "=" * len(mensaje)
    print("\n" + line)
    print(mensaje)
    print(line + "\n")
    
def imprimir_info_datasource(nombre, jndi, url, driver, usuario, servidor):
    print("-" * 20)
    print(" DataSource: %s" % nombre)
    print(" JNDI: %s" % jndi)
    print(" URL: %s" % url)
    print(" Driver: %s" % driver)
    print(" Usuario: %s" % usuario)
    print(" Servidor: %s" % servidor)

    print("-" * 20 + "\n")

def crear_propiedad(ruta, propiedad):
    cd(ruta)
    try:
        cmo.createProperty(propiedad)
    except weblogic.descriptor.BeanAlreadyExistsException:
        print("La propiedad "+propiedad+" ya existe para el recurso "+ruta+". Procedemos a su edicion.")


def asignar_propiedad(ruta, propiedad, valor):
    cd(ruta)
    set(propiedad,valor)


def crear_datasource(nombre, jndi, url, driver, usuario, password, servidor, test_query, conexionesMaximas):
    cd('/')
    try:
        cmo.createJDBCSystemResource(nombre)
    except weblogic.descriptor.BeanAlreadyExistsException:
        print("El datasource ya existe. Procedemos a su edicion.")
    
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
    
    asignar_propiedad(ruta_recurso+'/JDBCConnectionPoolParams/'+nombre, 'TestTableName', test_query)
    asignar_propiedad(ruta_recurso+'/JDBCConnectionPoolParams/'+nombre, 'InitialCapacity', 1)
    asignar_propiedad(ruta_recurso+'/JDBCConnectionPoolParams/'+nombre, 'MaxCapacity', conexionesMaximas)
    
    asignar_propiedad('/JDBCSystemResources/'+nombre, 'Targets',jarray.array([ObjectName('com.bea:Name='+servidor+',Type=Server')], ObjectName))

def crear_datasources():
    imprimir_mensaje_importante("Creando datasources.")
    carpeta_datasources=None
    for indice in range(1, len(sys.argv)): 
        parametro = sys.argv[indice]
        if parametro == "--datasources" or parametro == "-d":
            carpeta_datasources = sys.argv[indice + 1]
    if carpeta_datasources is not None:
        for datasource_index in range(1, 1000):
            try:
                fichero = carpeta_datasources+"/datasource"+str(datasource_index)+".properties"
                if not os.path.exists(fichero):
                    break
                loadProperties(fichero)
                print("Procesando fichero "+fichero)
                imprimir_info_datasource(datasource_nombre,
                                datasource_jndi,
                                datasource_url,
                                datasource_driver,
                                datasource_usuario,
                                datasource_servidor)
                crear_datasource(datasource_nombre,
                                datasource_jndi,
                                datasource_url,
                                datasource_driver,
                                datasource_usuario,
                                datasource_password,
                                datasource_servidor,
                                datasource_consultaDePrueba,
                                datasource_conexionesMaximas)
            except NameError,e:
                print("No se ha definido la propiedad del datasource "+str(e))
            except:
                break
    else:
        print("No se han encontrado datasources que cargar.")
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
    try: 
        usuario
    except NameError:
        usuario = None
    try:
        password
    except NameError:
        password = None
    try:
        protocolo
    except NameError:
        protocolo = None
    try:
        host
    except NameError:
        host = None
    try:
        puerto
    except NameError:
        puerto = None
        

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
        imprimir_mensaje_importante("Conectado al servidor weblogic.")
    except:
        print("Error: No ha sido posible conectarse con el servidor.")
        exit(1)

super_connect(_usuario="Weblogic", _protocolo="t3s", _host="localhost", _puerto=9002) 

edit()
startEdit()
imprimir_mensaje_importante("Editando el dominio.")
try:
    #crear_datasource("Mi Mysql", 
    #                 "jdbc/mysql", 
    #                 "jdbc:mysql://mysql:3306/basedatos", 
    #                 "com.mysql.jdbc.Driver", 
    #                 "usuario", 
    #                 "password", 
    #                 "AdminServer")
    crear_datasources()
    imprimir_mensaje_importante("Guardando y aplicando los cambios.")
    save()
    activate()
except:
    imprimir_mensaje_importante("Ha ocurrido un error al realizar los cambios.")
    import traceback
    apply(traceback.print_exception, sys.exc_info())
    stopEdit('y')

imprimir_mensaje_importante("Desconectando del servidor weblogic.")
disconnect()