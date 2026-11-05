import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.photo)
async def get_photo_id(message: Message):
    photo = message.photo[-1]

    await message.answer(
        f"🖼 ID фотографии:\n\n"
        f"<code>{photo.file_id}</code>",
        parse_mode="HTML"
    )


@dp.message(F.document)
async def get_document_id(message: Message):
    await message.answer(
        f"📁 ID файла:\n\n"
        f"<code>{message.document.file_id}</code>",
        parse_mode="HTML"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
