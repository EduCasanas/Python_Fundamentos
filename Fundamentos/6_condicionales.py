#CONTENIDO
"""
1) if-else
2) else-if (elif)  y anidacion de if's   
"""
# 1) IF-ELSE
edad = 9
if edad >= 18:
    print('Usted puede ingresar')
else:
    print('Usted es menor de edad, no puede pasar')    
# 2) ELSE-IF
edad2 = 68

if edad2 >=65:
    if edad2 == 70:
        print('Usted es de la tercera edad y ya esta jubilado')
    elif edad2 == 65:
        print('Usted recien es de la tercera edad')
    else:
        print('Usted es de la tercera edad')        
elif edad2 >= 18:
    print('Usted es mayor de edad')
else:
    print('Usted es menor de edad')        