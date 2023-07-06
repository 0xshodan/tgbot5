from aiogram import executor
from loader import dp
from handlers import register_all_handlers
from tortoise import Tortoise, run_async


async def init_db():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['db.models']}
    )
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    run_async(init_db())
    register_all_handlers(dp)
    print("started")
    executor.start_polling(dp)