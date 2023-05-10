from cursesmenu.items import MenuItem
from cursesmenu.curses_menu import CursesMenu
from typing import Callable, Any


class DynamicSubmenuItem(MenuItem):
    def __init__(
            self,
            text: str,
            generator: Callable[..., CursesMenu],
            menu: CursesMenu | None = None,
            args: list[Any] | None = None,
            kwargs: dict[Any, Any] | None = None,
    ) -> None:
        self._args: list[Any] | None = args
        self._kwargs: dict[Any, Any] | None = kwargs
        self._generator: Callable[..., CursesMenu] | None = generator
        self._menu: CursesMenu | None = menu
        self._submenu: CursesMenu | None = None
        super().__init__(
            text=text,
            menu=menu
        )

    @property
    def submenu(self) -> CursesMenu | None:
        return self._submenu

    @submenu.setter
    def submenu(self, submenu: CursesMenu | None) -> None:
        self._submenu = submenu
        if self._submenu is not None:
            self._submenu.parent = self._menu

    @property
    def menu(self) -> CursesMenu | None:
        return self._menu

    @menu.setter
    def menu(self, menu: CursesMenu | None) -> None:
        self._menu = menu
        if self._submenu is not None:
            self._submenu.parent = menu

    def set_up(self) -> None:
        assert self.menu is not None
        self.menu.pause()
        self.menu.clear_screen()

    def action(self) -> None:
        self.submenu = self._generator(*self._args if self._args else [],
                                       **self._kwargs if self._kwargs else {})
        self.submenu.start()

    def clean_up(self) -> None:
        assert self.menu is not None
        assert self.submenu is not None
        self.submenu.join()
        self.submenu.clear_screen()
        self.menu.resume()

    def get_return(self) -> Any:
        if self.submenu is not None:
            return self.submenu.returned_value
        return None
