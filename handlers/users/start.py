from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.menu import lang
from loader import dp,db
from states.state import Lang,Update

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        id = message.from_user.id
        malumot = db.filter(tg_id=id)
        if malumot[2] == id:
            if  malumot[3] == 'ru':
                await message.answer(f"Отправьте мне ссылку на Instagram – ролики, посты, медиа\n"
                                     "\n"
                                     f"Администратор - @UmarPython\n"
                                     f"Свяжитесь с @UmarPython, чтобы создать бота")

            elif  malumot[3] == 'en':
                await message.answer(f"Send me Instagram link - Reels, Posts , Media\n"
                                     f"\n"
                                     f"Admin - @UmarPython \n"
                                     f"Contact @UmarPython to Create a Bot")
            elif malumot[3] == 'uz':
                await message.answer(f"Menga Instagram havolasini yuboring - Reels, Posts , Media\n"
                                     f"\n"
                                     f"Admin - @UmarPython \n"
                                     f"Bot Yaratish uchun @UmarPython ga Murojaat Qiling")

    except:
        await message.answer('Please, Choose language',reply_markup=lang)
        await Lang.lang.set()

@dp.callback_query_handler(state=Lang.lang)
async def bot_echo(message: types.CallbackQuery, state: FSMContext):
    await message.message.delete()
    try:
        db.add_user(name=message.from_user.full_name, username=message.from_user.username ,tg_id=message.from_user.id,lang=message.data)

        if message.data == 'ru':
            await message.message.answer(f"Отправьте мне ссылку на Instagram – ролики, посты, медиа\n"
            "\n"
            f"Администратор - @UmarPython\n"
            f"Свяжитесь с @UmarPython, чтобы создать бота")

        elif message.data== 'en':
            await message.message.answer(f"Send me Instagram link - Reels, Posts , Media\n"
                                 f"\n"
                                 f"Admin - @UmarPython \n"
                                 f"Contact @UmarPython to Create a Bot")
        elif message.data== 'uz':
            await message.message.answer(f"Menga Instagram havolasini yuboring - Reels, Posts , Media\n"
                                 f"\n"
                                 f"Admin - @UmarPython \n"
                                 f"Bot Yaratish uchun @UmarPython ga Murojaat Qiling")



    except:
        await message.answer("Try again!", show_alert=True)
    await state.finish()


@dp.message_handler(commands='lang')
async def l(message: types.Message):
    await message.answer('Choose language 🌐',reply_markup=lang)
    await Update.lang.set()

@dp.callback_query_handler(state=Update.lang)
async def bot(message:types.CallbackQuery,state:FSMContext):
    await message.message.delete()
    try:
        db.update_lang(lang=message.data,tg_id=message.from_user.id)

        if message.data == 'ru':
            await message.message.answer(f"Отправьте мне ссылку на Instagram – ролики, посты, медиа\n"
                                         "\n"
                                         f"Администратор - @UmarPython\n"
                                         f"Свяжитесь с @UmarPython, чтобы создать бота")

        elif message.data == 'en':
            await message.message.answer(f"Send me Instagram link - Reels, Posts , Media\n"
                                         f"\n"
                                         f"Admin - @UmarPython \n"
                                         f"Contact @UmarPython to Create a Bot")
        elif message.data == 'uz':
            await message.message.answer(f"Menga Instagram havolasini yuboring - Reels, Posts , Media\n"
                                         f"\n"
                                         f"Admin - @UmarPython \n"
                                         f"Bot Yaratish uchun @UmarPython ga Murojaat Qiling")



    except:
        await message.answer("Try again!", show_alert=True)
    await state.finish()
