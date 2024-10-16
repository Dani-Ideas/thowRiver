from .base_know import basic_rules
class automatLside:
    def __init__(self, Lside):
        self.Lside = Lside

    def checkstatus(self, side):
        if "A" in side:
            rules_applid, result=basic_rules(side,False)
            if "R002" in rules_applid and "R004" in rules_applid:
                self.Lside.append(side.pop(side.index("A")))
                self.Lside.append(side.pop(side.index("B")))
            elif "R002" in rules_applid:
                self.Lside.append(side.pop(side.index("A")))
            elif "R004" in rules_applid and "R006" in rules_applid:
                self.Lside.append(side.pop(side.index("A")))

        return self.Lside , rules_applid
