# Qué es weblogic?

Un servidor de aplicaciones JAVA.

# JAVA

Cuando hablamos de JAVA nos referimos a 2 cosas bien diferentes:
- A un lenguaje de programación
- A un intérprete de código escrito en lenguaje byte-code

# Java como lenguaje de programación

Es un lenguaje con algunas características:
- Que soporta paradigmas: imperativo, procedural, funcional y "orientado a objetos"
- De tipado estático: Las variables tienen asignado un tipo de datos.

    Los datos que manejamos por un programa siemrpe tienen un tipo determinado... da igual el lenguaje de programación que utilice.
        Número: 33
        Texto: ivan@osuna.com
        Fecha: 01-03-2024
    Esos datos donde se guardan?
        - Memoria
        - Fichero de configuración
        - BBDD
        - Sistema de caché? Coherence
            0001 0000 0000 1010 0011 1101 -> Si lo interpreto como número: 12727
                                             Si lo interpreto como caracter: à
    Cuando guardo datos, en memoria, necesito poder luego acceder a esos datos  ---->  Mediante una variable
    Cuando guardo datos, en bbdd, necesito poder luego acceder a esos datos     ---->  Mediante una Identificador
    
    La memoria RAM la imaginamos como un cuaderno de cuadricula. Yo, al hacer un programa no guardo cosas en la RAM,
    se lo pido (delego) al SO.
    
        ```java
        String texto = "Hola";
        ```
        Esta linea de código hace 3 cosas:
            - "hola"        Ésto crea un "texto" (string) con el valor "hola" en memoria RAM.... en algún sitio... npi de donde
            - String texto  Ésto crea una variable, que puede asignarse a textos
                            Saco un postit del taco de postit de los de tipo texto (de los verdes)... 
                            En el postit escribo dentro la palabra "texto" (en nombre de la variable)
            - =             Asigna la variable al dato.
                            Pego el postit en la ram (en el cuaderno) al lado de donde se ha escrito "hola"
        En los lenguajes de tipado estático, las variables tienen asignado un TIPO de datos, también... igual que los datos.

    Si hemos dicho que la RAM es como un cuaderno de cuadrícula, una variable es como un postit.
    En JAVA (y otros, como JS, python)... las variables atienden más a la definición de PUNTERO!
    
        ```java
        String texto = "Hola";
        texto = "adios";
        ```
        Esta linea: 
            - "adios"       Ésto crea un "texto" (string) con el valor "adios" en memoria RAM.... en algún sitio... npi de donde
                            En un sitio diferente a donde está escrito "hola".
                            Llegados a este punto, cuántas cosas de tipo texto tengo en RAM? 2: "hola", "adios"
            - texto         Arranco el postit de donde estaba pegado 
            - =             Asigna la variable al dato.
                            Pego el postit en la ram (en el cuaderno) al lado de donde se ha escrito "adios"
        Llegados a este punto, el texto "hola" cuantos postit tiene al lado? Ninguno
        Se ha convertido en BASURA, ya que es un dato irrecuperable de la RAM.
        En un momento dado, quizás si... o quizás no... entrará el Recolector de Basura de JAVA (Garbage collector) y lo eliminará,
        marcando esa zona de memoria como libre de nuevo... para que pueda albergar otro dato.
    
    Yo podría hacer este mismo programa en C... y forzar desde el principio a que el dato "adios" se escribierá en la RAM en la misma zona 
    donde se guardaba el dato "hola". En JAVA no puedo hacer eso. No se permite... no hay instrucción en el lenguaje que nos deje hacer tal cosa a los desarrolladores.
    
    Dicho de otra forma: 
        El mismo programa hecho en JAVA necesita el doble de memoria RAM para funcionar que si lo hubiera hecho en C.
        JAVA es un lenguaje de programación que hace un destrozo (un uso muy poco eficiente) de la memoria RAM.
    
    Eso es bueno o malo... el que JAVA haga esto? ES UN FEATURE !
    JAVA se diseño de esa forma.
    El que creo JAVA dijo... voy a hacer un lenguaje que destroce la RAM.
    Crear programas en C++ o C es mucho más complejo que montarlos en JAVA. El desarrollador de C o C++ tiene que gestionar él mismo la memoria RAM... reservar memoria RAM... librerar memoria RAM... trabajar con PUNTEROS a bajo nivel.
    En el código C o C++ es muy habitual dejar MemoryLeaks... Son datos (basura) que no marco para su eliminación (yo como desarrollador)
    
    Echamos cuentas...
    - Cuantas horas de desarrollador C++  necesito para montar una APP: 500 horas x 60€/hora = 30000
    - Cuantas horas de desarrollador JAVA necesito para montar una APP: 450 horas x 50€/hora = 22500
                                                                                              ------
                                                                                                7500 €
    - Cuanto me cuesta 32 Gbs de Ram más al servidor: 500€ 
    Blanco y en botella! Más memoria!
    
    Ese recolector de basura es un proceso (un programa) que se ejecuta paralelo a mi programa. Ambos 2 programas los ejecuto dentro de una Máquina VIRTUAL.... como si la hubiera creado en hyperV, kvm... Citrix, vmware o virtualBox: JVM

