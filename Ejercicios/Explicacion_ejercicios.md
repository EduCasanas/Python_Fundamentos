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

tiempo_curso_actual_horas = 1.5
tiempo_curso_minimo_horas = 2.5
tiempo_curso_maximo_horas = 7
tiempo_curso_promedio_horas = 4

A) Diferencia porcentual entre el curso actual y:
![EjercicioA.1](https://github.com/EduCasanas/Python_Fundamentos/blob/main/Ejercicios/1_Ejercicio/Ejercicio1_A.1.png)

- el mas rapido de otros cursos

```Python
diferencia_porcentual_contra_rapido = ( (tiempo_curso_minimo_horas - tiempo_curso_actual_horas) / tiempo_curso_minimo_horas ) * 100
print(f"El curso actual dura {diferencia_porcentual_contra_rapido}% menos que el curso mas rapido.")
```
