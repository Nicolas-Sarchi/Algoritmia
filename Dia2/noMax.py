# Escribe un programa en Python que encuentre el número más grande en una lista de números sin usar la función max(). Deberás implementar tu propia lógica para determinar cuál es el número más grande en la lista.

numeros = [123, 3 ,32, 4 ,5, 3, 2, 546, 43 ,34, 65 ,3]

greater = 0

for num in numeros:
    if num > greater:
        greater = num

print (greater)        

