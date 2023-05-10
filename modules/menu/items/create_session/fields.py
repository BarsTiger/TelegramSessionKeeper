from cursesmenu.items import FunctionItem
from ...callbacks.create_session.callbacks import create_session_callback


create_new_session_item = FunctionItem(
    'Add new session', function=create_session_callback
)
