# 1. Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal.

#  función imprimir_hola_mundo
def imprimir_hola_mundo():
    print("Hola Mundo!")
# llamada a la función
imprimir_hola_mundo()

#  2. Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario.

# función saludar_usuario
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre_usuario = input("Ingrese su nombre: ")
# llamada a la función
print(saludar_usuario(nombre_usuario))

#  3. Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados. 

# función informacion_personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
# pedir datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")
# llamada a la función
informacion_personal(nombre, apellido, edad, residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

# importar la librería math para usar pi
import math
# funciones calcular_area_circulo y calcular_perimetro_circulo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio
# pedir el radio al usuario
radio = float(input("Ingrese el radio del círculo: "))
# llamar a las funciones y mostrar los resultados
print(f"Área del círculo: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro del círculo: {calcular_perimetro_circulo(radio):.2f}")

#  5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

# función segundos_a_horas
def segundos_a_horas(segundos):
    return segundos / 3600
# pedir al usuario la cantidad de segundos
segundos = int(input("Ingrese la cantidad de segundos: "))
# llamar a la función y mostrar el resultado
print(f"Cantidad de horas: {segundos_a_horas(segundos):.2f}")


#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.

# función tabla_multiplicar
def tabla_multiplicar(numero):
    # imprimir la tabla de multiplicar del 1 al 10
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
# pedir al usuario el número
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
# llamar a la función
tabla_multiplicar(numero)

#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.

# función operaciones_basicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)
# pedir al usuario los dos números
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
# llamar a la función y mostrar los resultados
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
# Nota: Asegurarse de manejar la división por cero si es necesario.

#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

# función calcular_imc
def calcular_imc(peso, altura):
    return peso / (altura ** 2)
# pedir al usuario el peso y la altura
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
# llamar a la función y mostrar el resultado con dos decimales
imc = calcular_imc(peso, altura)
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

# función celsius_a_fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# pedir al usuario la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
# llamar a la función y mostrar el resultado
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")

#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

# función calcular_promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3
# pedir al usuario los tres números
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
# llamar a la función y mostrar el resultado
promedio = calcular_promedio(a, b, c)
print(f"El promedio de los números es: {promedio:.2f}")