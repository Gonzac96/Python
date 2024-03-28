"""
En este desafío, debes encontrar al gatito más famoso con base en su número de seguidores.

Recibirás una lista de diccionarios que incluirán las siguientes propiedades:
"name": nombre del gatito.
"followers": una lista de números, donde cada uno representa los seguidores de cada red social.

Tu tarea es devolver una lista con los nombres de los gatos que tienen solo el mayor número de seguidores. 
Si hay dos o más gatos con el mismo número máximo de seguidores, deberás incluirlos en la lista resultante, 
manteniendo el orden en el que aparecen en la lista de entrada.
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
    "followers": [500, 200, 300, 600]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
  {
      "name": "Tom",
      "followers": [200, 600, 800]
  }
])

###Mejora de ese codigo con list comprehension
#cat = variable
def find_famous_cat_short(cats):
    famous = max(sum(cat["followers"]) for cat in cats)
    names = [cat["name"] for cat in cats if famous == sum(cat["followers"])]
    return print(names)


find_famous_cat_short([
  {
    "name": "Luna",
    "followers": [500, 200, 300, 600]
  },
  {
    "name": "Michi",
    "followers": [100, 300]
  },
  {
      "name": "Tom",
      "followers": [200, 600, 800]
  }
])