from modules.menu.menu import menu


def callback(f):
    def wrapper(*args, **kwargs):
        menu.pause()
        f(*args, **kwargs)
        menu.resume()

    return wrapper


def async_callback(f):
    def wrapper(*args, **kwargs):
        import asyncio
        menu.pause()
        asyncio.run(f(*args, **kwargs))
        menu.resume()

    return wrapper
