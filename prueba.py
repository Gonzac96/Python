"""
Estos son ejercicios de prueba para el curso de 21 dias de python
"""

x = int(input("Ingrese un numero: "))
print(type(x))

if x > 5:
    print("x es grande")
else:
    print("x es bajito\n")
    print("muy bajito")

for i in range(5):
        print(i)  

contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1  # Incrementa e    l contador en 1 en cada iteración

#Comentario para probar un commmit