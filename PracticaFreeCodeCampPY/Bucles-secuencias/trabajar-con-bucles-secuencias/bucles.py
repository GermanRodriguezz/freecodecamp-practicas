# Se usan para repetir un bloque de codigo un numero de determinado de veces

# El primer bucle que veremos es FOR

programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
    print(language)

# este bloque de codigo itera sobre la lista, guardando cada elemento en la variable
# lenguage

# recorrer una cadena
for char in 'code':
    print(char)
# al imprimir sobre cada iteracion se vera reflejado CADA LETRA DE LA CADENA


# tambien se pueden anidar FOR
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
    for food in foods:
        print(category, food)
# el for externo el de mas arriba itera sobre cada elemento de CATEGORIES guardando el valor en la variable CATEGORY
# el for interno itera sobre los valores de la lista FOODS guardando cada valor sobre la variable FOOD
# imprimiendo esto:
# Fruit Apple
# Fruit Carrot
# Fruit Banana
# Vegetable Apple
# Vegetable Carrot
# Vegetable Banana



# otro bucle es el while, repite el bloque mientras la condicion sea FALSA
secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')

print('You got it!')
# este bloque de codigo se detendra cuando el usuario ingrese un valor que sea igual al secret_number
# ingresa el valor el usuario y se pregunta con el if si es distinto al numero secreto
# de ser asi retoma al while y debe ingresar otro numero del 1-5



# declaraciones BREAK Y CONTINUE
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)
# cuando el nombre es igual a naomi sale del bucle imprimiendo unicamente el primer nombre de la lista

#La continue instruccion se usa para OMITIR la iteracion actual
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)
#ahora el resultado que se imprime es distinto, imprime todos los nombres de la lista menos el de naomi


# los bucles for y while se pueden combinar con una ELSE, que se ejecuta solo cuando el bucle no termina con un break
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")
# este bloque de codigo primero recorre cada elemento de la lista y lo guarda en la variable word
# luego recorre el elemento (palabra)
# pregunta si la letra de la palabra se encuentra en la cadena AEIOU
# de ser asi imprime el mensaje y sale del bucle de recorrer la palabra
# en caso contrario de recorrer toda la palabra y no encontrar una aparicion de la letra en la cadena AEIOU va al ELSE

