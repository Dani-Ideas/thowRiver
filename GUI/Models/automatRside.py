from .base_know import basic_rules

class automatRside:
    def __init__(self, Rside):
        self.Rside = Rside

    def checkstatus(self, side):
        if "A" in side:
            rules_applid, result=basic_rules(side,True)
            if "R001" in rules_applid and "R003" in rules_applid and "R005" in rules_applid:
                # le dio prioridad a la regla R001 ya que es la que no pone en peligro a ninguno de los items
                self.Rside.append(side.pop(side.index("A")))
                self.Rside.append(side.pop(side.index("B")))
            elif "R005" in rules_applid and "R003" in rules_applid:
                self.Rside.append(side.pop(side.index("A")))
                self.Rside.append(side.pop(side.index("C")))
            elif "R005" in rules_applid and "R001" in rules_applid:
                self.Rside.append(side.pop(side.index("A")))
                self.Rside.append(side.pop(side.index("D")))
            elif "R001" in rules_applid:
                self.Rside.append(side.pop(side.index("A")))
                self.Rside.append(side.pop(side.index("B")))
        else: 
            print("Pipipi")
        return self.Rside, rules_applid
        