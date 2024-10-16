from .automatRside import automatRside
from .automatLside import automatLside
from .base_know import vars

class comunicator:
    def __init__(self):
        self.right = []
        self.left = []
        # only flag to log
        self.rule="start"
        # Inicial condition
        self.initialStatusLeft = ["A", "B", "C", "D"]
        self.initialStatusRight = []
        # Final condition or Goal
        self.goalLeft=self.initialStatusRight
        self.goalRigth=self.initialStatusLeft

    
    def start(self):
        self.left = self.initialStatusLeft
        self.right= self.initialStatusRight
        automatRight = automatRside(self.right)
        automatLeft = automatLside(self.left)
        log=[]#registro de movimietos
        log_logic=[]#registro de logica


        while not self.goal():
            log.append([self.right.copy(), self.left.copy()])
            log_logic.append(self.rule)
            print(f"Del lado izquierdo se encuentran {self.left}, del lado derecho se encuentra {self.right}, se uso la regla {self.rule}")
            self.right ,self.rule= automatRight.checkstatus(self.left)
            log.append([self.right.copy(), self.left.copy()])
            log_logic.append(self.rule)
            print(f"Del lado izquierdo se encuentran {self.left}, del lado derecho se encuentra {self.right}, se uso la regla {self.rule}")
            if  self.goal():
                break
            self.left, self.rule = automatLeft.checkstatus(self.right)

        print(f"\n¡Éxito! Todos han cruzado el río.\nLado izquierdo: {self.left}\nLado derecho: {self.right}")
        log = self.replace_variables(log, vars)
        print(log)
        return log
    
    def goal(self):
        if self.goalLeft==self.left and self.goalRigth==self.right:
            return True
        else:
            return False
    def replace_variables(self, array, vars_dict):
        result = []
        for sublist in array:
            new_sublist = []
            for subsublist in sublist:
                new_subsublist = [vars_dict.get(item, item) for item in subsublist]
                new_sublist.append(new_subsublist)
            result.append(new_sublist)
        return result
