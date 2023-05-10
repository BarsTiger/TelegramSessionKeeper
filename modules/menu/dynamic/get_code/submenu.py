from ...menu import menu
from cursesmenu import CursesMenu
from modules.custom_items.DynamicSubmenu import DynamicSubmenuItem
from .generator import generate_get_code_menu


get_code_submenu = CursesMenu(
    title='Sessions'
)

get_code_submenu_item = DynamicSubmenuItem(
    text='Get confirmation code',
    generator=generate_get_code_menu,
    menu=menu
)
