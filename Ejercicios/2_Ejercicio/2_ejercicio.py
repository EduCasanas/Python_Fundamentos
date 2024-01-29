# Ejercicio 2
# Se sabe que una persona promedio pronuncia 2 palabras por segundo.

# A) Pedirle al usuario que diga cualquier texto real y:
# - calcular cuanto tardaria en decir esa frase.
# - cuantas palabras dijo?

# B) Si se tarda mas de 1 minuto:
# - decirle 'detente! has hablado mas de 1 minuto'

# C) El mas rapido en hablar lo hace un 30% mas que el promedio:
# - cuanto tardaria esta persona en decirlo? 

# ----SOLUCION------
palabras_por_segundo_promedio = (2 / 1) # 2 palabras / 1 segundo

# A) Pedirle al usuario que diga cualquier texto real y:
# - calcular cuanto tardaria en decir esa frase.
texto_por_consola = input("Ingrese un texto: ")
texto_a_lista = texto_por_consola.split(" ") # El split automaticamente crea una lista con los elementos
cantidad_palabras_ingresadas = len(texto_a_lista)
tiempo_de_palabras_ingresadas_promedio = cantidad_palabras_ingresadas * ( 1 / palabras_por_segundo_promedio) # Al multiplicar * (1 / palabras por segundo) se simplifica palabras y solo quedan segundos.
# Tambien podia simplemente en vez de multiplicar(* (1/palabras por segundo promedio)) directamente dividir 'palabras ingresadas' con 'palabras por segundo promedio'
print(f"Una persona promedio al pronunciar: {texto_a_lista} tardara {tiempo_de_palabras_ingresadas_promedio} segundos")
# - cuantas palabras dijo?
print(f"La persona pronuncio: {cantidad_palabras_ingresadas} palabras.")

# B) Si se tarda mas de 1 minuto(60 segundos):
# - decirle 'detente! has hablado mas de 1 minuto'
if tiempo_de_palabras_ingresadas_promedio > 60:
    print("Detente! has hablado mas de 1 minuto")

# C) El mas rapido en hablar lo hace un 30% mas que el promedio:
# - cuanto tardaria esta persona en decirlo?
palabras_por_segundo_rapido = palabras_por_segundo_promedio + 0.6
tiempo_mas_rapido = cantidad_palabras_ingresadas / palabras_por_segundo_rapido
print("La persona mas rapida pronuncia {} en {:.2f} segundos.".format(texto_a_lista, tiempo_mas_rapido))
