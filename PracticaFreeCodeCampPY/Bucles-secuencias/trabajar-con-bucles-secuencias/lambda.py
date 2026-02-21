# cuando se trata de trabajar con funciones de orden superior como map() filter() se puede usar una funcion en linea anonima
def square(num):
    return num ** 2

print(square(4)) # 16
# de la siguiente manera es en la cual se ve la funcion refactorizada en una funcion lambda
lambda num: num ** 2
# las funciones lambda son anonimas, por lo que esta funcion ya no tiene el nombre square, 
# son ideales cuando se necesitan usar funciones de orden superior como la siguiente
numbers = [1,2,3,4,5]
even_numbers = list(filter(lambda x: x % 2 == 0), numbers) # filtra por esta funcion sobre la lista numbers, el iterable que devuelve convertilo en lista


# SI TRABAJAS CON EXPRESIONES EN LINEA, PODRIA CONSIDERAR USAR UNA FUNCION LAMBDA.