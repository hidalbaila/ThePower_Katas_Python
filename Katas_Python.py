"""1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
de cada letra en la cadena. Los espacios no deben ser considerados."""
def ejercicio_1(cadena):
    # Defino la función llamada 'ejercicio_1' que recibe como parámetro una cadena de texto
    cadena = cadena.replace(" ", "")
    # Reemplazo los espacios en la cadena por "" (nada)
    # Esto hace que los espacios no se cuenten en la frecuencia de letras
    frecuencias = {}
    # Creo un diccionario vacío donde guardaré cuántas veces aparece cada letra
    for letra in cadena:
        # Recorro cada letra de la cadena (ya sin espacios)
        if letra in frecuencias:
            frecuencias[letra] += 1
            # Si la letra ya está en el diccionario, aumento su contador en 1
        else:
            frecuencias[letra] = 1
             # Si la letra no está en el diccionario, la agrego con valor 1
    return frecuencias
    # Devuelvo el diccionario con la frecuencia de cada letra
# Llamo a la función y muestro el resultado por pantalla
print(f'Resultado del ejercicio 1: {ejercicio_1("hola mundo")}') # {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}


""""2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()"""
def ejercicio_2(números):
    # Devuelve la lista con los números multiplicados por 2 usando map
    return list(map(lambda x: x*2, números))
# Lista de ejemplo
números = [1, 2, 3, 4, 5]
# Llamamos a la función y mostramos el resultado
print(f'Resultado del ejercicio 2: {ejercicio_2(números)}')  # [2, 4, 6, 8, 10]


"""3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo."""
def ejercicio_3(lista, objetivo):
    # Devuelve todas las palabras de la lista que contienen la palabra objetivo
    return [palabra for palabra in lista if objetivo in palabra]
# Lista de ejemplo
lista = ["invierno", "verano", "otoño", "primavera"]
objetivo = "no"
# Llamamos a la función y mostramos el resultado
resultado = ejercicio_3(lista, objetivo)
print(f'Resultado del ejercicio 3: {resultado}') # ['invierno', 'verano']


"""4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()"""
def ejercicio_4(lista_a, lista_b):
    # Usamos map con lambda para restar cada par de elementos de las dos listas
    return list(map(lambda x, y: x - y, lista_a, lista_b))
    # map aplica lambda x - y a cada par de elementos (x, y) de lista_a y lista_b
    # list() convierte el resultado de map en una lista
# Listas de ejemplo
lista_a = [8, 1, 0, 14]
lista_b = [4, 5, 9, 8]
# Llamamos a la función y mostramos el resultado
resultado = ejercicio_4(lista_a, lista_b)
print(f'Resultado del ejercicio 4: {resultado}')  # [8, 16, 24, 31]


"""5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado."""
def ejercicio_5(lista, nota_aprobado=5):
    media = round(sum(lista) / len(lista), 2)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)
# Lista de ejemplo
notas = [6,8,2,5,4,9]
resultado = ejercicio_5(notas)
print(f"Resultado del ejercicio 5: [{resultado[0]}, {resultado[1]}]") # [5.67, aprobado]


"""6. Escribe una función que calcule el factorial de un número de manera recursiva."""
def ejercicio_6(n):
    if n == 0 or n == 1:   # Caso base
        return 1
    else:
        return n * ejercicio_6(n - 1)   # Llamada recursiva
# Número de ejemplo
numero = 5
# Llamamos a la función y mostramos el resultado
resultado = ejercicio_6(numero)
print(f"Resultado del ejercicio 6: [{resultado}]")  # 120


"""7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()"""
def ejercicio_7(lista_tuplas):
    return list(map(lambda x: f"{x[0]} {x[1]}", lista_tuplas))
# Lista de ejemplo
personas = [("Pedro", 25), ("Alfredo", 30), ("Lucía", 22)]
# Llamamos a la función y mostramos el resultado
resultado = ejercicio_7(personas)
print(f"Resultado del ejercicio 7: {resultado}") # ['Pedro 25', 'Alfredo 30', 'Lucía 22']


