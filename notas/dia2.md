# Instalación de weblogic

Lo vamos a hacer mediante un contenedor.

Los contenedores son una forma de poner un software a funcionar dentro de un SO que ruede un kernel Linux.
Realmente se han convertido en LA FORMA. No queremos otra.
Porque no tiene sentido otra.

Un contenedor es un entorno aislado dentro de un SO Linux, donde correr procesos.
Entorno aislado??
- Tienen su propia conf. de red... y por ende su propia IP (en una red virtual creada por el gestor de contenedores)
- Tiene su propio FileSystem, independiente del host
- Tienen sus propias variables de entorno
- Pueden tener limitaciones de acceso al hierro

Instalar software a pelo (sobre el hierro) es problemático:
- Dependencias/Librerías que pueda necesitar una app... también tengo que montarlas... y puede haber incompatibilidades entre apps.
- Si un proceso se vuelve loco (CPU 100%) ese proceso queda OFFLINE... pero ni ese ni los otros que tenga en la máquina. <<<< JODIDO !
  Para evitar esto, hemos usado durante décadas Máquinas virtuales.
- Instalar software es complejo

---

     Weblogic  |  MariaDB
    -----------------------
        C1     |    C2    
    ----------------------
    Gestor de contenedores
    ----------------------
            SO LINUX
    ----------------------
             HIERRO
             
             
     Weblogic  |  MariaDB
    -----------------------
        SO1    |   SO2    
    -----------------------
        MV1    |   MV2    
    ----------------------
           Hipervisor
    ----------------------
            SO LINUX
    ----------------------
             HIERRO             

---  

Quiero instalar Weblogic:
1. JDK
2. Descargar el instalador de WL
3. Ejecutar el instalador
        - Configurar toda la mierda  
4. Arrancar el WL (comando de arranque?)
5. Saber operarlo:
    - los comandos para detenerlo, reiniciarlo, 
    - actualizarlo
    - ver los log

Cuando trabajo con contenedores, todo eso no ocurre.
Lo primero es que con contenedores no instalo -> despliego
Me voy a descargar una IMAGEN DE CONTENEDOR, que traerá un programa YA INSTALADO y PRECONFIGURADO por alguien (FABRICANTE)... y con las dependencias.
Y además, todo software que está dentro de un contenedor se opera de la misma forma... está estandarizado.

En entornos de prueba, desarrollo... usamos gestores de contenedores para trabajar con contenedores: DOCKER, PODMAN, CONTAINERD, CRIO
En entornos de producción necesito más!
Esos de gestores de contenedores gestionan los contenedores de 1 máquina... pero en un entorno de producción : HA/Escalabilidad necesito trabajar en cluster.
En cada máquina monto uno de esos gestores de contenedores... Y luego monto un programita llamado Kubernetes que se encarga de operarlos automáticamente.

Las imágenes de contenedor las sacamos de un registry de repositorios de imágenes de contenedor:
- Docker hub
- Redhat: quay.io
- Microsoft
- Oracle

---

Sistema de archivos de un contenedor:

/   
    bin/
        ls
        mv
        cp
        bash
        ... y muchos
    etc/
    var/
        lib/
            docker/
                    container/
                                mymariadb/
                                        etc/
                                            mariadb/
                                                    mariadb.conf
                                        var/
                                            mariadb/
                                                tablas
                    images/
                                mymariadb/              <<<< Se le hace creer a los procesos que este es el root del FS: chroot
                                                    <<<< Esta carpeta es INALTERABLE
                                        bin/
                                            ls
                                            mv
                                            cp
                                            bash
                                            ... y pocos
                                        etc/
                                            mariadb/
                                                    mariadb.conf
                                        var/
                                            mariadb/
                                        root/
                                        home/
                                        tmp/
                                        opt/
                                            mariadb/
                                                mariadb
    root/
    home/
    tmp/
    opt/
    
-----


    ---------red de amazon ----------- internet----- mi maquina
    |
    host 3.254.197.193:8888 -> 172.17.0.2:80
        ----------- red de docker
        
---
Los datos del dominio al final se guardan en un fichero...
Pero ese fichero se replica en todos los servidores que pertenecen a ese dominio.
Como toque el fichero en uno y no en los otros, la lio parda.

