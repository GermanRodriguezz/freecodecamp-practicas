# Son estructuras de datos integradas que almacenan conjuntos de pares clave-valor.
# Funcionan de forma muy similar a los diccionarios reales, donde se busca una palabra para encontrar su significado

# Se usa una clave para encontrar su valor correspondiente.
# Se recomienda usar diccionario se necesita asociar valores a claves unicas.
# Es util cuando se necesita encontrar un valor rapidamente a partir de la clave y cuando se necesitan representar datos estructurados

dictionary = {
        'key1' : 1,
        'key2' : 2
}

# cada clave esta asociada a un valor, por lo que se puede usar para acceder a el.
# Despues cada valor, excepto el ultimo, se separa con una coma los diferentes pares clave-valor .
# Claves unicas en el diccionario y deben ser de un tipo inmutable.
# un ejemplo :

pizza = {
    'name' : 'Margherita Pizza',
    'price' : 8.9,
    'calories_per_slice' : 250,
    'toppings' : ['mozzarella', 'basil']
}

# otra alternativa es el dict() constructor
# pasamos una lista e tuplas como argumento, estas tuplas contienen clave como primer elemento y valor como segundo elemento.
pizza = dict([('name','Margherita Pizza'), ('price','8,9'),('calories_per_slice','250'),('toppings',['mozzarella','basil'])])

# para acceder al valor de un par clave-valor, puede usar esta sintaxis conocida como notacion de corchetes.
# es el nombre de la variable que contiene el diccionario, seguido de corchetes, y la clave a la que desea acceder dentro de los corchetes.
# siguiendo con el ejemplo anterior declarado :
pizza['name'] # devuelve 'Margherita pizza'

#Para actualizar un valor, solo necesitas agregar el operador de asignacion seguido del nuevo valor
# Si la clave no existe en el diccionario, se creara un nuevo par clave-valor.
pizza['name'] = 'Margherita'

# El .get() metodo recupera el valor asociado a una clave.
# dictionary.get(key,default)

# en la linea siguiente, si la toppings clave no existe, devolvera una lista vacia, 
# que es el valor predeterminado que pasamos como segundo argumento.
# Pero si toppinga existe devolvera el valor.

pizza.get('toppings',[]) # ['mozzarella', 'basil']


# Los metodos .keys() y .values() devuelven un objeto de vista con todas las claves y valores del diccionario
pizza.keys() #  dict_keys(['name', 'price', 'calories_per_slice'])
pizza.values() #  dict_values(['Margherita Pizza', 8.9, 250])

# El .items() devuelve un objeto de vista con todos los pares clave-valor del diccionario.
pizza.items() # dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])

# El .clear() elimina todos los pares clave-valor
pizza.clear()

# El .pop() elimina el par clave-valor con la clave especificada como primer argumento y devuelve su valor.
# si la clave no existe, devuelve el valor predeterminado especificado como segundo argumento
# si la clave no existe y no se pasa un valor predeterminado, se lanza KeyError
pizza.pop('price', 10)
pizza.pop('total_price') # KeyError

# El .update() actualiza los pares clave-valor con los clave-valor de otro diccionario. 
# Si comparten claves, sus valores se sobrescriben.

# En este ejemplo, actualizamos el pizza diccionario. La price clave existe en ambos, 
# por lo que su valor se reemplazara por 15

pizza.update({'price' : 15, 'total_time': 25})