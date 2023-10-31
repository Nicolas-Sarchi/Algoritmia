# Supongamos que estás desarrollando una red social simplificada y necesitas implementar la funcionalidad para gestionar las publicaciones de los usuarios. Cada publicación tiene un texto asociado, un autor y un número de "me gusta".

# Debes crear una función en Python que tome una lista de publicaciones y devuelva la publicación más popular, es decir, la publicación con más "me gusta". También debes imprimir el nombre del autor de la publicación más popular.

publicaciones = [
    {"autor": "Usuario1", "texto": "¡Hoy es un gran día!", "me_gusta": 155},
    {"autor": "Usuario2", "texto": "Disfrutando del clima soleado.", "me_gusta": 20},
    {"autor": "Usuario3", "texto": "Nueva receta deliciosa.", "me_gusta": 10},
    {"autor": "Usuario4", "texto": "Fiesta en la playa este fin de semana.", "me_gusta": 35},
    {"autor": "Usuario5", "texto": "¡Increíble concierto anoche!", "me_gusta": 28},
]


def masPopular(publicaciones) :
    masLikes = 0 
    autor = ""
    for publicacion in publicaciones:
        if publicacion["me_gusta"] > masLikes:
            masLikes = publicacion["me_gusta"]
            autor = publicacion["autor"]
    return autor

print("EL Autor de la publicacion mas popular es :", masPopular(publicaciones))        