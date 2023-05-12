import os
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
from typing import Callable, Any

from modules.config import sessions
from modules.config.models import SessionConfig


def generate_sessions_list(menu_name: str, callback: Callable[..., Any]) -> CursesMenu:
    submenu = CursesMenu(
        title=menu_name,
        subtitle='name - phone - id - profile name - username'
    )
    for session_name in sessions.keys():
        if os.path.isfile(f'{session_name}.session'):
            submenu.items.append(FunctionItem(
                f'{session_name} - {SessionConfig(**sessions[session_name])}',
                function=callback,
                args=[session_name]
            ))

    return submenu
