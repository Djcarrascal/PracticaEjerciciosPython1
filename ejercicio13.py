valor_producto = float(input("Ingrese el valor del producto: "))
descuento = valor_producto * 0.10

if valor_producto > 100:
    total = valor_producto - descuento
    print(f"El valor final del producto con descuento es: {total:.3f}")
else:
    print(f"El valor del producto sin descuento es: {valor_producto:.3f}")