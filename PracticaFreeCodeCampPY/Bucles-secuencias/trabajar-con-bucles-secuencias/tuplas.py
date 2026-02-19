# Una tupla es un tipo de dato de python que se utiliza para crear una secuencia ordenada de valores
# Pueden contener un conjunto mixto de tipos de datos como este
developer = ('Alice', 34, 'Rust Developer')

# Son similares a las listas, las tuplas son INMUTABLES, los elementos de una tupla NO SE PUEDEN MODIFICAR UNA VEZ CREADA.
# Si intenta actualizar uno de los elementos de la tupla, obtendra un error TypeError
programming_languages = ('Python', 'Java', 'C++', 'Rust')
programming_languages[0] = 'JavaScript'

"""
Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
TypeError: 'tuple' object does not support item assignment
"""

# Para acceder a un elemeto de una tupla, puede utilizar la notacion de corchetes y el numero de indice
developer = ('Alice', 34, 'Rust Developer')
developer[1] # 34

# Otra forma de crear un tupla es usando el tuple() constructor de esta manera
developer = 'Jessica'
tuple(developer) # ('J', 'e', 's', 's', 'i', 'c', 'a')

# Para el tuple() constructor, puedes pasar diferentes iterables como cadenas, listas e incluso otras tuplas
# Para comprobar si un elemento está en una tupla, puedes usar la palabra IN 
programming_languages = ('Python', 'Java', 'C++', 'Rust')

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False

# Tambien se puede descomprimir elementos de una tupla como con las listas
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

# Si queremos eliminar un elemento de una tupla, no es posible porque las tuplas son INMUTABLES

# METODOS COMUNES

# para determinar cuantas veces aparece un elemento en una tupla usaremos COUNT()
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2 devuelve la cantidad de ocurrencias

# para encontrar el indice donde se encuentra un elemento especifico en una tupla usamos el metodo INDEX()
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java') # 1 es la posicion donde se encuentra el elemento

# Otra opción que se puede usar con este index()método es pasar argumentos opcionales de índice de inicio y de fin. 
# A continuación, se muestra un ejemplo de cómo pasar un índice de inicio opcional:
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5 la busqueda comienza desde el indice 3 y devuelve el indice donde se encuentra el elemento

# También puede pasar un índice de parada opcional
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5) # 2 indice donde se encuentra el elemento entre las posicion 2 y 5

# otra funcion comun con tuplas es la SORTED()
# cómo crear una nueva lista de números utilizando la sorted()función:
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]



# la sorted funcion SIEMPRE CREARA UNA NUEVA LISTA CON VALORES ORDENADOS



# si se quiere personalizar el ordenamiento es un iterable, puede usar los argumentos opcionales REVERSE, en este ejemplo se usa el ordenamiento KEY = LEN
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']



# para crear una nueva lista de valores en orden inverso usamos el REVERSE
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']