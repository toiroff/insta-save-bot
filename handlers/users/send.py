from aiogram import types
from loader import dp,bot
from aiogram.dispatcher.filters import Text
from insta import instadownloader

@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send(messgae:types.Message):
    await messgae.answer('🔍')

    link = messgae.text
    data = instadownloader(link=link)
    if data == 'Bad':
        await messgae.answer("⚠️ Media faylni yuklab bo'lmadi.")

    else:
        if data['type'] == 'post-image':
                await messgae.answer_photo(photo=data['media'],caption='@Insta_Saver_uzbot orqali yuklab olindi 📥')

        if data['type'] == 'image':
                await messgae.answer_photo(photo=data['media'],caption='@Insta_Saver_uzbot orqali yuklab olindi 📥')


        elif data['type'] == 'video':
            await messgae.answer_video(video=data['media'],caption='@Insta_Saver_uzbot orqali yuklab olindi 📥')

        elif data['type'] == 'carousel':
            for i in data['media']:
                await messgae.answer_document(document=i,caption='@Insta_Saver_uzbot orqali yuklab olindi 📥')





