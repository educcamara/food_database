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
        text = (f"{'NOME':<15}|{'PROT':>10}|{'CARB':>10}|{'GORD':>10}|\n"
                f"{'-' * 15}|{'-' * 10}|{'-' * 10}|{'-' * 10}|\n")
        for food in lst:
            text += f"{food.compact_text}|\n"
    else:
        text = "Não há comidas."
    print(text)


def create_food(lst: [Food]):
    f_name = input("Nome >> ")
    f_prot = input("Prot >> ")
    f_carb = input("Carb >> ")
    f_fat = input("Fat  >> ")
    lst.append(Food(f_name, f_prot, f_carb, f_fat))
    lst.sort(key=lambda f: f.name)


def edit_food(lst: [Food]):
    f_name = input("Nome da Comida >> ").lower()
    food_name_dict = {f.name: f for f in lst}
    if f_name in food_name_dict:
        attr_dict = {
            "nome": "name",
            "prot": "prot",
            "carb": "carb",
            "gord": "fat"
        }
        food = food_name_dict[f_name]
        attr, value = input("<atributo> <valor> >>").split()
        attr = attr_dict[attr.lower()]
        food.config(attr, value)
        print(f"Atributo <{attr}> editado com sucesso para \"{value}\".")
    else:
        print("Comida não encontrada.")
    lst.sort(key=lambda f: f.name)


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


main()
