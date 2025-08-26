# Actividades:

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

# Se solicita la edad del usuario
edad = int(input("Ingrese su edad: "))
# Se verifica si es mayor de edad
if edad > 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”. 

# Se solicita la nota del usuario
nota = float(input("Ingrese su nota: "))
# Se verifica si está aprobado o desaprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# Se solicita un número al usuario
numero = int(input("Ingrese un número: "))
# Se verifica si el número es par o impar
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

# Se solicita la edad del usuario
edad = int(input("Ingrese su edad: "))
# Se verifica a qué categoría pertenece
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")
else:
    pass

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
# como una lista o un string.

# Se solicita la contraseña al usuario
contrasena = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
# Se verifica la longitud de la contraseña
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, 
# su mediana y su media y las compare para determinar si hay sesgo positivo, negativo 
# o no hay sesgo. Imprimir el resultado por pantalla. 

# Definir la lista numeros_aleatorios de la siguiente forma: 
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de 
# forma aleatoria. 

# Se importa la librería random y statistics
import random
from statistics import mean, median, mode
# Se define la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Se calcula la media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
# Se imprime la lista y los valores calculados
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")
# Se determina el sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    print("No hay sesgo")
else:
    pass

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla.

# Se solicita una frase o palabra al usuario
frase = input("Ingrese una frase o palabra: ")
# Se verifica si termina con vocal
if frase[-1].lower() in 'aeiou':
    frase += '!'
    print(frase)
else:
    print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Se solicita el nombre al usuario
nombre = input("Ingrese su nombre: ")
# Se solicita la opción al usuario
opcion = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas, 3 para primera letra mayúscula: "))
# Se transforma el nombre según la opción seleccionada
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Se solicita la magnitud del terremoto al usuario
magnitud = float(input("Ingrese la magnitud del terremoto: "))
# Se clasifica la magnitud según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano. 

# Se solicita el hemisferio al usuario
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
# Se solicita el mes al usuario
mes = int(input("¿Qué mes del año es? (1-12): "))
# Se solicita el día al usuario
dia = int(input("¿Qué día del mes es? (1-31): "))
# Se determina la estación del año según el hemisferio, mes y día
if hemisferio == 'N':
    if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or (mes == 1 or mes == 2):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes == 4 or mes == 5):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes == 7 or mes == 8):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes == 10 or mes == 11):
        print("Otoño")
    else:
        print("Fecha inválida")
elif hemisferio == 'S':
    if (mes == 12 and dia >= 21) or (mes == 3 and dia <= 20) or (mes == 1 or mes == 2):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes == 6 and dia <= 20) or (mes == 4 or mes == 5):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 9 and dia <= 20) or (mes == 7 or mes == 8):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 12 and dia <= 20) or (mes == 10 or mes == 11):
        print("Primavera")
    else:
        print("Fecha inválida")
else:
    print("Hemisferio inválido")

# Nota: Se asume que el usuario ingresa valores válidos para el mes (1-12) y el día (1-31)
# y que no se tienen en cuenta los años bisiestos ni la cantidad de días de cada mes.