#punto 1
#Modelo matematico
#Volumen del solido
#V_Total = (2/3) * pi * r1**3 + (1/3) * pi * r2**2 * 
import math

#punto 2
#funcion para calcular el volúmen del solido
def volumen_solido(r1, r2, h):
    volumen_mitad_esfera = (2/3) * math.pi * (r1**3)
    volumen_cono = (1/3) * math.pi * (r2**2) * h
    volumen_total = volumen_mitad_esfera + volumen_cono
    return volumen_total

#punto 3

r1 = 3
r2 = 4
#Caso 1
h1 = 9/2
volumen1 = volumen_solido(r1, r2, h1)
print(f"volumen del solido con h = 9/2 (h = {h1}): {volumen1: .4f}")

#Caso 2
h2 = 9//2
volumen2 = volumen_solido(r1, r2, h2)
print(f"volumen del solido con h = 9//2(h = {h2}): {volumen2:.4f}")

print("\nConclusión:")
if volumen1 > volumen2:
    print("El volumen usando h = 9/2 es mayor que usando h = 9//2, porque 9/2 da 4.5 y 9//2 da 4")
else:
    print("El volumen usando h = 9/2 es igual o menor, revisar calculos")

print("____________________________________________________________________")

#Punto 2
#Area lateral del vagón:
#Área = (a * b) - 2 * pi * r**2

#Funcion

def area_lateral_vagon(a, b ,r):
    area_rectangulo = a * b
    area_ruedas = 2 * math.pi * (r**2)
    area_total = area_rectangulo - area_ruedas
    return area_total

#Ejemplo
a = 4
b = 10
r = 1

area = area_lateral_vagon(a, b, r)

print(f"Area lateral del vagón (a={a}, b={b}, r={r}): {area:.4f}")

print("____________________________________________________________________")

#Punto 3
def area_circulo(r):
  return math.pi* r**2

def area_rectangulo(a,b):
    return a*b

def suma(x,y):
    return x+y

def area_lateral_carro(a1, b1, r1, a2, b2, r2 ):
    area_total_rectangulos = 2*(suma(area_rectangulo(a1, b1), area_rectangulo(a2, b2)))
    area_total_ruedas = suma(area_circulo(r1), area_circulo(r2))
    area_total = area_total_rectangulos - area_total_ruedas
    return area_total

#Ejemplo
a1 = 3
b1 = 10
r1 = 1
a2 = 4
b2 = 8
r2 = 0.5
print("Area lateral del carro:", area_lateral_carro(a1, b1, r1, a2, b2, r2))

print("____________________________________________________________________________")

#Punto 4
#Cantidad de carne de aves

def carne_aves(N, M, K):
    carne_total = (N * 6) + (M * 7) + (K * 1)
    return carne_total

#Ejemplo
print("Cantidad de carne:", carne_aves(3, 4, 8), "kilos")

print("________________________________________________________________")

#Punto 5
#Vueltas de la compra

def calculo_vueltas(P, M, H, B):
    valor_total = (P * 300) + (M * 3300) + (H * 350)
    vueltas = B - valor_total
    return vueltas

#Ejemplo
print("vueltas:", calculo_vueltas(2, 1, 6, 10000), "pesos")

print("_____________________________________________________________________")

#Punto 6
#Prestamo con interes

def prestamo_con_interes(P):
    interes_mensual = 0.03
    monto_mes1 = P * (1 + interes_mensual)
    monto_mes2 = monto_mes1 * (1 + interes_mensual)
    return monto_mes2

#Ejemplo
print("Total a pagar al final del segundo mes:", prestamo_con_interes(6000), "pesos")

print("_________________________________________________________________________")

#Punto 7
#Contagios de Covid-19

def contagios(C, D):
    total_contagios = C * (2 ** D)
    return total_contagios

#Ejemplo
print("Contagios despues de 8 dias:", contagios(200, 8))

    

