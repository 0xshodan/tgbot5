
from aiogram.dispatcher.filters import CommandStart
from aiogram import types, Dispatcher
from db.models import User
from tortoise.exceptions import DoesNotExist
from loader import bot


async def welcome_handler(message: types.Message):
    try:
        await User.get(tgid = message.from_user.id)
    except DoesNotExist:
        await User.create(
            tgid=message.from_user.id,
            )
    await message.answer("Ожидайте сообщений")

async def admin_handler(message: types.Message):
    url = message.text.replace("/send_url ", "")
    users = await User.all()
    for user in users:
        await bot.send_message(user.tgid, url)

def register_all_handlers(dp: Dispatcher):
    dp.register_message_handler(welcome_handler, CommandStart(), state="*")
    dp.register_message_handler(admin_handler, commands=["send_url"], state="*")