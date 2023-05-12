from sqlite3 import OperationalError
from rich import print
from modules.decorators.callback import async_callback
from modules.client import GeneratedClient
from modules.config import sessions
from modules.config.models import SessionConfig


@async_callback
async def create_session_callback():
    session_name = input('New session name: ')
    while session_name in sessions.keys():
        session_name = input('Session with this name is already saved. Try another name: ')

    try:
        await (client := GeneratedClient(name=session_name)).start()
        sessions[session_name] = SessionConfig(
            id=client.me.id,
            phone=client.phone_number,
            profile_name=client.me.first_name + (f' {client.me.last_name}' if client.me.last_name else ''),
            username=client.me.username
        ).json()
        print(f'[green]Created[/] session {session_name}...')
        await client.stop()
        input()

    except OperationalError:
        print('[red]Cannot create session file.[/] Try using different name...')
        input()

    except Exception as e:
        print(f'[red]Error:[/] {e}...')
        input()
        return
