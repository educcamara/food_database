class Food:
    def __init__(self, name, prot, carb, fat):
        self.name = name.lower()
        self.prot = float(prot)
        self.carb = float(carb)
        self.fat = float(fat)

    @property
    def compact_text(self):
        return f"{self.name:<10}|{self.prot:>6}|{self.carb:>6}|{self.fat:>6}"

    @property
    def text(self):
        return (f"{self.name.capitalize()}: \n"
                f"\tProteínas:    {self.prot}\n"
                f"\tCarboidratos: {self.carb}\n"
                f"\tGorduras:     {self.fat}")

    def __repr__(self):
        return f"{self.name.capitalize()}"

    def config(self, obj: str, value: str):
        if obj != "name":
            value = float(value)
        setattr(self, obj, value)
