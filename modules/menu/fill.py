from .menu import menu


def fill_menu():
    from .items.main import items_list
    for item in items_list:
        menu.items.append(item)
