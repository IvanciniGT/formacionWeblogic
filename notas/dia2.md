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