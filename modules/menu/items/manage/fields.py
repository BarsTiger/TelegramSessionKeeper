from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
from ...callbacks.overkill import overkill_callback
from ...callbacks.load_sessions import load_sessions_callback
from ...dynamic import update
from ...dynamic import delete


def get_items_list(menu: CursesMenu):
    _ = [
        update.get_submenu_item,
        delete.get_submenu_item,
        lambda _: FunctionItem('Delete overkill sessions', function=overkill_callback),
        lambda _: FunctionItem('Load new sessions in folder', function=load_sessions_callback)
    ]
    return [x(menu) for x in _]
