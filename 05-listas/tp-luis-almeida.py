# 1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa. 
# • Calcular y mostrar el promedio. 
# • Indicar la nota más alta y la más baja. 

# Lista con las notas de 10 estudiantes
notas = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
# Mostrar la lista completa
for  nota in notas:
    print("Nota del estudiante:", nota)
# Calcular y mostrar el promedio
promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)
# Indicar la nota más alta y la más baja
notaMax = max(notas)
notaMin = min(notas)
print("Nota más alta:", notaMax)
print("Nota más baja:", notaMin)

# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

# Lista para almacenar los productos
productos = []
# Pedir al usuario que ingrese 5 productos
for i in range(5):
    producto = input("Ingrese el nombre del producto: ")
    productos.append(producto)
# Mostrar la lista ordenada alfabéticamente
productos = sorted(productos)
for producto in productos:
    print("Producto ordenado:", producto)
# Preguntar al usuario qué producto desea eliminar
producto_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
# Verificar si el producto está en la lista antes de eliminar
if producto_eliminar in productos:
    # Eliminar el producto de la lista
    productos.remove(producto_eliminar)
    for producto in productos:
        print("Lista actualizada:", producto)

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
# • Crear una lista con los pares y otra con los impares. 
# • Mostrar cuántos números tiene cada lista. 

# Generar lista con 15 números enteros al azar entre 1 y 100
import random
# Inicializar la lista de números
numeros = []
# Llenar la lista con 15 números aleatorios
for numero in range(15):
    numero = random.randint(1, 100)
    numeros.append(numero)
    print("Número generado:", numero)
# Crear listas para pares e impares
pares = []
impares = []
# Recorrer la lista de números y clasificarlos
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))

# 4) Dada una lista con valores repetidos: 
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 

# Lista inicial con valores repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# Crear una nueva lista sin elementos repetidos
datos_sin_repetidos = []
# Recorrer la lista original y agregar solo los elementos no repetidos
for dato in datos:
    # Verificar si el dato ya está en la nueva lista
    if dato not in datos_sin_repetidos:
        datos_sin_repetidos.append(dato)
# Mostrar los datos sin repetir
for dato in datos_sin_repetidos:
    print("Dato sin repetir:", dato)


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

# Lista inicial de estudiantes
estudiantes = ["Ana", "Luis", "Marta", "Carlos", "Sofía", "Jorge", "Lucía", "Pedro"]
# Ciclo para agregar o eliminar estudiantes
while True:
    accion = input("¿Desea agregar (a) o eliminar (e) un estudiante? (s para salir): ").lower()
    # Realizar la acción según la elección del usuario
    if accion == 'a':        
        nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
        # Agregar el nuevo estudiante a la lista
        estudiantes.append(nuevo_estudiante)
    elif accion == 'e':
        estudiante_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
        # Verificar si el estudiante está en la lista antes de eliminar
        if estudiante_eliminar in estudiantes:
            # Eliminar el estudiante de la lista
            estudiantes.remove(estudiante_eliminar)
        else:
            print("El estudiante no está en la lista.")
    elif accion == 's':
        break    
    else:
        print("Acción no válida. Intente de nuevo.")
        continue
# Mostrar la lista actualizada de estudiantes
    print("Lista actualizada de estudiantes:")
    for estudiante in estudiantes:
        print(estudiante)

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
# último pasa a ser el primero). 

# Lista inicial
numeros = [10, 20, 30, 40, 50, 60, 70]
# Guardamos el último elemento de la lista
ultimo = numeros[-1]
# Recorremos la lista desde el final hacia el principio, desplazando cada elemento una posición hacia la derecha
for i in range(len(numeros) - 1, 0, -1):
    numeros[i] = numeros[i - 1]
# Colocamos el último elemento en la primera posición
numeros[0] = ultimo
# Mostrar la lista rotada
for numero in numeros:
    print("Número rotado:", numero)

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica. 

# Matriz de temperaturas (7 días, 2 columnas: mínima y máxima)
matriz_temperaturas = [
    [12, 17],  # Lunes
    [11, 21],  # Martes
    [14, 22],  # Miércoles
    [13, 22],  # Jueves
    [12, 20],  # Viernes
    [14, 19],  # Sábado
    [15, 21]   # Domingo
]
# Inicializar variables para cálculos
suma_minimas = 0
suma_maximas = 0
amplitud_maxima = 0
dia_amplitud_maxima = 0
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# Recorrer cada día en la matriz
for i in range(len(matriz_temperaturas)):
    # Extraer las temperaturas mínima y máxima del día i
    minima = matriz_temperaturas[i][0]
    maxima = matriz_temperaturas[i][1]
    # Acumular las sumas de mínimas y máximas
    suma_minimas += minima
    suma_maximas += maxima
    # Calcular la amplitud térmica del día i
    amplitud = maxima - minima
    # Verificar si es la mayor amplitud registrada
    if amplitud > amplitud_maxima:
        amplitud_maxima = amplitud
        dia_amplitud_maxima = i
