lista = [1, 2, 3, 4, 5] # Lista de ejemplo
dato_a_buscar = 1 # Posición que quiero buscar
dato = lista[dato_a_buscar] # Posición del dato que está en la lista []

puts lista.inspect # Imprime el array completo

puts dato # Imprime el dato

lista.push(6)  # Agregar el número 6 al final de la lista

otra_lista = [7, 8, 9]
lista.concat(otra_lista)  # Extender mi_lista con otra_lista
lista += otra_lista # Cumple la misma función que el concat

lista.unshift(0) # Agrega 0 al principio del array
lista.shift # Elimina y devuelve 0
puts lista.length # Imprime el tamaño de la lista
puts lista.include?(2) # Devuelve true

### diccionarios ###
# Define el diccionario (o también llamado hash en ruby) y la clave que vas a buscar
diccionario = { 
    "key_1" => "value_1", 
    "key_2" => "value_2", 
    "key_3" => "value_3"
}

puts diccionario["key_1"]  # Imprimirá "value_1"

### iteradores ###

pets = ["perro", "gato", "pájaro"]

pets.each do |pet|
    puts pet
end

### algoritmo de busqueda binaria ###

# Ejemplo de uso para listas:
# Define el diccionario y la clave que vas a buscar

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17]
elemento_buscado = 7

# Ejecuta la función de búsqueda
resultado = busqueda_binaria(lista, elemento_buscado)

# Ejecuta la función de búsqueda
def busqueda_binaria(lista, elemento)
    izquierda = 0
    derecha = lista.length - 1
  
    while izquierda <= derecha
      medio = (izquierda + derecha) / 2
  
      if lista[medio] == elemento
        return medio  # El elemento ha sido encontrado, devuelve su índice.
      elsif lista[medio] < elemento
        izquierda = medio + 1
      else
        derecha = medio - 1
      end
    end
  
    return -1  # El elemento no ha sido encontrado en la lista.
end
  
# Imprime el resultado
  
if resultado != -1
    puts "El elemento #{elemento_buscado} se encuentra en el índice #{resultado}."
else
    puts "El elemento #{elemento_buscado} no se encuentra en la lista."
end
  
# Ejemplo de uso para diccionarios:

# Ejemplo de uso:
# Define el diccionario/hash y la clave que vas a buscar

mi_hash = {
  "nombre" => "Juan",
  "edad" => 30,
  "ciudad" => "Ejemploville"
}

clave_a_buscar = "edad"

# Ejecuta la función de búsqueda
resultado = buscar_en_hash(mi_hash, clave_a_buscar)

def buscar_en_hash(hash, clave_buscar)
    if hash.key?(clave_buscar)
        return hash[clave_buscar]
    else
        return nil  # La clave no se encontró en el hash.
    end
end
  
# Imprime el resultado  
if resultado
    puts "El valor asociado a la clave '#{clave_a_buscar}' es '#{resultado}'."
else
    puts "La clave '#{clave_a_buscar}' no se encontró en el hash."
end
  