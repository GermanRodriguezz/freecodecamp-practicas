# La funcion range se usa para generar una secuencia de enteros
# range(start,stop,step)

# el stop es un enetero que representa el punto final de la secuencia de numeros generada
for num in range(3):
        print(num)
# este bloque de codigo genera un secuencia de numeros entre el 0 y 2
#no incluye el numero 3
#si START no se especifica siempre comenzara desde el 0


for num in range(1, 5):
    print(num)
# el bloque anterior genera la secuencia de numeros enteros desde 1 hasta 4


for num in range(2,11,2):
    print(num)
# este bloque de codigo generara la secuencia de numeros enteros desde el 2 al 10 saltando de 2 en 2
#si no tiene argumentos aparecera el TypeError


#se pueden generar lista a traves del range
numeros = list(range(2,11,2))
print(numeros) # [2,4,6,8,10]