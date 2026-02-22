"""una bibilioteca es como una caja de herramientas para los desarrolladores
en iugar de tener que implementar cada parte del codigo usted mismo desde cero, una biblioteca proporciona codigo preescrito
y reutibilizable, como funciones,clases y estructuras de datos que se puede usar en proyectos
python cuenta con una extensa biblioteca estandar con numerosos modulos integrados.
Todos ellos son solluciones estandarizadas y probadas para muchos de los problemas y tareas que enfrentaras a diario como programador

Algunos de los ejemplos de modulos integrados populares son MATH, RANDOM, RE y DATETIME

El math modilo tiene funciones utiles para realizar operaciones matematicas mas complejas

El random modulo se utiliza para generar numeros aleatorios

El re modulo se utiliza para trabajar con expresiones regulares

El datetime modlo es util para trabajar con fechas y horas en Python

Para accedera las variables, constantes, funciones y clases definidas se usa una sentencia de importacion
Estas sentencias permiten importar modulos a un script de python.
Se utiliza la IMPORT sentencia seguida del nombre del modulo

import module_name

Luego si se necesita llamar a un metodo desde ese modulo en su script de python, utilizaria la notacion de punto, con el nombre del modulo seguido del nombre del metodo

module_name.method_name()
ejemplo
"""
import math
# para obtener la raiz cuadrada de 36
math.sqrt(36)

"""Si se necesita importar el modulo con un nombre diferente se usa la sintaxis as seguido del alias al final de la delcaracion de importacion"""
# import module_name as module_alias
import math as m

"""cuando no se necesite importar todo el modulo solamente una o dos funciones cambia la declaracion
y comienza con la FROM seguido del nombre del modulo y luego la importacion
"""

from math import radians, sin, cos


"""Ejemplo de una clase del datetime
Se crea un objeto de fecha que representa 15 de julio de 1959
"""
import datetime
fc = datetime.date(1959,7,15)
print(fc.day)
print(fc.month)
print(fc.year)


"""
__name__ es una variable incorporada especial en python

Cuando se ejecuta un archivo python directamente, python establece el valor de esta variable en la cadena "__main__"
if __name__ == "__main__"

Si el archivo Python se importa como un modulo en otro script de python, el valor de la __name__ variable se establece en el nombre de ese modulo(generalmente el nombre del archivo sin la .py extension)


"""