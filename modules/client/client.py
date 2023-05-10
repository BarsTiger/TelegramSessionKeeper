from ..config import config
from pyrogram import Client


class GeneratedClient(Client):
    def __init__(self, name: str):
        if not config.get('api_id'):
            config['api_id'] = input('api_id from my.telegram.org: ')
        if not config.get('api_hash'):
            config['api_hash'] = input('api_hash from my.telegram.org: ')

        super().__init__(
            name=name,
            api_id=config['api_id'],
            api_hash=config['api_hash'],
            device_model=config.get('device_model', 'Session Keeper'),
            app_version=config.get('app_version', 'DO NOT DEAUTH THIS SESSION'),
            system_version=config.get('system_version', 'Bars\'s TelegramSessionKeeper')
        )
