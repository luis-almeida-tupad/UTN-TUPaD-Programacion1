# Trabajo practico: Estructuras secuenciales
# Alumno: Luis Almeida

#### Ejercicio 1 ####
print("Hola Mundo!")

#### Ejercicio 2 ####
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")

#### Ejercicio 3 ####
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuál es tu edad? ")
pias_residencia = input("¿En qué país resides? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pias_residencia}")

#### Ejercicio 4 ####
radio = float(input("Indique el radio del círculo: "))
print(f"El área del círculo es: {3.14 * radio ** 2}")
print(f"El perímetro del círculo es: {2 * 3.14 * radio}")

#### Ejercicio 5 ####
segundos = int(input("Indique el número de segundos: "))
print(f"El número de horas es: {segundos // 3600}")

#### Ejercicio 6 ####
numero = int(input("Indique un número: "))
print(f"La tabla de multiplicar del {numero} es:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#### Ejercicio 7 ####
numero = int(input("Indique un número entero distinto a 0: "))
numero2 = int(input("Indique otro número entero distinto a 0: "))
print(f"La suma de {numero} y {numero2} es: {numero + numero2}")
print(f"La resta de {numero} y {numero2} es: {numero - numero2}")
print(f"La multiplicación de {numero} y {numero2} es: {numero * numero2}")
print(f"La división de {numero} y {numero2} es: {numero / numero2}")

#### Ejercicio 8 ####
altura = float(input("Indique su altura en metros: "))
peso = float(input("Indique su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc}")

#### Ejercicio 9 ####
gradosCelsius = float(input("Indique la temperatura en grados Celsius: "))
gradosFahrenheit = (gradosCelsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {gradosFahrenheit}")

#### Ejercicio 10 ####
primerNumero = int(input("Indique el primer número: "))
segundoNumero = int(input("Indique el segundo número: "))
tercerNumero = int(input("Indique el tercer número: "))
print(f"El promedio de los tres números es: {(primerNumero + segundoNumero + tercerNumero) / 3}")

