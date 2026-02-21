# funciones Enumerate y zip
# si quisieramos controlar el indice de cada elemento podemos usar la funcion ENUMERATE()
# funcion que registra el indice de un iterable y devuelve un objeto enumerado

languages = ['Spanish', 'English', 'Russian', 'Chinese']

list(enumerate(languages))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]

# cambiando el ejemplo anterior para que se vea mejor
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')
# este codigo imprimira por separado el index y el elemento, separamos el valor de CADA TUPLA
# Index 0 and language Spanish
# Index 1 and language English
# Index 2 and language Russian
# Index 3 and language Chinese



# la funcion tambien acepta un start argumento opcional que especifica el valor inicial del recuento.
# si no esta el argumento comienza desde 0

# por ahora solo iteramos sobre una lista. 
# si quisieramos iterar sobre varios iterables se puede usar la ZIP()
# funcion que combina listas en pares de elementos y devuelve un iterador de tuplas

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

list(zip(developers, ids))
# [('Naomi', 1), ('Dario', 2), ('Jessica', 3), ('Tom', 4)]
# en este ejemplo devuelve una lista con la list() funcion.


developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {id}')
# este bucle descomprime cada tupla en name y id devolviendo un iterador de tuplas.

