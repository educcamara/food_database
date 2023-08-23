class Food:
    def __init__(self, name, prot, carb, fat):
        self.name = name.lower()
        self.prot = float(prot)
        self.carb = float(carb)
        self.fat = float(fat)

    @property
    def compact_text(self):
        return f"{self.name.capitalize():<15}|{self.prot:>10}|{self.carb:>10}|{self.fat:>10}"

    @property
    def text(self):
        return (f"{self.name.capitalize()}: \n"
                f"\t| Proteínas:    {self.prot}\n"
                f"\t| Carboidratos: {self.carb}\n"
                f"\t| Gorduras:     {self.fat}")

    def __repr__(self):
        return f"{self.name.capitalize()}"

    def config(self, attr: str, value: str):
        if attr != "name":
            value = float(value)
        setattr(self, attr, value)
