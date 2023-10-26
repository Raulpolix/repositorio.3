#recibo la altura
altura = float(input("Introduce la altura inicial"))
#recibo la gravedad
gravedad = float(input("Introduce la gravedad"))
#reecibo el instante en el que quieero medir su posicion
tiempo = float(input("Introduce el instante en el que quieres meedir su posicion"))
#calculamos su altura final
alturafinal=altura-0.5*gravedad*tiempo**2
#se la comunicamos
print(alturafinal)
