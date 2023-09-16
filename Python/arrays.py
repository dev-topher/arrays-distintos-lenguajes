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

diccionario = {"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}

valor_a_buscar = diccionario["key_1"] 

print(valor_a_buscar) # Imprime el valor del diccionario asociado a la llave buscada