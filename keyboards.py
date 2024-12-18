from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup)

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
    text='Разместить сообщение в теме "Вакансии"',
    callback_data='button_1_pressed')],
                     [InlineKeyboardButton(
    text='Разместить сообщение в теме "Покупай у Своих"',
    callback_data='button_2_pressed')],
                     [InlineKeyboardButton(
    text='Подать заявку на вступление в кибердружину',
    callback_data='button_3_pressed')],
                     [InlineKeyboardButton(
    text='Пожаловаться',
    callback_data='button_complain_pressed')]
    ])

menu_button = InlineKeyboardButton(
    text='Вернуться в меню',
    callback_data='menu'
)

keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
    text='Приступить к заполнению формы',
    callback_data='button_4_pressed')],[menu_button]])

keyboard3 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
    text='Пропустить',
    callback_data='button_skip_pressed')]]
)

keyboard4 = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
    text='Пропустить',
    callback_data='button_skip_pressed2')]]
)

keyboard5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Проверить',
            callback_data='button_5_pressed')]
    ]
)

keyboard6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Отправить на проверку',
            callback_data='button_6_pressed')],
        [InlineKeyboardButton(
            text='Удалить объявление',
            callback_data='button_7_pressed')],
        [menu_button]
    ]
)

keyboard7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text='Опубликовать в группе',
            callback_data='button_8_pressed')],
        [InlineKeyboardButton(
            text='Удалить',
            callback_data='button_9_pressed'),
        InlineKeyboardButton(
                text='Забанить',
                callback_data='button_10_pressed')
        ]
    ]
)

keyboard8 = InlineKeyboardMarkup(inline_keyboard=[[menu_button]])
