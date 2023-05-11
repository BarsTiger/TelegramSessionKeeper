from modules.decorators.callback import async_callback
from modules.client import GeneratedClient
from rich import print
import os
import re


@async_callback
async def get_code_callback(session_name: str):
    print('Getting messages...')
    client = GeneratedClient(session_name)

    await client.start()

    messages = [item async for item in client.get_chat_history(777000, limit=3)]

    for message in messages:
        try:
            group = re.search(r': (\d{5})\D', message.text).groups()[0]
            print(f"Confirmation code: \n{group}")
            break
        except Exception as e:
            assert e
            continue

    print('Last messages from Telegram: ')
    for message in messages:
        print('-' * os.get_terminal_size().columns)
        print(message.date)
        print(message.text)
    print('-' * os.get_terminal_size().columns)

    await client.stop()

    input()
