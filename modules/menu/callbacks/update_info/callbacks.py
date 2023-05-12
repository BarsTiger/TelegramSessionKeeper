from modules.decorators.callback import async_callback
from modules.client import GeneratedClient
from modules.config import sessions
from modules.config.models import SessionConfig
from rich import print


@async_callback
async def update_info_callback(session_name: str):
    print('Getting info about profile...')
    await (client := GeneratedClient(name=session_name)).start()

    sessions[session_name] = SessionConfig(
        id=client.me.id,
        phone=f'+{client.me.phone_number}',
        profile_name=client.me.first_name + (f' {client.me.last_name}' if client.me.last_name else ''),
        username=client.me.username
    ).json()
    print(f'[green]Updated[/] info for {session_name}. Go back in menu to update it in interface...')

    await client.stop()
    input()
