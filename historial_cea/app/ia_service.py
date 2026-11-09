import random

def generar_comentario_ia(nombre_participante, lista_notas, nombre_taller):
    if not lista_notas:
        return f"El participante {nombre_participante} aún no cuenta con evaluaciones registradas en el taller {nombre_taller} para generar un análisis."

    # Calculamos el promedio de las notas para "simular" el análisis de la IA
    promedio = sum(lista_notas) / len(lista_notas)
    
    # Creamos respuestas lógicas basadas en el promedio
    if promedio >= 85:
        return f"El participante {nombre_participante} demuestra un rendimiento excelente en {nombre_taller}, con un promedio de {promedio:.2f}. Se recomienda seguir motivando su aprendizaje."
    elif promedio >= 51:
        return f"El participante {nombre_participante} tiene un rendimiento regular en {nombre_taller}, con un promedio de {promedio:.2f}. Se sugiere reforzar los temas vistos en clase."
    else:
        return f"El participante {nombre_participante} presenta dificultades en {nombre_taller}, con un promedio de {promedio:.2f}. Se recomienda un acompañamiento pedagógico personalizado."