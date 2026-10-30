num_habitacion = int(input("Cuantas habitaciones hay: "))

tranquila = 0
susto = 0
maldita = 0
total_fantasmas = 0

for habitacion in range(num_habitacion):
    num_fantasmas = int(input("Cuantos fantasmas hay: "))
    if num_fantasmas == 0:
        tranquila += 1
        print("Habitacion tranquila")
    elif num_fantasmas >= 1 and num_fantasmas <= 3:
        susto += 1
        print("Susto")
    else:
        maldita += 1
        print("Habitacion maldita")
    total_fantasmas += num_fantasmas

print(f"Hay {tranquila} habitaciones tranquilas\nHay {susto} habitaciones de susto\nHay {maldita} habitaciones malditas")

media_fantasmas = total_fantasmas / num_habitacion

print(f"Total fantasmas: {total_fantasmas}\nMedia de fantasmas: {media_fantasmas}")