# El objetivo de este ejercicio es convertir una cadena en una nueva cadena en la que cada carácter de la nueva cadena sea "(" si ese carácter aparece sólo una vez en la cadena original, o ")" si ese carácter aparece más de una vez en la cadena original. Ignora las mayúsculas cuando determines si un carácter es un duplicado.

def duplicate_encode(word):
    word = word.upper()
    var = ""
    for i in word :
        if word.count(i) == 1:
            var += "("
        else :
            var += ")"
 
    return var       


def scount(s):
   return False


print(duplicate_encode('Success'))