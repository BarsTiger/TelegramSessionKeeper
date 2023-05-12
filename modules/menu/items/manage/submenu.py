from ...menu import menu
from cursesmenu import CursesMenu
from cursesmenu.items import SubmenuItem
from .fields import get_items_list


manage_submenu = CursesMenu(
    title='Manage'
)
for item in get_items_list(manage_submenu):
    manage_submenu.items.append(item)

manage_submenu_item = SubmenuItem(
    text='Manage/edit/delete sessions',
    submenu=manage_submenu,
    menu=menu
)
