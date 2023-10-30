#¡Los trolls están atacando tu sección de comentarios!

#Una forma habitual de afrontar esta situación es eliminar todas las vocales de los comentarios de los trolls, neutralizando así la amenaza.

#Tu tarea es escribir una función que tome una cadena y devuelva una nueva cadena con todas las vocales eliminadas.

def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u" ]
    
    for l in string_:
        if l.lower() in vowels:
            string_= string_.replace(l, "")
    
    return string_        

print(disemvowel("PACO"))