"""8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no."""
def ejercicio_8():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 / num2
    except ValueError:
        print("Error: Debes introducir valores numéricos.")    
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")    
    else:
        print(f"La división fue exitosa. Resultado: {resultado}")    
    finally:
        print("Fin del programa.")
# Llamamos a la función
ejercicio_8()


"""9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()"""
def ejercicio_9(lista_animales):
    lista_animales_prohibidos = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda animal: animal not in lista_animales_prohibidos, lista_animales))
# Lista de ejemplo
lista_animales = ["Perro", "Mapache", "Mapache", "Gato", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
resultado = ejercicio_9(lista_animales)
print(f"Resultado del ejercicio 9: {resultado}")   # ['Perro', 'Gato']


"""10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente."""
class ListaVaciaError(Exception):
    pass
# Definir excepción personalizada
def ejercicio_10(lista_numeros):    
    if not lista_numeros:  # Verifica si la lista está vacía
        raise ListaVaciaError("La lista está vacía por lo que no se puede calcular el promedio.")    
    promedio = round(sum(lista_numeros) / len(lista_numeros), 2)
    return promedio
# Ejemplos de listas
listas = [
    [8.3, 4, 25],
    []  # Lista vacía para probar la excepción
]
for lista in listas:
    try:
        resultado = ejercicio_10(lista)
    except ListaVaciaError as e:
        print(f"Error: {e}")
    else:
        print(f"Resultado del ejercicio 10: {resultado}")


"""11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente."""
def ejercicio_11():
    while True:  # Bucle hasta que el usuario ingrese un valor válido
        try:
            edad = input("¿Cuál es tu edad? ").strip()
            edad = float(edad)  # Convertimos a número            
            if edad < 0 or edad > 120:
                raise ValueError("Edad fuera del rango permitido (0-120).")                
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")
        else:
            print(f"Resultado del ejercicio 11: {int(edad)}")
            break  # Salimos del bucle si todo está correcto
# Llamamos a la función
ejercicio_11() 


"""12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()"""
def ejercicio_12(frase):
    palabras = frase.split()  # Separamos la frase en palabras
    return list(map(len, palabras))  # map() aplica len a cada palabra
# Frase de ejemplo
frase = "El perro está mirando por la ventana"
resultado = ejercicio_12(frase)
print(f"Resultado del ejercicio 12: {resultado}") # [2, 5, 4, 7, 3, 2, 7]


"""13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()"""
def ejercicio_13(caracteres):
    # Nos aseguramos de que no haya letras repetidas
    caracteres_unicos = set(caracteres)    
    # Función que convierte cada letra a mayúscula y minúscula
    resultado = map(lambda c: (c.upper(), c.lower()), caracteres_unicos)    
    # Convertimos a lista y devolvemos
    return list(resultado)
# Conjunto de ejemplo
conjunto = {'a', 'b', 'C', 'd', 'a', 'B'}  # Repetidos se eliminan automáticamente
resultado = ejercicio_13(conjunto)
print(f"Resultado del ejercicio 13: {resultado}") #[('B', 'b'), ('D', 'd'), ('A', 'a'), ('B', 'b'), ('C', 'c')]


"""14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
función filter()"""
def ejercicio_14(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))
# Lista de ejemplo
lista_palabras = ["Hola", "Aceite", "Pájaro", "Ventana", "Alberto"]
resultado = ejercicio_14(lista_palabras, "A")
print(f"Resultado del ejercicio 14: {resultado}")


"""15. Crea una función lambda que sume 3 a cada número de una lista dada."""
def ejercicio_15(lista_numeros):
    return list(map(lambda x: x + 3, lista_numeros))
