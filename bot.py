from aiogram import Bot, Dispatcher, F
from aiogram.enums import InputMediaType, ChatType
from aiogram.filters import CommandStart, StateFilter, Filter, Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery,Message, ContentType, InputMediaPhoto, BotCommand)

import texts, keyboards, users, feedback, topics

storage: MemoryStorage = MemoryStorage()
bot: Bot = Bot('')
dp: Dispatcher = Dispatcher(storage=storage)


class Filter_by_topic(Filter):
    def __init__(self, topic_list: list) -> None:
        self.topic_list = topic_list

    async def __call__(self, message: Message) -> bool:
        if message.reply_to_message is not None:
            return message.reply_to_message.forum_topic_created.name in self.topic_list
        else:
            return False

class Check_in_ban(Filter):
    def __init__(self) -> None:
        self.ban_ids = users.get_ids_ban()

    async def __call__(self, message: Message) -> bool:
        return not message.from_user.id in self.ban_ids

class Check_in_admin(Filter):
    def __init__(self) -> None:
        self.admins_ids = users.get_ids_admins()

    async def __call__(self, message: Message) -> bool:
        return  message.from_user.id in self.admins_ids

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
    fill_16 = State()
    fill_17 = State()
    fill_18 = State()
    fill_19 = State()
    fill_20 = State()
    fill_21 = State()
    fill_22 = State()
    fill_23 = State()
    fill_24 = State()

async def set_main_menu(bot:Bot):
    main_menu_commands = [
        BotCommand(command='/menu',
                   description='Переход в меню')]
    await bot.set_my_commands(main_menu_commands)

class Check_command_ban(Filter):
    def __init__(self) -> None:
        self.command = '/ban'

    async def __call__(self, message: Message) -> bool:
        return  self.command in message.text

#Забанить пользователя
@dp.message(F.content_type == ContentType.TEXT, Check_in_admin(), Check_command_ban())
async def ban1(message: Message):
    s = message.text.split('@')[1]
    users.add_to_ban(s)
    await bot.send_message(chat_id=message.chat.id, text=f'Пользователь @{s} забанен!')

#Добавить топик в список молчания
@dp.message(Check_in_admin(), Command(commands='set1'))
async def admin_set1(message:Message):
    topics.add_topic_in_list(id=message.message_thread_id, name=message.reply_to_message.forum_topic_created.name)

#Бот удаляет все сообщения в группе с нужным топиком
@dp.message(Filter_by_topic(topics.get_topics_names()))
async def command_start(message: Message):
    await bot.delete_message(message.chat.id, message.message_id)
    #await bot.send_message(message.chat.id, "Попал?", message_thread_id=message.message_thread_id)
    #print(*message.reply_to_message, sep='\n')

@dp.message(~Check_in_ban())
async def command_ban(message: Message):
    await message.answer(texts.text0)

@dp.callback_query(Check_in_ban(), F.data == 'menu')
@dp.message(Check_in_ban(), CommandStart, StateFilter(default_state))
async def command_start(message: Message, state: State):
    users.add_user(message)
    await state.clear()
    await bot.send_message(chat_id=message.from_user.id, text=texts.text1, reply_markup=keyboards.keyboard1)

@dp.callback_query(Check_in_ban(), F.data == 'button_1_pressed', StateFilter(default_state))
async def command1(callback: CallbackQuery, state: State):
    await bot.send_message(chat_id=callback.message.chat.id, text=texts.text2, reply_markup=keyboards.keyboard2)
    feedback.create_current_feedback(callback.from_user.id)
    await state.set_state(FSMFillForm.fill_1)

@dp.callback_query(Check_in_ban(), F.data == 'button_4_pressed', StateFilter(FSMFillForm.fill_1))
async def command4(callback: CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=callback.message.chat.id, text=texts.text3)
    await state.set_state(FSMFillForm.fill_2)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_2))
async def get_text1(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Название должности:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text4)
    await state.set_state(FSMFillForm.fill_3)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_3))
async def get_text2(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Задачи сотрудника:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text5)
    await state.set_state(FSMFillForm.fill_4)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_4))
async def get_text3(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Место работы:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text6)
    await state.set_state(FSMFillForm.fill_5)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_5))
async def get_text4(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Название организации-нанимателя:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text7)
    await state.set_state(FSMFillForm.fill_6)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_6))
async def get_text5(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Заработная плата:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text8, reply_markup=keyboards.keyboard3)
    await state.set_state(FSMFillForm.fill_7)

