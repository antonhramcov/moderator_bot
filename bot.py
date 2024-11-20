from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, StateFilter, Filter
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery,Message, BotCommand, ContentType)

import feedback
import texts, keyboards, users

storage: MemoryStorage = MemoryStorage()
bot: Bot = Bot('8042028214:AAGXYWA3Cz_iMjVqyGbSbkXTFtlj6hTQPKY')
dp: Dispatcher = Dispatcher(storage=storage)

topic_list = ['Вакансии']

class Filter_by_topic(Filter):
    def __init__(self, topic_list: list) -> None:
        self.topic_list = topic_list

    async def __call__(self, message: Message) -> bool:
        if message.reply_to_message is not None:
            return message.reply_to_message.forum_topic_created.name in self.topic_list
        else:
            return False

class FSMFillForm(StatesGroup):
    fill_1 = State()
    fill_2 = State()
    fill_3 = State()
    fill_4 = State()
    fill_5 = State()
    fill_6 = State()
    fill_7 = State()
    fill_8 = State()
    fill_9 = State()
    fill_10 = State()
    fill_11 = State()
    fill_12 = State()
    fill_13 = State()
    fill_14 = State()
    fill_15 = State()

#Бот удаляет все сообщения в группе с нужным топиком
@dp.message(Filter_by_topic(topic_list))
async def command_start(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    #await bot.send_message(message.chat.id, "Попал?", message_thread_id=message.message_thread_id)
    #print(*message.reply_to_message, sep='\n')

@dp.message(CommandStart, StateFilter(default_state))
async def command_start(message: Message):
    users.add_user(message)
    if not users.check_in_ban(message):
        await message.answer(texts.text1, reply_markup=keyboards.keyboard1)
    else:
        await message.answer(texts.text0)

@dp.callback_query(F.data == 'button_1_pressed', StateFilter(default_state))
async def command1(callback: CallbackQuery, state: State):
    await bot.send_message(chat_id=callback.message.chat.id, text=texts.text2, reply_markup=keyboards.keyboard2)
    feedback.create_current_feedback(callback.from_user.id)
    await state.set_state(FSMFillForm.fill_1)

@dp.callback_query(F.data == 'button_4_pressed', StateFilter(FSMFillForm.fill_1))
async def command4(callback: CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=callback.message.chat.id, text=texts.text3)
    await state.set_state(FSMFillForm.fill_2)

@dp.message(F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_2))
async def get_text1(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Название должности:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text4)
    await state.set_state(FSMFillForm.fill_3)

@dp.message(F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_3))
async def get_text2(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Задачи сотрудника:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text5)
    await state.set_state(FSMFillForm.fill_4)

@dp.message(F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_4))
async def get_text3(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Место работы:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text6)
    await state.set_state(FSMFillForm.fill_5)

@dp.message(F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_5))
async def get_text4(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Название организации-нанимателя:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text7)
    await state.set_state(FSMFillForm.fill_6)

@dp.message(F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_6))
async def get_text5(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Заработная плата:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text8)
    await state.set_state(FSMFillForm.fill_7)

@dp.message(F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_7))
async def get_text6(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Ссылка на вакансию:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text9)
    await state.set_state(FSMFillForm.fill_8)

@dp.message(F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_8))
async def get_text7(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Контакты для связи:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text10)
    await state.set_state(FSMFillForm.fill_9)

@dp.message(F.content_type == ContentType.PHOTO, StateFilter(FSMFillForm.fill_9))
async def get_media8(message: Message, state: FSMContext):
    #feedback.add_to_current_feedback(message.from_user.id, key='Фото:', val=message.photo.file)
    await bot.send_message(chat_id=message.chat.id, text=texts.text10)
    await state.set_state(FSMFillForm.fill_9)

@dp.message(F.content_type == ContentType.VIDEO, StateFilter(FSMFillForm.fill_9))
async def get_media9(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Видео:', val=message.video.file_id)
    


# Запускаем пуллинг
if __name__ == '__main__':
    dp.startup()
    dp.run_polling(bot, skip_updates=False)