# Lista dada
lista_numeros = (3, 5, 7, 8)
resultado = ejercicio_15(lista_numeros)
print(f"Resultado del ejercicio 15: {resultado}") #[6, 8, 10, 11]


"""16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
todas las palabras que sean más largas que n. Usa la función filter()"""
def ejercicio_16(cadena_texto, n):
    palabras = cadena_texto.split()  # Convertimos el texto en lista de palabras
    return list(filter(lambda palabra: len(palabra) > n, palabras))
# Texto de ejemplo
cadena_texto = "Hola Adiós Ventana Sol Luz"
n = 3
resultado = ejercicio_16(cadena_texto, n)
print(f"Resultado del ejercicio 16: {resultado}") #['Hola', 'Adiós', 'Ventana']


"""17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2]
corresponde al número quinientos setenta y dos (572). Usa la función reduce()"""
from functools import reduce
def ejercicio_17(lista_digitos):
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, lista_digitos)
# Lista de ejemplo
lista = [5, 7, 2]
resultado = ejercicio_17(lista)
print(f"Resultado del ejercicio 17: {resultado}") #[572]


"""18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()"""
def ejercicio_18(info_estudiantes):
        # Usamos filter() para quedarnos solo con los estudiantes cuya calificación sea mayor o igual a 90
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, info_estudiantes))  # Iterable: lista de diccionarios
# Lista de diccionarios con información de estudiantes
info_estudiantes = [
    {"nombre": "María", "edad": 25, "calificacion": 98},
    {"nombre": "Arturo", "edad": 26, "calificacion": 92},
    {"nombre": "Paco", "edad": 28, "calificacion": 89}
]
# Llamamos a la función
resultado = ejercicio_18(info_estudiantes)
# Mostramos el resultado
print(f"Resultado del ejercicio 18: {resultado}") # [{'nombre': 'María', 'edad': 25, 'calificacion': 98}, {'nombre': 'Arturo', 'edad': 26, 'calificacion': 92}]


"""19. Crea una función lambda que filtre los números impares de una lista dada."""
def ejercicio_19(lista_numeros):
    # filter deja pasar solo los números que cumplen la condición (impares)
    return list(filter(lambda x: x % 2 != 0, lista_numeros))
# Lista de ejemplo
list_numeros = [6, 8, 9, 3, 82]
# Llamamos a la función
resultado = ejercicio_19(list_numeros)
# Mostramos el resultado
print(f"Resultado del ejercicio 19: {resultado}")  #  [9, 3]


"""20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función 
filter()"""
def ejercicio_20(lista):
    # filter deja pasar solo los elementos que sean enteros
    return list(filter(lambda x: type(x) == int, lista))
# Lista de ejemplo
lista_mixta = ["Hola", "Sol", 9, "Pájaro", 8, 7]
# Llamamos a la función
resultado = ejercicio_20(lista_mixta)
# Mostramos el resultado
print(f"Resultado del ejercicio 20: {resultado}")  #[9, 8, 7]


"""21. Crea una función que calcule el cubo de un número dado mediante una función"""
def ejercicio_21(x):
    # Calcula el cubo de x
    return x ** 3  # también se puede usar x*x*x
# Número de ejemplo
x = 3
# Llamamos a la función
resultado = ejercicio_21(x)
# Mostramos el resultado
print(f"Resultado del ejercicio 21: {resultado}")  #[27]


"""22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce()."""
from functools import reduce
def ejercicio_22(producto_total):
    # reduce aplica la función lambda acumulando el producto de los elementos
    return reduce(lambda x, y: x * y, producto_total)
# Lista de ejemplo
producto_total = [2, 3, 4, 5, 6]
# Llamamos a la función
resultado = ejercicio_22(producto_total)
# Mostramos el resultado
print(f"Resultado del ejercicio 22: {resultado}")  #[720]


"""23. Concatena una lista de palabras. Usa la función reduce()."""
from functools import reduce
def ejercicio_23(lista_palabras):
    # reduce aplica la función lambda concatenando las palabras
    return reduce(lambda x, y: x + y, lista_palabras)
