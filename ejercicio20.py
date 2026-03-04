edad = int(input("Ingrese su edad: "))
estrato = int(input("Ingrese su estrato social (1-6): "))

if edad >= 18 and edad <25 and estrato <= 3:
    print("Aplica para el subsidio.")
else:
    print("No aplica para el subsidio.")