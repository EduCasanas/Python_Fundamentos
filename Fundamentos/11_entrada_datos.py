#CONTENIDO
"""
1) Pedir datos al usuario (input) => input("Texto a mostrarse en consola")
"""
# 1) Pedir datos al usuario (input)
name = input("Escribe tu nombre: ") # educa
print(name) # educa

# Tip: Si escribo un numero (50) por consola, este sera de tipo string '50'
edad = input("dame tu edad: ") # 30
print(edad) # 30
print(type(edad)) # <class 'str'>

# Casteo o conversion de un numero tipo string a numero entero
edad2 = input("dame tu edad2: ") # 50
edad_to_int = int(edad2)
print(type(edad_to_int)) # <class 'int'>

# Otra forma de casteo:
edad2 = int(input("dame tu edad2: ")) # 50
print(edad2*2) # 100