# Lista de ejemplo
lista_palabras_concatenadas = ["Hola,", " ", "soy ", "tu ", "tía"]
# Llamamos a la función
resultado = ejercicio_23(lista_palabras_concatenadas)
# Mostramos el resultado
print(f"Resultado del ejercicio 23: {resultado}") #[Hola, soy tu tía]


"""24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()."""
from functools import reduce
def ejercicio_24(diferencia_total):
    # reduce aplica la función lambda restando el producto de los elementos
    return reduce(lambda x, y: x - y, diferencia_total)
# Lista de ejemplo
diferencia_total = [2, 3, 4, 5, 6]
# Llamamos a la función
resultado = ejercicio_24(diferencia_total)
# Mostramos el resultado
print(f"Resultado del ejercicio 24: {resultado}")  #[-16]


"""25. Crea una función que cuente el número de caracteres en una cadena de texto dada."""
def ejercicio_25(cadena):
    # len() devuelve el número de caracteres de la cadena
    return len(cadena)
# Cadena de ejemplo
cadena = "La casa está fría"
# Llamamos a la función
resultado = ejercicio_25(cadena)
# Mostramos el resultado
print(f"Resultado del ejercicio 25: {resultado}")  #[17]


"""26. Crea una función lambda que calcule el resto de la división entre dos números dados."""
def ejercicio_26():
    # Función lambda que recibe dos números y devuelve el resto
    resto_division = lambda x, y: x % y
       # Llamamos a la función lambda
    resultado = resto_division(8, 3)
    # Mostramos el resultado
    print(f"Resultado del ejercicio 26: {resultado}")  # [2]
# Llamamos a la función
ejercicio_26()


"""27. Crea una función que calcule el promedio de una lista de números."""
def ejercicio_27(lista_promedio):
    # Calcula el promedio usando sum() y len()
    promedio = sum(lista_promedio) / len(lista_promedio)
    return promedio
# Lista de ejemplo
números = [8, 5, 9, 15, 3]
# Llamamos a la función
resultado = ejercicio_27(números)
# Mostramos el resultado
print(f"Resultado del ejercicio 27: {resultado}") # [8.0]


"""28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada."""
def ejercicio_28(lista):
    vistos = set()  # Guardamos los elementos que ya hemos visto
    for elemento in lista:
        if elemento in vistos:
            return elemento  # Devolvemos el primer duplicado
        vistos.add(elemento)
    return None  # Si no hay duplicados
# Lista de ejemplo
lista_duplicados = ["Hola", "HOLa", "Hola", 2, 5, 2, 7]
# Llamamos a la función
resultado = ejercicio_28(lista_duplicados)
# Mostramos el resultado
print(f"Resultado del ejercicio 28: {resultado}")  # Hola


"""29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
carácter '#', excepto los últimos cuatro."""
def ejercicio_29(valor):
    # Convertimos el valor a cadena
    texto = str(valor)
    # Calculamos la parte enmascarada
    enmascarado = '#' * max(len(texto) - 4, 0)  # Evita negativos si tiene menos de 4 caracteres
    # Concatenamos los últimos 4 caracteres sin enmascarar
    resultado = enmascarado + texto[-4:]
    return resultado
# Ejemplo
números_confidenciales = 1234567890
print(f"Resultado del ejercicio 29 (número): {ejercicio_29(números_confidenciales)}")      # ######7890


"""30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
pero en diferente orden."""
from collections import Counter
def ejercicio_30():
    def son_anagramas(palabra1, palabra2):
        # Eliminamos espacios y pasamos a minúsculas
        palabra1 = palabra1.replace(" ", "").lower()
        palabra2 = palabra2.replace(" ", "").lower()
        # Comparamos la frecuencia de cada letra
        return Counter(palabra1) == Counter(palabra2)
    # Ejemplo
    resultado = son_anagramas("Cara", "arca")
    print(f"Resultado del ejercicio 30: {resultado}")  # True
