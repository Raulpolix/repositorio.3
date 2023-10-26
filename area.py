#funcion calcular area triangulo

def calc_area(base,altura):
        area= (base * altura)/2  #formula del area dentro de la funcion
        return area
altura_in= float(input("altura "))   #pedimos los dos datos nevcesarios(base y altura)
base_in= float(input("Base "))

area_calc=calc_area(altura_in,base_in)
print(area_calc)  #Lo imprimimos



