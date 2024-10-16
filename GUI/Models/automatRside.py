from .base_know import basic_rules

class automatRside:
    def __init__(self, Rside):
        self.Rside = Rside

    def checkstatus(self, side):
        if "A" in side:
            rules_applid, result=basic_rules(side,True)
            if "R001" in rules_applid and "R003" in rules_applid and "R005" in rules_applid:
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
    
    def danger(self,side, result):
        danger_level = 0

        if "A" not in side:
            if "B" in side and "C" in side:
                danger_level += 2  
            if "B" in side and "D" in side:
                danger_level += 1  

        return danger_level