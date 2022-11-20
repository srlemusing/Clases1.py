"""
buenos dias, mi nombre es Jhonatan Lemus. 
# Este es mi comienzo en el aprendizaje de python bajo visual studio code
# Fecha: 28/OCT/2022
# Hra: 10:09AM
"""
#Creamos el archivo en el servidor asi: file > new file > nombre.py 

from operator import truediv

#Mostrar mensajes en pantalla clasico
print("Hola mundo")

#Mostrar mensajes en pantalla largo
nn="hola mundo"
print(nn)

#Declarando variables
nombre="nom" #sencillo
myNombre="diego" #caso de carmel
MyNombre="jhona" #Caso Pascual
my_nombre="lemus" #Caso serpiente
ej1, ej2, ej3 = "amarillo", "azul", "rojo"

#Numeros de Python:int, float, complex
ag=1 #int
ad=2.5 #float
af=1j #complex

#Variables sencillo (suma comun)
a0=2
b0=1
c0=int(a0+b0)
print(c0)

#Variables tipo int (suma enteros, no tienen fraccion ni decimales)
a=22
b=12
c=int(a+b)
print(int(c))

#Variables tipo str(se expresan como cadenas de textos y numeros)
d=str(22)
e=str(12)
f=str(d+e)
print(str(f))

#Variables flotantes (tienen decimales o fracciones)
g=float(2.0)
h=float(1.0)
i= float(g+h)
print(float(i))

#Variables boleanas (Verdadero o falso)
positivo= True
Falso = False

#Generar numero aleatorio con el modulo random

from cgi import print_directory
import random
print(random.randrange(1,20))

#Guardar y Expresar caracter y numeros
Edad="ed"
print("Ghael, ¿Cuál es su edad?")

#Saber cuantas letras tiene una cadena de texto
dr="hola mundosss"
print(len(dr))

#Comprobar si una palabra está en un parrafo
txt="esta es una corta prueba de palabras"
if "hoy" in txt:
    print("Si esta la palabra")
else:
    print("no esta la palabra")

#Metodo que devuelva una cadena en mayuscula
print(dr.upper())

#Eliminar espacios en blanco
print(dr.strip())

"""
#Listas: Son ordenadas y sus elementos se mantiene en el orden en que se crean
# Las listas pueden ser mutables, es decir, se pueden modificar sus elemento.
"""
#crear y mostrar lista
lista1 =["lis1", "lis2", "lis3"]
print(lista1)

#Lista con variable flotante, boleana, texto y elemento repetido
lista2 =[1, 2.0, True, "lis4", 1]
print(lista2)

#Indices: Se refiere a la posición de un elemento en dentro de una lista
#El primer elemento siempre tiene la posición cero

#Obtener el primer elemento de la lista
print(lista2[0])

#Obtener la longitud o tamaño de la lista
len(lista1)
print(len(lista1))

#La ultima posicion de la lista: Es = a la longitud -1
#Ejemplo: Si la longitud es 4, la ultima posicion es 3
print(lista2[3])

#Mostrar elemento por rango, ejemplo: al indicar el rango [0:2] 
# nos mostrará los elementos en la posicion cero y uno de la lista.
print(lista2[0:2])

#Una lista puede contener elementos que ya tienen una lista, aninada se llama
Lista3=[lista1, lista2, "eje1", 22]
print(Lista3)
#obtener la longitud de la lista que está dentro de la lista
print(len(Lista3[0]))
#Acceder al primer elemento de la sublista dentro de la lista
print(Lista3[0][0])

#Modificacion de elementos de la lista o reemplazarlos: Aqui solo
#expresa el nombre de la lista, indicando la posisicon del elemento
# y definimos su nuevo nombre de elemento
Lista3[2]= "cambios"
print(Lista3)

#Funcion append: permite agregar elemento a la ultima posicion de la lista
Lista3.append("nuevoelemento")
print(Lista3)

#Funcion extend: permite unos dos listas como una sola
lista1.extend(lista2)
print(lista1)

#Tuplas: estructuras de datos que permiten almancer elementos, similar a la listas
# Las tuplas no son mutables, es decir, no dejen modificar sus elementos
tupla1 = ("pru1", 27, 2.1)
print(tupla1)

#Obtener la longitud de la tupla
len(tupla1)
print(len(tupla1))

#Obtener una posicion de la tupla
tupla1[1]
print(tupla1[1])

