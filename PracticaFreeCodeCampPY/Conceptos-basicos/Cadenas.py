# Una cadena es una secuencia de caracteres
my_str_1 = 'Hello'

# A veces, puede que necesites comprobar si una cadena contiene 
# uno o más caracteres. Para ello, Python proporciona el inoperador, 
# que devuelve un valor booleano que especifica si el carácter o los 
# caracteres existen en la cadena.
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False



# veamos como obtener la longitud de una cadena y trabajar con sus caracteres
# individuales, un proceso llamado indexacion. Para obtener la longitud de una 
# cadena, se puede usar la funcion integrada LEN()
my_str = 'Hello world'
print(len(my_str))  # 11



# Cada carácter de una cadena tiene una posición llamada índice. 
# El índice se basa en cero, lo que significa que el índice del 
# primer carácter de una cadena es 0, el del segundo es 1, 
# y así sucesivamente. Para acceder a un carácter por su índice, 
# se utilizan corchetes ( []) con el índice del carácter al que se desea 
# acceder dentro. 
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w



# También se permite la indexación negativa, por lo que puede obtener 
# el último carácter de cualquier cadena con -1, el penúltimo carácter 
# con -2, y así sucesivamente:
my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l



# En Python, se pueden combinar varias cadenas con el +operador más ().
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World



# También puede usar el operador de asignación aumentada para la 
# concatenación. Este se representa con un signo más e igual ( +=) 
# y realiza la concatenación y la asignación en un solo paso. 
# Aquí lo vemos en acción:
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26




# Python cuenta con una categoría de cadenas denominada f-strings 
# (abreviatura de literales de cadena formateados), que 
# permite gestionar la interpolación con una sintaxis compacta y legible.
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') 




# Python proporciona varios métodos integrados que facilitan el trabajo con cadenas. 
# Entre ellos se incluyen los siguientes:
# upper():Devuelve una nueva cadena con todos los caracteres convertidos a mayúsculas
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD



# lower():Devuelve una nueva cadena con todos los caracteres convertidos a minúsculas.
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world



# strip(): Devuelve una nueva cadena sin los caracteres iniciales ni finales especificados. 
# Si no se pasa ningún argumento, se eliminan los espacios iniciales y finales.
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"



# replace(old, new): Devuelve una nueva cadena 
# con todas las apariciones de oldreemplazadas por new.
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world




# split(separator)Divide una cadena según un separador especificado en una lista de cadenas.
#  Si no se especifica ningún separador, se divide por espacios.
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']



# count(substring):Devuelve el número de veces que aparece una subcadena en una cadena.
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2




# capitalize():Devuelve una nueva cadena con el primer carácter en mayúscula 
# y los demás caracteres en minúscula.
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world



