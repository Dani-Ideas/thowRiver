class automatRside:
    def __init__(self, Rside):
        self.Rside = Rside

    def checkstatus(self, side):
        if "Granjero" in side:
            if "Gallina" in side and "Lobo" in side and "Maíz" in side:
                side.remove("Granjero")
                side.remove("Gallina")
                self.Rside.append("Granjero")
                self.Rside.append("Gallina")
            elif "Lobo" in side and "Gallina" not in side:
                side.remove("Granjero")
                side.remove("Lobo")
                self.Rside.append("Granjero")
                self.Rside.append("Lobo")##
            #elif "Maíz" in side and "Lobo" not in side and "Gallina" not in side:
            #    side.remove("Granjero")
            #    side.remove("Maíz")
            #    self.Rside.append("Granjero")
            #    self.Rside.append("Maíz")
            elif "Gallina" in side and "Maíz" in side and "Lobo" not in side:
                side.remove("Granjero")
                side.remove("Maíz")
                self.Rside.append("Granjero")
                self.Rside.append("Maíz")
            elif "Gallina" in side and "Maíz" not in side and "Lobo" not in side:
                side.remove("Granjero")
                side.remove("Gallina")
                self.Rside.append("Granjero")
                self.Rside.append("Gallina")
        else: 
            print("Pipipi")
        return self.Rside
