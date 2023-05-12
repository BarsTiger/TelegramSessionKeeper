from modules.decorators.callback import async_callback
from modules.client import GeneratedClient
from modules.config import sessions
from rich import print


@async_callback
async def log_out_callback(session_name: str):
    if input('Do you really want to log out? If you don\'t have access to phone number or you are not logged in '
             'on other devices/clients, you will loose your account! (y/N) ') not in ['y', 'Y']:
        return
    print('Logging out...')
    await (client := GeneratedClient(name=session_name)).start()
    await client.log_out()
    del sessions[session_name]

    print(f'[green]Logged out[/] from {session_name}. Go back in menu to update interface...')
    input()
