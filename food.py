class Food:
    def __init__(self, name: str, prot: float, carb: float, fat: float, fiber: float, measure: float):
        self.name = name.lower()
        self.prot = self._convert_value(prot, measure)
        self.carb = self._convert_value(carb, measure)
        self.fat = self._convert_value(fat, measure)
        self.fiber = self._convert_value(fiber, measure)

    def __repr__(self):
        return f"{self.name.capitalize()}({self.prot:.2f}, {self.carb:.2f}, {self.fat:.2f}, {self.fiber:.2f})"

    def config(self, attr, value, measure: float):
        if attr != "name":
            value = self._convert_value(float(value), measure)
        else:
            value = value.lower()
        setattr(self, attr, value)

    @staticmethod
    def _convert_value(value: float, measure: float):
        return (100 * value) / measure


def show_food_list(lst: [Food]):
    if lst:
        text = ""
        for food in lst:
            text += (f"{food.name.capitalize()} (100g):\n"
                     f"\t| Proteínas:    {food.prot}\n"
                     f"\t| Carboidratos: {food.carb}\n"
                     f"\t| Gorduras:     {food.fat}\n"
                     f"\t| Fibras:       {food.fiber}\n")
    else:
        text = "Não há comidas."
    print(text)
