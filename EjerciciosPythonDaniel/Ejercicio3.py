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

alias = nombre[0:2].upper() + "-" + apellido[0:2].upper() + "-" + str(largo)

print(alias)