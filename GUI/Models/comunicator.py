from automatLside import automatLside
from automatRside import automatRside

def main():
    initialStatus = ["Granjero", "Gallina", "Lobo", "Maíz"]
    right = []
    left = initialStatus
    automatRight = automatRside(right)
    automatLeft = automatLside(left)
    while "Vacio" not in left:
        print(f"Del lado izquierdo se encuentran {left}, del lado derecho se encuentra {right}")
        right = automatRight.checkstatus(left)
        print(f"Del lado izquierdo se encuentran {left}, del lado derecho se encuentra {right}")

        left = automatLeft.checkstatus(right)
    print(f"\n¡Éxito! Todos han cruzado el río.\nLado izquierdo: {left}\nLado derecho: {right}")

if __name__ == "__main__":
    main()
