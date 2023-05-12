from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
from ...callbacks.overkill import overkill_callback
from ...dynamic import update
from ...dynamic import delete


def get_items_list(menu: CursesMenu):
    _ = [
        update.get_submenu_item,
        delete.get_submenu_item,
        lambda _: FunctionItem('Delete overkill sessions', function=overkill_callback)
    ]
    return [x(menu) for x in _]
