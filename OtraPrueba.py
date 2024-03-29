"""#OtraPrueba
from typing import Tuple, Dict, List, Set

edad: int = 30

edad = 7.38934

print(edad)

tupla: Tuple = (0, 1, 2, 3)"""

"""def calculate_tip(bill_amount, tipPercentage):
   s = (bill_amount*tipPercentage)/100
   return round(s, 2)

print(calculate_tip(851.7894,10))"""

##################################################

"""
En este desafío de Python, debes crear la lógica de la función is_leap_year, que determina si un año es bisiesto o no.
Un año es bisiesto si cumple con las siguientes condiciones:
-Es divisible por 4, pero no por 100.
-Si es divisible por 100 debe serlo por 400 también.
La función is_leap_year recibe un único parámetro: el año a evaluar. Debe devolver True si el año es bisiesto o False en caso contrario.

Toma en cuenta que la función debe ser capaz de manejar valores no enteros o negativos.
"""
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
       

response = is_leap_year(2000)
print(response)"""

###########################################

"""
En este desafío, debes dibujar un triángulo equilatero usando bucles.

Recibirás dos parámetros: size y character, que definen el número de filas que tendrá y el carácter con el que se debe construir el triángulo, respectivamente.
Además, el triángulo debe estar alineado al centro, lo que significa que la misma cantidad de caracteres debe haber en ambos lados.

Recuerda que para hacer el salto de línea debes usar "\n", no olvides removerla de la última parte, debes retornar todo esto en una variable.
"""

"""
def print_triangle(size, character):
    triangle = ''
    #print(type(triangle))
    for i in range(size):
        triangle += " " * (size - i - 1)
        triangle += character + character * (2 * i)
        if i != size - 1:
            triangle += "\n"
    return print(triangle)

print_triangle(5, "+")
"""

#########################################

"""
En este desafío, debes encontrar al gatito más famoso con base en su número de seguidores.

Recibirás una lista de diccionarios que incluirán las siguientes propiedades:
"name": nombre del gatito.
"followers": una lista de números, donde cada uno representa los seguidores de cada red social.

Tu tarea es devolver una lista con los nombres de los gatos que tienen solo el mayor número de seguidores. 
Si hay dos o más gatos con el mismo número máximo de seguidores, deberás incluirlos en la lista resultante, 
manteniendo el orden en el que aparecen en la lista de entrada.
"""

"""
def find_famous_cat(cats):
    c = 0
    famous_cat = []
    for cat in cats:
        suma = sum(cat["followers"]) 
        if suma > c:
            c = suma
            famous_cat = cat["name"]
        elif suma == c:
          famous_cat += ", " + (cat["name"])
    return print(famous_cat)

find_famous_cat([
  {
    "name": "Luna",
    "followers": [500, 200, 300]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
  {
      "name": "Gordita",
      "followers": [200, 600, 800]
  }
])"""

###Mejora de ese codigo con list comprehension
"""
def find_famous_cat(cats):
    famous = max(sum(cat["followers"]) for cat in cats)
    names = [cat["name"] for cat in cats if famous == sum(cat["followers"])]
    return print(names)
"""

#####################################

"""
En este desafío, deberás calcular el promedio general de una clase, así como el promedio individual de cada estudiante.

Para ello, se te proporcionará una lista de diccionarios, cada uno de los cuales representará a un estudiante y tendrá las siguientes propiedades:
-"name": El nombre del estudiante
-"grades": Las notas de cada materia del estudiante

A partir de esta información, debes retornar un nuevo diccionario que tenga la propiedad "class_average" 
con el promedio de la clase y una lista de "students" con los estudiantes y sus promedios individuales.

Es importante mencionar que los promedios deben ser calculados con precisión y se deben redondear a dos decimales
para que los test pasen sin problema alguno.
"""

def get_student_average(students):
  classStudents = {"class_average" : 0, "students": []}
  averageClass = 0
  for i in students:
    student = {
        "name" : i["name"],
        "average" : round(sum(i["grades"])/len(i["grades"]), 2)
    }
    averageClass += student["average"]
    classStudents["students"].append(student)
  classStudents["class_average"] = round(averageClass/len(students), 2)
  return classStudents


print(get_student_average([
  {
    "name": "Pedro",
    "grades": [90, 87, 88, 90],
  },
  {
    "name": "Jose",
    "grades": [99, 71, 88, 96],
  },
  {
    "name": "Maria",
    "grades": [92, 81, 80, 96],
  },
]))