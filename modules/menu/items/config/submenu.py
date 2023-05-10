from ...menu import menu
from cursesmenu import CursesMenu
from cursesmenu.items import SubmenuItem
from .fields import items_list


config_submenu = CursesMenu(
    title='Config'
)
for item in items_list:
    config_submenu.items.append(item)

config_submenu_item = SubmenuItem(
    text='Edit config',
    submenu=config_submenu,
    menu=menu
)
