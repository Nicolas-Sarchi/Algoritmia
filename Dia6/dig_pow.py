# Dado un número entero positivo n escrito como abcd... (siendo a, b, c, d... dígitos) y un número entero positivo p

# queremos encontrar un número entero positivo k, si existe, tal que la suma de los dígitos de n llevados a las potencias sucesivas de p sea igual a k * n.
# Dicho de otro modo:

# ¿Existe un número entero k tal que : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# Si es el caso devolveremos k, si no devolveremos -1.

# Nota: n y p se darán siempre como números enteros estrictamente positivos.



def dig_pow(n, p):
    total =  0
    for i in str(n) :
       total += pow(int(i), p) 
       p = p+1
    
    k = total / n
    
    if total % n == 0:
        return int(k)
    
    else :
        return -1
    

    

print(dig_pow(92234324324234, 1))    
 