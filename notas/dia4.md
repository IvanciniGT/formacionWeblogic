# Tamaño del pool (máximo)
# Leer los datos de un fichero proerties
# Test query al fichero de parametros
# Y que pueda haber muchos ficheros
# Que el programa reciba un dato: carpeta que contiene los ficheros properties de datasources
# datasource1.properties , datasource2.properties, datasource3.properties
# IDEMPOTENCIA: Que de igual el estado de partida, que el script funcione...
# y me deje el sistema en el mismo estado siempre.

# Varios servidores


# DEVOPS

Es la cultura de la automatización.
Un movimiento global en pro de la automatización.
De qué? De todo lo que hay entre el DEV de un sistema y su OPS .

Las AUTOMATIZACIONES


---

En una máquina yo instalo weblogic:
- Puedo tener varios dominios definidos
    - Puedo levantar varios servidores de weblogic (instancias)

# NodeManager

Arrancar los servidores.
Esos servidores pertenecerán a un dominio X.

Yo a priori necesito un único nodemanager en un host.
El node manager es un proceso (JAVA independiente) que se levanta en el host.
Habitualmente lo configuramos como un servicio con arranque automático.
Y se encarga de recibir peticiones por un puerto de red para iniciar servidores de los dominios que gestione.


# Apps que despliego HTTP
tcp        0      0 172.19.0.2:7001         0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:7001          0.0.0.0:*               LISTEN     

# Apps que despliego HTTPs
tcp        0      0 172.19.0.2:7002         0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:7002          0.0.0.0:*               LISTEN     

# Consola administración
tcp        0      0 172.19.0.2:9002         0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:9002          0.0.0.0:*               LISTEN     

# Node Manager
tcp        0      0 127.0.0.1:5556          0.0.0.0:*               LISTEN     

Mi máquina (contenedor) tiene varias IP:
- En la interfaz de loopback: 127.0.0.1
- En la red de docker (mi red ethernet): 172.19.0.2

Quién se va a comunicar con el NodeManager?
- Administración de Weblogic (console)
- WLST

Donde tenemos la Administración de Weblogic. En qué máquina? En esta... (en nuestro caso un contenedor)
Podré copnectarme desde ahí al NodeManager según está configurado? SI

Si la admin estviera en otra máquina? podría? NO

/u01/oracle/user_projects/domains/base_domain/Script1709809174169.py


Si en una Máquina física (HOST) tengo varias IP...
- Puede ser que una de esas IPs sea de servicio.   eth0 - 192.168.0.101 (4 tarjetas de red 1Gb-10Gb... en bond)
- Pero otra de administración                      eth1 - 172.31.0.201 ( Otra de 100Mb) para administración
Y son redes físicas diferentes


# Cluster en WL

Es una agrupación de instancias, que me permite: 
- Hacer despliegues, aplicar configuraciones a todas a la vez

# Configuración del pool de ejecutores

Lo que me limita fijo es la RAM.
Las CPUs que tengo también son fijas... pero puedo graduar el uso de CPU? CLARO QUE SI... mediante el pool de ejecutores
Si abro un hilo... cuantas cpus voy a usar? como mucho 1
Si tengo 8 cores, cuantos hilos pueden estar a la vez ejecutando tareas? 8? NO
Los hilos hace trabajos de distinta naturales:
- Computos: CPU
- Leer o escribir un archivo: HDD (hilo sin usar la CPU)
- Leer o transmitir por red: RED (la CPU no se usa)
    - Acceso a BBDD (la CPU queda libre)

Puedo tener muchos hilos en paralelo. Entrando en CPU, como mucho, tantos como CPUs tenga (hyperthreading)
Pero... muchos hilos en un momento dado están a la espera: RED, HDD, BBDD, RAM

Cuantos más hilos, más uso de CPU voy a tener... siempre y cuando sature esos hilos.
400 hilos y recibo 400 peticiones. NPI de que va a pasar!

Voy a saturar el sistema:
200 peticiones y miro:
- RAM: Que no pete... ni se acerque mucho a petar: 80-90%
- CPU: Que no llegue al 100%

Y cuando hablo de sos porcentajes, es sobre el 100% marcado por HA: 25% (y si se caen 3 máquinas, que una pueda absorber toda la carga de trabajo)

Qué no llego aún... más hilos... y más peticiones.
Llegará un momento que una de las 2 cifras llegue al límite:
- CPU
- RAM
Y paro.
Esas cifras tendrían que llegar a saturarse en paralelo... Eso sería lo bonito. Eso es que tengo en el host bien aprovechados los recursos.
CPU al 100%
RAM al 30%. QUITA RAM!

Y con esos hilos, calculo las peticiones/segundo que puedo llegar a atender.
Si necesito atender más peticiones... más instancias(servidores) ESCALADO HORIZONTAL
                                      más máquina                ESCALADO VERTICAL
                                      
A todo esto, tendré en cuenta negocio. Quizás para 1 app, no necesito muchas peticiones (tengo pocos clientes).
Voy a montar una instancia por app? o meto varias apps en una instancia?
- 1 app por instancia
    Se me complica la configuración (tengo que crear un huevo de servidores)
- Varias apps por instancia
    Si una app toma demasiada memoria... me tumba todas las apps
    Si una app empieza a dejar hilos stuck... me tumba todas las apps


Maquina 1
    Instancia 1 - JVM 
        app1 ESTA SE VUELVE LOCA y tira la Instancia 1
        app2
        app3
Maquina 2
    Instancia 2
        app1
        app2
        app3

Pero he perdido una instancia para todas las apps
---

1. Configuramos otro servidor
2. Creamos un cluster con ese nuevo y el de antes
3. Desplegamos una app. BBDD a nivel de cluster
WLST. Dar de alta el recurso a nivel de cluster