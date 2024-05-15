"""
En este desafío, te encuentras trabajando para una empresa de transporte de carga que necesita llevar un registro de los paquetes que se envían en cada viaje. 
Para ello, se te proporcionará una lista de tuplas, cada una de las cuales representará un paquete y tendrá las siguientes propiedades:
(id, weight, destination)

A partir de esta información, debes crear una función que calcule el peso total de los paquetes, así como la cantidad de paquetes que se enviarán a cada destino. 
Para ello, debes retornar un nuevo diccionario que tenga las siguientes propiedades:
"total_weight": El peso total de los paquetes.
"destinations": Un diccionario con los destinos como claves y la cantidad de paquetes como valores.

Es importante mencionar que la función debe redondear el peso total a dos decimales y que cada destino debe aparecer sólo una vez en el diccionario.
"""

def get_packages_info(packages):
    weight = [package[1] for package in packages]
    tuple_destinations = tuple(package[2] for package in packages)
    destinations = {destino: tuple_destinations.count(destino) for destino in tuple_destinations}
    total_weight = round(sum(weight),2)
    return {"total_weight: ":total_weight, "destinations: ":destinations}

print(get_packages_info([
  (1, 20, "México"),
  (2, 15.5, "Colombia"),
  (3, 30, "México"),
  (4, 12, "Argentina"),
  (5, 8.2, "Colombia"),
  (6, 25, "México"),
  (7, 18.7, "Argentina"),
  (8, 5, "Colombia"),
  (9, 22.3, "Argentina"),
  (10, 14.8, "Colombia")
]))