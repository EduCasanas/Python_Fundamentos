# Fundamentos de Python
---
### Archivo "0_intro.py"

1) Comentarios => `#` o `""" """`
2) Impresion por pantalla => `print(variable)`
---
### Archivo "1_tipos_de_datos_simples.py"
1) Tipos de datos(**string**("hola"), **int**(99), **float**(9.7), **bool**(True, False))
---
### Archivo "2_variables.py"
1) Variables
2) Concatenacion (+)

    2.1) Interpolacion(agregar variables dentro de strings => `f"Hola {variable}"`)

    2.2) Eliminar variables => `del variable`
    
    2.3) Operadores de pertenencia => `in`, `not in`
3) Recomendacion de escritura de variables => **snake_case**        
---
### Archivo "3_datos_compuestos.py"
1) Listas =>[ ]
2) Tuplas =>( )
3) Sets o Conjuntos =>{ }
4) Diccionarios =>{key: value}
---
### Archivo "4_operadores_aritmeticos.py"
1) Suma y Resta =>( +, - )
2) Multiplicacion y Division =>( *, / )
3) Potenciacion =>( ** )
4) Division entera =>( // )
5) Resto o modulo =>( % )
6) Tipo de dato =>( type( ) )
---
### Archivo "5_operadores_comparacion.py"
1) Igualdad =>( == )
2) Distinto =>( != )
3) Menor o menor igual =>( <, <= )
4) Mayor o mayor igual =>( >, >= ) 
---
### Archivo "6_condicionales.py"
1) if-else
2) else-if (elif)  y anidacion de if's
---
### Archivo "7_operadores_logicos.py"
1) o =>( | )
2) y =>( & )
3) no =>( not )
---
### Archivo "8_metodos_cadenas.py"
1) dir (me dice que metodos son aplicables a una variable) => `dir(variable)`
2) Mayuscula (UPPER) => `variable.upper()`
3) Minuscula (LOWER) => `variable.lower()`
4) Letra capital o primera letra en Mayuscula (CAPITALIZE) => `variable.capitalize()`
5) Encuentra un valor(la 1era) sino devuelve 1 (FIND) => `variable.find()`
6) Encuentra el indice de una letra o palabra (INDEX) => `variable.index()`
7) Es numerico, si hay numeros en un string (ISNUMERIC) => `variable.isnumeric()`
8) Es alphanumerico, solo letras A-Z (ALPHA) => `variable.isalpha()`
9) Conteo de subcadenas de una cadena dada (COUNT) => `variable.count("palabra")`
10) Longitud de una cadena (LEN) => `len(variable)`
11) Cadena empieza con una palabra o letra (STARTSWITH) => `variable.startswith("palabra")` 
12) Cadena termina con una palabra o letra (ENDSWITH) => `variable.endswith("palabra")`
13) Reemplaza un valor por otro (REPLACE) => `variable.replace("antiguo", "nuevo")`
14) Separa por el parametro dado (SPLIT) => `variable.split("parametro: espacio, coma, caracter, etc")`
---
### Archivo "9_metodos_listas.py"
1) Crear una lista (list) => `list(["cadena", int, float, bool])`
2) Longitud de una lista (len) => `len(lista)`
3) Agregar elementos al final de la lista (append) => `lista.append("palabra")`
4) Insertar un elemento dentro de una lista (insert) => `lista.insert(posicion_dentro_de_la_lista, "Lo que queremos agregar:palabra, int, float,etc..")`
5) Agregar varios elementos a una lista (extend) => `lista.extend(["cadena", bool, int])`
6) Eliminar un elemento de la lista por indice (pop) => `lista.pop(indice de elemento a eliminar)`
7) Elimina un elemento de la lista segun el elemento (remove) => `lista.remove(elemento de la lista)`
8) Elimina todos los elementos de la lista (clear) => `lista.clear()`
9) Ordena una lista de forma ascendente (sort) => `lista.sort()` | orden descendente: `lista.sort(reverse=True)` 
10) Invierte los elementos de una lista (reverse) => `lista.reverse()`
11) Posicion de un elemento de una lista (index) => `lista.index(elemento en la lista)`
---