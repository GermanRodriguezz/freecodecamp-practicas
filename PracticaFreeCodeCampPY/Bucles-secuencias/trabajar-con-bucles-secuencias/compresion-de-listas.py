# estas funciones acortan el codigo y a menudo lo hace mas legible
even_numbers = []

for num in range(21):
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)
# esta seria la forma convencion de agregar un numero par a una lista

# el siguiente bloque es la manera de hacerlo con compresion de listas
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
# la comprension de listas recorre los numeros de 0-20 e incluye solo aquellos divisibles
# por 2, otro ejemplo para entender mejor como funciona la comprension de listas

numbers = [1, 2, 3, 4, 5]
result = [(num, 'Even') if num % 2 == 0 else (num, 'Odd') for num in numbers]
print(result)

# hay una lista de numeros NUMBERS, y queremos crear una lista de tuplas que indiquen cuales
# son pares o impares.
# se usa el if para comprobar si el nuemro es divisible por 2. De ser asi el resultado es una tupla
# con ese numero seguido de la palabra 'Even' sino el resultado es una tupla con el numero seguido de 'Odd'


# OTRA FORMA DE CREAR UNA LISTA ES APARTIR DE UN ITERABLE FILTER()
# Se usa para seleccionar elementos de un iterable que cumplen una condicion especifica.
# Acepta una funcion y in iterable como argumentos.
# en el ejemplo siguiente pasamos una funcion a la filter() para comprobar si el numero de la palabras
# actual es mayor que 4. Todas las palabras con un numero de caracteres mayor a 4 se añaden a una nueva lista
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']


# OTRA FUNCION UTIL ES LA MAP() toma un iterable y aplica una funcion a cada uno de sus elementos.
# ejemplo de la map() para convertir una lista de temperaturas celsius a fahrenheit.
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
    return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]
# dentro del map, pasamos dos parametros la funcion y el parametro de la funcion



# OTRA FUNCION ES LA SUM() se usa para obtener la suma de un iterable, como una lista o una tupla
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50
# se puede pasar un start argumento opcional que declara el valor inicial de la suma.

