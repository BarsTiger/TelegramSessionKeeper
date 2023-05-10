import os
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem

from modules.config import sessions
from modules.config.models import SessionConfig
from ...callbacks.get_code import get_code_callback


def generate_get_code_menu() -> CursesMenu:
    submenu = CursesMenu(
        title='Sessions'
    )
    for session_name in sessions.keys():
        if os.path.isfile(f'{session_name}.session'):
            submenu.items.append(FunctionItem(
                f'{session_name} - {SessionConfig(**sessions[session_name])}',
                function=get_code_callback,
                args=[session_name]
            ))

    return submenu
