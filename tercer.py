sueldo_base = int(input('Sueldo base: '))
venta1 = int(input('Venta 1: '))
venta2 = int(input('Venta 2: '))
venta3 = int(input('Venta 3: '))

comision = (venta1 + venta2 + venta3) * 0.1
sueldo_final = sueldo_base + comision

print('Comision: ', comision)
print('Sueldo final: ', sueldo_final)