- Los lenguajes de programación los clasificamos adicionalmente en: compilados / interpretados

    Quién ejecuta (quién está en comunicación) con mi programa? Sistema Operativo
        Y el SO sabe de JAVA? NPI
        Y el SO sabe de C?    NPI
        Y el SO sabe de PYTHON? NPI
    Los SO solo hablan su lenguaje propio.
    
    Cuando yo escribo un código (un programa) y uso un lenguaje de programación, ese código hay que traducirlo al lenguaje del SO.
    Y hay 2 grandes formas de hacer este trabajo:
    - PRETRADUCCION:             COMPILACION/ENSAMBLADO
    - TRADUCCION EN TIEMPO REAL: INTERPRETACION (que se realiza por un intérprete)
    
    C es un lenguaje?       Compilado
    PYTHON es un lenguaje?  Interpretado
    BASH?                   Interpretado
    JAVA?                   Compilado y además INTERPRETADO
    
            PROGRAMA                 COMPILACION                                    INTERPRETADOS (JIT)
               ||                                                                     JVM
        Colección de ficheros .java  -- javac --->  Colección de ficheros .class   -- java -->
                                                Esos ficheros están en un lenguaje de 
                                                programación llamado byte-code (.jar, .war, .ear.. archivos .zip con la extensión cambiada)
    
    La arquitectura de la JVM es una pasada... está muy bien pensada... y funciona muy bien.
    JAVA como lenguaje de programación hace aguas por todos los sitios.
    De hecho hoy en día tenemos alternativas al lenguaje de programación JAVA que usan la arquitectura de la JVM para funcionar
    
        KOTLIN?
        colección de ficheros .kt     -- kotlinc ---> .class ---> JVM
        colección de ficheros .scala  -- scalac  ---> .class ---> JVM
        
    La compilación tiene muchas ventajas: Hacemos una revisión completa del código (una relectura) para poder traducirlo...
    Y en ese momento tenemos la oportunidad de identificar errores que hayamos cometido.
    La interpretación también tiene sus ventajas: Me quito de encima el follonazo de gestionar multiples distribuciones de mi programa:
    - Una distribuciuón para Windows
    - Una distribuciuón para MacOS
    - Una distribuciuón para Linux
    Siempre distribuyo lo mismo... a todo el mundo... Que se preocupen ellos de tener un INTERPRETE ADECUADO.
    
## J2EE 

    J2EE                    -> JEE                      ---> JEE
    Java Enterprise Edition    Java Enterprise Edition       Jakarta Enterprise Edition
    
Es una colección de ESTANDARES que especifican cómo montar una aplicación usando lenguaje JAVA para su uso en empresas.
Dentro de esta colección de estándares encontramos:
- Cómo montar código JAVA que sea accesible desde el serv. de aplicaciones: 
    - Servlets
    - JSPs
    - JFCs
- JDBC: Cómo conectar con BBDD desde JAVA
- JMS:  Mensajería
- JPA:  Persistencia
    Hibernate: Es una librería JAVA para ayudar a trabajar con BBDD... escribe las queries por el desarrollador.
        Hibernate ----> JPA
- Como empaquetar una aplicación web para su despliegue en uno de esos servidores web: (.war .ear)
Hoy en día, los desarrollos los hacemos mediante el framework Spring de JAVA... y dentro de usa Hibernate y JPA.

Hoy en día se han puesto de moda las arquitecturas de microservicios, que van en contraposición total de las arquitecturas MONOLITICAS.
Antiguamente monábamos apps MUY GRANDES y muy complejas.. que hacían muchas cosas... Nos dimos cuenta que el mnto y evolución de estos sistemas es una tortura!!!
Y hoy en día no montamos ya esas apps tan grandes... lo que montamos son sistemas constituidos por muchas miniaplicaciones (microservicios)
que todos juntos ofrecen la funcionalidad que antes ofrecian los mega-sistemas monolíticos.

Esas mega-aplcaciones que montábamos antes necesitaban de un MEGASERVIDOR de apps (Weblogic-Oracle-Bea systems, Websphere-IBM, JBoss-Redhat-Wildfly)
Hoy en día que montamos MINIAPLICACIONES, tiramos con Tomcat.

Dentro del estandar JEE, también se define lo que es un Servidores de aplicaciones... y los tipos de servidores de apps:
- Serv app de clase empresarial: Weblogic
- Serv de apps de clase web: Tomcat

---

# HISTORIA DE JAVA

Java versión 1.0 sale en el 1996
Java versión 1.1 sale en el 1997
Java versión 1.2 sale en el 1998
Java versión 1.3 sale en el 2000
Java versión 1.4 sale en el 2002
Java versión 1.5 sale en el 2004
Java versión 1.6 sale en el 2006
--- Oracle compra SUN Microsystems... y java le vale mierda
    MySQL       ---> MariaDB
    OpenOffice  ---> LibreOffice
    Hudson      ---> Jenkins
