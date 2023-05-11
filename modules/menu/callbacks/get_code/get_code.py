from modules.decorators.callback import async_callback
from modules.client import GeneratedClient
from rich import print


@async_callback
async def get_code_callback(session_name: str):
    print('Getting messages...')
    client = GeneratedClient(session_name)

    await client.start()
    async for message in client.get_chat_history(777000, limit=3):
        print(message.date)
        print(message.text)
        print()

    await client.stop()

    input()
