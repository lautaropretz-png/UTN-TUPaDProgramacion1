# Ejercicio N° 1

nombre = input("Ingrese su nombre ")

while not nombre.isalpha():
    print("Error: el nombre solo debe contener caracteres")
    nombre = input("Ingrese su nombre ")

cant = input("Ingrese la cantidad de produtos: ")

while not cant.isdigit(): 
    print("Error: la cantidad de productos debe ser únicamente un número")
    cant = input("Ingrese la cantidad de produtos: ")

cant = int(cant)

total_precio = 0

total_precio_float = 0

for num in range(1,cant+1):
    precio=input(f"Ingrese el precio del producto {num}: ")
    while not precio.isdigit():
        print("Error: el precio debe ser un número")
        precio = input(f"Ingrese el precio del produto {num}: ")

    precio = int(precio)

    descuento = input("Tiene descuento? (S/N) ").lower()

    while descuento != "s" and descuento != "n":
        print("Error: solo puede ingresar S o N")
        descuento = input("Tiene descuento? (S/N) ").lower()

    if descuento == "s":
        precio_descontado = float(precio)
        precio_descontado = precio_descontado * 0.9
    else: precio_descontado = precio

    total_precio += precio

    total_precio_float += precio_descontado

ahorro = total_precio - total_precio_float

promedio = total_precio_float / cant

print(f"Total sin descuento: {total_precio}")
print(f"Total con descuento: {total_precio_float}")
print(f"Ahorro: {ahorro}")
print(f"El promedio de precio por producto es {promedio}")
    

        