Java versión 1.7 sale en el 2011... EIN??? 5 años???
Java versión 1.8 sale en el 2014... EIN??? 3 años???
    A Oracle se le ocurre la genial idea de decir... voy a cobrar por la JVM:
        25$/year a los usuarios individuales
        50$/month por core en servidor en empresas
    Google forzó a Oracle a muchas cosas:
        - Liberar la JVM... convirtiéndola en un ESTANDAR !
            Hoy en día tenemos MUCHAS implementaciones de la JVM... antes solo la de Oracle:
                - oracleJDK
                - openJDK
                - Eclipse Temurin
                - Amazon Correto
            Llegar a un acuerdo para generar nuevas versiones de Java cada 6 meses
        - Quistarse de en medio el JEE--> SE donó a una fundación independiente: JAKARTA
            De hecho desde Java17, hay un cambio de nomenclatura en las librerías de java:
                java.http
                jakarta.http
    Google no perdonó:
        - Solicitar a JetBrains (la gente que fabrica el mejor IDE de JAVA: IntelliJ) la creación de un nuevo lenguaje de programación,
        compatible con la arquitectura de la JVM: KOTLIN, para quitarse a JAVA como lenguaje de encima en Android
        - Liberaron el interprete de JS del navegador Chromium (base de Chrome, Edge, Safai, Opera...) como proyecto independiente
        para poder ejecutar código JS fuera de un navegador: NODE JS
            NODE es el equivalente en el mundo JS a la JVM
Java versión   9 sale en el 2017... EIN??? 3 años??? En 11 años, 3 versiones
Java versión  10 sale en el 2018... EIN??? 1 año??? En 4 años, 2 versiones
    Además... no cualquieras 11 años... Del 2006-2017... Cuando explota el mundo web, los smatphones.
Java versión  11 sale en el 2018... 
Java versión  12 sale en el 2019... 
Java versión  13 sale en el 2019...
Java versión  14 sale en el 2020...
Java versión  15 sale en el 2020...
Java versión  16 sale en el 2021...
Java versión  17 sale en el 2021...
Java versión  18 sale en el 2022...
Java versión  19 sale en el 2022...
Java versión  20 sale en el 2023...
Java versión  21 sale en el 2023...
Java versión  22 sale en el 2024...

# Servidor de aplicaciones

Lo podríamos definir como un servidor WEB vitaminizado.

## Mundo WEB

La web arranca en 1995, con Tim Berners Lee: http + html

Nos permite acceder a documentos html en un servidor remoto, mediante peticiones HTTP.

    cliente:                            servidor:                                                                       HDD
        navegador web ----> http -->        servidor web: (apache httpd, nginx, iis)                                  /var/html
                                                atender una petición http://miservidor.es/index.html              ---> DOCUMENT_ROOT /index.html
                                                                     http://miservidor.es/contacto/horarios.html  ----> D_R /contactos/horario.h

En un momento dado, nos hastiamos de páginas web tan simplonas... queríamos más. Nos interesaba tener la capacidad de devolver a cada usuario que hiciese una petición un documento html generado bajo demanda: Aplicación WEB
Los html ya no eran generados por personas, sino por programas: JAVA, PHP, C

Los servidores web tuvieron que mutar... evolucionar... Su trabajo ya no era buscar un archivo en un HDD... sino :
Pedir a un programa que genere un HTML... capturarlo y enviarlo al cliente.

Esos servidores web, con capacidad de hablar con programas creados en un determinado lenguaje de programación es lo que se denominó Servidores de aplicaciones.

Poco a poco... estos servidores web fueron además tomando más responsabilidades.
Cosas que hacíamos en todas las aplciaciones... en lugar de rehacerlas desde cero en cada una... las empezamos a reutilizar... y esa funcionalidad se la comen los servidores de aplicaciones:
- Gestionar las conexiones a una BBDD 
- Trabajar con un sistema de mensajería
- Guardar algo en una cache
- Gestiono la sesión del usuario

---

Internet es un conjunto de redes descentralizado... que permite comunicar computadoras muy alejadas geográficamente.
Sobre internet funcionan muchos tipos de servicios:
- Correo electrónico: IMAP, POP3, SMTP
- Envío de archivos: P2P, FTP
- TVIP
- VozIP
- Juegos online
- WEB: HTTP

---

# Despliegue de apps dentro de un servidor de apps JAVA

Ese JAVA alude a la JVM... que decíamos que interpreta lenguaje Byte-Code

## Archivos .war

