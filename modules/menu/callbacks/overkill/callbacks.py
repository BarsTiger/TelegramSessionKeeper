from modules.decorators.callback import callback
from modules.config import sessions
from rich import print
import os


@callback
def overkill_callback():
    if input('Do you really want to delete overkill items in database? This will remove junk from it, '
             'but won\'t affect your sessions (y/N) ') not in ['y', 'Y']:
        return
    print('Clearing...')
    deleted = 0
    for session_name in sessions.keys():
        if not os.path.isfile(f'{session_name}.session'):
            del sessions[session_name]
            deleted += 1

    print(f'[green]Deleted[/] {deleted} records...')
    input()