# Llamamos a la función
ejercicio_30()


"""31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción."""
def ejercicio_31():
    class NombreNoEncontrado(Exception): pass
    try:
        # Pedimos la lista de nombres y limpiamos espacios, pasamos a minúsculas
        lista_nombres = [n.strip().lower() for n in input("Introduce una lista de nombres separados por comas: ").split(",") if n.strip()]
        if not lista_nombres:
            raise ValueError("La lista está vacía. Debes introducir al menos un nombre.")
        # Pedimos el nombre a buscar
        nombre_a_buscar = input("Introduce el nombre que quieres buscar: ").strip().lower()
        # Comprobamos si el nombre está en la lista
        if nombre_a_buscar in lista_nombres:
            print(f"✅ El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
        else:
            raise NombreNoEncontrado(f"❌ El nombre '{nombre_a_buscar}' no se encuentra en la lista.")
    except (NombreNoEncontrado, ValueError) as e:
        print(f"Resultado ejercicio 31: {e}")
# Ejecutamos el ejercicio 31
print("Resultado del ejercicio 31:")
ejercicio_31()


"""32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí."""
def ejercicio_32():
    # Lista de empleados: diccionarios con nombre y puesto
    lista_empleados = [
        {"nombre": "Juan Ruiz", "puesto": "Dependiente"},
        {"nombre": "Amancio Ortega", "puesto": "Contable"},
        {"nombre": "Ana Dominguez", "puesto": "Gerente"}
    ]
    # Excepción personalizada
    class NombreNoEncontrado(Exception): pass
    try:
        # Pedimos nombre completo al usuario
        nombre_a_buscar = input("Introduce el nombre completo: ").strip().lower()
        # Buscamos el nombre en la lista de empleados
        encontrado = False
        for empleado in lista_empleados:
            if empleado["nombre"].lower() == nombre_a_buscar:
                print(f"✅ {empleado['nombre']} trabaja aquí como {empleado['puesto']}.")
                encontrado = True
                break
        # Si no se encontró el empleado, lanzamos excepción
        if not encontrado:
            raise NombreNoEncontrado(f"❌ El nombre '{nombre_a_buscar}' no se encuentra en la lista.")
    
    except NombreNoEncontrado as e:
        print(f"Resultado del ejercicio 32: {e}")
# Ejecutamos el ejercicio 32
print("Resultado del ejercicio 32:")
ejercicio_32()


"""33. Crea una función lambda que sume elementos correspondientes de dos listas dadas."""
def ejercicio_33(lista1, lista2):
    # Usamos map con lambda para sumar elemento a elemento
    return list(map(lambda x, y: x + y, lista1, lista2))
# Listas de ejemplo
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
# Llamamos a la función
resultado = ejercicio_33(x, y)
# Mostramos el resultado
print(f"Resultado del ejercicio 33: {resultado}")  # [6, 8, 10, 12]

""""34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol.
Código a seguir:
    1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
    2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
    3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
    6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las longitudes de las
    mismas.
Caso de uso:
    1. Crear un árbol.
    2. Hacer crecer el tronco del árbol una unidad.
    3. Añadir una nueva rama al árbol.
    4. Hacer crecer todas las ramas del árbol una unidad.
    5. Añadir dos nuevas ramas al árbol.
    6. Retirar la rama situada en la posición 2.
    7. Obtener información sobre el árbol."""
class Arbol:
    def __init__(self):
        """Inicializa el árbol con tronco de longitud 1 y lista vacía de ramas"""
        self.tronco = 1
        self.ramas = []
    def crecer_tronco(self):
        """Aumenta la longitud del tronco en 1"""
        self.tronco += 1
    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1"""
        self.ramas.append(1)
    def crecer_ramas(self):
        """Aumenta en 1 la longitud de todas las ramas existentes"""
        self.ramas = [rama + 1 for rama in self.ramas]
    def quitar_rama(self, posicion):
        """Elimina una rama en la posición indicada (si existe)"""
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print(f"⚠️ No existe una rama en la posición {posicion}.")
    def info_arbol(self):
        """Devuelve información sobre el tronco, número de ramas y longitudes"""
        return {
            "tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }
# =========================
# Caso de uso
# =========================
arbol = Arbol()                 # 1. Crear un árbol
arbol.crecer_tronco()           # 2. Hacer crecer el tronco una unidad
arbol.nueva_rama()              # 3. Añadir una nueva rama
arbol.crecer_ramas()            # 4. Hacer crecer todas las ramas una unidad
arbol.nueva_rama()              # 5. Añadir dos nuevas ramas
arbol.nueva_rama()
arbol.quitar_rama(2)            # 6. Retirar la rama situada en la posición 2 (índice 2)
info = arbol.info_arbol()       # 7. Obtener información sobre el árbol
print(f"Resultado del ejercicio 34: {info}")


"""35. N/A"""
print ("Resultado del ejercicio 35: ❌ No existe en proyecto, salta del ejercicio 34 al 36")


"""36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo.
Código a seguir:
    1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False .
    2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no
    poder hacerse.
    3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
    Lanzará un error en caso de no poder hacerse.
    4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
    1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    2. Agregar 20 unidades de saldo de "Bob".
    3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
    4. Retirar 50 unidades de saldo a "Alicia"."""
def ejercicio_36():
    class UsuarioBanco:
        def __init__(self, nombre, saldo, cuenta_corriente=True):
            self.nombre = nombre
            self.saldo = saldo
            self.cuenta_corriente = cuenta_corriente

        def retirar_dinero(self, cantidad):
            """Resta dinero del saldo si es posible"""
            if not self.cuenta_corriente:
                raise Exception(f"{self.nombre} no tiene cuenta corriente activa.")
            if cantidad <= 0:
                raise ValueError("La cantidad a retirar debe ser positiva.")
            if cantidad > self.saldo:
                raise Exception(f"Fondos insuficientes en la cuenta de {self.nombre}.")
            self.saldo -= cantidad
            print(f"{self.nombre} retiró {cantidad}. Saldo actual: {self.saldo}")

        def transferir_dinero(self, otro_usuario, cantidad):
            """Transfiere dinero a otro usuario si es posible"""
            if cantidad <= 0:
                raise ValueError("La cantidad a transferir debe ser positiva.")
            if cantidad > self.saldo:
                raise Exception(f"{self.nombre} no tiene fondos suficientes para transferir.")
            self.saldo -= cantidad
            otro_usuario.saldo += cantidad
            print(f"{self.nombre} envió {cantidad} a {otro_usuario.nombre}.")
            print(f"Saldo actual: {self.nombre}: {self.saldo}, {otro_usuario.nombre}: {otro_usuario.saldo}")

        def agregar_dinero(self, cantidad):
            """Agrega dinero al saldo"""
            if cantidad <= 0:
                raise ValueError("La cantidad a agregar debe ser positiva.")
            self.saldo += cantidad
            print(f"{self.nombre} agregó {cantidad}. Saldo actual: {self.saldo}")

        def __str__(self):
            return f"{self.nombre} | Saldo: {self.saldo} | Cuenta corriente: {self.cuenta_corriente}"

    # ===== Caso de uso =====
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)

    print("Estado inicial:")
    print(alicia)
    print(bob)
    print("------------------------")

    # 1. Bob agrega 20 unidades de saldo
    bob.agregar_dinero(20)
    print("------------------------")

    # 2. Transferencia de 80 desde Bob a Alicia con manejo de error
    try:
        bob.transferir_dinero(alicia, 80)
    except Exception as e:
        print(f"Error en la transferencia: {e}")
    print("------------------------")

    # 3. Alicia retira 50
    try:
        alicia.retirar_dinero(50)
    except Exception as e:
        print(f"Error en el retiro: {e}")
    print("------------------------")

    # Estado final
    print("Estado final:")
    print(alicia)
    print(bob)

# ===== Ejecutamos el ejercicio =====
print("Resultado del ejercicio 36:")
ejercicio_36()


"""37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, 
reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto.
Código a seguir:
    1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene
    que devolver un diccionario.
    2. Crear una función reemplazar_palabras para remplazar una palabra_original del texto por una palabra_nueva . Tiene
    que devolver el texto con el remplazo de palabras.
    3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra
    eliminada.
    4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un
    número de argumentos variable según la opción indicada.
Caso de uso:
    Comprueba el funcionamiento completo de la función procesar_texto."""
import re

def ejercicio_37():
    # Función para contar palabras
    def contar_palabras(texto):
        # Eliminamos puntuación y pasamos a minúsculas
        palabras = re.findall(r'\b\w+\b', texto.lower())
        contador = {}
        for palabra in palabras:
            contador[palabra] = contador.get(palabra, 0) + 1
        return contador

    # Función para reemplazar palabras exactas
    def reemplazar_palabras(texto, palabra_original, palabra_nueva):
        return re.sub(rf'\b{re.escape(palabra_original)}\b', palabra_nueva, texto)

    # Función para eliminar palabras exactas
    def eliminar_palabra(texto, palabra_a_eliminar):
        return re.sub(rf'\b{re.escape(palabra_a_eliminar)}\b', '', texto).replace("  ", " ").strip()

    # Función principal
    def procesar_texto(texto, opcion, *args):
        if opcion == "contar":
            return contar_palabras(texto)
        elif opcion == "reemplazar":
            if len(args) != 2:
                raise ValueError("Se requieren dos argumentos: palabra_original y palabra_nueva")
            return reemplazar_palabras(texto, args[0], args[1])
        elif opcion == "eliminar":
            if len(args) != 1:
                raise ValueError("Se requiere un argumento: palabra_a_eliminar")
            return eliminar_palabra(texto, args[0])
        else:
            raise ValueError("Opción no válida. Elige entre 'contar', 'reemplazar', 'eliminar'.")

    texto = "Hola, Hola estoy aquí desde que llegué aquí"

    # Contar palabras
    print("Resultado del ejercicio 37 (contar palabras):")
    print(procesar_texto(texto, "contar"))

    # Reemplazar "Hola" por "Hi"
    print("\nResultado del ejercicio 37 (reemplazar 'Hola' por 'Hi'):")
    print(procesar_texto(texto, "reemplazar", "Hola", "Hi"))

    # Eliminar "aquí"
    print("\nResultado del ejercicio 37 (eliminar 'aquí'):")
    print(procesar_texto(texto, "eliminar", "aquí"))

ejercicio_37()


"""38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario."""
def ejercicio_38():
    try:
        entrada = input("Introduce la hora en formato 24h (HH:MM): ").strip()
        # Separamos horas y minutos
        partes = entrada.split(":")
        if len(partes) != 2:
            raise ValueError("Formato incorrecto. Usa HH:MM.")
        hora = int(partes[0])
        minutos = int(partes[1])
        
        if not (0 <= hora <= 23 and 0 <= minutos <= 59):
            raise ValueError("Hora o minutos fuera de rango.")
                # Convertimos todo a minutos desde medianoche para comparar fácilmente
        total_minutos = hora * 60 + minutos
                # Definimos rangos: mañana 6:00-11:59, tarde 12:00-19:59, noche 20:00-5:59
        if 6*60 <= total_minutos < 12*60:
            periodo = "por la mañana (día)"
        elif 12*60 <= total_minutos < 20*60:
            periodo = "por la tarde"
        else:
            periodo = "de noche"        
        print(f"Resultado del ejercicio 38: Son las {hora:02d}:{minutos:02d}, es {periodo}.")
    except ValueError as e:
        print(f"Error: {e}")
# Llamamos a la función
ejercicio_38()


"""39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
- 0 - 69 insuficiente
- 70 - 79 bien
- 80 - 89 muy bien
- 90 - 100 excelente"""
def ejercicio_39():
    try:
        nota_str = input("Introduce la calificación del alumno (0-100): ").strip()
        nota = float(nota_str)
        if nota < 0 or nota > 100:
            raise ValueError("La calificación debe estar entre 0 y 100.")
        # Redondeamos la calificación a entero
        nota_entero = int(round(nota))
        # Determinar calificación en texto
        if 0 <= nota_entero <= 69:
            calificacion_texto = "Insuficiente"
        elif 70 <= nota_entero <= 79:
            calificacion_texto = "Bien"
        elif 80 <= nota_entero <= 89:
            calificacion_texto = "Muy bien"
        else:  # 90 - 100
            calificacion_texto = "Excelente"
        print(f"Resultado del ejercicio 39: La calificación {nota_entero} corresponde a '{calificacion_texto}'")
    except ValueError as e:
        print(f"Error: {e}")
# Llamamos a la función
ejercicio_39()


"""40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o 
"triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura)."""
import math

def ejercicio_40(figura, datos):
    """
    Calcula el área de una figura geométrica.
        Parámetros:
    - figura: "rectangulo", "circulo" o "triangulo"
    - datos: tupla con los datos necesarios para calcular el área
      rectangulo -> (base, altura)
      circulo    -> (radio,)
      triangulo  -> (base, altura)
    """
    figura = figura.lower() 
    if figura == "rectangulo":
        if len(datos) != 2:
            raise ValueError("Rectángulo requiere base y altura")
        base, altura = datos
        area = base * altura
    elif figura == "circulo":
        if len(datos) != 1:
            raise ValueError("Círculo requiere radio")
        radio = datos[0]
        area = math.pi * radio ** 2
    elif figura == "triangulo":
        if len(datos) != 2:
            raise ValueError("Triángulo requiere base y altura")
        base, altura = datos
        area = (base * altura) / 2
    else:
        raise ValueError("Figura no válida. Debe ser 'rectangulo', 'circulo' o 'triangulo'.")
    return round(area, 2)
# Ejemplos de uso
print(f"Resultado del ejercicio 40 (rectángulo 5x3): {ejercicio_40('rectangulo', (5, 3))}")
print(f"Resultado del ejercicio 40 (círculo radio 4): {ejercicio_40('circulo', (4,))}")
print(f"Resultado del ejercicio 40 (triángulo 6x2): {ejercicio_40('triangulo', (6, 2))}")


"""41. En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente:
    1. Solicita al usuario que ingrese el precio original de un artículo.
    2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
    3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
    4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
    a cero). Por ejemplo, descuento de 15€. 
    5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
    6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
    programa de Python."""
def ejercicio_41():
    try:
        # 1️⃣ Precio original
        precio_str = input("Introduce el precio original del artículo (€): ").strip()
        precio = float(precio_str)
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")

        # 2️⃣ Preguntar por cupón
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        # 3️⃣ Aplicar descuento si hay cupón
        if tiene_cupon == "sí" or tiene_cupon == "si":
            cupon_str = input("Introduce el valor del cupón (€): ").strip()
            descuento = float(cupon_str)
            if descuento <= 0:
                print("El cupón no es válido. No se aplicará descuento.")
                descuento = 0
        else:
            descuento = 0

        # 4️⃣ Calcular precio final
        precio_final = max(precio - descuento, 0)  # Evita precio negativo
        print(f"Resultado del ejercicio 41: El precio final de la compra es {precio_final:.2f}€")

    except ValueError as e:
        print(f"⚠️ Error: {e}")

# Llamamos a la función
ejercicio_41()