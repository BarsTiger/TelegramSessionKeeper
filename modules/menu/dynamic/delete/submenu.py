from cursesmenu import CursesMenu
from modules.custom_items.DynamicSubmenu import DynamicSubmenuItem
from ..common_generators.valid_sessions_generator import generate_sessions_list
from ...callbacks.delete.callbacks import log_out_callback


def get_submenu_item(parent_menu: CursesMenu):
    return DynamicSubmenuItem(
        text='Delete sessions (log out)',
        generator=generate_sessions_list,
        args=['Log out from', log_out_callback],
        menu=parent_menu
    )
