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
        campo = input("que campo deseas modificar")
        nuevo = input("ingrese el nuevo dato")
        ficha[campo] = nuevo
    elif opc == 3:
        print("saliste del programa")
        print(f"tu ficha actualizada es: {ficha}")
        break