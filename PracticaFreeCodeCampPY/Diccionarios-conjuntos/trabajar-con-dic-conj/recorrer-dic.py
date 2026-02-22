# Recorrer un diccionario si necesitas acceder y procesar sus pares
# clave-valor. Esto resulta util para actualizar sus valores o aplicarles logica
products = {
    'Laptop' : 990,
    'Smartphone' : 600,
    'Tablet' : 250,
    'Headphones' : 70
}

# si queremos ofrecer un descuento del 20% en todos nuestros productos, 
# podemos recorrer todos los pares clave-valor y modificar los precios.

# Los metodos values, keys y items son esenciales para estas tecnicas.
# Devuelven un objeto de vista con los valores, las claves y los pares clave-valor
# del diccionario. Puedes usar estos objetos de vista en for bucles para iterar sobre los elementos

# Se escribe for, la variable de bucle (price en este caso),
# products.values() para obtener todos los valores del products diccionario

for price in products.values():
    print(price)

# esto funciona igual .keys() si necesitas iterar sobre las claves de un diccionario.
# esto funciona igual .items() si necesitas iterar sobre las clave-valor


# ahora que sabemos podemos volver a nuestro ejemplo inicial. Aplicar el 20% de descuento
for product, price in products.items():
    product[product] = round(price * 0.8)

# SI se necesita iterar sobre los pares clave-valor mientras controla un contador se puede usar la enumerate()
# actua como especie de indice o conteo.
# La fucion devuelve un objeto que asigna un entero a cada par clave-valor.
for product in enumerate(products):
    print(product) # obtenemos tuplas con el entero y la clave 
"""
(0, 'Laptop')
(1, 'Smartphone')
(2, 'Tablet')
(3, 'Headphones')
"""

# se puede asignar estos valores a variables de bucle independientes.
# Aqui tenemos dos variables de bucle (index y product)
for index,product in enumerate(products) :
    print(index,product)

# si necesitas iterar sobre los valores reemplazamos enumerate(products.values()): e product x price

# y podemos usar tambien la funcion .items() para obtener el indice y las clave-valor del diccionario
for index, product in enumerate(products.items()):
    print(index,product)

