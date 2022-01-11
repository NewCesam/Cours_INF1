def add(x, y):
    if y == 0:
        return x
    if y > 0:
        return 1 + add(x, y-1)
    return  add(x, y+1) - 1

print("---addition de deux nombres")
nombre1 = int(input("Entrer un nombre:\n"))
nombre2 = int(input("Entrer un nombre:\n"))
print("l'addition des nombres ",nombre1," et ", nombre2," est ", add(nombre1,nombre2))