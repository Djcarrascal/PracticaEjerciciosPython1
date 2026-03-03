producto = int(input("Ingrese el valor del producto en dólares: "))
iva = producto * 0.19
total = producto + iva

print(f"Valor Bruto: ${producto:.2f}")
print(f"Iva: ${iva:.2f}")
print(f"Total compra: ${total:.2f}")