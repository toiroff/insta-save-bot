from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


lang = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇷🇺 Russian",callback_data='ru')
        ],
[
            InlineKeyboardButton(text="🇺🇸 English",callback_data='en')
        ],
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek",callback_data='uz')
        ]

    ]
)