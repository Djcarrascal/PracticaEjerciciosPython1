Nota1 = int(input("Ingrese la primera nota: "))
Nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))
Promedio = (Nota1 + Nota2 + nota3) / 3

print(f"El promedio de las notas es: {Promedio}")

if Promedio <= 54:
    print("Tu calificacion es baja, has reprobado.")
elif Promedio >= 55 and Promedio <= 59:
    print("Tu calificacion es insuficiente, pero entras a habilitacion.")
else:
    print("Tu calificacion es buena, has aprobado.")