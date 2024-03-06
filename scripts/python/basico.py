# Comentarios con el cuadradito

# Tipos de datos
# Numeros
3               # Colocaría un dato de tipo número en RAM
3.4             # Pero al ser irrecuperable... pasa de ello

# Valores lógicos
True            # Coloca un dato de tipo Lógico en RAM
False

# Textos
'Texto'         # Coloca un dato de tipo Texto en RAM
"Texto"

"""
Hola,
Yo soy un texto de varias lineas
"""

'''
Yo también
soy un texto
que ocupa varias lienas
'''

# Como truco rastrero y sucio en python, usamos el operador """ para "escribir comentarios en bloque"""

numero = 33
numero = "texto"
numero = True

# Tipos de datos de coleccion: 

## Tupla: Secuencia ordenada e inalterable de datos
mi_tupla = (1,"texto", True, 3, "Chao pescao", False)
print( mi_tupla )
print( mi_tupla[1] )
print( mi_tupla[1:4] )
print( mi_tupla[-2] )
print( mi_tupla[-3:-1] )
print( mi_tupla[-3:] )
print( mi_tupla[:3] )
print( len(mi_tupla) )

## Textos: Los texto realmente son tuplas de caracteres
mi_texto ="En un lugar de la mancha de cuyo nombre...."
print( len(mi_texto) )
print( mi_texto[5] )
print( mi_texto[5:10] )
print( mi_texto[:15] )
print( mi_texto[5:] )
print( mi_texto[-5:] )

## Listas: Como una lista, pero alterable
mi_lista = [1,"texto", True, 3, "Chao pescao", False]
print( mi_lista )
print( mi_lista[1] )
print( mi_lista[1:4] )
print( mi_lista[-2] )
print( mi_lista[-3:-1] )
print( mi_lista[-3:] )
print( mi_lista[:3] )
print( len(mi_lista) )

print( mi_lista )
mi_lista[1] = "Otro texto"
print( mi_lista )

#mi_tupla[1] = "Otro texto"
mi_lista.append(33)
mi_lista.insert(4, "Qué tal")
del mi_lista[1]
mi_lista.remove("Chao pescao")
print( mi_lista )

## Diccionarios: Como una lista, pero los elementos se identifican no por su posición
# sino por una clave
mi_diccionario = {"primero": 1,"segundo": "texto", "tercero": True}

print( mi_diccionario )
print( mi_diccionario["segundo"] )


mi_lista_como_diccionario = {0: 1,1: "texto", 2: True}
print( mi_lista_como_diccionario )
print( mi_lista_como_diccionario[1] )

# Operadores
## Números:
print( 3+4-2*5/8 )

## Textos
print( "texto" + "otro texto" )
print( "texto" * 10 )
print( "-" * 80 )

## Lógicos
print( not (True and False or True) )

## Relacionales
print( 3 == 4 )
print( 3 >  4 )
print( 3 <  4 )
print( 3 >= 4 )
print( 3 <= 4 )
print( 3 != 4 )

## Control de flujo (IF, FOR, WHILE)

### Condicionales
#if <CONDICION>:
    # Lo que quiero que se haga si se cumple CONDICION
#elif <CONDICION2:
    # Lo que quiero que se haga si se no cumple CONDICION pero si CONDICION2
#else:
    # Lo que quiero que se haga si se no cumple ni CONDICION ni CONDICION2

if len(mi_tupla) > 3 :
    print( "Tengo más de 3 cositas" )
    print( "Soy rico !!!!!" )
else:
    print( "No tengo más de 3 cositas" )

print( "Yo me ejecuto siempre" )

# WHILE: Como el if... pero mientras se cumple la condicion, se sigue ejecutando lo de dentro
numero = 3
while numero > 0:
    print( "el numero vale: " + str(numero) )
    #numero = numero - 1
    numero -= 1 # Tenemos los operadores: -= += *= /=

# FOR: Permiten hacer una operación sobre cada elemento de una coleccion
# for cada_elemento in COLECCION:
#    Lo que quiera hacer con cada_elemento
numeros = (1,2,3,4)

for numero in numeros:
    print( numero )

for cosa in mi_tupla:
    print( cosa )

for cosa in mi_lista:
    print( cosa )

for cosa in mi_diccionario:
    print( cosa )
    print( mi_diccionario[cosa] )

for numero in range(1,1000,10):
    print( numero )
    
for numero in range(1000,1,-10):
    print( numero )

## Funciones: Trozos de código reutilizables.
# Python trae muchas funciones: range, srt, print, len
# Yo puedo crear las mias

def saluda(nombre):
    print( "Hola "+ nombre)
    
saluda("Felipe")
saluda("Menchu")

def super_saluda(nombre, formal=True, tratamiento="Don"):
    if formal:
        print( "Buenos días " + tratamiento + " " + nombre)
    else:
        print( "¿Qué hay " + nombre + "?")

super_saluda("Felipe", True)
super_saluda("Menchu", False)
super_saluda("Federico")
super_saluda("Ortíz", True, "Sr.")
super_saluda("Catalina", tratamiento="Srta.")


nombre = input("Dame su nombre: ")
super_saluda(nombre, True)

## En según qué versión de python, en lugar de input, usamos raw_input
# Input puede ser que evalue el texto introducido por consola, como si fuera código python
# INPUT:        3+3     ---->       6
# RAW_INPUT:    3+3     ---->       3+3

#capturado = raw_input("Dame argo!!!! ")
#print( capturado )