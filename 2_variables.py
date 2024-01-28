#CONTENIDO
"""
1) Variables
2) Concatenacion (+)
    2.1) Interpolacion(agregar variables dentro de strings => f"Hola {variable}")
    2.2) Eliminar variables
    2.3) Operadores de pertenencia
3) Recomendacion de escritura de variables => snake_case    
"""
# 1) Variables
a = 40.2
b = 40
c = a + b
print(c) # 80.2
# ---------------------
name = "educa"
print(name) # educa
# ---------------------
numero = 10
numero += 1 # numero = 10 + 1 tambien se puede decrementar con "-="
print(numero)

# 2) Concatenacion
nombre = "Educa"
bienvenida = "Buenos dias, "
saludo = bienvenida + nombre
print(saludo) # Buenos dias, Educa

# 2.1) Interpolacion
saludo2 = f"{bienvenida}{nombre}. Como estas?"
print(saludo2) # Buenos dias, Educa. Como estas?

# 2.2) Eliminar variables
del saludo2

# 2.3) Operadores de pertenencia
print("Educa" in saludo) # True: 'Educa' si esta en la variable saludo   
print("Buenos" not in saludo) # False: la instruccion dice 'Buenos' no esta en la variable saludo? es falso ya que si esta.

# 3) Recomendacion de escritura de variables   
variable_usando_snake_case = "python"
