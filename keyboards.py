from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
    text='Разместить сообщение в теме "Вакансии"',
    callback_data='button_1_pressed')],
                     [InlineKeyboardButton(
    text='Разместить сообщение в теме "Покупай у Своих"',
    callback_data='button_2_pressed')],
                     [InlineKeyboardButton(
    text='Подать заявку на вступление в кибердружину',
    callback_data='button_3_pressed')]])

keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
    text='Приступить к заполнению формы',
    callback_data='button_4_pressed')]])