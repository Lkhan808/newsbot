from config import bot, dp
from aiogram.utils import executor
from parsing.parsing import main
import logging

from handlers import commands
commands.register_message_handlers(dp)

async def on_startup(_):
    main()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