En el estandar JEE de define como empquetar una aplciación para su despliegue en un servidor de apps java:

    carpeta/ (1)
        WEB-INF/
            web.xml     Con configuración de mi aplicación
            classes/
                archivos .class (bytecode)                                              ***
            lib/
                archivos .jar (comprimidos .zip conteniendo archivos .class) de mi app  ***
                dependencias que tenga mi app
        otras carpetas/
        otros archivos/ Con contenido estático (imágen... pdf...css....js)
        Adicionalmente podemos encontrar por aquí fuera archivos .jsp, que son plantillas HTML que dentro llevan snippet (trocito) de código JAVA.
        
        
        *** Entre otros, ahí irán los servlets de la aplicación.
        Un servlet es un programa hecho en JAVA (una clase) que tiene una función: doGet(HttpRequest, HttpResponse),  doPost(HttpRequest, HttpResponse)
        
        En el archivo de configuración (web.xml) se mapean los servlets (Código JAVA) a las URL asociadas
            http://SERVIDOR:PUERTO/app/RUTA1     ----->      Servlet17.class
    
    Un archivo .war, que es lo más sencillo que podemos desplegar en un servidor de aplicaciones JAVA es un ZIP de la estructura de arriba (1)
    
Cuando instalamos JAVA en una máquina, tradicionalmente hemos tenido 2 distribuciones paralelas:
- JRE: Java Runtime Edition
        Esto lleva dentro la máquina virtual de JAVA: comando java
- JDK: Java development Kit
        Esto lleva dentro la máquina virtual de JAVA: comando java + compilador de java: javac

Pregunta... qué necesitan los app web servers JAVA: JRE o JDK.
- JRE √
- JDK √√√   <<<<<< Por el compilador por si hay .jsp

Va a compilar el servidor de aplicaciones código JAVA? o es algo que ya hizo el desarrollador.. y lo que llega al servidor de aplicaciones es un archivo comprimido que dentro lo que tienes es byte-code (ya compilado java) ?
En los archivos .war pueden venir archivos .jsp... que llevan JAVA PELAO .. sin precompilar...
Y será responsabilidad del servidor de aplciaciones el precompilar esos JSPs (el JAVA que hay dentro)
Por eso los servidores de aplciaciones requieren de JDK... y no solo del JRE

## Archivos .ear

Para su despliegue necesito un servidor de aplicaciones de clase EMPRESARIAL... No alen los servidorcitos de apps tipo TOMCAT

Un archivo ear es otro comprimido zip...
que dento puede llevar:
- 1 o varios archivos .war < Cada .war es una aplicación
- 1 o varios archivos .jar (que tengan dentro lo que en JEE se denomina un Java Enterprise Bean)

Un Java Enterprise Bean es un programa que permite acceder a unos datos... y que puede ser compartido por multiples aplicaciones.

## Archivos .jar

Un archivo .jar no lleva dentro una aplciación web (a priori)... al menos el tipo de archivos .jar que nosotros vamos a trabajar.
Antiguamente ( y hoy en día... aunque hoy en día se usan para otras cossas adicionales) dentro de los archivos .jar iban librerías JAVA o aplicaciones AUTOEJECUTABLES (script java... app de consola java... app desktop java).

En los servidores de aplciaciones JAVA en ocasiones desplegamos archivos .jar (librerías)... como por ejemplo los drivers de las bases de datos.
Hemos dicho que el servidor de apps es el que va a agestionar las conexiones a la BBDD... Por tanto necesita de un driver para comunicarse con la BBDD... No la aplicación... el servidor de apps... y es necesario cargarle esos drivers, que vienen como archivos .jar.

    NOTA: 
        Os decía que hoy en día usamos mucho Spring para crear apps (microservicios)
        Una app realizada con Spring (Framework de desarrollo java) genera un archivo .jar... que dentro lleva:
        - Una app web JAVA .war
        - Un servidor de aplicaciones embebido (tomcat, jetty)
        Ese archivo jar es ejecutable por la JVM

---

# Comunicaciones con la BBDD

Cuando un desarrollador necesita que su aplicación ejecute una query a la BBDD... para ejecutar esa QUERY necesita una CONEXION a la BBDD.
Me pasa igual si quiero conectarme desde un cliente de escritorio a una BBDD... Abro una CONEXION a la BBDD.

Las conexiones a las BBDD son muy diferentes si las miro desde el punto de vista de un desarrollador de una aplicación o si las veo desde el punto de vista de la BBDD.

Una conexión a bbdd en un cliente (mi aplicación puede ser un cliente de la bbdd) se abre en un hilo de ejecución dentro del proceso asociado a ese cliente (mi aplicación).

Tengo una app de escritorio: TOAD

Cuando ejecuto el TOAD se abre un proceso a nivel de SO. 
El SO abre un hilo para ese proceso... y empieza a ejecutar el código... El hilo
- Arranca la app...
- Muestra la ventanita de turno...
En un momento dado quiero ejecutar una query en ese cliente (TOAD)
Necesito una conexión.
El desarrollador del toad (o de mi app web) tiene 2 opciones:
1. En su hilo de ejecución principal, abrir una conexión con la bbdd... lanzarle la query... esperar a que acabe ... y mostrar por pantalla los resultados.,
2. Que su hilo principal abra un segundo hilo.
    - En ese segundo hilo, abrir una conexión con la bbdd... lanzarle la query... esperar a que acabe ... y mostrar por pantalla los resultados.
    - Mientras en paralelo tengo el hilo principal libra para otras tareas de la aplicación: Ejecutar una segunda query en paralelo... Cancelar la query que he ejecutado

