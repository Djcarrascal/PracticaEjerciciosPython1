print("\nBienvenido a tu cajero")
saldo = 1000
print(f"\nTu saldo es de:{saldo}")
print("\nQue quieres hacer hoy?")
print("\n1 - Consultar Saldo")
print("2 - Retirar dinero")
print("3 - Depositar")


eleccion = int(input("\nIngrese el numero se su eleccion: "))

if eleccion == 1:
    print(f"\nSu saldo es de: {saldo}")

if eleccion == 2:
    retiro = int(input("Ingrese el monto a retirar: "))
    print(f"\nRetiro efecturado, su nuevo saldo es de: {saldo - retiro}")


