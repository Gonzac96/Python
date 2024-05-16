"""
En este desafío, debes dibujar un triángulo equilatero usando bucles.

Recibirás dos parámetros: size y character, que definen el número de filas que tendrá y el carácter con el que se debe construir el triángulo, respectivamente.
Además, el triángulo debe estar alineado al centro, lo que significa que la misma cantidad de caracteres debe haber en ambos lados.
"""

def print_triangle(size, character):
    triangle = ''
    for i in range(size):
        #Hace las separaciones necesarias para dejar al caracter/los caracteres en el medio
        triangle += " " * (size - i - 1)
        #Suma la cantidad de caracteres necesarios para la fila
        triangle += character + character * (2 * i)
        #Si no es la ultima fila, aplica el salto de linea
        if i != size - 1:
            triangle += "\n"
    return print(triangle)

tamaño = int(input("Ingrese cuantas filas tendrá el triangulo equilatero: "))
caracter = input("Ingrese un caracter para construir el triangulo: ")
print_triangle(tamaño, caracter)