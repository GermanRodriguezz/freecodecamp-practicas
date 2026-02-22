# Son estructuras de datos integradas. No almacenan valores duplicados
# Son mutables y desordenados, lo que signidica que sus elementos no se almacenan en un orden especifico
# Contienen valores de tipos de datos inmutables, como numeros, cadenas y tuplas.

my_set = {1,2,3,4,5}

# una peculiaridad es que si necesitas definir un conjunto vacio,debes usar la set() funcion
# si escribes llaves vacias {}, python crea un diccionario

set()

# se agrega un elemento a un conjunto con el .add() y pasar el nuevo elemento como argumento
my_set.add(6)

# si intentas añadir un elemento que ya esta en el conjunto solo se conservara uno.

# para eliminar un elemento del conjunto hay dos opciones .remove() o .discard() y pasar como argumento el elemento a eliminar
# el .remove() lanza un KeyError si no encuentra el elemento y el .discard() no


# .clear() elimina todos los elementos del conjunto

# .issubset() y .issuperset comprueban si un conjunto es un subconjunto o superconjunto de otro conjunto
my_set = {1,2,3,4,5}
your_set = {2,3,4,6}

print(your_set.issubset(my_set)) # False ya que se esta comprobando si YOUR_SET es un subconjunto de MY_SET y no todos los elementos de your_set estan en my_set
print(my_set.issuperset(your_set)) #False ya que se esta comprobando si my_set es un SUPERCONJUNTO de YOUR_SET y no,no tiene todos los elementos de your_set 

# El .isdisjoint comprueba si dos conjuntos son disjuntos es decir que no tienen ningun elemento en comun.
# En estos dos conjuntos hay numero en comun de este modo la funcion devuelve False
print(my_set.isdisjoint(your_set)) # False

# el operador | devuelve un nuevo conjunto con todos los elementos de amvos conjuntos
my_set | your_set # {1,2,3,4,5,6}

# el operador de interseccion & devuelve un nuevo conjunto con solo los elementos que los conjuntos tienen en comun
my_set & your_set # {2,3,4}

# el operador de diferencia devuelve un nuevo conjunto con los elementos del primer conjunto que noe stan en los otros conjuntos.
my_set - your_set # {1,5}


