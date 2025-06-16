import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import load_config, Config
import handlers
#from handlers import other_handlers, user_handlers


async def main() -> None:
    
    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(handlers.user_router)
    dp.include_router(handlers.other_router)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())