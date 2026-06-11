ficha = {
    "nombre": "benjamin",
    "telefono": "9938343432",
    "email": "benja124@gmail.com",
    "edad": 20
}

while True:
    print("---MENU---")
    print("[1] Ver ficha")
    print("[2] Editar dato")
    print("[3] Salir")

    opc = int(input("elige una opcion"))

    if opc == 1:
        print(ficha)
    elif opc == 2:
        print(f"la ficha actual es: {ficha}")
        remplazar = input("que vas a editar (nombre, telefono, email,edad)")
    elif opc == 3:
        print("saliste del programa")
        break