from rich import print

from modules.menu.menu import menu
from ..exceptions.pretty_exception import PrettyException


def callback(f):
    def wrapper(*args, **kwargs):
        menu.pause()
        try:
            f(*args, **kwargs)
        except Exception as e:
            print(PrettyException(e).pretty_exception)
            input()
        menu.resume()

    return wrapper


def async_callback(f):
    def wrapper(*args, **kwargs):
        import asyncio
        menu.pause()
        try:
            asyncio.run(f(*args, **kwargs))
        except Exception as e:
            print(PrettyException(e).pretty_exception)
            input()
        menu.resume()

    return wrapper
