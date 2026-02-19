# El tipo de dato lista es una secuencia ordenada de elementos qu epuede estar compuesta por cadenas
# numero o incluso otras listas. SON MUTABLES y utilizan indexacion basada en cero,
# lo que significa que ele primer elemento de la lista se encuentra en el indice cero

cities = ['Los Angeles', 'London', 'Tokyo']

# para accerder a un elemento de la cities lista, puede referenciar su numero de indice en la secuencia.
# a continuacion, se muestra un ejemplo de acceso al primer elemento

cities = ['Los Angeles', 'London', 'Tokyo']
cities[0] # 'Los Angeles'

# la indexacion negativa se utiliza para acceder a los elementos desde el final de la lista en lugar
# desde el principio en el indice 0. Para acceder al ultimo elemento de cualquier lista
# se puede usar -1:

cities = ['Los Angeles', 'London', 'Tokyo']
cities[-1] # 'Tokyo'

# otra forma de crear una lista es usar el LIST() constructor.
# el list() se usa para convertir un iterable en una lista como esta :

developer = 'Jessica'
list(developer) # ['J', 'e', 's', 's', 'i', 'c', 'a']

# Un iterable es un tipo especial de objeto que permite recorrer un elemento a la vez.
# Para obtener el numero total de elementos en una lista, puedes usar la LEN() funcion

numbers = [1, 2, 3, 4, 5]
len(numbers) # 5

# Dado que las listas son MUTABLES , puede actualizar cualquier elemento de la lista siempre que pase un numero de indice valido

# si desesa eliminar un elemento de una lista se usa la funcion DEL()
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']


# A veces resulta util comprobar si un elemento esta dentro de la lista. Para ello se usa la palabra IN

programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False

# A veces es comun tener listas anidadas dentro de otras listas como esta:
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]

# tenemos una lista anidada que conteiene tres lenguajes de programacion populares.
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2] # ['Python', 'Rust', 'C++']

# Para acceder al segundo idioma desde la lista anidada, debera acceder a el usando el indice 1
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][1] # 'Rust'

# descomprimir valores de una lista es una tecnica que se utiliza para asignar valores de una lista a nuevas variables.
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

# METODOS COMUNES

#Append metodo, que se usa para agregar un elemento al final de la lista.
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]

# la lista completa de even_numbers quedo anidada dentro de la otra lista
# si quisiera agregar todos los numeros individuales de la eve_number lista AL FINAL DE LA NUMBERS se usa el extend
# El extend() es similar al append(), solo que permite agregar varios elementos de una lista a otra.

numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]

# para insertar un elemento en un indice especifico es una lista se usa el INSERT(), se necesitan dos argumentos, el indice y el nuevo elemento

numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # [1, 2, 2.5, 3, 4, 5]

# para eliminiar un elemento de una lista se usa el remove(), toma como argumento el valor del elemento a eliminar

numbers = [10, 20, 30, 40, 50, 50]
numbers.remove(50)

print(numbers) # [10, 20, 30, 40, 50]
#elimina la primer aparicion

# para eliminar un elemento en un indice especifico se usa el pop()
# si no especifica un elemento para el pop se elimina el ultimo elemento

numbers = [1, 2, 3, 4, 5]
numbers.pop(1) # The number 2 is returned

# para ordenar los elementos se usa el metodo SORT()

numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67]

# a diferencia del SORT() existe el SORTED() que funciona con cualquier iterable
# DEVUELVE UNA NUEVA LISTA ORDENADA en lugar de modificar la lista original

numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(numbers) # [19, 2, 35, 1, 67, 41]
print(sorted_numbers) # [1, 2, 19, 35, 41, 67]

# Un iterable es un tipo especial de objeto sobre el que se puede realizar un bucle
# Tanto el sort() como el sorted() aceptan parametros opcionales KEY/REVERSE

#para invertir una lista de elementos en su lugar usaremos REVERSE()

numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # [1, 2, 3, 4, 5, 6]

# para encontrar el primer indice donde se encuentra un elemento en una lista se usa el metodo INDEX()
# en el ejemplo se encontrara el idioma 'java'

programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1



