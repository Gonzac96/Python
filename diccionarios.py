"""     OBTEN EL PROMEDIO DE LOS ESTUDIANTES
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