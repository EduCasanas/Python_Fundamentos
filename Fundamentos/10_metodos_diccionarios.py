#CONTENIDO
"""
1) Devuelve las claves del diccionario (keys) => diccionario.keys()
2) Devuelve el valor de una clave (get) => diccionario.get("key del diccionario")
3) Elimina todos los elementos del diccionario (clear) => diccionario.clear()
4) Elimina un elemento del diccionario (pop) => diccionario.pop("key del diccionario")
5) Convierte el diccionario a una lista de elementos (items) => diccionario.items()
"""
# 1) Devuelve las claves del diccionario (keys) 
diccionario = {
    "name" : "educa",
    "age" : 30,
    "gender" : "Male"
}
claves = diccionario.keys()
print(claves) # dict_keys(['name', 'age', 'gender'])

# 2) Devuelve el valor de una clave (get) 
diccionario2 = {
    "name" : "educa",
    "age" : 30,
    "gender" : "Male"
}
value_of_key = diccionario2.get("gender")
print(value_of_key) # Male

# Tambien puedo acceder al diccionario asi:
value_of_key2 = diccionario2["name"]
print(value_of_key2) # educa

# La diferencia entre 'get' y '["key"]' es que el segundo al buscar algo que no esta 
# en el diccionario me salta una excepcion mientras que el 'get' me dice 'None'

# 3) Elimina todos los elementos del diccionario (clear) 
diccionario3 = {
    "name" : "educa",
    "age" : 30,
    "gender" : "Male"
}
diccionario3.clear()
print(diccionario3) # {}

# 4) Elimina un elemento del diccionario (pop) 
diccionario4 = {
    "name" : "educa",
    "age" : 30,
    "gender" : "Male"
}
diccionario4.pop("name")
print(diccionario4) # {'age': 30, 'gender': 'Male'}

# 5) Itera el diccionario (items)
diccionario5 = {
    "name" : "educa",
    "age" : 30,
    "gender" : "Male"
}
iterar_diccionario = diccionario5.items()
print(iterar_diccionario) # dict_items([('name', 'educa'), ('age', 30), ('gender', 'Male')])
