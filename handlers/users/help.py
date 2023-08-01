from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("🇺🇿 - Salom menga instagramdan havolani yuboring\n"
            "Men Reels, Photos, Posts yuklay olaman .\n\n"

            "🇷🇺 - Привет скинь мне ССЫЛКУ с инстаграма\n"
            "Я могу скачать RReels, Photos, Posts.\n\n"
    
            "🇺🇸 - Hey send me the link from instagram"
            "I can download Reels, Photos, Posts.")

    await message.answer(text)
