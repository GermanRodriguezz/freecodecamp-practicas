# En Python, el alcance determina el punto en el que se puede acceder a una variable. 
# Es lo que controla su duración y cómo se resuelve en las diferentes partes del código. 
# Para determinar correctamente el alcance, Python sigue la regla LEGB , que significa lo siguiente:
# Ámbito local (L) : Variables definidas en funciones o clases.
# Ámbito envolvente (E) : Variables definidas en funciones envolventes o anidadas.
# Ámbito global (G): Variables definidas en el nivel superior del módulo o archivo.
# Ámbito incorporado (B) : Nombres reservados en Python para funciones, módulos, palabras clave y objetos predefinidos.
# Python usa la regla LEGB para determinar el alcance de las variables de tu programa. Analizaremos cada una de estas reglas para que comprendas mejor el proceso.
# El ámbito local significa que a una variable declarada dentro de una función o clase solo se puede acceder dentro de esa función o clase.

def my_func():
    my_var = 10
    print(my_var)

# En este ejemplo si quisieramos imprimir la variable "my_var" fuera del modulo
# No seria posible ya que solo existe en la funcion

# AMBITO ENVOLVENTE#
def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func() # Hello there!

# la funcion interna inner_func puede acceder libremente a la msg variable definida en la funcion externa
# outher_func. Sin embargo tenga en cuenta que las funciones externas no pueden acceder
# a las variables definidas dentro de ninguna funcion anidada:

def outer_func():
    msg = 'Hello there'
    print(res)

    def inner_func():
        res = 'How are you'
        print(msg)

    inner_func()

outer_func()

# res su alcance local es inner_func. Ademas outer_func intenta imprimir RES
# antes de inner_func.

# AMBITO GLOBAL
# Se refiere a las variables declaradas fuera de cualquier funcion o clase
#  las que se puede acceder desde cualquier parte del programa
# my_var se puede accerder desde cualquier lugar, incluso dentro de una funcion

my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100