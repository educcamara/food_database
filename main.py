from food import Food


def show_list(lst: [Food]) -> str:
    pass


def show_compact_list(lst: [Food]) -> str:
    pass


def create_food():
    pass


def edit_food():
    pass


def delete_food():
    pass


def main():
    food_list: [Food] = []
    command_dict = {
        '1': 'show_list',
        '1.1': 'show_compact_list',
        '2': 'create_food',
        '3': 'edit_food',
        '4': 'delete_food'
    }


if __name__ == '__main__':
    main()
