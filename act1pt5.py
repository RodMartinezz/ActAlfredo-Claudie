def obtener_valor_difuso(respuesta):
    opciones = {
        '1': 1.0,   # Sí
        '2': 0.75,  # Probablemente sí
        '3': 0.5,   # No lo sé / Neutro
        '4': 0.25,  # Probablemente no
        '5': 0.0    # No
    }
    return opciones.get(respuesta, 0.5)

def jugar_akinator_difuso():
    print("¡Bienvenido al Akinator de Películas Nivel Avanzado!")
    print("Piensa en una de estas 12 películas:")
    print("1. Matrix           5. El Padrino       9. Buscando a Nemo")
    print("2. Titanic          6. Avatar           10. El Origen (Inception)")
    print("3. Jurassic Park    7. Scarface         11. King Kong")
    print("4. El Rey León      8. Gladiador        12. El Diario de Noah")
    print("13. the great showman")
    print("\nResponde a las preguntas con los siguientes números:")
    print("1 = Sí | 2 = Probablemente sí | 3 = No lo sé | 4 = Probablemente no | 5 = No\n")

    # Base de conocimiento (8 atributos): 
    # [Ciencia ficción/Efectos, Romance, Animales/Criaturas, Época/Pasado, Crimen/Mafia, Animada, Otro mundo/Fantasía, Violencia/Acción intensa]
    peliculas = {
        "Matrix":                [1.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.25, 1.0, 0.0, 0.0],
        "Titanic":               [0.25, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        "Jurassic Park":         [1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.75, 0.0, 0.0],
        "El Rey León":           [0.0, 0.5, 1.0, 0.0, 0.0, 1.0, 0.0, 0.25, 1.0, 0.0],
        "El Padrino":            [0.0, 0.5, 0.0, 1.0, 1.0, 0.0, 0.0, 0.75, 0.0, 0.0],
        "Avatar":                [1.0, 0.75, 1.0, 0.0, 0.0, 0.25, 1.0, 0.75, 0.0, 0.0],
        "Scarface":              [0.0, 0.0, 0.0, 0.75, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0],
        "Gladiador":             [0.0, 0.25, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
        "Buscando a Nemo":       [0.0, 0.25, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0],
        "El Origen (Inception)": [1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.75, 0.0, 0.0],
        "King Kong":             [0.75, 0.5, 1.0, 1.0, 0.0, 0.0, 0.25, 0.75, 0.0, 0.0],
        "El Diario de Noah":     [0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        "The Great Showman":     [0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0]
    }

    preguntas = [
        "1. ¿La película destaca por sus efectos especiales o elementos de ciencia ficción?",
        "2. ¿La historia se centra fuertemente en el amor o un drama romántico?",
        "3. ¿Los animales o criaturas tienen un papel central en la trama?",
        "4. ¿La trama transcurre en el pasado (eventos históricos o de otra época)?",
        "5. ¿La historia trata principalmente sobre el crimen organizado, drogas o mafia?",
        "6. ¿Es una película animada (dibujos 2D o animación 3D)?",
        "7. ¿La historia se desarrolla en el espacio, en sueños o en un mundo fantástico/inventado?",
        "8. ¿La película tiene violencia explícita, disparos o batallas intensas?",
        "9. ¿La película se centra en la música o el entretenimiento?",
        "10. ¿La película transcurre en el mar?"
    ]

    respuestas_usuario = []

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

    mejor_coincidencia = None
    menor_distancia = float('inf')

    for nombre, valores_pelicula in peliculas.items():
        distancia_total = sum(abs(u - p) for u, p in zip(respuestas_usuario, valores_pelicula))
        
        if distancia_total < menor_distancia:
            menor_distancia = distancia_total
            mejor_coincidencia = nombre

    # La distancia máxima ahora es 8.0 porque hay 8 preguntas
    certeza = (1 - (menor_distancia / 10.0)) * 100

    print("\n" + "="*50)
    print(f"¡El sistema ha procesado tus respuestas!")
    print(f"Estoy un {certeza:.1f}% seguro de que estás pensando en: **{mejor_coincidencia}**")
    print("="*50)

if __name__ == "__main__":
    jugar_akinator_difuso()