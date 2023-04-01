from config import bot, dp
from aiogram.utils import executor
from parsing.parsing import main
import logging

from handlers import client_commands


async def on_startup(_):
    main()


client_commands.register_handlers_client(dp)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
