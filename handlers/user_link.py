import json
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ChatJoinRequest
from sqlalchemy.dialects.mssql import pyodbc



from data import config
from filters import IsGroup, IsAdmin, IsPrivate
from loader import dp, bot
from utils.db_api import quick_commands


#
# @dp.message_handler()
# async def chats(message: Message):
#     await message.answer(text=message.message_id)
users = []
with open('users.json') as f:
    templates = json.load(f)

for key in templates['users']:
    for value in key:
        if value == 'user_id':
            users.append(key[value])

users = set(users)
@dp.chat_join_request_handler()
async def some_handler(call: ChatJoinRequest):
    # await chat_member.from_user.url()
    # chats = -1001698907470
    chats = -1001705729606
    # chats = -1001855063926
    user = call.from_user.id


    if user in users:
        await call.bot.approve_chat_join_request(chat_id=chats, user_id=user)

        await call.bot.send_message(chat_id=user, text='https://t.me/+3A-jUjs7jZtlNjhi')
    dp.register_chat_join_request_handler(some_handler)
