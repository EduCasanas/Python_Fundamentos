#CONTENIDO
"""
1) dir (me dice que metodos son aplicables a una variable) => dir(variable)
2) Mayuscula (UPPER) => variable.upper()
3) Minuscula (LOWER) => variable.lower()
4) Letra capital o primera letra en Mayuscula (CAPITALIZE) => variable.capitalize()
5) Encuentra un valor(la 1era) sino devuelve 1 (FIND) => variable.find()
6) Encuentra el indice de una letra o palabra (INDEX) => variable.index()
7) Es numerico, si hay numeros en un string (ISNUMERIC) => variable.isnumeric()
8) Es alphanumerico, solo letras A-Z (ALPHA) => variable.isalpha()
9) Conteo de subcadenas de una cadena dada (COUNT) => variable.count("palabra")
10) Longitud de una cadena (LEN) => len(variable)
11) Cadena empieza con una palabra o letra (STARTSWITH) => variable.startswith("palabra") 
12) Cadena termina con una palabra o letra (ENDSWITH) => variable.endswith("palabra")
13) Reemplaza un valor por otro (REPLACE) => variable.replace("antiguo", "nuevo")
14) Separa por el parametro dado y crea una lista de estos elementos (SPLIT) => variable.split("parametro: espacio, coma, caracter, etc")
"""
# 1) dir (me dice que metodos son aplicables a una variable)
cadena1 = "Hola educa"
cadena2 = "Bienvenido al curso de python"
print(dir(cadena1))
""" Por ejemplo 'cadena1' es un string tiene los siguientes metodos aplicables:
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
'__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode',
'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust',
'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
# 2) Mayuscula (UPPER)
name = "jorge eduardo"
name_mayusculas = name.upper()
print(name_mayusculas)

# 3) Minuscula (LOWER)
last_name = "CASANAS CUENCA"
last_name_lower = last_name.lower()
print(last_name_lower)

# 4) Letra capital (CAPITALIZE)
cita = 'buenos Dias Edu'
cita_capital = cita.capitalize() # Primero convierte a lower y coloca la 1era letra a Mayuscula
print(cita_capital)

# 5) Encuentra un valor(la 1era) sino devuelve 1 (FIND)
cita_especial = "Hola buenos dias educa, como estas hoy"
busqueda1 = cita_especial.find("educa")
busqueda2 = cita_especial.find("z")
print(busqueda1) # 17 es decir me dio la posicion donde empieza la palabra
print(busqueda2) # -1 porque no esta este valor en la cadena

# 6) Encuentra el indice de una letra o palabra (INDEX)
frase = "Hola bienvenido"
# busqueda3 = frase.index("z")
# print(busqueda3) # cuando no encuentra la letra en una cadena lanza un error, a 
# diferencia del 'find' que da un '-1'

# 7) Es numerico (ISNUMERIC)
es_numerico = "hola"
es_numerico2 = "123456"
# es_numerico3 = 123456

resultado1 = es_numerico.isnumeric()
resultado2 = es_numerico2.isnumeric()
#resultado3 = es_numerico3.isnumeric()

print(resultado1) # False
print(resultado2) # True
# print(resultado3) # ERROR => el objeto 'int' no tiene el atributo 'isnumeric'

# 8) Es alphanumerico (ALPHA)
abecedario = "abcdefghijklmno"
print(abecedario.isalpha()) # True
# ----------------------------------
abecedario2 = "abcdefghijklmno123"
print(abecedario2.isalpha()) # False
# -----------------------------------
abecedario3 = "hola educa"
print(abecedario3.isalpha()) # False

# 9) Conteo de subcadenas de una cadena dada (COUNT) 
cadena = "Hola como estas educa"
# ---------------------------------
coincidencias = cadena.count("o")
print(coincidencias) # 3 veces aparece la 'o'
# ----------------------------------
coincidencias2 = cadena.count("1")
print(coincidencias2) # 0 ya que no aparece el '1' en la cadena
# ----------------------------------
coincidencias3 = cadena.count("educa")
print(coincidencias3) # 'educa' aparece 1 vez

# 10) Longitud de una cadena (LEN)
frase_motivacion = "Sigue adelante, cada dia da un pasito"
longitud_cadena = len(frase_motivacion)
print(longitud_cadena) # 37 elementos contando los espacios

# 11) Cadena empieza con una palabra o letra (STARTSWITH) 
cadena_starts = "Buenos dia educa, que tal el dia"
empieza_con = cadena_starts.startswith("Buenos")
empieza_con2 = cadena_starts.startswith("buenos ")

print(empieza_con) # True
print(empieza_con2) # False

# 12) Cadena termina con una palabra o letra (ENDSWITH)  
cadena_ends = "Buenos dia educa, que tal el dia"
termina_con = cadena_ends.endswith("dia")
termina_con2 = cadena_ends.endswith("tal")

print(termina_con) # True
print(termina_con2) # False

# 13) Reemplaza un valor por otro (REPLACE)
oracion1 = "Hola educa que tal tu dia hoy?"
reemplazo = oracion1.replace("educa", "jorge")
print(reemplazo) # Hola jorge que tal tu dia hoy?

# 14) Separa por el parametro dado (SPLIT)
oracion2 = "Hola educa que tal tu dia hoy?"
separacion = oracion2.split(" ")
print(separacion) # ['Hola', 'educa', 'que', 'tal', 'tu', 'dia', 'hoy?']
