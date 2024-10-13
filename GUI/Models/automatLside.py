class automatLside:
    def __init__(self, Lside):
        self.Lside = Lside

    def checkstatus(self, side):
        if "Granjero" in side:
            if "Gallina" in side and "Lobo" in side and "Maíz" in side:
                return ["Vacio"]
            elif "Gallina" in side and "Lobo" not in side and "Maíz" not in side:
                side.remove("Granjero")
                self.Lside.append("Granjero")#
            elif "Lobo" in side and "Gallina" in side:
                side.remove("Gallina")
                side.remove("Granjero")
                self.Lside.append("Gallina")
                self.Lside.append("Granjero")
            elif "Gallina" not in side and "Lobo" in side and "Maíz" in side:
                side.remove("Granjero")
                self.Lside.append("Granjero")
        return self.Lside