# Calcular y mostrar los promedios
promedio_minimas = suma_minimas / len(matriz_temperaturas)
promedio_maximas = suma_maximas / len(matriz_temperaturas)
print("Promedio de temperaturas mínimas:", promedio_minimas)
print("Promedio de temperaturas máximas:", promedio_maximas)
print("El día con mayor amplitud térmica fue:", dias_semana[dia_amplitud_maxima], "con una amplitud de", amplitud_maxima)


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
# • Mostrar el promedio de cada estudiante. 
# • Mostrar el promedio de cada materia. 

# Matriz de notas (5 estudiantes, 3 materias)
notas_estudiantes = [
    [85, 90, 78],  # Estudiante 1
    [92, 88, 76],  # Estudiante 2
    [95, 89, 84],  # Estudiante 3
    [91, 87, 80],  # Estudiante 4
    [88, 92, 79]   # Estudiante 5
]
# Calcular el promedio de cada estudiante
for i in range(len(notas_estudiantes)):
    promedio_estudiante = sum(notas_estudiantes[i]) / len(notas_estudiantes[i])
    print("Promedio del Estudiante", i + 1, ":", promedio_estudiante)

# Calcular el promedio de cada materia
for j in range(len(notas_estudiantes[0])):
    # Reinicializar la suma para cada materia
    suma_materia = 0
    # Sumar las notas de la materia j para todos los estudiantes i
    for i in range(len(notas_estudiantes)):
        suma_materia += notas_estudiantes[i][j]
    promedio_materia = suma_materia / len(notas_estudiantes)
    print("Promedio de la Materia", j + 1, ":", promedio_materia)

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
# • Inicializarlo con guiones "-" representando casillas vacías. 
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
# • Mostrar el tablero después de cada jugada. 

# Inicializar el tablero
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
print("")
print("Tablero inicial:")
print("")
# Mostrar el tablero
for fila in tablero:
    print(" | ".join(fila))
    print("-" * 9)
turno = 0
# Ciclo de juego
while turno < 9:
    # Determinar el jugador actual    
    jugador = "X" if turno % 2 == 0 else "O"
    print("")
    # Pedir al jugador que ingrese fila y columna
    fila = int(input(f"Jugador {jugador}, ingrese la fila (0-2): "))
    columna = int(input(f"Jugador {jugador}, ingrese la columna (0-2): "))
    # Verificar si el jugador desea salir
    if fila < 0 or columna < 0 or fila > 2 or columna > 2:
        print("Fin del juego.")
        break
    # Verificar si la posición está vacía
    if tablero[fila][columna] == "-":
        # Colocar la marca del jugador en la posición indicada
        tablero[fila][columna] = jugador
        print("")
        for fila in tablero:
            print(" | ".join(fila))
            print("-" * 9)
        turno += 1
    else:
        print("Casilla ya ocupada. Intente de nuevo.")
        


# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana.

# Matriz de ventas (4 productos, 7 días)
ventas = [
    [150, 200, 250, 300, 350, 400, 450],  # Producto 1
    [100, 150, 200, 250, 300, 350, 400],  # Producto 2
    [200, 250, 300, 350, 400, 450, 500],  # Producto 3
    [250, 300, 350, 400, 450, 500, 550]   # Producto 4
]
# Calcular el total vendido por cada producto
total_por_producto = []
for i in range(len(ventas)):
    # sum() calcula la suma de los elementos en la lista ventas[i]
    total = sum(ventas[i])
    # append() agrega el total calculado a la lista total_por_producto
    total_por_producto.append(total)
    print("Total vendido del Producto", i + 1, ":", total)

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

total_por_dia = [0, 0, 0, 0, 0, 0, 0] 
# Calcular el total vendido por cada día
for j in range(len(ventas[0])):
    for i in range(len(ventas)):
        # Sumar las ventas del día j para todos los productos i
        total_por_dia[j] += ventas[i][j]

# index() devuelve el índice del primer elemento que coincide con el valor especificado
# max() devuelve el valor máximo en la lista total_por_dia
dia_mayores_ventas = total_por_dia.index(max(total_por_dia))
print("El día con mayores ventas totales fue:", dias_semana[dia_mayores_ventas], "con un total de", total_por_dia[dia_mayores_ventas])

# Determinar cuál fue el producto más vendido en la semana
producto_mas_vendido = total_por_producto.index(max(total_por_producto))
print("El producto más vendido en la semana fue el Producto", producto_mas_vendido + 1, "con un total de", total_por_producto[producto_mas_vendido])