@dp.callback_query(Check_in_ban(), F.data == 'button_skip_pressed', StateFilter(FSMFillForm.fill_7))
async def get_text6_1(callback: CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=callback.message.chat.id, text=texts.text9)
    await state.set_state(FSMFillForm.fill_8)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_7))
async def get_text6_2(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Ссылка на вакансию:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text9)
    await state.set_state(FSMFillForm.fill_8)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_8))
async def get_text7(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Контакты для связи:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text10, reply_markup=keyboards.keyboard4)
    await state.set_state(FSMFillForm.fill_9)

@dp.callback_query(Check_in_ban(), F.data == 'button_skip_pressed2', StateFilter(FSMFillForm.fill_9))
async def check_text(callback: CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=callback.message.chat.id, text=texts.text11, reply_markup=keyboards.keyboard5)
    await state.set_state(FSMFillForm.fill_10)

@dp.message(Check_in_ban(), F.content_type.in_({ContentType.PHOTO, ContentType.VIDEO}), StateFilter(FSMFillForm.fill_9))
async def get_media8(message: Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id, text=texts.text11, reply_markup=keyboards.keyboard5)
    if message.photo:
        key = 'Фото'
        val = message.photo[-1].file_id
    elif message.video:
        key = 'Видео'
        val = message.video.file_id
    feedback.add_to_current_feedback(message.from_user.id, key=key, val=val)
    await state.set_state(FSMFillForm.fill_10)

@dp.callback_query(Check_in_ban(), F.data == 'button_5_pressed', StateFilter(FSMFillForm.fill_10))
async def check1(callback: CallbackQuery, state: FSMContext):
    text = ''
    data = feedback.get_current_feedback(callback.from_user.id)
    for key, val in data.items():
        if key not in ['Фото', 'Видео']:
            text += f'{key} {val}\n'
    if 'Фото' in data:
        if isinstance(data['Фото'], list):
            media = []
            for i in range(len(data['Фото'])):
                media.append(InputMediaPhoto(type=InputMediaType.PHOTO, media=data['Фото'][i], caption=text))
            await bot.send_media_group(chat_id=callback.from_user.id, media=media)
        else:
            await bot.send_photo(chat_id=callback.from_user.id, photo=data['Фото'], caption=text)
    elif 'Видео' in data:
        await bot.send_video(chat_id=callback.from_user.id, video=data['Видео'], caption=text)
    else:
        await bot.send_message(chat_id=callback.from_user.id, text=text)
    await bot.send_message(chat_id=callback.from_user.id, text='Для публикации объявления отправьте его на проверку администратору', reply_markup=keyboards.keyboard6)
    await state.set_state(FSMFillForm.fill_11)

@dp.callback_query(Check_in_ban(), F.data == 'button_6_pressed', StateFilter(FSMFillForm.fill_11))
async def check2(callback: CallbackQuery, state: FSMContext):
    if F.data == 'button_6_pressed':
        feedback.send_current_feedback_to_moderator(callback.from_user.id)
        await bot.send_message(chat_id=callback.from_user.id, text=texts.text12)
        moderator = users.get_id_moderator()
        text = f'От пользователя @{callback.from_user.username}:\n'
        data = feedback.get_current_feedback(callback.from_user.id)
        for key, val in data.items():
            if key not in ['Фото', 'Видео']:
                text += f'{key} {val}\n'
        if 'Фото' in data:
            if isinstance(data['Фото'], list):
                media = []
                for i in range(len(data['Фото'])):
                    media.append(InputMediaPhoto(type=InputMediaType.PHOTO, media=data['Фото'][i], caption=text))
                await bot.send_media_group(chat_id=moderator, media=media)
            else:
                await bot.send_photo(chat_id=moderator, photo=data['Фото'], caption=text+texts.text_dop_info)
        elif 'Видео' in data:
            await bot.send_video(chat_id=moderator, video=data['Видео'], caption=text+texts.text_dop_info)
        else:
            await bot.send_message(chat_id=moderator, text=text+texts.text_dop_info)
    else:
        feedback.dell_current_feedback(callback.from_user.id)
        await bot.send_message(chat_id=callback.from_user.id, text=texts.text12)
    await state.clear()

@dp.callback_query(Check_in_ban(), F.data == 'button_2_pressed', StateFilter(default_state))
async def command5(callback: CallbackQuery, state: State):
    await bot.send_message(chat_id=callback.message.chat.id, text=texts.text14, reply_markup=keyboards.keyboard2)
    feedback.create_current_feedback(callback.from_user.id)
    await state.set_state(FSMFillForm.fill_12)

