from food import Food
import pickle


def show_list(lst: [Food]):
    if lst:
        text = ""
        for food in lst:
            text += f"{food.text}\n"
    else:
        text = "Não há comidas."
    print(text)


def show_compact_list(lst: [Food]):
    if lst:
        text = (f"{'NOME':<15}|{'PROTEINAS':>10}|{'CARBS':>10}|{'GORDURAS':>10}|{'FIBRAS':>10}|\n"
                f"{'-' * 15}|{'-' * 10}|{'-' * 10}|{'-' * 10}|{'-' * 10}|\n")
        for food in lst:
            text += f"{food.name.capitalize():<15}|{food.prot:>10}|{food.carb:>10}|{food.fat:>10}|{food.fiber:>10}|\n"
    else:
        text = "Não há comidas."
    print(text)


def create_food(lst: [Food]):
    f_name = input("Nome >> ")
    f_measure = float(input("Medida total >> "))
    f_prot = float(input("Prot  >> "))
    f_carb = float(input("Carb  >> "))
    f_fat = float(input("Gord  >> "))
    f_fiber = float(input("Fibra  >> "))
    lst.append(Food(f_name, f_prot, f_carb, f_fat, f_fiber, f_measure))
    lst.sort(key=lambda f: f.name)


def edit_food(lst: [Food]):
    f_name = input("Nome da Comida >> ").lower()
    food_name_dict = {f.name: f for f in lst}
    if f_name in food_name_dict:
        attr_dict = {
            "nome": "name",
            "prot": "prot",
            "carb": "carb",
            "gord": "fat",
            "fibra": "fiber"
        }
        food = food_name_dict[f_name]
        print(f"{'NOME':<15}|{'PROT':>10}|{'CARB':>10}|{'GORD':>10}|{'FIBRA':>10}|\n"
              f"{food.name.capitalize():<15}|{food.prot:>10}|{food.carb:>10}|{food.fat:>10}|{food.fiber:>10}|")
        attr = input("Atributo >> ")
        attr = attr_dict[attr.lower()]
        if attr == "name":
            value = input("Novo valor >> ")
            food.config(attr, value)
            lst.sort(key=lambda f: f.name)
        else:
            value, measure = input("<novo_valor> <medida> >> ").split()
            food.config(attr, value, float(measure))
        print(f"Atributo <{attr}> editado com sucesso para \"{value}\".")
    else:
        print("Comida não encontrada.")


def delete_food(lst: [Food]):
    f_name = input("Nome da Comida >> ").lower()
    food_name_dict = {f.name: f for f in lst}
    if f_name in food_name_dict:
        food = food_name_dict[f_name]
        lst.remove(food)
        print(f"Comida \"{food}\" removida com sucesso.")
    else:
        print("Comida não encontrada.")


def main():
    try:
        with open("food_list", "rb") as file:
            food_list: [Food] = pickle.load(file)
    except (EOFError, FileNotFoundError):
        food_list: [Food] = []

    command_dict = {
        '1': show_list,
        '1.1': show_compact_list,
        '2': create_food,
        '3': edit_food,
        '4': delete_food
    }
    print("1 - Mostrar lista (1.1 para lista compactada)\n"
          "2 - Adicionar comida\n"
          "3 - Editar comida\n"
          "4 - Remover comida\n"
          "q - Sair do programa\n")
    while True:
        command_input = input("<comando> >> ")
        if command_input.lower() == 'q':
            with open("food_list", "wb") as file:
                pickle.dump(food_list, file)
            print("Saindo do programa...")
            break
        if command_input not in command_dict:
            print("Comando inválido")
            continue
        command = command_dict.get(command_input)
        command(food_list)


if __name__ == '__main__':
    main()
