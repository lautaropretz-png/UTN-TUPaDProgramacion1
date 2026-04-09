nombre = input("ingrese el nombre del Gladiador: ")
while not nombre.isalpha():
    nombre = input("Error: Solo se permiten letras")
salud_g = 100
salud_e = 100
pos_vida = 3
daño_g= 15
daño_e = 12
turno_g = True

while salud_g > 0 and salud_e > 0:
    print(f"Vida del Gladiador: {salud_g}\nVida del Enemigo: {salud_e}\nPosiciones restantes: {pos_vida}")
    opcion = input("1) Ataque pesado 2) Ráfaga veloz 3) Curar\n")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) >3:
        opcion = input("Error: Debes elegir alguna de las opciones")
    
    if opcion == "1":
        if salud_e < 20:
            salud_e = salud_e - (daño_g * 1.5)
            print(f"¡Atacaste al enemigo por {daño_g * 1.5} puntos de daño")
        else:
            salud_e = salud_e - daño_g
            print(f"Atacaste al enemigo por {daño_g} puntos de daño")

    elif opcion == "2":
        for i in range(3):
            salud_e = salud_e - 5
            print("Golpe conectado por 5 de daño")
    
    elif opcion == "3":
        if pos_vida > 0:
            salud_g += 30
            pos_vida -= 1
        else:
            print("¡No quedan posiciones!")
    
    salud_g -= 12
    print("¡El enemigo te atacó por 12 puntos de daño")

if salud_g > 0:
    print("¡VICTORIA!", nombre, "ha ganado la batalla")
else:
    print("DERROTA. Has caído en combate")