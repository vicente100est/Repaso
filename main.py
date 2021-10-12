#Ejercicio N1

a=float(input("Ingresa a: "))
b=float(input("Ingresa b: "))
c=float(input("Ingresa c: "))

resultado =((c+5)*(b**2-3*a*c)*a**2)/(4*a)

print(f"El resultado es {resultado}")

#Ejercicio N2

a=input("a: ")
b=input("b: ")

a,b=b,a

print(f"El Nuevo de a valor es: {a}")
print(f"El Nuevo de b valor es: {b}")

#Ejercicio N3
import math as mt
r=float(input("Ingrese el Radio: "))
area=mt.pi*r**2
longitud=2*mt.pi*r

print(f"El area es: {area:.1f}")
print(f"La longitud es: {longitud:.1f}")

#Ejercicio N4
precio=float(input("Ingresa el precio: "))
procentaje=float(input("Ingresa el procentaje de descuento: "))
_por=procentaje/100
descuento=precio*_por
total=precio-descuento
print(f"El total a pagar es: ${total:.2f}MXN")