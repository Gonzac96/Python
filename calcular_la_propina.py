"""
La función calculate_tip recibirá dos parámetros:
bill_amount que representa el costo total de lo que se haya consumido y 
tip_percentage que representa el porcentaje de propina a dejar.
Ambos valores serán de tipo float y siempre serán positivos, incluyendo el 0. 
La función deberá devolver el valor de la propina como un número.
"""

def calculate_tip(bill_amount, tipPercentage):
   s = (bill_amount*tipPercentage)/100
   return round(s, 2)

bill = float(input("Ingrese el valor de lo que haya consumido: "))

tip = float(input("Ingrese el porcentaje de propina que desea dejar: "))

print(calculate_tip(bill, tip))