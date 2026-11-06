nombre = input("Introduzca su nombre: ")
apellido = input("Introduzca su apellido: ")

while nombre.isdigit() == True and apellido.isdigit() == False:
    print("Solo letras")
    nombre = input("Introduzca su nombre: ")
    apellido = input("Introduzca su apellido: ")

largo = ""

if len(nombre) > len(apellido):
    largo = len(nombre)
elif len(apellido) > len(nombre):
    largo = len(apellido)
else:
    largo = len(nombre)

alias = nombre[:3].upper() + "-" + apellido[-3:].upper() + "-" + str(largo)

print(alias)