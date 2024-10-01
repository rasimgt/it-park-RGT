from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
Token = os.getenv('Token')
bot = Bot(token=Token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(mesage: types.Message):
    await message.answer('Привет я первый бот, могу отвечать')
if __name__ == '__main__':
    executor.start_polling(dp)
    