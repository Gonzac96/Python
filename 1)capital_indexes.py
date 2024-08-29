
def capital_indexes(s):
    return [indice for indice, char in enumerate(s) if char.isupper()]

print("Ingrese una palabra: ")
palabra = input()

print("La lista es ", end="")
print(capital_indexes(palabra))
