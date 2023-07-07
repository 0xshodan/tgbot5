from tortoise import Tortoise, run_async
from db.models import User
from aiogram import Bot

async def init_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['db.models']}
    )
    await Tortoise.generate_schemas()
run_async(init_db())

async def send_url(url: str):
    bot = Bot("6343457869:AAGbJUKd6LaDNxcMLK0sE2w7D5pkws2chAE")
    users = await User.all()
    for user in users:
        await bot.send_message(user.tgid, url)
    await bot.close()

