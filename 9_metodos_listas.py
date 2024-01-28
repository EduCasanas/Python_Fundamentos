#CONTENIDO
"""
1) Crear una lista (list) => list(["cadena", int, float, bool])
2) Longitud de una lista (len) => len(lista)
3) Agregar elementos al final de la lista (append) => lista.append("palabra")
4) Insertar un elemento dentro de una lista (insert) => lista.insert(posicion_dentro_de_la_lista, "Lo que queremos agregar:palabra, int, float,etc..")
5) Agregar varios elementos a una lista (extend) => lista.extend(["cadena", bool, int])
6) Eliminar un elemento de la lista por indice (pop) => lista.pop(indice de elemento a eliminar)
7) Elimina un elemento de la lista segun el elemento (remove) => lista.remove(elemento de la lista)
8) Elimina todos los elementos de la lista (clear) => lista.clear()
9) Ordena una lista de forma ascendente (sort) => lista.sort() | orden descendente: lista.sort(reverse=True) 
10) Invierte los elementos de una lista (reverse) => lista.reverse()
11) Posicion de un elemento de una lista (index) => lista.index(elemento en la lista)
"""
# 1) Crear una lista (list)
nueva_lista = list(["hola", 12, 15.7, False])
print(nueva_lista) # ['hola', 12, 15.7, False]

# 2) Longitud de una lista (len)
nueva_lista_2 = list(["hola", 12, 15.7, False])
longitud_lista = len(nueva_lista_2)
print(longitud_lista) # 4

# 3) Agregar elementos a una lista (append)
nueva_lista_3 = ["hola", 12, 15.7, False]
nueva_lista_3.append("educa")
print(nueva_lista_3) # ['hola', 12, 15.7, False, 'educa']

# 4) Insertar un elemento dentro de una lista (insert)
nueva_lista_4 = ["hola", 12, 15.7, False]
nueva_lista_4.insert(1, "educa")
print(nueva_lista_4) # ['hola', 'educa', 12, 15.7, False]

# 5) Agregar varios elementos a una lista (extend)
nueva_lista_5 = ["hola", 12, 15.7, False]
nueva_lista_5.extend(["educa", True, 15.3])
print(nueva_lista_5) # ['hola', 12, 15.7, False, 'educa', True, 15.3]

# 6) Eliminar un elemento de la lista (pop)
nueva_lista_6 = ["hola", 12, 15.7, False]
nueva_lista_6.pop(0) # Elimina el ultimo elemento al no especificarle
print(nueva_lista_6) # [12, 15.7, False]

# tip: Elimina el ultimo elemento al no especificarle un indice 'lista.pop()'
# tip: Elimina el ultimo elemento de la lista con '-1'

nueva_lista_6.pop(-1)
print(nueva_lista_6) # [12, 15.7]

# 7) Elimina un elemento de la lista segun el elemento (remove)
nueva_lista_7 = ["hola", 12, 15.7, False]
nueva_lista_7.remove(15.7)
print(nueva_lista_7) # ['hola', 12, False]

# 8) Elimina todos los elementos de la lista (clear)
nueva_lista_8 = ["hola", 12, 15.7, False]
nueva_lista_8.clear()
print(nueva_lista_8) # []

# 9) Ordena los elementos de una lista de forma ascendente (sort)
lista_a_ordenar = [2, 7, 9, 1, 0, 99]
lista_a_ordenar.sort()
print(lista_a_ordenar) # [0, 1, 2, 7, 9, 99]

# Ordena la lista en forma ascendente y luego invierte los valores'ordena descendentemente' 
lista_a_ordenar.sort(reverse = True)
print(lista_a_ordenar) # [99, 9, 7, 2, 1, 0]

# Tambien puede ordenar una lista de caracteres
lista_a_ordenar2 = ['z', 'b', 'a', 'x', 'y', 'c']
lista_a_ordenar2.sort()
print(lista_a_ordenar2) # ['a', 'b', 'c', 'x', 'y', 'z']

# Tambien ordena palabras tomando la primera letra de la palabra
lista_a_ordenar3 = ["zorro", "yegua", "avion", "dedo"]
lista_a_ordenar3.sort()
print(lista_a_ordenar3) # ['avion', 'dedo', 'yegua', 'zorro']

# 10) Invierte los elementos de una lista (reverse)
nueva_lista_9 = ["hola", 12, 15.7, False]
nueva_lista_9.reverse()
print(nueva_lista_9) # [False, 15.7, 12, 'hola']

# 11) Posicion de un elemento de una lista (index)
nueva_lista_10 = ["hola", 12, 15.7, False, "educa"]
posicion_lista = nueva_lista_10.index(False)
print(posicion_lista) # 3 