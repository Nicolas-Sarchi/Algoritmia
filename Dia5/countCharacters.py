# La idea principal es contar todos los caracteres que aparecen en una cadena. Si tienes una cadena como aba, entonces el resultado debería ser {'a': 2, 'b': 1}.

# ¿Y si la cadena está vacía? Entonces el resultado debería ser un objeto literal vacío, {}

def scount(s):
    if (s) == 0 :
        return {}
    else:
        chars = {}
        for i in s :
            chars[i] += 1
    return chars


print (acount("paxo"))        
            