Las conexiones a la BBDD siempre las hacemos en hilos de ejecución paralelos al principal asociado al proceso (a mi aplciación)

Los desarrolladores abren hilos para comunicarse con una BBDD.
Las BBDD abren procesos a nivel de SO para cada conexión establecida.
    Una conexión contra un oracle da lugar a un proceso nuevo a nivel de SO.... con su reserva de RAM... su código a la memoria...
    
A nivel de SO, pensais que abrir un hilo es algo que consuma muchos recursos? NO... de hecho podemos abrir miles de hilos sin problema.
A nivel de SO, abrir un proceso es algo que consuma muchos recursos? Desde luego es otra liga comparado con los hilos.
El proceso requiere de reserva de memoria RAM, subida de código a RAM, creación de un hilo, preparación de un thread stack region en la RAM.... un follón.... comparado con lo que es abrir un hilo.

Pero las BBDD para conexión abren procesos. Y es que los hilos que se ejecurán dentro de esos procesos NO DEBEN COMPARTIR MEMORIA RAM (al menos no toda).

Si abro una conexión a la BBDD...
    Y hago 25 inserts
    75000 updates
    4350 deletes
    ... donde se guarda todos esos cambios que voy haciendo a los datos? en un fichero de la BBDD? NO hasta que se ha realizado una operación llamada COMMIT (confirmación de los cambios)
    
Si entre medias tuviera otra conexión a la BBDD que hicera una query... vería los cambios QUE VA HACIENDO (aún sin commitear) el otro proceso? NO... Cada uno tiene su propia memoria RAM.

Esos 2 procesos adicionalmente operan en conjunto con un tercer proceso: El de la BBDD que he arrancado.
El servidor va colocando en RAM datos de los ficheros que van siendo usados.
Ese proceso le pide al SO (es una funcionalidad que ofrecen los SO) que un trozo de su memoria RAM sea accesible por otros procesos (SHARED MEMORY)

    PROCESO PRINCIPAL BBDD                                      PROCESO CONEXION 1              PROCESO CONEXION 2
        RAM                                                     RAM                             RAM
            ZONA RESTRINGIDA.           ZONA COMPARTIDA         ZONA RESTRINGIDA                ZONA RESTRINGIDA
        ------------------------------------------------------------------------------------------------------------------
            Datos que leo de            Cache de las tablas     Modificaciones sin commit       Resultado de una query
            ficheros de configuración

Resumen:
A nivel de la BBDD, abrir una conexión es un follón de huevos... 

Como consecuencia:

Cuando estoy montando una app WEB, de esas en JAVA que desplegaremos en el Weblogic...
Y necesito una conexión a la BBDD... en el lado del WEBLOGIC, voy a abrir un hilo
Pero... en el lado del servidor de BBDD abro un proceso... que tardará un raito en abrirse (300ms)

Si cada vez que la aplicación necesita hacer una query ocurre eso... estoy metiendo una sobrecarga de cojones a la BBDD...
Y una demora de huevos a la aplicación.

SOLUCION: Tener conexiones a la BBDD precreadas: Connection Pool

El connection pool es un conjunto dinñamico de conexiones precreadas a la BBDD.
En un momento tendré 5... si hay más carga de trabajo tendré 25... las que vaya necesitando.
Le defino un tamaño mínimo... un máximo... y cómo ha de ir incrementándose o decrementandose.

Eso es algo que me surge en una única app... o que me pasará en todas las apps? TODAS... por eso esta funcionalidad queda fuera de las apps... e integrada en el App server (weblogic)

Además de otra cosita.... El que abra conexión con la BBDD lo primero que necesita es:
- URL de conexión a la BBDD
- usuario
- contraseña

Y le voy a dar yo esos datos de mi empresa del entorno de producción a un pringao que esta desarrollando la app? NI DE COÑA !
La app no sabe a qué BBDD se está conectando... ni que usuario usa.. y menos su contraseña.

Esos datos los configuro en el Weblogic de turno (el sys admin del entorno)... y pongo un ID PUBLICO A esa BBDD en weblogic.
Al desarrollador solo le doy ese ID PUBLICO. Cuando va a ejecutar una query, el desarrollador usa ese nombre ID publico para perdirle al WL una conexión a esa BBDD ... dame una conexión a la BBDD PRODUCCION. Y el WL se la entrega ya abierta (el WL es el que crea la conexión...y el que por tanto necesita la contraseña, el usuario y la url).

Ese ID PUBLICO ES LO QUE LLAMOS EL nombre jndi, según se define en el estandar JEE.

---

Arranco el Weblogic de turno... a nivel de SO eso da lugar a un PROCESO. Ese proceso tendrá al menos un HILO.

