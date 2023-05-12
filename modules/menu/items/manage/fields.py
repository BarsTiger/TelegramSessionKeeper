from cursesmenu import CursesMenu
from ...dynamic import update
from ...dynamic import delete


def get_items_list(menu: CursesMenu):
    _ = [
        update.get_submenu_item,
        delete.get_submenu_item
    ]
    return [x(menu) for x in _]
