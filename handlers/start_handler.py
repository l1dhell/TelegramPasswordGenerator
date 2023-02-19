from aiogram import types
from keyboards import user_keyboard

async def start_handler(message: types.Message):
    await message.reply("Hello!",reply_markup=user_keyboard)
