# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

# Se usa un bucle for para iterar desde 0 hasta 100 e imprimir cada número en una línea separada.
# La función range(101) genera números desde 0 hasta 100 inclusive.
for numero in range(101):
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene. 

# Solicitamos un número entero al usuario
numero = int(input("Ingrese un número entero: "))
# Inicializamos un contador para los dígitos
cantidad_digitos = 0
# Usamos un bucle while para contar los dígitos dividiendo el número por 10 hasta que sea 0
while numero != 0:
    numero //= 10
    cantidad_digitos += 1
print("La cantidad de dígitos es:", cantidad_digitos)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 


print("números enteros comprendidos entre dos valores")
# Solicitamos los dos valores al usuario
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
# Inicializamos la suma en 0
suma = 0
# Usamos un bucle for para sumar los números entre valor1 y valor2, excluyendo ambos
for numero in range(valor1 + 1, valor2):
    suma += numero
print("La suma de los números entre", valor1, "y", valor2, "es:", suma)
# Nota: se da por sentado que el primer valor es menor que el segundo.
# Si no es así, se puede agregar una validación para intercambiar los valores si es necesario.

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

# Inicializamos la suma en 0
suma = 0
# Usamos un bucle while para permitir al usuario ingresar números hasta que ingrese 0
while True:
    numero = int(input("Ingrese un número entero (0 para finalizar): "))
    # Si el número es 0, salimos del bucle
    if numero == 0:
        break
    # Si no es 0, lo sumamos al total acumulado
    suma += numero
print("La suma total es:", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

# Importamos el módulo random para generar un número aleatorio
import random
# Generamos un número aleatorio entre 0 y 9
numero_aleatorio = random.randint(0, 9)
# Inicializamos el contador de intentos
intentos = 0
# Usamos un bucle while para permitir al usuario adivinar el número hasta que lo acierte
while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    # Si el intento es correcto, mostramos un mensaje y salimos del bucle
    if intento == numero_aleatorio:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
        break
    else:
        print("Número incorrecto. Intenta de nuevo.")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente. 

# Usamos un bucle for para iterar desde 100 hasta 0 en pasos de -1
# Dentro del bucle, verificamos si el número es par y lo imprimimos si lo es
for numero in range(100, 0, -1):
    if numero % 2 == 0:
        print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

# Solicitamos un número entero positivo al usuario
numero = int(input("Ingrese un número entero positivo: "))
# Inicializamos la suma en 0
suma = 0
# Usamos un bucle for para sumar los números desde 0 hasta el número indicado, excluyendo el número
for i in range(numero):
    suma += i
print("La suma de los números entre 0 y", numero, "es:", suma)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Definimos la cantidad de números a ingresar
cantidad_numeros = 100
# Inicializamos los contadores en 0
pares = 0
impares = 0
positivos = 0
negativos = 0
# Usamos un bucle for para permitir al usuario ingresar la cantidad definida de números
for _ in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    # Verificamos si el número es par o impar y actualizamos los contadores correspondientes
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    # Verificamos si el número es positivo o negativo y actualizamos los contadores correspondientes
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor). 

# Definimos la cantidad de números a ingresar
cantidad_numeros = 100
# Inicializamos la suma en 0
suma = 0
# Usamos un bucle for para permitir al usuario ingresar la cantidad definida de números
for _ in range(cantidad_numeros):
    numero = int(input("Ingrese un número entero: "))
    suma += numero
# Calculamos la media dividiendo la suma total por la cantidad de números ingresados
media = suma / cantidad_numeros
print("La media de los números ingresados es:", media)

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

# Solicitamos un número entero al usuario
numero = int(input("Ingrese un número entero: "))
# Inicializamos la variable para el número invertido
numero_invertido = 0
# Usamos un bucle while para invertir los dígitos del número
while numero != 0:
    # Extraemos el último dígito del número
    digito = numero % 10
    # Construimos el número invertido agregando el dígito extraído
    numero_invertido = numero_invertido * 10 + digito
    # Eliminamos el último dígito del número original
    numero //= 10
print("El número invertido es:", numero_invertido)