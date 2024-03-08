Maquina 1 - Admin
    Dominio 1
        AdminServer - Instancia para administración
           v
    NodeManager < WLST

Máquina 2 
    Dominio 1
        Instancia1 - Lo configuraremos como un servicio en el host
        Instancia2
    Dominio 2
        Instancia3 - Lo configuraremos como un servicio en el host
    NodeManager - Lo configuraremos como un servicio en el host


/u01/oracle/user_projects/domains/base_domain/bin/startNodeManager.sh &

---

# Montar una segunda máquina para el mismo dominio.

Pasos:
1- Tener una segunda máquina física
2- Instalar JVM y Weblogic en la segunda máquina
3- Copiar el diretorio del dominio a la segunda máquina. ESO NO SE HACE EN AUTOMATICO:
    - Copiando directamente los archivos de una máquina a otra: Más sencillo
        No se recomienda... porque hay que saber lo que se copia y hace.
    - Comandos especiales que ofrece wl: pack y unpack
        Realmente estos comandos me permiten:
            - Pack: generar una plantilla de dominio desde un dominio existente
            - Unpack: Desde una plantilla expandir un dominio (crear un dominio en un host)
        Estos comandos me sirven para replicar dominios... o para crear nuevos dominios similares a otros que tenga
        También para automatizar un redespliegue
        El unpack, nos permite tunear ciertos aspectos del dominio al hacer el unpack:
            - Cambiar usuario/contraseña, dev/prod
4- Arrancar NodeManager
5- Arrancar servidores de WL. Qué servidores?

---

TLS:
Nos ayuda frustrar 2 tipos de ataques:
- Man in the middle: Encriptamos los mensajes
   Tenemos 2 tipos de algoritmos clave simétrica/asimétrica
    SIMETRICA: con una clave que se genera en cada comunicación y se comparte cifrada mediante un algoritmo de clave asimétrica.
    Asimétrico: Par de claves (pública y una privada)
- Phishing: Suplantación de identidad: AUTENTICAR a un servidor: CERTIFICADO
    TLS doble: El cliente también presenta certificado.

En el caso de java, esos datos se guardan en un fichero jks (llavero), que incluye datos cifrados:
- Clave privada
- Certificado (incluyendo nuestra clave pública)
- Certificado de las CAs en las que confiemos

----


Demora: 1000                Tiempo que simula trabajo en el ExecutorThread
                            No consume cpu... pero hace que se retrasen las peticiones
Demora BBDD: 1              Tiempo que simula trabajo en una conexión de BBDD
                            No consume CPU... pero bloquea la conexión
Objetos en Cache: 50        Tiene impacto en la RAM permanente asociada a la app
Objetos por peticion: 5     Simula datos que se cren asociados a una petición. 
                            Al acabar la petición ya no son necesarios... y el GC puede borrarlos.
                            
---

JAVA es un lenguaje compilado e interptretado

En la JVM de JAVA hay un proceso que corre llamado JIT: JustInTime compiler.
Ese es el que hace la interpretación en tiempo de ejecución.
En JAVA 1.2 se añadió un módulo a ese JIT, llamado el HOTSPOT.
Ese módulo es una caché de compilaciones.
De forma que la primera vez que se ejecuta un código BYTE-CODE (lo que los desarrolladores mandan en los war... jar)
ese código es interpretado (compilado en tiempo real) y el resultado de la compilación(interpretación) 
se guarda en una caché (HOTSPOT)
Esa cache es compleja... trabaja mediante conceptos estadísticos... 
las partes del código que más se van usando, son las que se van almacenando en caché.

El resultado es que:
- Cuando arranco una app JAVA o empiezo a hacer peticiones a pantallas que aún no han sido muy utilizadas, 
  obtendo unos tiempos de respuesta malos.
- Según voy usando la app, el HOTSPOT(esa caché) se va llenando.
  Y eso hace que las ejecuciones se vuelvan más rápidas

No me puedo fiar de los primeros tiempos que vea... tengo que CALENTAR LA JVM 
---

Sé que una petición tarda 2 segundos. LINEA BASE
Esto lo marca la propia app y su nateuraleza (las cosas que hace)
Mejor tiempo que ese no lo voy a tener.
Mi objetivo como configurador del WL es mantener ese tiempo para la carga de trabajo prevista
En nuestro caso al poner 100 peticiones se nos van los tiempos a 9 segundos.
10 peticiones por segundo.
PROBLEMAS POTENCIALES. ORIGENES DEL CUELLO DE BOTELLA:
- Necesito más hilos del pool de ejecutores... los he saturado. NO ES MI CASO
- GC está entrando mucho. NO ES PROBLEMAS
- Pool BBDD
 
---
Parámetros para trobleshooting de la Memoria y el GC

# Volcado del heap en caso de OutOfMemory
-XX:+HeapDumpOnOutOfMemoryError
-XX:HeapDumpPath=/tmp/dumpHeapJava (jvisualvm o jsualvm / JProfiler / ECLIPSE ... viene con java de oracle)
    PROBLEMA: 
        - Genera un fichero que ocupa un huevo: 16Gbs de RAM -> Fichero de 16Gbs
        - Tarda un huevo. Mientras se hace, no se acaba el proceso JAVA... y por ende no puedo reiniciarlo.

    Esos programas permiten ordenar por tipo de objeto y lo ocupa en RAM... y cantidad de datos de un tipo que tengo en RAM.
    
# Estos hacen un log del recolector de basura.
-XX:+PrintGCDetails
-XX:+PrintGCDateStamps
-Xloggc:/ruta/al/archivo/gc.log
-XX:SurvivorRatio=5
Quiero un ratio 1:5 entre young y old

OLD => CACHE + SESIONES DE USUARIO (stateful... guardan datos de la sesion del usuario en el servidor)
YOUNG solo nos intera los datos asociados a las peticiones

Me permite ver cuánto entra el GC y cuánto libera cada vez que entra
Problema, pequeño impacto en rendimiento
El problemón es el tamaño de archivo que genera

System.gc(); # ESTO ES MALA PRACTICA !