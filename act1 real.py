def obtener_valor_difuso(respuesta):
    """Convierte la respuesta en texto a un valor de lógica difusa entre 0.0 y 1.0"""
    opciones = {
        '1': 1.0,   # Sí
        '2': 0.75,  # Probablemente sí
        '3': 0.5,   # No lo sé / Neutro
        '4': 0.25,  # Probablemente no
        '5': 0.0    # No
    }
    return opciones.get(respuesta, 0.5) # Devuelve neutro por defecto si hay error

def jugar_akinator_difuso():
    print("¡Bienvenido al Akinator de Películas!")
    print("Piensa en una de estas 5 películas:")
    print("- Matrix\n- Titanic\n- Jurassic Park\n- El Rey León\n- El Padrino\n")
    print("Responde a las preguntas con los siguientes números:")
    print("1 = Sí | 2 = Probablemente sí | 3 = No lo sé | 4 = Probablemente no | 5 = No\n")

    # Base de conocimiento: [Ciencia ficción/Efectos, Romance/Drama trágico, Animales/Criaturas, Época/Pasado, Crimen/Mafia]
    peliculas = {
        "Matrix":        [1.0, 0.25, 0.0, 0.0, 0.5],
        "Titanic":       [0.25, 1.0, 0.0, 1.0, 0.0],
        "Jurassic Park": [1.0, 0.0, 1.0, 0.0, 0.0],
        "El Rey León":   [0.0, 0.75, 1.0, 0.0, 0.0],
        "El Padrino":    [0.0, 0.75, 0.0, 1.0, 1.0]
    }

    preguntas = [
        "¿La película destaca por sus efectos especiales o elementos de ciencia ficción?",
        "¿La historia se centra fuertemente en el amor o un drama romántico/familiar?",
        "¿Los animales o criaturas (reales, animadas o extintas) tienen un papel central?",
        "¿La trama transcurre en el pasado (eventos históricos o de época)?",
        "¿La historia trata principalmente sobre el crimen organizado o la mafia?"
    ]

    respuestas_usuario = []

    # Realizar las preguntas
    for pregunta in preguntas:
        while True:
            print(f"\n{pregunta}")
            respuesta = input("Tu respuesta (1-5): ").strip()
            if respuesta in ['1', '2', '3', '4', '5']:
                valor_difuso = obtener_valor_difuso(respuesta)
                respuestas_usuario.append(valor_difuso)
                break
            else:
                print("Por favor, ingresa un número válido del 1 al 5.")

    # Calcular la similitud usando lógica difusa (Menor distancia = Mayor coincidencia)
    mejor_coincidencia = None
    menor_distancia = float('inf')

    for nombre, valores_pelicula in peliculas.items():
        # Calculamos la distancia absoluta entre las respuestas del usuario y el perfil de la película
        distancia_total = sum(abs(u - p) for u, p in zip(respuestas_usuario, valores_pelicula))
        
        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            mejor_coincidencia = nombre

    # Porcentaje de certeza basado en la distancia máxima posible (5 preguntas * diferencia máxima de 1.0 = 5.0)
    certeza = (1 - (menor_distancia / 5.0)) * 100

    print("\n" + "="*40)
    print(f"¡El sistema ha procesado tus respuestas!")
    print(f"Estoy un {certeza:.1f}% seguro de que estás pensando en: **{mejor_coincidencia}**")
    print("="*40)

if __name__ == "__main__":
    jugar_akinator_difuso()