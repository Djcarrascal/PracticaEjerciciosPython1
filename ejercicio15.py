sueldo = int(input("Ingrese su sueldo mensual: "))
if sueldo < 1500000:
    impuesto = 0

elif sueldo >= 1500000 and sueldo < 3000000:
    impuesto = sueldo * 0.05

elif sueldo >= 3000000:
    impuesto = sueldo * 0.10

print(f"Su impuesto es de: {impuesto}")
print(f"Su sueldo neto después de impuestos es: {sueldo - impuesto}")