from .automatRside import automatRside
from .automatLside import automatLside

class comunicator:
    def __init__(self):
        pass
    def start(self):
        initialStatus = ["Granjero", "Gallina", "Lobo", "Maíz"]
        right = []
        left = initialStatus
        automatRight = automatRside(right)
        automatLeft = automatLside(left)
        log=[]
        while "Vacio" not in left:
            log.append([right.copy(), left.copy()]) 
            print(f"Del lado izquierdo se encuentran {left}, del lado derecho se encuentra {right}")
            right = automatRight.checkstatus(left)
            log.append([right.copy(), left.copy()]) 
            print(f"Del lado izquierdo se encuentran {left}, del lado derecho se encuentra {right}")
            left = automatLeft.checkstatus(right)

        print(f"\n¡Éxito! Todos han cruzado el río.\nLado izquierdo: {left}\nLado derecho: {right}")
        return log