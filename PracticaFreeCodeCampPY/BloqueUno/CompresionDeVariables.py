# Python es un lenguaje de tipado dinamico, como JS, lo que significa que 
# no es necesario declarar explicitamente los tipos de variables. El
# lenguaje reconoce el tipo de dato de una variable seun lo que se le asigne
    

name = 'John Doe'
age = 25

# Dadp qie pyrhon determina los tipos de datos mientras el programa se
# ejecuta, los errores de tipo solo se detectan en ese momento.
# Si llega a una linea donde se espera que un objeto se comporte de forma
# incorrecta, python se detendra y mostrara un error.
# Estos son los tipos de datos mas comunes que se usan en python

# entero 
my_integer_var = 10
print('Integer:', my_integer_var)

# flotante
my_float_var = 4.50
print('Float:', my_float_var)

# cadena
my_string_var = 'hello'
print('String:', my_string_var)

# boolean
my_boolean_var = true
print('Boolean', my_boolean_var)

# conjunto : coleccion desordenada de elementos unicos
my_set_var = {5,6,8}
print('Set', my_set_var)

# diccionario : coleccion de pares clave-valor encerrados entre llaves
my_dictionary_var = {'name' : 'alice', 'agre' : 24}
print('Dictionary', my_dictionary_var)

# tupla : coleccion ordenada inmutable, encerrada entre parentesis
my_tuple_var = (7, 5, 8)
print('Tuple:', my_tuple_var)

# rango : secuencia de numeros, utilizada en bucles
my_range_var = range(5)
print('Range:', my_range_var)

# lista : coleccion ordenada de elementos que admite diferentes tipos de datos
my_list = [22, 'Hello world', 3.14, True]
print(my_list)

# Para obtener el tipo de datos de una variable, 
# puede utilizar la type()función:
my_var_1 = 'Hello world'
my_var_2 = 21
print(type(my_var_1)) 
print(type (my_var_2))

#La función integrada isinstance()permite comprobar si una variable
# coincide con un tipo de dato específico. 
# Toma un objeto y el tipo con el que se desea compararlo, y devuelve 
# un valor booleano. Aquí hay algunos ejemplos:

isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False