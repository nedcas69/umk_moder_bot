from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards import ikb_menu # Импортируем нашу клавиатуру
from loader import dp

@dp.message_handler(Command("start")) # Создаём message handler который ловит команду /menu
async def menu(message: types.Message): # Создаём асинхронную функцию
    # Отправляем сообщение пользователю
    await message.answer("Канал", reply_markup=ikb_menu)


@dp.message_handler(text='Kanal') # Создаём message handler который ловит команду /menu
async def menu(message: types.Message): # Создаём асинхронную функцию
    # Отправляем сообщение пользователю
    await message.answer("Канал", reply_markup=ikb_menu)

