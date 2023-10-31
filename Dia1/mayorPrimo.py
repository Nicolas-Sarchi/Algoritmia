# El ejercicio consiste en encontrar el número primo más grande menor que un número dado. Un número primo es un número mayor que 1 que solo es divisible por sí mismo y 1.


# función para saber si un numero es primo

def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            
            return False
    
    return True

# funcion para encontrar el mayor primo

def mayor_primo(n):
    for i in range(n, 1, -1):
        if es_primo(i):
            return i
        
    
  