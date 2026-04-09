usuario_correcto = "alumno"
clave_correcta = "python123"

for i in range(0,3):
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    if usuario==usuario_correcto and clave==clave_correcta:
        opcion = 0
        while opcion != 4:
            opcion=int(input("1) Estado 2) Cambiar clave 3) Mesaje 4) Salir"))
            if opcion == 4: 
                print("ha salido del programa")
            elif opcion == 1:
                print("Inscripto")
            elif opcion == 3:
                print("Sigue esforzándote, pronto llegarán los resultados")
            elif opcion == 2:
                clave_conf = "0"
                while clave_conf != clave:
                    clave = input("Ingrese la nueva clave, tien que ser de 6 caracteres o mas: ")
                    while len(clave)<6:
                        clave = input("Error: la clave es inválida, ingresela nuevamente: ")
                    clave_conf = input("Confirmación de clave: ")
                    if clave == clave_conf:
                        print("Clave generada")
                    else:
                        print("Las claves no coinciden, intente nuevamente")
            if not str(opcion).isdigit() or opcion > 4 or opcion < 1:
                print("La opcion ingresada es invalida")
        break
    else:
        print("El usurio y/o clave son incorrectos")
print("Usaste el numero de intentos permitidos, usuario bloqueado")
                    