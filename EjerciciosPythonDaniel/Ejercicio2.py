caramelos = 0
sustos = 0

while caramelos != 15 and sustos != 3:
    que_ocurre = int(input("Que ocurre en la casa: "))
    if que_ocurre == 1:
        caramelos += 3
    elif que_ocurre == 2:
        sustos += 1
    else:
        print("La casa está vacía")

if caramelos == 15:
    print("Saco lleno")
elif sustos == 3:
    print("Demasiados sustos")
    
print(f"Caramelos: {caramelos}\nSustos: {sustos}")