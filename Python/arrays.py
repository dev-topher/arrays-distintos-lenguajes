lista = [1, 2, 3, 4, 5] # Lista de ejemplo
dato_a_buscar = 1 # Posición que quiero buscar
dato = lista[dato_a_buscar] # Posición del dato que está en la lista []

print(dato) # Imprime el dato

lista.append(6)  # Agregar el número 6 al final de la lista

otra_lista = [7, 8, 9]
lista.extend(otra_lista)  # Extender mi_lista con otra_lista

mi_lista.insert(2, 99)  # Insertar 99 en la posición 2
mi_lista.remove(3)  # Eliminar el valor 3 de la lista
del mi_lista[1]  # Eliminar el elemento en el índice 1

longitud = len(mi_lista)  # Obtener la longitud de la lista

mi_lista.sort()  # Ordenar la lista en orden ascendente
mi_lista.reverse()  # Invertir el orden de la lista

### diccionarios ###
# Define el diccionario y la clave que vas a buscar
diccionario = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}
valor_a_buscar = diccionario["key_1"] 

print(valor_a_buscar) # Imprime el valor del diccionario asociado a la llave buscada

### iterador ###

pets = ["perro", "gato", "pájaro"]

for pet in pets :
    print(pet)

### algoritmo de busqueda binaria ###

# Ejemplo de uso para listas:
# Define el diccionario y la clave que vas a buscar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
objetivo = 7

# Ejecuta la función de búsqueda
resultado = busqueda_binaria(lista, objetivo)

# Ejecuta la función de búsqueda
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2  # Encontrar el índice medio

        if lista[medio] == objetivo:
            return medio  # Se encontró el objetivo, devolver su índice
        elif lista[medio] < objetivo:
            inicio = medio + 1  # El objetivo está en la mitad derecha
        else:
            fin = medio - 1  # El objetivo está en la mitad izquierda

    return -1  # El objetivo no se encontró en la lista

# Imprime el resultado
if resultado != -1:
    print(f"El objetivo {objetivo} se encuentra en el índice {resultado}.")
else:
    print(f"El objetivo {objetivo} no se encuentra en la lista.")


# Ejemplo de uso para diccionarios:

# Ejemplo de uso:
# Define el diccionario y la clave que vas a buscar
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}
clave_buscar = "clave2"

# Ejecuta la función de búsqueda
resultado = buscar_en_diccionario(mi_diccionario, clave_buscar)

def buscar_en_diccionario(diccionario, clave_objetivo):
    if clave_objetivo in diccionario:
        return diccionario[clave_objetivo]
    else:
        return None  # La clave no se encontró en el diccionario

# Imprime el resultado
if resultado is not None:
    print(f"El valor asociado a la clave '{clave_buscar}' es '{resultado}'.")
else:
    print(f"La clave '{clave_buscar}' no se encontró en el diccionario.")
