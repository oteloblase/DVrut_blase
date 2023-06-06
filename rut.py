
import math
suma = 0
def multiplicado(lista_rut,lista_multiplos):
    return[lista_rut[i]*lista_multiplos[i] for i in range(len(lista_rut))]

lista_multiplos=[2,3,4,5,6,7,2,3]

rut = input("digite su rut sin guion \n")
lista_rut=[]
# multiplicar numeros
for i in rut:
    lista_rut.append(i)

lista_rut.reverse()

print(lista_rut)

lista_rut=[int(i) for i in lista_rut]
print(lista_rut)

lista_total=multiplicado (lista_rut,lista_multiplos)
print(lista_total)

# calcular dv

for i in lista_total:
    suma += i
print(suma)

suma_div = (math.floor(suma/11))
print (suma_div)

suma_mult = (suma_div*11)
print (suma_mult)

suma_mult_2 = (suma-suma_mult)
print (suma_mult_2)

final = (11-suma_mult_2)
print (final)

if final == 10:
    final = 'k'
    print("el digito verificador del rut: ", rut, "es: ", final)
elif final == 11:
    final = 0
    print("el digito verificador del rut: ", rut, "es: ", final)
else:
    print("el digito verificador del rut: ", rut, "es: ", final)