#Diccionarios: Son tipos de estructuras de datos que permiten almacenar informacion
#en pares de datos llamados llave y valor, cada valor es un elemento que corresponde a una llave

diccio = {
    "nomb": "diego",
    "apell": "lemus"
}
print(diccio)

#Conocer el valor de una llave
print(diccio["nomb"])

#Agregar nuevo elemento al diccionario
diccio["cel"]=310374
print(diccio)

#Agregar elemento que es una lista al diccionario
diccio["direc"]=["call", "cra", "esquina"]
print(diccio)

#Funcion: keys, items y values: 

#items: nos da la lista de tuplas con su respectiva llave y valor
diccio.items()
print(diccio.items())

#Keys: nos da las llaves del diccionario
diccio.keys()
print(diccio.keys())

#Values: nos da los valores de las llaves del diccionario
diccio.values()
print(diccio.values())

#Set: Estructuras de datos que permiten guardar elementos unicos, no son ordendas
# no se pueden acceder a sus indices. Pueden tener elementos de distintos tipos.
# Si se le regsitran dos datos iguales, solo guarda uno, el otro lo omite.
#Permite agregar elememtos, pero no modificar sus elementos (no mutables)
set1 = {"exito", 45, 2.11, "false"}
print(set1)

#Agregar elemento al set
set1.add("agregado")
print(set1)

#Eliminar elemento del set
set1.discard("agregado")
print(set1)

#Conocer longitud del set
len(set1)
print(len(set1))

"""
#Condiciones y ciclos: Sentencias condicionales, intrucciones que se ejecutan
# o no al cumplirse una condicion, las condiciones dependen de una condicion
# logica o de comparacion.
# igual== , diferente !=, menor < , mayor > , >= , <=
# is = valida si dos variables se refieren al misma objeto, es decir, si es el mismo
# retorna true sino, false.
# and = une dos o mas condiciones, si todas las condiciones se cumplen retorna true
# sino, false.
# or = une dos o mas condiciones, si alguna de las condiciones se cumple, retorna true
# si todas son false, retorna false.
# not = retorna true si el valor evaluado no es verdadero
"""
#Estructura de if:
"""
if<condicion logica>: #instrucciones que se ejecutan si se cumple la condicion
    print("if opcion1")
elif <condicion logica>: (indica sino, intrucciones que se ejeuctan si incumple una condiciones diferente a la opcion1)
    print("elif opcion2")
else:
    print("else opcion3") (Intrucciones que se ejecutan si nignuna de las opciones anteriores se cumple)
"""
#Ejemplos 
a = 2
b = 2

#Evaluando enteros o caracteres
if a > b:
    print("A es mayor que B")
elif b > a:
    print("B es mayor que A")
else:
    print("A y B son iguales")

#Evaluando booleanas
c = True
if c:
    print("Es verdadero")
else:
    print("Es falso")

#Evaluando tipos de datos
d = False

if type(d) is bool:
    print("D es de tipo booleano")
else:
    print("Debe ser otro tipo de dato")

#Evaluando AND y OR
e = 2
f = 5
g = 1

if e > f and f > g:
    print("Se cumple, ambas opciones son verdaderas")
elif e < f and f < g:
    print("E es menor que F y G mayor que F")
else:
    print("alguna condicion no se cumple")

#Ciclos FOR Y WHILE
"""
Ciclos: Instrucciones que se repiten hasta que se cumple una condicion.

Ciclo for, tiene la soguiente estructura:

for <element> in <objet>:
    print("element:" <element>)

ciclo While, tiene la siguiente estructura:

While <condicion>:
    prinr("ciclo while")
"""
#Ejemplo FOR

# j queda siendo igual a prueba, entonces en este caso nos muestra cada
# letra de la palabra "prueba"
for j in "prueba":
    print(j)

#Creamos una lista y aplicamos for

lista4 = ["java", "visual", "Flutter"]
for elementos in lista4:
    print(elementos)
    if elementos == "visual": #Indica que cuando el ciclo llegue hasta este elemento se termine
         break #Hace referencia a pausar ciclo automaticamente

#Utilizando FOR en rangos: Me muestra los numeros segun indiquemos
# range(8): me mostraria los numero del 0 al 7
# range(1, 8): me mostraria los numeros del 1 al 7
#for num in range(8):
    #print(num)

#Ejemplo  WHILE

t = 1
while t <= 5:
    print(t)
    t = t+1
    

  
