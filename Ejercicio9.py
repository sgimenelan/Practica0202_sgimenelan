fecha = input("Dime tu fecha de nacimiento (formato dd/mm/aaaa) ")
dia, mes, año = fecha.split("/")
indice = 10
if dia < indice:
    dia = ("0" + dia)
print("Dia: " + dia)
print("Mes: " + mes)
print("Año: " + año)