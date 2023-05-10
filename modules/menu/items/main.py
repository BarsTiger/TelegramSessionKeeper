from .config import config_submenu_item
from .create_session import create_new_session_item
from ..dynamic.get_code import get_code_submenu_item


items_list = [
    create_new_session_item,
    get_code_submenu_item,
    config_submenu_item
]
