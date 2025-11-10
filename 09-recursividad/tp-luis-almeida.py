# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    else:
        # Llamada recursiva
        return n * factorial(n - 1)
# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo para calcular sus factoriales: "))
# Calcular y mostrar el factorial de todos los números desde 1 hasta el número ingresado
for i in range(1, numero + 1):
    print(f"Factorial de {i} es {factorial(i)}") 

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

def fibonacci(n):
    # Caso base: los dos primeros números de Fibonacci son 0 y 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Llamada recursiva
        return fibonacci(n - 1) + fibonacci(n - 2)
# Solicitar al usuario la posición hasta donde quiere ver la serie de Fibonacci
posicion = int(input("Ingrese la posición hasta donde desea ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(posicion):
    print(fibonacci(i), end=" ")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 
def potencia(base, exponente):
    # Caso base: cualquier número elevado a la potencia 0 es 1
    if exponente == 0:
        return 1
    else:
        # Llamada recursiva
        return base * potencia(base, exponente - 1)
# Solicitar al usuario la base y el exponente
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente (entero no negativo): "))
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

def decimal_a_binario(n):
    # Caso base: si el número es 0, devolver cadena vacía
    if n == 0:
        return ""
    else:
        # Llamada recursiva y concatenación del bit menos significativo
        return decimal_a_binario(n // 2) + str(n % 2)
# Solicitar al usuario un número entero positivo
numero_decimal = int(input("Ingrese un número entero positivo para convertir a binario: "))
binario = decimal_a_binario(numero_decimal)
# Manejar el caso especial cuando el número es 0
if binario == "":
    binario = "0"
print(f"La representación binaria de {numero_decimal} es {binario}")


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
#      Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed(). 

def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 letra, es un palíndromo
    if len(palabra) <= 1:
        return True
    else:
        # Comparar la primera y última letra
        if palabra[0].lower() == palabra[-1].lower():
            # Llamada recursiva con la subcadena sin la primera y última letra
            return es_palindromo(palabra[1:-1])
        else:
            return False
# Solicitar al usuario una palabra
palabra_usuario = input("Ingrese una palabra para verificar si es un palíndromo:")
if es_palindromo(palabra_usuario):
    print(f"{palabra_usuario} es un palíndromo.")
else:
    print(f"{palabra_usuario} no es un palíndromo.")


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
#      Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5) 

def suma_digitos(n):
    # Caso base: si el número es 0, la suma es 0
    if n == 0:
        return 0
    else:
        # Sumar el último dígito y llamar recursivamente con el resto del número
        return (n % 10) + suma_digitos(n // 10)
# Solicitar al usuario un número entero positivo
numero_suma = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
resultado_suma = suma_digitos(numero_suma)
print(f"La suma de los dígitos de {numero_suma} es {resultado_suma}.")


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide.
# Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1) 

def contar_bloques(n):
    # Caso base: si hay 0 bloques, el total es 0
    if n == 0:
        return 0
    else:
        # Sumar los bloques del nivel actual y llamar recursivamente con n-1
        return n + contar_bloques(n - 1)
# Solicitar al usuario el número de bloques en el nivel más bajo
bloques_nivel_bajo = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
total_bloques = contar_bloques(bloques_nivel_bajo)
print(f"El total de bloques necesarios para construir la pirámide es {total_bloques}.")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
# Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4
# contar_digito(123456, 7)     → 0

def contar_digito(numero, digito):
    # Caso base: si el número es 0, no hay dígitos que contar
    if numero == 0:
        return 0
    else:
        # Verificar si el último dígito coincide con el dígito buscado
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
# Solicitar al usuario un número entero positivo y un dígito
numero_usuario = int(input("Ingrese un número entero positivo: "))
digito_usuario = int(input("Ingrese un dígito (0-9) para contar: "))
veces = contar_digito(numero_usuario, digito_usuario)
print(f"El dígito {digito_usuario} aparece {veces} veces en el número {numero_usuario}.")