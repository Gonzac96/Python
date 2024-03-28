"""
En este desafío de Python, debes crear la lógica de la función is_leap_year, que determina si un año es bisiesto o no.
Un año es bisiesto si cumple con las siguientes condiciones:
-Es divisible por 4, pero no por 100.
-Si es divisible por 100 debe serlo por 400 también.
La función is_leap_year recibe un único parámetro: el año a evaluar. Debe devolver True si el año es bisiesto o False en caso contrario.

Toma en cuenta que la función debe ser capaz de manejar valores no enteros o negativos.
"""

def is_leap_year(year):
    if year % 1 != 0 or year <=0: 
      return False
    
    if year % 4 == 0:
      if year % 100 == 0 and year % 400 == 0:
         return True

      if year % 100 == 0:
         return False
      
      return True
    
    return False
       

bisiesto = is_leap_year(2024)
print(bisiesto)