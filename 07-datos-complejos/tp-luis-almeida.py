# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300 

# Definición del diccionario inicial de precios de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir nuevas frutas y precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
# Mostrar el diccionario actualizado
print("Diccionario de precios de frutas actualizado:")
print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

# Actualizar los precios de las frutas especificadas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
# Mostrar el diccionario con los precios actualizados
print("Diccionario de precios de frutas con precios actualizados:")
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 

frutas = list(precios_frutas.keys())
print("Lista de frutas sin precios:")
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe. 

# Crear un diccionario para almacenar los contactos
agenda_telefonica = {}
# Cargar 5 contactos
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    agenda_telefonica[nombre] = numero
# Consultar un número por nombre
nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
# Mostrar el número si el contacto existe
if nombre_consulta in agenda_telefonica:
    print(f"El número de {nombre_consulta} es: {agenda_telefonica[nombre_consulta]}")
else:
    print(f"No se encontró el contacto {nombre_consulta} en la agenda.")

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra. 

frase = input("Ingrese una frase: ")
palabras = frase.split()
# Palabras únicas usando un set
palabras_unicas = set(palabras)
print("Palabras únicas:")
print(palabras_unicas)
# Diccionario con la cantidad de veces que aparece cada palabra
contador_palabras = {}
# Contar las apariciones de cada palabra
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1
# Mostrar el diccionario de conteo de palabras
print("Cantidad de veces que aparece cada palabra:")
print(contador_palabras)


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 

alumnos = {}
# Ingresar nombres de 3 alumnos
for _ in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []
    # Ingresar 3 notas para cada alumno
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i+1} de {nombre}: "))
        notas.append(nota)
    # Almacenar las notas como una tupla en el diccionario
    alumnos[nombre] = tuple(notas)
# Calcular y mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    # Mostrar el promedio con dos decimales
    print(f"El promedio de {nombre} es: {promedio:.2f}")
    

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {104, 105, 106, 107, 108}
# Estudiantes que aprobaron ambos parciales
ambos_parciales = parcial_1.intersection(parcial_2)
print("Estudiantes que aprobaron ambos parciales:")
print(ambos_parciales)
# Estudiantes que aprobaron solo uno de los dos parciales
solo_uno = parcial_1.symmetric_difference(parcial_2)
print("Estudiantes que aprobaron solo uno de los dos parciales:")
print(solo_uno)
# Lista total de estudiantes que aprobaron al menos un parcial
al_menos_uno = parcial_1.union(parcial_2)
print("Lista total de estudiantes que aprobaron al menos un parcial:")
print(al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe. 

stock_productos = {}
# Consultar stock de un producto
def consultar_stock(producto):
    return stock_productos.get(producto, "Producto no encontrado")
# Agregar o actualizar un producto en el stock
def agregar_producto(producto, cantidad):
    if producto in stock_productos:
        stock_productos[producto] += cantidad
    else:
        stock_productos[producto] = cantidad

while True:
    print("\nGestión de stock de productos")
    print("1. Consultar stock")
    print("2. Agregar/Actualizar producto")
    print("3. Salir")
    accion = input("\nIngrese la acción que desea realizar (1/2/3): ").lower()
    match accion:
        case '1':
            producto = input("Ingrese el nombre del producto a consultar: ")
            print(f"Stock de {producto}: {consultar_stock(producto)}")
        case '2':
            producto = input("Ingrese el nombre del producto a agregar/actualizar: ")
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            agregar_producto(producto, cantidad)
            print(f"Producto {producto} actualizado. Stock actual: {stock_productos[producto]}")
        case '3':
            print("Saliendo del programa.")
            break
        case _:
            print("Acción no válida. Por favor, intente nuevamente.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Permití consultar qué actividad hay en cierto día y hora. 

agenda = {
    ('Lunes', '10:00'): 'Reunión de equipo',
    ('Martes', '14:00'): 'Cita con el dentista',
    ('Miércoles', '09:00'): 'Clase de yoga',
}

# Consultar actividad en cierto día y hora
dia = input("Ingrese el día (por ejemplo, Lunes): ")
hora = input("Ingrese la hora (por ejemplo, 10:00): ")
# Buscar el evento en la agenda
evento = agenda.get((dia, hora), "No hay actividad programada en ese día y hora.")
# Mostrar el resultado
print(f"Actividad programada: {evento}")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Perú': 'Lima',
    'Colombia': 'Bogotá'
}

# Invertir el diccionario para que las capitales sean las claves
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
# Mostrar el diccionario invertido
print("Diccionario de capitales y países invertido:")
print(capitales_paises)