
ancho = int(input("Ingrese el ancho del cuarto en metros: "))
largo = int(input("Ingrese el largo del cuarto en metros: "))
area = ancho * largo

print(f"El área del cuarto es: {area} metros cuadrados, por ende: ")

if area < 12:
    print("El cuarto es pequeño")
elif area >= 12 and area <= 20:
    print("El cuarto es mediano")
else:
    print("El cuarto es grande")