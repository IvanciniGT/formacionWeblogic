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
