#CONTENIDO
"""
1) Listas []
2) Tuplas ()
3) Sets o Conjuntos {}
4) Diccionarios {key: value}    
"""
# 1) Lista
lista = ["edu", True, 1.88]
print(lista)

# 2) Tupla (inmutables, es decir que no se puede modificar sus elementos pero 
# si reasiganar al valor de toda la tupla)
tupla = ("edu", True, 1.88)
print(tupla[2])
# si intento cambiar el valor me sale error porque no soportan la asignacion de items.
# tupla[0] = "jorge"
# print(tupla)
tupla = (5)
print(tupla)

# 3) Set o Conjunto(elementos desordenados) Al igual que las tuplas 
# son inmutables por elementos pero si puedo cambiar el valor de todo el conjunto.
# Tambien NO puedo acceder a sus elementos por indices.
# Si tengo elementos repetidos, no los va a mostrar.

conjunto = {"hola", 13, False, 15.2}
conjunto = {"hola"}
print(conjunto)
# ------------------------------------------------
conjunto2 = {"hola", 13, False, 15.2, 13, "hola"}
print(conjunto2)
# print(conjunto2[0]) => ERROR

# 4) Diccionarios
diccionario = {
    'name' : 'educa',
    'canal' : 'educasdev',
    'edad' : 30,
    'es_programador' : True
}
print(diccionario['edad'])