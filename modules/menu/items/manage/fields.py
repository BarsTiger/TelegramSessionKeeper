from cursesmenu import CursesMenu
from ...dynamic import update


def get_items_list(menu: CursesMenu):
    _ = [
        update.get_submenu_item
    ]
    return [x(menu) for x in _]
