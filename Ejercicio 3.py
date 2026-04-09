lunes1=lunes2=lunes3=lunes4=""
martes1=martes2=martes3=""

nombre_op = input("Nombre de operador: ")

while not nombre_op.isalpha():
    nombre_op = input("Error: el nombre debe contener únicamente letras\nIngrese nombre: ")

opcion = input("1)Reservar turno\n2)Cancelar turno\n3)Ver agenda del dia\n4)Ver resumen general\n5)Cerrar sistema")
while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
    opcion  = input("Error\nElija una opcion: ")

while opcion !="5":

    if opcion == "1":
        dia = input("Elegir dia lunes (1) o martes (2): ")
        while dia != "1" and dia != "2":
            dia = input("Error.\nElegir dia lunes (1) o martes (2): ")
        nombre = input("Ingrese el nombre del paciente: ")
        while not nombre.isalpha():
            nombre = input("Error: el nombre debe contener únicamente letras\nIngrese nombre: ")
        if dia == "1":
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre== lunes4:
                print("El paciente está cargado en el día")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print ("No hay turnos disponibles")
        elif dia == "2":
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("El paciente está cargado en el día")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print ("No hay turnos disponibles")

    elif  opcion == "2":
        dia = input("Para cancelar el turno elige el dia lunes (1) o el dia martes (2): ")
        while dia != "1" and dia != "2":
            dia = input("Error.\nElegir dia lunes (1) o martes (2): ")
        nombre = input("Ingrese el nombre del paciente: ")
        while not nombre.isalpha():
            nombre = input("Error: el nombre debe contener unicamente letras.\nIngrese nombre: ")
        if dia == "1":
            if nombre == lunes1:
                lunes1 = ""
            elif nombre == lunes2:
                lunes2 = ""
            elif nombre == lunes3:
                lunes3 = ""
            elif nombre == lunes4:
                lunes4 = ""
        if dia == "2":
            if nombre == martes1:
                martes1 = ""
            elif nombre == martes2:
                martes2 = ""
            elif nombre == martes3:
                martes3 = ""
    elif opcion == "3":
        print("Turnos del dia lunes")
        if lunes1 == "":
            print("Turno 1 (libre)")
        else:
            print(f"Turno 1: {lunes1}")
        if lunes2 == "":
            print("Turno 2 (libre)")
        else:
            print(f"Turno 2: {lunes2}")
        if lunes3 == "":
            print("Turno 3 (libre)")
        else:
            print(f"Turno 3: {lunes3}")
        if lunes4 == "":
            print("Turno 4 (libre)")
        else:
            print(f"Turno 4: {lunes4}")
        print("Turnos del dia martes")
        if martes1 == "":
            print("Turno 1 (libre)")
        else:
            print(f"Turno 1: {martes1}")
        if martes2 == "":
            print("Turno 2 (libre)")
        else:
            print(f"Turno 2: {martes2}")
        if martes3 == "":
            print("Turno 3 (libre)")
        else:
            print(f"Turno 3: {martes3}")
    elif opcion == "4":
        nl=0
        nm=0
        if lunes1 == "":
            nl+=1
        if lunes2 == "":
            nl+=1
        if lunes3 == "":
            nl+=1 
        if lunes4 == "":
            nl+=1 
        if martes1 == "":
            nm+=1
        if martes2 == "":
            nm+=1 
        if martes3 == "":
            nm+=1 
        print(f"Lunes\nTurnos ocupados: {4 - nl}\nTurnos libes: {nl}")  
        print(f"Martes\nTurnos ocupados: {3 - nm}\nTurnos libes: {nm}") 
        if (4-nl)>(3-nm):
            print("Lunes con mayor cantidad de turnos")
        elif (3-nm)>(4-nl):
            print("Martes con mayor cantidad de turnos")
        else:
            print("Ambos días tiene la misma cantidad de turnos ocupados")  
    opcion = input("1)Reservar turno\n2)Cancelar turno\n3)Ver agenda del dia\n4)Ver resumen general\n5)Cerrar sistema")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        opcion  = input("Error\nElija una opcion: ")