Cuando lleguen peticiones por http a un puerto, el SO las reenvía al PROCESO que haya solicitado el control del puerto.
Todas las peticiones que vaya recibiendo las atenderá un solo hilo o varios hilos en el weblogic de turno?
- Si fuese 1 solo... eso significaría que las peticiones las voy atendiendo una a una... hasta que no acabe una no puedo atender otra... SOLO TENGO UN TIO(hilo) atendiendo peticiones... no tiene sentido.
- Varios hilos

En el WebLogic vamos a tener un monton de hilos atendiendo peticiones: Executor Pool: POOL DE EJECUTORES.
En realidad es más complejo:

Existe un hilo que recibe TODAS LAS PETICIONES... su trabajo es añadirlas a una COLA DE EJECUCIONES.
Y lo que tenemos es un pool de ejecutores (hilos) que va leyendo peticiones de esa cola de peticiones.

Pregunta... si tengo pocos hilos configurados en el pool de ejecuciones, entonces? Se van quedando las peticiones más tiempo en la cola... y yo despacho menos peticiones por unidad de tiempo.
En un momento el servidor puede no admitir más peticiones en la cola... lleno la cola... y empieza a no responder a los clientes.

A mi me interesa tener muchos hilos ejecutores... pero... cada hilo ejecutor no me sale gratis...
Cuando un hilo recibe una petición, para atenderla necesita: RAM y CPU
- CPU para ejecutar trabajo
- RAM para depositar datos temporales asociados a esa petición concreta

Si abro demasiados... tengo 2 potenciales problemas:
- Colapso CPU... y empiezo a encolar a nivel de SO las peticiones de trabajo a la CPU
  Si los hilos tardan mucho en responder, el WL puede pensar que los hilos se han quedado cuajados* (Hilos Stuck)
- Que me quede sin RAM... Más hilos necesitan más RAM... espacio para poner datos temporales de trabajo: OUT OF MEMORY EXCEPTION

Un tuneo que necesitamos hacer a nuestros WL de turno es cúantos hilos son capaces de abrir con la cantidad de RAM que tengo en máquina y la cantidad de CPU que tengo en máquina... y me puede pasar que esos 2 datos no estén balanceados entre si.
Según RAM podría llegar a abrir 200 hilos, pero. la CPU no da para más de 150 hilos... En este caso: ME SOBRA RAM o me falta CPU
Y es un ratio que me interesará calcular. RAM/CPU + #hilos~RAM/CPU.
Con ese # de hilos, RAM y CPU seré capaz de atender X peticiones por unidad de tiempo.
Y si recibo más de esas peticiones por unidad de tiempo en un momento dado? Tengo un problema... ya que este servidor no va a aser capaz de responder a todas esas peticiones: ESCALO HORIZONTALMENTE: Otro servidor de WL... haciendo la misma mierda que éste.
Y delante de ellos: UN BALANCEADOR DE CARGA... Oracle me da el suyo:OHS (que básicamente es un Apache tuneao), aunque puedo montar el que me de la real gana.

Aquí luego hay otro factor a tener en cuenta: HA

Cluster de WL:              CPU
    Tengo una máquina 1      50%
    Tengo una máquina 2      55%
    
    Voy bien? ESTOY ACOJONADO PERDIDO: Si una máquina sea cae, la otra no es capaz de asumir la carga de trabajo... y tengo una caída en cascaca del cluster.

Y definiré unos márgenes: En ITNow, aún cayéndose 3 máquinas, la que queda debe ser capaz de asumir la carga de trabajo.
En condiciones normales, la CPU/RAM nunca debería sobrepasar el 25%... aunque en el caso de la RAM hay truco (el del almendruco)


---

# Uso de la memoria RAM por parte de las aplciaciones. Para qué la usan?

- Almacenar datos temporales de trabajo (1)
- El código de la aplicación: PERM(metaspace) SUELE SER PEQUEÑO... comparado con el uso global de RAM
- El stack de hilos: MINIMO
- Caches. Las usamos para tener un acceso más rápido a ciertos datos (BBDD)
    El 99% de los OutOfMemory de las apps son bugs de desarrollo con las caches... debido a falta de conocimientos/experiencia del desarrollador.
    Podría ser que tenga configurado un pool de ejecutor demasiado grande para la RAM que tengo.
        Cada hilo tendrá una necesidad de RAM... más hilos más RAM. RARO Que sea el problema... podría ser.
    El que libera RAM en el caso de una app JAVA es: el GARBAGE COLLECTOR: Recolector de basura.
    Y para ello, esos datos que tengo en RAM tiene que ser BASURA: IRRECUPERABLES.
    De lo contrario el GC no los elimina.
    Los datos de trabajo (1), están referenciados por variables que se crean a nivel de una petición HTTP.
    Cuando la petición HTTP ha finalizado (se responde al usuario), todas esas variables son destruidas... y los datos a los que puntaban, marcados para su futura eliminación (por el GC)... no son borrados en ese momento.. solo marcados para eliminación
    Pero los datos que tenemos en cache, la propia cache es una forma de recuperar los datos. La cache guarda sus propias variables internas apuntando a los datos. La gestión de la memoria en las caches, SI ES RESPONSABILIDAD del desarrollador JAVA... y muchos lo ignoran.
    Se suelen utilizar "HashMap" como cache... lo cual es un error gigante... Pero hay la mala costumbre de hacerlo.
    Eso se va llenando pero no se vacíua... y al cabo del tiempo: OUT OF MEMORY.
        En muchas ocasiones, aunque pido a desarrollo que lo investiguen y lo arreglen... pasan de mi culo.
    A veces lo que me toca es de vez en cuando reiniciar el servicio... y libero la CACHE.
    Y en ocasiones esto lo programo todos los domingos... días 31 de mes... y sale más barato que investigar: CHAPUZA... pero BARATO !