NO LO TOCAMOS "NUNCA".
Podría ser que monte un servidor, configure su archivo de dominio... y luego lo copie a otras servidores > TEMPLATE 

Los cambios en ese fichero los hacemos:
- Consola Web (NO NOS GUSTA)
- Script jython ejecutable desde la WLST (LO ADORAMOS)
---
Arquitectura de Weblogic:

Tendremos máquinas. Esas máquinas, con WL instalado, podrán ejecutar instancias de Weblogic.
Cada instancia de Weblogic, se ejecutará dentro de su propia JVM.
En esas instancias podré ejecutar aplicaciones.

Tenemos una instancia, desplegada en una máquina donde desplegaremos la aplicación de administración de weblogic (consola de administración).

Desde esa consola voy a poder :
- Arrancar, parar, reiniciar instancias de Weblogic.
  Arrancar una instancia de weblogic implica arrancar una JVM.

  Maquina 1
    Instancia 1
        Console         JVM (proceso que corre dentro de la máquina 1)
    Instancia 2
        app1            JVM (otro proceso que corre dentro de la máquina 1)

  Máquina 2
    Node Manager        Su propia JVM
                        Es un demonio que necesito configurar con arranque automático en cada host
    Instancia 1
        app2            JVM (proceso que corre dentro de la máquina 2)
    Instancia 2
        app1            JVM (proceso que corre dentro de la máquina 2)
    
  Máquina 3
    Node Manager        Su propia JVM
    Instancia 1
        app1            JVM (proceso que corre dentro de la máquina 2)
    Instancia 2
        app2            JVM (proceso que corre dentro de la máquina 2)
    Instancia 3
        app3            JVM (proceso que corre dentro de la máquina 2)
    Instancia 4
        app4            JVM (proceso que corre dentro de la máquina 2)
        app5            JVM (proceso que corre dentro de la máquina 2)
    
    Desde la consola podría parar la app2? Si.. ya que hay un proceso en la JVM app2, que está en continua comunicación con la administración. Y la consola de administración, tiene la capacidad de enviar comandos a ese proceso para que se detenga.
    Desde la consola podría iniciar la app2? a priori no!
    Cómo abro yo un proceso en otra máquina?
    Gracias al node manager, la consola de administración podrá iniciar procesos JVM (instancias) en otras máquinas... tiene allí un infiltrado... que le hará el trabajo.
---

# Configuración de memoria en la JVM

- Xms1000m      Memoria (HEAP: Cache + datos trabajo = OLD + YOUNG) inicial con la que arranca la JVM
- Xmx2000m      Memoria máxima que puede llegar a usarse.

Cómo configuramos esos valores? Que sean iguales, para evitar que la JVM necesite en un momento más memoria y no esté disponible a nivel de SO y me dé un OUT OF MEMORY.
Si considero que voy a llegar a usar 4gbs, reservo los 4gbs de partida... para que no me los quite nadie.

Solo cambiaría este criterio si:
- Estoy en un caso muy especial
- Y conoczco muy bien los patrones de comportamiento de los sistemas


Statement
UPDATE usuarios SET nombre='Federico', apellidos='Ruiz' WHERE id=17;
1. Lo primero que ocurre en la BBDD es que se valida el SQL
2. Se valida que existan las tablas... y las columnas dentro de esa tablas
3. Se valida que los tipos de datos que suministro sean los que tienen las columnas asignados
4. Se prepara el plan de ejecución de la query.
   La BBDD piensa la mejor estrategia para ejecutar esta query.
5. Ejecuta la query

PreparedStatement = QUERY EDICION USUARIO
UPDATE usuarios SET nombre=?, apellidos=? WHERE id=?; (texto, texto, numero)
1. Lo primero que ocurre en la BBDD es que se valida el SQL
2. Se valida que existan las tablas... y las columnas dentro de esa tablas
3. Se valida que los tipos de datos que suministro sean los que tienen las columnas asignados
4. Se prepara el plan de ejecución de la query.
   La BBDD piensa la mejor estrategia para ejecutar esta query.

Y ya queda almacenado
EJECUTA QUERY EDICION USUARIO (menchu, garcía, 17)
5. Ejecuta la query
EJECUTA QUERY EDICION USUARIO (felipe, mateo, 2347)
5. Ejecuta la query
