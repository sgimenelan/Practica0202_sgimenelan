fecha = input("Dime tu fecha de nacimiento (formato dd/mm/aaaa) ")
dia, mes, año = fecha.split("/")
if str(0) < dia < str(10):
    dia = ("0" + dia)
if dia > str(31):
    print("Error, no hay ningun mes con " + dia + " dias")
    exit()
if str(0) < mes < str(10):
    mes = ("0" + mes)
if mes > str(12):
    print("Error, no hay ningun año con " + mes + " meses")
    exit()
if año > str(2024):
    print("Error, todavia no has nacido")
    exit()
if dia < str(0):
    print("No puedes introducir nummeros negativos")
    exit()
if mes < str(0):
    print("No puedes introducir nummeros negativos")
    exit()
if año < str(0):
    print("No puedes introducir nummeros negativos")
    exit()
print("Dia: " + dia)
print("Mes: " + mes)
print("Año: " + año)