- Buffers (al escribir a un fichero... al leer por red) Los Buffers son gestionado habitualmente por el SO
    Si tengo una máquina con 16 Gbs de RAM... y quiero omntar el WL... cuánta RAM le doy al WL? 16Gbs - Memoria SO - (Buffers).
    No pasaré de un 60%
    De dónde saco esta info? Me la da desarrollo? NO... Monitorización!
        Haré una estimación... con algún programita de estos que sirven para simular un huevo de usuarios... JMeter, Loadrunner
        Y la refinaré con Monitorización.

Si le pregunto a desarrollo, cuánta RAM le pongo al sistema? NPI
Pero es verdad, desarrollo no tiene npi de esto. Depende de cómo los usuarios usen el sistema.

> Pregunta: Si tengo un megaservidor de WL donde se está usando real 30 Gbs de RAM por el WL.
Si dedico partir ese WL en 2 servidores más pequeños, cuánta RAM le tengo que poner a cada uno? Sin tener en cuenta HA.
- 15Gbs
Pero la realidad es que si arrancase ese entorno y mido... vería que cada uno necesita unos 20... más o menos...
Por qué? La cache se replica en las máquinas... las 2 necesitan cache.

Necesitaré determinar las necesidades de RAM asociadas a caches.

Tanto Caches como memoria de trabajo en JAVA se almacenan en una zona denominada: HEAP

Y el HEAP se divide en varias zonas: OLD GEN, <> ,YOUNG GEN
    En el OLD se guardan datos que llevan mucho tiempo cargados... y se siguen usando
    Los datos nuevos, se almacenan en el YOUNG... y si son de trabajo, pronto son eliminados... y nunca pasan al OLD
    
    CACHE: OLD
    Datos de trabajo asociados a peticiones: YOUNG

Me tocará medirlo.

Me sirve para analizar el uso de memoria en JAVA hacer un ps o un top a nivel del SO?
NO... por qué? Solo veo el consumo de RAM de la MV de JAVA.

Si en un SO arranco una máquina virtual con VMWare... y le doy 4 Gbs... a nivel de SO veo que ese proceso usa 4Gbs.
Pero los programas que hay dentro pueden estar usando solo 1 Gbs de esos 4... En este caso estaría haciendo el capullo. 

Necesito de herramientas especiales para ver el uso de memoria dentro de la JVM

## Habeis visto un gráfico de memoria de una app JAVA?
    
    RAM
    
    ^
    |
    |
8Gbs|     o    o    o    o    o    o    ^
    |    oo   oo   oo   oo   oo   oo    |   Memoria necesaria de trabajo
    |   ooo  ooo  ooo  ooo  ooo  ooo    |
    |  oooo oooo oooo oooo oooo oooo    v
5Gbs| oooooooooooooooooooooooooooooo
    +------------------------------------------------------------------------------> TIEMPO

Si lo veo así, todo está bien.
Mi sistema necesita al menos, entre código, stack de hilos y cache: 5Gbs... ES LA LINA BASE
Menos de esto no arranca la app... ni puede funcionar.
A partir de ahí cuanta más memoria, más trabajo podré soportar... eso es lo que será medio proporcional con el número de hilos.

Si veo que los picos aparecen con mucha frecuencia (si están muy juntos): Tengo poca memoria para trabajo
Y el GC entra demasiado. El GC sale gratis? NO... requiere CPU... pero no solo eso: BLOQUEA EL ACCESO A RAM -> Provoca demora 
Me interesará subir un poco la RAM.

Si los picos están muy separados en el tiempo: Tengo demasiada RAM para trabajo... podría quitarle y dársela a otra máquina.

El problema más gordo es que la linea base no sea horizontal... y vaya creciendo con el tiempo

    RAM
    
    ^
    |
    |
8Gbs|     o   o  o o o o o
    |    oo  oo oooooooooo
    |   ooo oooooooooooooo
    |  ooooooooooooooooooo
5Gbs| oooooooooooooooooooo
    +------------------------------------------------------------------------------> TIEMPO

Eso qué significaría? Que la cache no deja de crecer!! MEMORY LEAK
Problema de desarrollo... que a veces resolvemos y a veces no.

