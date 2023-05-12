from modules.decorators.callback import async_callback
from modules.config import sessions
from modules.client import GeneratedClient
from modules.config.models import SessionConfig
from rich import print
import os


@async_callback
async def load_sessions_callback():
    if input('Do you really want to load all .session files that are not in database? '
             'It may cause bans of your accounts, because logging to many sessions from one IP at once may seem'
             'suspicious for Telegram (y/N) ') not in ['y', 'Y']:
        return
    print('Loading...')
    loaded = 0
    for file in os.listdir():
        if not file.endswith('.session'):
            continue
        file = file.replace('.session', '')
        if file not in sessions.keys():
            try:
                await (client := GeneratedClient(name=file)).start()
                sessions[file] = SessionConfig(
                    id=client.me.id,
                    phone=client.me.phone_number,
                    profile_name=client.me.first_name + (f' {client.me.last_name}' if client.me.last_name else ''),
                    username=client.me.username
                ).json()
                print(f'[green]Created[/] session {file}...')
                await client.stop()
                loaded += 1
            except Exception as e:
                print(f'[red]Error[/] loading {file} ({e}), skipping...')

    print(f'[green]Created[/] {loaded} records...')
    input()
