from aiogram.utils import executor
from create_bot import dp
from Procfile.handlers import client


async def on_startup(_):
    print('Бот вышел в online')


client.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # Команда запуска бота
