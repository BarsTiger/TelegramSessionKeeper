from modules.decorators.callback import async_callback


@async_callback
async def get_code_callback(session_name: str):
    ...
