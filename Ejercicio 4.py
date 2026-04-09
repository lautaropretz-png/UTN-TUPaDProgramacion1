energia = 100
tiempo = 12
cerradura_abierta = 0
alarma = False
codigo_parcial = ""
cont = 0

nombre_agent = input("Ingrese el nombre del agente: ")
while not nombre_agent.isalpha():
    nombre_agent = input("Error.\nIngrese un nombre válido: ")

while energia>0 and tiempo>0 and cerradura_abierta<3:
    print(f"Energía: {energia}\nTiempo: {tiempo}\nCerraduras abiertas: {cerradura_abierta}\nAlarma: {alarma}")
    if alarma == True and tiempo <=3:
        print("La alarma está encendida y no tienes tiempo suficiente. Sistema bloqueado")
        break
    opcion = input("1) Forzar cerradura. 2) Hackear panel. 3) Descansar.")
    while not opcion.isdigit() or int(opcion)>3 or int(opcion)<1:
        opcion = input("Error.\nIngrese una de las opciones.\n1) Forzar cerradura. 2) Hackear panel. 3) Descansar.")
    
    if opcion == "1":
        print("Frozar cerradura. Costo: -20 energía, -2 tiempo")
        energia -=20
        tiempo -=2
        cont+=1
        if cont == 3:
            alarma = True
            print("Intentaste forzar 3 veces seguidas. Alarma activada")
        else:
            if energia < 40:
                print("Hay riesgo de alarma")
                n = input("Ingrese un numero del 1 al 3")
                while not n.isdigit() or int(n)<1 or int(n)>3:
                    n =input("Error. Ingrese un numero del 1 al 3: ")
                if n == "3":
                    alarma = True
                    print("Se encendió la alarma")
            else:
                cerradura_abierta += 1    

    elif opcion == "2":
        cont = 0
        print("Hackear panel. Costo: -10 energía, -3 tiempo")
        energia-=10
        tiempo-=3
        for i in range(4):
            print(f"Paso {i + 1}")
            codigo_parcial += "A"
            print(f"Codigo parcial: {codigo_parcial}")
        if len(codigo_parcial) >= 8:
            cerradura_abierta += 1
            codigo_parcial = ""

    elif opcion == "3":
        cont = 0
        print("Descansar. Costo: + 15 energía (máx 100), -1 tiempo, si alarma ON: -10 energía extra")
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma == True:
            energia-=10
if cerradura_abierta == 3:
    print("Felicitaciones! Haz ganado")
else:
    print("Haz perdido")