@dp.callback_query(Check_in_ban(), F.data == 'button_4_pressed', StateFilter(FSMFillForm.fill_12))
async def command6(callback: CallbackQuery, state: FSMContext):
    feedback.create_current_feedback(callback.from_user.id)
    await bot.send_message(chat_id=callback.message.chat.id, text=texts.text15)
    await state.set_state(FSMFillForm.fill_13)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_13))
async def get_text8(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Наименование', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text16)
    await state.set_state(FSMFillForm.fill_14)

@dp.message(Check_in_ban(), F.content_type == ContentType.PHOTO, StateFilter(FSMFillForm.fill_15))
async def get_media10(message: Message):
    key = 'Фото'
    val = message.photo[-1].file_id
    feedback.add_to_current_feedback(message.from_user.id, key=key, val=val)

@dp.message(Check_in_ban(), F.content_type.in_({ContentType.PHOTO, ContentType.VIDEO}), StateFilter(FSMFillForm.fill_14))
async def get_media9(message: Message, state: FSMContext):
    if message.photo:
        key = 'Фото'
        val = message.photo[-1].file_id
    elif message.video:
        key = 'Видео'
        val = message.video.file_id
    await state.set_state(FSMFillForm.fill_15)
    await bot.send_message(chat_id=message.chat.id, text=texts.text17)
    feedback.add_to_current_feedback(message.from_user.id, key=key, val=val)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_15))
async def get_text10(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Описание', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text18)
    await state.set_state(FSMFillForm.fill_16)

@dp.message(Check_in_ban(),  F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_16))
async def get_text11(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Стоимость', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text19)
    await state.set_state(FSMFillForm.fill_17)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_17))
async def get_text12(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Скидка для общинников', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text20)
    await state.set_state(FSMFillForm.fill_18)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_18))
async def get_text13(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Контакты', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text11, reply_markup=keyboards.keyboard5)
    await state.set_state(FSMFillForm.fill_10)

@dp.callback_query(Check_in_ban(), F.data == 'button_complain_pressed')
async def get_complain(callback: CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=callback.message.chat.id, text=texts.text21, reply_markup=keyboards.keyboard8)
    await state.set_state(FSMFillForm.fill_20)

@dp.message(Check_in_ban(), F.content_type.in_({ContentType.TEXT, ContentType.PHOTO, ContentType.VIDEO}), StateFilter(FSMFillForm.fill_20))
async def get_complain2(message: Message, state: FSMContext):
    moderator = users.get_id_moderator()
    await bot.send_message(chat_id=moderator, text=f'Получена жалоба от пользователя @{message.from_user.username}')
    await message.send_copy(chat_id=moderator)
    await bot.send_message(chat_id=message.chat.id, text=texts.text22)
    await state.clear()

@dp.callback_query(Check_in_ban(), F.data == 'button_3_pressed')
async def get_info_kb(callback: CallbackQuery, state: FSMContext):
    await bot.send_message(chat_id=callback.message.chat.id, text=texts.text23, reply_markup=keyboards.keyboard8)
    feedback.create_current_feedback(callback.from_user.id)
    await state.set_state(FSMFillForm.fill_21)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_21))
async def get_info_kb1(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='ФИО:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text23_2)
    await state.set_state(FSMFillForm.fill_22)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_22))
async def get_info_kb2(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Номер телефона:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text24)
    await state.set_state(FSMFillForm.fill_23)

@dp.message(Check_in_ban(), F.content_type == ContentType.TEXT, StateFilter(FSMFillForm.fill_23))
async def get_info_kb3(message: Message, state: FSMContext):
    feedback.add_to_current_feedback(message.from_user.id, key='Дата рождения:', val=message.text)
    await bot.send_message(chat_id=message.chat.id, text=texts.text25)
    await state.set_state(FSMFillForm.fill_24)

@dp.message(Check_in_ban(), F.content_type == ContentType.VIDEO_NOTE, StateFilter(FSMFillForm.fill_24))
async def get_info_kb4(message: Message, state: FSMContext):
    await bot.send_message(chat_id=message.chat.id, text=texts.text26, reply_markup=keyboards.keyboard8)
    await state.clear()
    text = f'Получена заявка от пользователя @{message.from_user.username}:\n'
    data = feedback.get_current_feedback(message.from_user.id)
    for key, val in data.items():
        text += f'{key} {val}\n'
    await bot.send_message(chat_id=7393932451, text=text)


# Запускаем пуллинг
if __name__ == '__main__':
    dp.startup()
    dp.run_polling(bot, skip_updates=False)