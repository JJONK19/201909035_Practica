SIMPLEQL V.1.0.0

DESCRIPCIÓN
SimpleQl es una aplicación de consultas que tiene como objetivo principal es permitir al usuario leer y información contenida en cualquier archivo de extensión .JSON. La forma en que funciona es a través de consola, en donde el usuario puede ingresar una serie de instrucciones usando una sintaxis previamente definida. Entre las funciones del programa, se encuentran las de abrir, buscar, contar los registros contenidos en el archivo o crear un atractivo reporte con dichos registros.

MENÚ PRINCIPAL
Al ejecutar la aplicación, lo primero que se puede observar es un menú con el listado de funciones que pueden ejecutarse y un pequeño ejemplo de la sintaxis que estas deben de manejar para que se ejecuten correctamente los comandos. Abajo de esto, aparece un espacio para comenzar a escribir instrucciones. 

****NOTA: Las instrucciones hacen caso omiso a las mayusculas, exceptuando en aquellas donde deba escribrse un atributo o ingresar el valor de algun atributo cualquiera.

1.- CARGAR
Como su nombre lo indica, esta funcion se encarga de leer la informacion del/los archivos .JSON y prepararla para que el programa pueda analizarla. La estructura de esta instruccion consiste en iniciar con la palabra "cargar" y añadir despues la direccion absoluta de los archivos con los que se desee trabajar seguidos de una coma. Cada vez que se ejecute este comando se quitan de la memoria los archivos con los que se estaba trabajando antes, asi que, si desea realizar el analisis de varios archivos, asegurese de agregar todos los archivos en una sola instruccion.

    -CARGAR archivo1, archivo2, archivo3, archivoN

****NOTA: Si una de las direcciones es erronea o el archivo no funciona, obtendra un mensaje de error y tendra que repetir de nuevo la instrucción.

2.- SELECCIONAR
Esta funcion se encarga de buscar registros que cumplan una condicion indicada previamente por el usuario o simplemente mostrar todos los registros que se hayan cargado. En caso de no existir el atributo de la condicion o que no exista ningun registro que cumpla con ella, arrojara un mensaje indicandolo. La estructura de la instruccion inicia con la palabra reservada "seleccionar". Seguido de ella, se añaden con comas el listado de atributos que se quiere mostrar de los registros encontrados y la palabra reservada "donde" que marca el inicio de la condicion de busqueda. Esta se compone del nombre del atributo y el valor que se quiere buscar.

    -SELECCIONAR atributo1, atributo2, atributoN DONDE atributo=valor

Si desea mostrar todos los registros, ingrese un asterisco seguido de la palabra seleccionar.

    -SELECCIONAR *

3.- MAXIMO
Esta funcion permite encontrar el valor más grande en el conjunto de numeros guardados que posea un atributo. La estructura de la instruccion esta dada por la palabra reservada "maximo" y el atributo del archivo con el que se desee trabajar. 

    -MAXIMO EDAD

****NOTA: Esta instruccion solo funciona con atributos que contengan datos numericos de cualquier tipo. De no ser asi, se mostrara un mensaje de error.

4.- MINIMO
Esta funcion permite encontrar el valor más pequeño en el conjunto de numeros guardados que posea un atributo. La estructura de la instruccion esta dada por la palabra reservada "minimo" y el atributo del archivo con el que se desee trabajar. 

    -MINIMO EDAD

****NOTA: Esta instruccion solo funciona con atributos que contengan datos numericos de cualquier tipo. De no ser asi, se mostrara un mensaje de error.

5.- SUMA
Esta funcion permite encontrar la suma de un conjunto de numeros guardados que posea un atributo. La estructura de la instruccion esta dada por la palabra reservada "suma" y el atributo del archivo con el que se desee trabajar. 

    -SUMA edad

****NOTA: Esta instruccion solo funciona con atributos que contengan datos numericos de cualquier tipo. De no ser asi, se mostrara un mensaje de error.

6.- CUENTA
Esta funcion muestra el total de registros que se hayan cargado a la memoria entre todos los archivos JSON. Como consejo, si se desea saber cuando tiene un archivo en concreto, cargue solo ese documento. La estructura de esta instruccion esta dada por la palabra reservada "cuenta" sin ningun otra palabra. 

    -CUENTA

7.- REPORTAR
Esta funcion crear un reporte en un html agregando el numero de registros que este quiere ver. Si no sabe cuantos registros tiene en total y quiere agregar todos, añada un numero arbritariamente grande. La estructura de esta instruccion esta dada  por la palabra reservada "reportar" seguido del numero de datos que quiere mostrar. De ingresar alguna letra, se mostrara un mensaje de error.

    -REPORTAR 52

****NOTA: El archivo del registro se encuentra en la carpeta del programa.

TERMINAR LA EJECUCION
Si desea finalizar, ingrese la palabra "salida". 




