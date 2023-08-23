from food import Food


def show(lst: [Food]):
    if lst:
        text = ""
        for food in lst:
            text += food.view()
    else:
        text = "Não há comidas!"
    return text


def show_compact(lst: [Food]):
    if lst:
        text = f"{'NOME':<10}|{'PROT':>6}|{'CARB':>6}|{'FAT':>6}\n"
        for food in lst:
            text += food.compact_view()
    else:
        text = "Não há comidas!"
    return text


def main():
    atributes = {
        "NOME": "name",
        "PROT": "prot",
        "CARB": "carb",
        "FAT": "fat"
    }

    # feijao = Food("Feijao", 1, 2, 3)
    # arroz = Food("Arroz", 10, 20, 30)
    # food_list: [Food] = [feijao, arroz]
    food_list: [Food] = []
    print("1  - Mostrar Lista (1.1 para Lista Compactada)\n"
          "2  - Adicionar Comida\n"
          "3  - Editar Comida\n"
          "4  - Remover Comida")
    while True:
        # print(food_list)
        command_input = input(" > ")
        if command_input == "1":  # MOSTRAR LISTA
            print(show(food_list))

        elif command_input == "1.1":  # MOSTRAR LISTA COMPACTADA
            print(show_compact(food_list))

        elif command_input == "2":  # ADICIONAR COMIDA
            f_name = input("Digite o nome da comida: ")
            f_prot = input("Digite quanto de proteína: ")
            f_carb = input("Digite quanto de carb: ")
            f_fat = input("Digite quanto de gordura: ")
            food_list.append(Food(f_name, f_prot, f_carb, f_fat))

        elif command_input == "3":  # EDITAR COMIDA
            if food_list:
                print(show_compact(food_list))
                f_input = input("Digite o nome da comida: ").capitalize()
                atrr, value = input("Digite o atributo que deseja mudar e seu novo valor: ").split()
                attr = atributes[atrr.upper()]
                for food in food_list:
                    if f_input == f"{food}":
                        food.config(attr, value)
            else:
                print("Não há comidas para editar!")

        elif command_input == "4":  # REMOVER COMIDA
            if food_list:
                print(show_compact(food_list))
                f_input = input("Digite o nome da comida: ").capitalize()
                for food in food_list:
                    if f_input == f"{food}":
                        food_list.remove(food)

            else:
                print("Não há comidas para remover!")

        else:  # SAIR DO PROGRAMA
            break


if __name__ == '__main__':
    main()
