vars = {
    "A": "Granjero",
    "B": "Gallina",
    "C": "Lobo",
    "D": "Maíz"
}

def basic_rules(facts, direction):
    reglas_aplicadas = []
    result=[]
    
    # R001: Si Granjero y Gallina están juntos y direction=True (derecha), ambos cruzan hacia la derecha
    if "A" in facts and "B" in facts and direction:
        reglas_aplicadas.append("R001") 
        result.append(["A","B"]) # Granjero y Gallina cruzan

    # R002: Si Granjero y Gallina están juntos y direction=False (izquierda), solo el Granjero cruza
    if "A" in facts and "B" in facts and not direction:
        reglas_aplicadas.append("R002")
        result.append("A") # Solo el Granjero cruza

    # R003: Si Granjero y Lobo están juntos y direction=True (derecha), ambos cruzan hacia la derecha
    if "A" in facts and "C" in facts and direction:
        reglas_aplicadas.append("R003")
        result.append(["A", "C"])  # Granjero y Lobo cruzan

    # R004: Si Granjero y Lobo están juntos y direction=False (izquierda), solo el Granjero cruza
    if "A" in facts and "C" in facts and not direction:
        reglas_aplicadas.append("R004")
        result.append("A")  # Solo el Granjero cruza

    # R005: Si Granjero y Maíz están juntos y direction=True (derecha), ambos cruzan hacia la derecha
    if "A" in facts and "D" in facts and direction:
        reglas_aplicadas.append("R005")
        result.append(["A", "D"])  # Granjero y Maíz cruzan

    # R006: Si Granjero y Maíz están juntos y direction=False (izquierda), solo el Granjero cruza
    if "A" in facts and "D" in facts and not direction:
        reglas_aplicadas.append("R006")
        result.append("A")  # Solo el Granjero cruza

    return reglas_aplicadas, result
