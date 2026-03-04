numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
if numero1 > numero2:
    print(f"El número {numero1} es mayor que el número {numero2}.")
elif numero2 > numero1:
    print(f"El número {numero2} es mayor que el número {numero1}.")
else:
    print("Ambos números son iguales.")