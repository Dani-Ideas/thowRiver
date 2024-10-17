from .automatRside import automatRside
from .automatLside import automatLside
from .base_know import vars
from .base_know import default_case

class comunicator:
    def __init__(self, initialStatusLeft=None, initialStatusRight=None, goalLeft=None, goalRight=None):
        # # Inicial condition if is NONE get default_case
        self.initialStatusLeft = initialStatusLeft if initialStatusLeft is not None else default_case["initialStatusLeft"]
        self.initialStatusRight = initialStatusRight if initialStatusRight is not None else default_case["initialStatusRight"]
        # Final condition or Goal
        self.goalLeft = goalLeft if goalLeft is not None else default_case["goalLeft"]
        self.goalRight = goalRight if goalRight is not None else default_case["goalRight"]
        #it's only a flag
        self.rule = "start"
        self.right = []
        self.left = []

    def start(self):
        self.left = self.initialStatusLeft
        self.right = self.initialStatusRight
        automatRight = automatRside(self.right)
        automatLeft = automatLside(self.left)
        log = []  # registro de movimientos
        log_logic = []  # registro de lógica
        #n=0

        while not self.goal():
            #n+=1
            log.append([self.right.copy(), self.left.copy()])
            log_logic.append(self.rule)
            print(f"Del lado izquierdo se encuentran {self.left}, del lado derecho se encuentra {self.right}, se usó la regla {self.rule}")
            self.right, self.rule = automatRight.checkstatus(self.left)
            log.append([self.right.copy(), self.left.copy()])
            log_logic.append(self.rule)
            print(f"Del lado izquierdo se encuentran {self.left}, del lado derecho se encuentra {self.right}, se usó la regla {self.rule}")
            if self.goal():
                break
            self.left, self.rule = automatLeft.checkstatus(self.right)


        print(f"\n¡Éxito! Todos han cruzado el río.\nLado izquierdo: {self.left}\nLado derecho: {self.right}")
        log = self.replace_variables(log, vars)
        print(log)
        return log

    def goal(self):
        return sorted(self.goalLeft) == sorted(self.left) and sorted(self.goalRight) == sorted(self.right)

    def replace_variables(self, array, vars_dict):
        result = []
        for sublist in array:
            new_sublist = []
            for subsublist in sublist:
                new_subsublist = [vars_dict.get(item, item) for item in subsublist]
                new_sublist.append(new_subsublist)
            result.append(new_sublist)
        return result
