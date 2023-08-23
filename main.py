from food import Food


def show_list(lst: [Food]):
    if lst:
        text = ""
        for food in lst:
            text += f"{food.text}\n"
    else:
        text = "Não há comidas!"
    print(text)


def show_compact_list(lst: [Food]):
    if lst:
        text = ""
        for food in lst:
            text += f"{food.compact_text}\n"
    else:
        text = "Não há comidas!"
    print(text)


def create_food(lst: [Food]):
    f_name = input("Nome: ")
    f_prot = input("Prot: ")
    f_carb = input("Carb: ")
    f_fat = input("Fat: ")
    lst.append(Food(f_name, f_prot, f_carb, f_fat))


def edit_food(lst: [Food]):
    f_name = input("Digite o nome da comida: ").lower()
    food_name_dict = {f.name: f for f in lst}
    if f_name in food_name_dict:
        food = food_name_dict[f_name]
        attr, value = input("digite o nome do atributo e seu novo valor: ").split()
        food.config(attr, value)
    else:
        print("Não há essa comida!")


def delete_food(lst: [Food]):
    f_name = input("Digite o nome da comida: ").lower()
    food_name_dict = {f.name: f for f in lst}
    if f_name in food_name_dict:
        food = food_name_dict[f_name]
        lst.remove(food)
    else:
        print("Não há essa comida!")


def main():
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
          "4 - Remover comida")
    while True:
        command_input = input("Digite seu comando: ")
        if command_input not in command_dict:
            break
        command = command_dict.get(command_input)
        command(food_list)


if __name__ == '__main__':
    main()
