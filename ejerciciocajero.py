#Definimos los campos iniciales de bienvenida del cajero
print("\nBienvenido a tu cajero")
saldo = 1000
print(f"\nTu saldo es de:{saldo}")
operacion = int(input("\nCuantas operaciones deseas realizar hoy?: "))
for i in range(operacion):

    print("\nQue quieres hacer hoy?")
    print("\n1 - Consultar Saldo")
    print("2 - Retirar dinero")
    print("3 - Depositar")


    eleccion = int(input("\nIngrese el numero se su eleccion: "))
    while eleccion < 1 or eleccion > 3:
        print("\nOpcion no valida\n")
        eleccion = int(input("\nIngrese el numero se su eleccion: "))

    if eleccion == 1:
        print(f"\nSu saldo es de: {saldo}\n")

    elif eleccion == 2:
            retiro = int(input("\nIngrese el monto a retirar: "))

            while retiro <= 0:
                print("\nEl monto ingresado no es valido\n")
                retiro = int(input("\nIngrese el monto a retirar: "))

            if retiro <= saldo:
                saldo -= retiro
                print(f"\nRetiro efectuado!\n"
                f"\nSu nuevo saldo es de: {saldo}\n")
                
            else:
                print("\nNo tienes suficiente saldo para realizar esta operacion\n")
    if eleccion == 3:
            deposito = int(input("\nIngrese el monto a depositar: "))
            while deposito <= 0:
                print("\nEl monto ingresado no es valido\n")
                deposito = int(input("\nIngrese el monto a depositar: "))
            print(f"\nDeposito exitoso!\n"
                    f"\nSu nuevo saldo es de: {saldo + deposito}\n")
            
    print("\nGracias por usar nuestro cajero, vuelva pronto!\n")


