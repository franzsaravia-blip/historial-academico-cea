from huggingface_hub import InferenceClient

# Usamos el modelo gratuito FLAN-T5 de Google alojado en Hugging Face
def generar_comentario_ia(nombre_participante, lista_notas, nombre_taller):
    # Si no hay notas, devolvemos un mensaje por defecto
    if not lista_notas:
        return "El participante aún no cuenta con evaluaciones registradas para generar un análisis."

    # Inicializamos el cliente (no requiere token para modelos públicos)
    client = InferenceClient(model="google/flan-t5-large")
    
    # Construimos el texto (prompt) que leerá la IA
    prompt = f"Eres un facilitador experto. El participante {nombre_participante} tiene las siguientes notas en el taller {nombre_taller}: {', '.join(map(str, lista_notas))}. Escribe un breve comentario de 2 líneas sobre su rendimiento académico y qué debería mejorar."
    
    try:
        # Hacemos la llamada a la IA
        respuesta = client.text_generation(prompt, max_new_tokens=100)
        return respuesta
    except Exception as e:
        return f"Error al conectar con la IA: {str(e)}"