# El ejercicio consiste en calcular el número de dígitos pares e impares en un número entero dado.

print("\n\n")

print("Ingrese un número entero: ")	
n = int(input())

pares = 0
impares = 0

numero = str(n)

for i in numero:
    i = int(i)
    if i % 2 == 0 :
        pares += 1
    else :
        impares += 1
        
print("La cantidad de digitos pares es : "  , pares, "La cantidad de digitos impares es: " , impares )            



print("\n\n")