El GC de repente (no es progresivo) se vuelve loco... básicamente cada dato que se mete en RAM necesitamos liberarlo para dejar hueco al siguiente... me deja el sistema agonizando... Todo se ralentiza al extremo: 30 segundos hasta que una petición acaba.
Se me llevan las colas.
Se me quedan threads como stuck.
Hasta que con el tiempo me da el OutOfMemory

* NOTA: El que un hilo se quede cuajado es algo posible... incluso habitual... en una app:
    - Tengo un hilo esperando a una BBDD ... pero la BBDD está cuajada... el hilo queda permanentemente en espera... ni acaba su trabajo, ni ejecuta nuevos trabajos.
    - Un hilo espera a que otro libere un recurso... pero el otro está esperando a que el uno libere el mismo recurso: DEADLOCK

Si tengo que atender a 600 peticiones por minuto.
Cuántos hilos tengo que abrir? Depende de lo que tarde cada petición.
Si tardan 1 segundo: 10 hilos = 10 peticiones/segundo x 60 segundos = 600 peticiones / minuto
 > Otra cosa es que la RAM me de para configurar ese número de hilos.

Si mis peticiones tardan 2 segundo: 20 hilos= 20 peticiones/2 segundos = 10 peticiones/segundo = 600 peticiones/minuto

Y cuántos hilos para el pool de conexiones a la BBDD? Depende de lo que los hilos estén esperando a la BBDD... lo que tarde en contestar la BBDD.

Si tengo que la conexión a la BBDD tarda 1 segundo.
Cuántas peticiones por segundo tengo que contestar? 10 hilos es suficiente
Necesitaré siempre entre 1 y número de ejecutores... Pero cuánto? NPI... MONITORIZACION !

Hay que calcular el ratio ejecutores/conexiones BBDD

Si abro más conexiones de las que uso? Tengo un problema? YO NO... ninguno... al finl y al cabo, para mi abrir una conexión a BBDD es solo abrir un hilo... que sale prácticamente gratis a nivel de SO.
Eso si... quién tiene un problema? El de BBDD... que me va a llamar con un kalashnikov en mano!
Me van a limitar por allí... Lo suyo es llegar a un acuerdo con BBDD... 

Si abro menos conexiones de las que necesito... de las que el pool de ejecutores requiere para no encolar peticiones?
Empiezo a encolar peticiones del pool de ejecutores... y el sistema tarda más en responder.
Mi objetivo es que esa cola esté siempre vacia, sin abrir más conexiones de las que necesito.
En un momento puntual puede haber una pequeña cola... para eso están las colas... pero puntual.
Si siempre tengo ahí 3 tios esperando... desde luego la app podría ir más rápido... y el problema lo tengo en la conf. BBDD.

---

# Hilos vs Procesos

## Qué es un proceso en un SO?

Un programa en ejecución.
Cuando le pedimos al SO que ejecute un programa, el SO crea un proceso para ejecutarlo... y reserva memoria para ese proceso.
El proceso es una agrupación conceptual a nivel del SO de todo lo que necesito a nivel del SO para controlar la ejecución de un programa.

- Un ID
- Un estado
    - Al acabar tengo un return code:
        - 0: Terminó correctamente
        - !=0: Terminó con error
- Un espacio de memoria asignmado (RAM)
- Hilos
- ...

Al arrancar un programa, el SO pone en RAM todo el código de la aplicación. 

Los procesos son los que ejecutan el código de la aplicación? no
A nivel de SO se abren hilos de ejecución... asociados a ese proceso.
Todo programa (proceso) al menos tiene un hilo de ejecución (el principal).
El hilo es el encargado de ir leyendo el código de la aplciación e irlo mandando al cpu.

Si queremos un programa que haga varias cosas a la vez, necesitamos que ese programa abra varios hilos (le pida varios hilos de ejecución paralela al SO)

El mismo trozo de código en un momento dado puede estar siendo ejecutado en paralelo por varios hilos.

Los hilos de ejecución de un proceso, todos tienen acceso a la Memoria RAM asociada a ese proceso... comparten memoria RAM.

---

1º Montar un WL
2º Le daremos un repaso básico a su configuración
    - Despliegue
    - BBDD
3º Monitorización
    Identificar problemas < - SOLUCION
4º Automatización de trabajos: WLST (scripts python)
5º Instalación más avanzada: HA/ESCALABILIDAD: Cluster WL / BALANCEADOR
        
        Máquina 1   192.168.100.201 <<<<<<<             sticky sessions
            app1*                            BALANCEADOR DE CARGA    192.168.100.200     <<<        PC MENCHU (Paso1>Paso2>Paso3)
                Sesión de usuario (RAM): Paso1 + Paso2
        Máquina 2   192.168.100.202 <<<<<<<
            app1

    En ocasiones me puede hacer falta una cache compartida distribuida.
    Los datos se replican entre la RAM de las máquinas (en todas o en algunas al menos)
    Eso lo necesito hacer con herrameintas externas: REDIS... Oracle me da una alternativa: *Coherence*

Las instalaciones las haremos con contenedores.