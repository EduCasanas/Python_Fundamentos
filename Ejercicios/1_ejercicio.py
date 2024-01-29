# Ejercicio 1 => Ver imagen 'Ejercicio_1_python.png'

# A) Diferencia porcentual entre el curso actual y:
#   - el mas rapido de otros cursos
#   - el mas lento de otros cursos
#   - el promedio de otros cursos

# B) Porcentaje de material inservible que se reduce en:
#   - el promedio de los cursos
#   - el curso actual(este curso)

# C) Ver 10 horas de este curso a cuantas horas de otros cursos equivale? y alreves? 

# -----------------------------------------------------------------------------------
# SOLUCION
tiempo_curso_actual_horas = 1.5
tiempo_curso_minimo_horas = 2.5
tiempo_curso_maximo_horas = 7
tiempo_curso_promedio_horas = 4
# A) Diferencia porcentual entre el curso actual y:
#   - el mas rapido de otros cursos
diferencia_porcentual_contra_rapido = ( (tiempo_curso_minimo_horas - tiempo_curso_actual_horas) / tiempo_curso_minimo_horas ) * 100
print(f"El curso actual dura {diferencia_porcentual_contra_rapido}% menos que el curso mas rapido.")

#   - el mas lento de otros cursos
diferencia_porcentual_contra_lento = ( (tiempo_curso_maximo_horas - tiempo_curso_actual_horas) / tiempo_curso_maximo_horas ) * 100
print("El curso actual dura {:.2f}% menos que el curso mas lento.".format(diferencia_porcentual_contra_lento))

#   - el promedio de otros cursos
diferencia_porcentual_contra_promedio = ( (tiempo_curso_promedio_horas - tiempo_curso_actual_horas) / tiempo_curso_promedio_horas ) * 100
print(f"El curso actual dura {diferencia_porcentual_contra_promedio}% menos que el curso promedio.")

# B) Porcentaje de material inservible que se reduce en:
#   - el promedio de los cursos
# Haciendo la misma analogia de los ejercicios anteriores tenemos:
tiempo_curso_promedio_crudo_horas = 5
tiempo_curso_actual_crudo_horas = 3.5

porcentaje_inservible_video_promedio = ( (tiempo_curso_promedio_crudo_horas - tiempo_curso_promedio_horas) / tiempo_curso_promedio_crudo_horas) * 100
print(f"El porcentaje inservible que se reduce en el video promedio es: {porcentaje_inservible_video_promedio}%")

#   - el curso actual(este curso)
porcentaje_inservible_video_actual = ( (tiempo_curso_actual_crudo_horas - tiempo_curso_actual_horas) / tiempo_curso_actual_crudo_horas ) * 100
print("El porcentaje inservible que se reduce en el curso actual es: {:.2f}%".format(porcentaje_inservible_video_actual))

# C) Ver 10 horas de este curso a cuantas horas de otros cursos promedio equivale? y alreves?
# Haciendo una regla de 3 (Ver imagen 'Ejercicio_C.1.png')
equivalencia_horas_a_promedio = (tiempo_curso_promedio_horas * 10) / tiempo_curso_actual_horas
print("Ver 10 horas del curso actual representan a ver {:.2f} horas de un curso promedio".format(equivalencia_horas_a_promedio)) 

# Ahora alreves 10 horas de un curso promedio a cuanto equivale en horas al curso actual
# Haciendo una regla de 3 (Ver imagen 'Ejercicio_C.2.png')
equivalencia_horas_a_actual = (tiempo_curso_actual_horas * 10) / tiempo_curso_promedio_horas
print("Ver 10 horas del curso actual representan a ver {:.2f} horas de un curso promedio".format(equivalencia_horas_a_actual)) 
