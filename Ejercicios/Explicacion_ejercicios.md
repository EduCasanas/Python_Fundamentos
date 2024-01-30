# Ejercicios en Python
## Ejercicio 1

A) Diferencia porcentual entre el curso actual y:
   - el mas rapido de otros cursos
   - el mas lento de otros cursos
   - el promedio de otros cursos

 B) Porcentaje de material inservible que se reduce en:
   - el promedio de los cursos
   - el curso actual(este curso)

 C) Ver 10 horas de este curso a cuantas horas de otros cursos equivale? y alreves?

![Ejercicio1](https://github.com/EduCasanas/Python_Fundamentos/blob/main/Ejercicios/1_Ejercicio/Ejercicio1_python.png)

---

## Solucion

#### A) Diferencia porcentual entre el curso actual y:

- el mas rapido de otros cursos:

![EjercicioA.1](https://github.com/EduCasanas/Python_Fundamentos/blob/main/Ejercicios/1_Ejercicio/Ejercicio1_A.1.png)

```Python
tiempo_curso_actual_horas = 1.5
tiempo_curso_minimo_horas = 2.5
tiempo_curso_maximo_horas = 7
tiempo_curso_promedio_horas = 4

diferencia_porcentual_contra_rapido = ( (tiempo_curso_minimo_horas - tiempo_curso_actual_horas) / tiempo_curso_minimo_horas ) * 100
print(f"El curso actual dura {diferencia_porcentual_contra_rapido}% menos que el curso mas rapido.")

# El curso actual dura 40.0% menos que el curso mas rapido.
```

- el mas lento de otros cursos:

![EjercicioA.2](https://github.com/EduCasanas/Python_Fundamentos/blob/main/Ejercicios/1_Ejercicio/Ejercicio1_A.2.png)

```Python
diferencia_porcentual_contra_lento = ( (tiempo_curso_maximo_horas - tiempo_curso_actual_horas) / tiempo_curso_maximo_horas ) * 100
print("El curso actual dura {:.2f}% menos que el curso mas lento.".format(diferencia_porcentual_contra_lento))

# El curso actual dura 78.57% menos que el curso mas lento.
```

- el promedio de otros cursos:

![EjercicioA.3](https://github.com/EduCasanas/Python_Fundamentos/blob/main/Ejercicios/1_Ejercicio/Ejercicio1_A.3.png)

```Python
diferencia_porcentual_contra_promedio = ( (tiempo_curso_promedio_horas - tiempo_curso_actual_horas) / tiempo_curso_promedio_horas ) * 100
print(f"El curso actual dura {diferencia_porcentual_contra_promedio}% menos que el curso promedio.")

# El curso actual dura 62.5% menos que el curso promedio.
```

#### B) Porcentaje de material inservible que se reduce en:

- el promedio de los cursos:

```Python
# Haciendo la misma analogia de los ejercicios anteriores tenemos:
tiempo_curso_promedio_crudo_horas = 5
tiempo_curso_actual_crudo_horas = 3.5

porcentaje_inservible_video_promedio = ( (tiempo_curso_promedio_crudo_horas - tiempo_curso_promedio_horas) / tiempo_curso_promedio_crudo_horas) * 100
print(f"El porcentaje inservible que se reduce en el video promedio es: {porcentaje_inservible_video_promedio}%")

# El porcentaje inservible que se reduce en el video promedio es: 20.0%
```

- el curso actual(este curso):

```Python
porcentaje_inservible_video_actual = ( (tiempo_curso_actual_crudo_horas - tiempo_curso_actual_horas) / tiempo_curso_actual_crudo_horas ) * 100
print("El porcentaje inservible que se reduce en el curso actual es: {:.2f}%".format(porcentaje_inservible_video_actual))

# El porcentaje inservible que se reduce en el curso actual es: 57.14%
```

#### C) Ver 10 horas de este curso a cuantas horas de otros cursos promedio equivale? y alreves?

![Ejercicio1_C.1](https://github.com/EduCasanas/Python_Fundamentos/blob/main/Ejercicios/1_Ejercicio/Ejercicio1_C.1.png)

```Python
# Haciendo una regla de 3: 
equivalencia_horas_a_promedio = (tiempo_curso_promedio_horas * 10) / tiempo_curso_actual_horas
print("Ver 10 horas del curso actual representan a ver {:.2f} horas de un curso promedio.".format(equivalencia_horas_a_promedio)) 

# Ver 10 horas del curso actual representan a ver 26.67 horas de un curso promedio.
```

#### Ahora alreves 10 horas de un curso promedio a cuanto equivale en horas al curso actual?

![Ejercicio1_C.2](https://github.com/EduCasanas/Python_Fundamentos/blob/main/Ejercicios/1_Ejercicio/Ejercicio1_C.2.png)

```Python
# Haciendo una regla de 3:
equivalencia_horas_a_actual = (tiempo_curso_actual_horas * 10) / tiempo_curso_promedio_horas
print("Ver 10 horas de un curso promedio representan a ver {:.2f} horas del curso actual.".format(equivalencia_horas_a_actual)) 

# Ver 10 horas de un curso promedio representan a ver 3.75 horas del curso actual.
```
---

## Ejercicio 2

Se sabe que una persona promedio pronuncia 2 palabras por segundo.

A) Pedirle al usuario que diga cualquier texto real y:
- calcular cuanto tardaria en decir esa frase.
- cuantas palabras dijo?

B) Si se tarda mas de 1 minuto:
- decirle 'detente! has hablado mas de 1 minuto'

C) El mas rapido en hablar lo hace un 30% mas que el promedio:
- cuanto tardaria esta persona en decirlo?

## Solucion


#### A) Pedirle al usuario que diga cualquier texto real y:
- calcular cuanto tardaria en decir esa frase.

```Python
palabras_por_segundo_promedio = (2 / 1) # 2 palabras / 1 segundo
texto_por_consola = input("Ingrese un texto: ")
texto_a_lista = texto_por_consola.split(" ") # El split automaticamente crea una lista con los elementos
cantidad_palabras_ingresadas = len(texto_a_lista)
tiempo_de_palabras_ingresadas_promedio = cantidad_palabras_ingresadas * ( 1 / palabras_por_segundo_promedio) # Al multiplicar * (1 / palabras por segundo) se simplifica palabras y solo quedan segundos.
# Tambien podia simplemente en vez de multiplicar(* (1/palabras por segundo promedio)) directamente dividir 'palabras ingresadas' con 'palabras por segundo promedio'
print(f"Una persona promedio al pronunciar: {texto_a_lista} tardara {tiempo_de_palabras_ingresadas_promedio} segundos")
```

- cuantas palabras dijo?

```Python
print(f"La persona pronuncio: {cantidad_palabras_ingresadas} palabras.")
```

#### B) Si se tarda mas de 1 minuto(60 segundos):
- decirle 'detente! has hablado mas de 1 minuto'

```Python
if tiempo_de_palabras_ingresadas_promedio > 60:
    print("Detente! has hablado mas de 1 minuto")
```

#### C) El mas rapido en hablar lo hace un 30% mas que el promedio:
- cuanto tardaria esta persona en decirlo?

![Ejercicio2_C.1](https://github.com/EduCasanas/Python_Fundamentos/blob/main/Ejercicios/2_Ejercicio/Ejercicio2_C.1.png)

```Python
palabras_por_segundo_rapido = palabras_por_segundo_promedio + 0.6
tiempo_mas_rapido = cantidad_palabras_ingresadas / palabras_por_segundo_rapido
print("La persona mas rapida pronuncia {} en {:.2f} segundos.".format(texto_a_lista, tiempo_mas_rapido))
```

## Ejercicio 3

## Ejercicio 4
