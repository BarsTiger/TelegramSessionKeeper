from cursesmenu import CursesMenu
from modules.custom_items.DynamicSubmenu import DynamicSubmenuItem
from ..common_generators.valid_sessions_generator import generate_sessions_list
from ...callbacks.update_info import update_info_callback


def get_submenu_item(parent_menu: CursesMenu):
    return DynamicSubmenuItem(
        text='Update account info',
        generator=generate_sessions_list,
        args=['Update info for', update_info_callback],
        menu=parent_menu
    )
