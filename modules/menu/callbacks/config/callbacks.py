from modules.decorators.callback import callback
from modules.config import config


@callback
def edit_config_callback(field: str, comments: str, default: str = None):
    print(f'Current value is {config.get(field)}')
    print(f'Default value is {default}. Press Enter to restore it')
    config[field] = input(f'{field} ({comments}) > ')
    if config[field] in ['None', 'none']:
        del config[field]

    if config[field] == '' and default is not None:
        config[field] = default
    elif default is None:
        del config[field]
