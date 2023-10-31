# Escribe un programa en Python que solicite al usuario ingresar un número entero no negativo y luego calcule y muestre el factorial de ese número.
        

def factorial(num) :
    a = 1
    
    if num == 0 :
        return 1
    elif num < 0:
        print("No se puede calcular el factorial de un número negativo")
    
    else : 
        for i in range(1, num +1) :
            a *= i
            
        return a
    
print(factorial(10))    