kilometros = int(input("Ingrese la cantidad de kilómetros a recorridos por el taxi: "))
tiempo = int(input("Ingrese el tiempo en minutos que duro el viaje: "))
costoxk = 800
minima = 5000

if tiempo < 10:
    print(f"El valor de su viaje es de: {minima}")
else:
    print(f"El costo de su viaje es de: {kilometros * costoxk}")
