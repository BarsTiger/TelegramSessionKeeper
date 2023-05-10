from cursesmenu.items import FunctionItem
from ...callbacks.config.callbacks import edit_config_callback


items_list = [
    FunctionItem('app_id', function=edit_config_callback,
                 args=['app_id', 'Telegram app_id, can be obtained on my.telegram.org']),
    FunctionItem('api_hash', function=edit_config_callback,
                 args=['api_hash', 'Telegram api_hash, can be obtained on my.telegram.org']),
    FunctionItem('device_model', function=edit_config_callback,
                 args=['device_model', 'Device model is first line of information about login in devices settings. ',
                       'Session Keeper']),
    FunctionItem('app_version', function=edit_config_callback,
                 args=['app_version', 'App version is second line of information about login in devices settings.',
                       'DO NOT DEAUTH THIS SESSION']),
    FunctionItem('system_version', function=edit_config_callback,
                 args=['system_version',
                       'App version is shown in detailed information about login in devices settings. ',
                       'Bars\'s TelegramSessionKeeper']),
]
