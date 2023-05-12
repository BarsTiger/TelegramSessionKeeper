from ...menu import menu
from cursesmenu import CursesMenu
from modules.custom_items.DynamicSubmenu import DynamicSubmenuItem
from ..common_generators.valid_sessions_generator import generate_sessions_list
from ...callbacks.get_code import get_code_callback


get_code_submenu = CursesMenu(
    title='Sessions'
)

get_code_submenu_item = DynamicSubmenuItem(
    text='Get confirmation code',
    generator=generate_sessions_list,
    args=['Get code for', get_code_callback],
    menu=menu
)
