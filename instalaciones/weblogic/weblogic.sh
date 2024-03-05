docker pull container-registry.oracle.com/middleware/weblogic:12.2.1.4
docker image pull container-registry.oracle.com/middleware/weblogic:12.2.1.4


docker TIPO_OBJETO verbo <args>
       image       pull push inspect rm list
       container   create rm start stop restart logs inspect   list
       volume      create rm inspect list
       network     create rm inspect list
       
                                ALIAS
docker image list               docker images
docker image pull               docker pull
docker image rm                 docker rmi

docker container list           docker ps
docker container start          docker start

docker run -d -p 7001:7001 -p 9002:9002 \
      -v $PWD:/u01/oracle/properties container-registry.oracle.com/middleware/weblogic:12.2.1.4

Este comando hace muchas cosas:
    docker image pull container-registry.oracle.com/middleware/weblogic:12.2.1.4
    docker container create -p 7001:7001 -p 9002:9002 \
      -v $PWD:/u01/oracle/properties container-registry.oracle.com/middleware/weblogic:12.2.1.4
        >> Al ejecutarse devuelve el ID del nuevo contenedor creado
        
        NI DE COÑA QUEREMOS TRABAJAR CON ESE ID... queremos un nombre reconocible y publico
        Si no le pongo nombre, docker se vuelve creativo y genera un nombre aleatorio
        
    docker start ID
    docker logs ID -f (para ver los logs) y deja la terminal bloqueada. EN NUESTRO CASO el -d evita este comando
    
    
    docker container create \
        --name miwl \
        -p 7001:7001 \
        -p 9002:9002 \
        -v ./domain.properties:/u01/oracle/properties/domain.properties \
        container-registry.oracle.com/middleware/weblogic:12.2.1.4
    
    Puertos:
        9002: Consola de administración
        7001: Apps
        
echo "https://$(curl -S ifconfig.me):9002/console"