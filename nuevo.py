import pandas as pd

tabla = pd.DataFrame(data = [[1, 1, 1], [2, 4, 8], [3, 9, 27]],
                     columns = ['número', 'número²', 'número³'])

print(tabla)

prom = tabla['número³'].mean()
media = tabla['número³'].median()
moda = tabla['número³'].mode()[0]

print("De la columna de cubos:\nEl promedio es", prom, "\nLa media es", media, "\nLa moda es", moda, "\n")
