nombre_completo = str(input("Dime tu nombre completo "))
nombre, apellido = nombre_completo.split(" ")
print (nombre.lower() + " " + apellido.lower())
print (nombre.upper() + " " + apellido.upper())
print (nombre.title() + " " + apellido.title())