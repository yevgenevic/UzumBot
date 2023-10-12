from aiogram import types

btn3 = [
    [types.InlineKeyboardButton(text="Выбрать все", callback_data="vse"),
     types.InlineKeyboardButton(text="Beauty4you", callback_data="beauty4you"),
     types.InlineKeyboardButton(text="Lucky kids", callback_data="luckykids"),
     ],
    [types.InlineKeyboardButton(text="Top Price", callback_data="topprice"),
     types.InlineKeyboardButton(text="to.Be", callback_data="tobe"),
     types.InlineKeyboardButton(text="Smoke Cases", callback_data="smokecases")]
]

btn_подтверждение = [
    [
        types.InlineKeyboardButton(text='да', callback_data='да'),
        types.InlineKeyboardButton(text='нет', callback_data='нет')
    ]
]

commands = [
    types.BotCommand(command="start", description="Start"),
    types.BotCommand(command="report", description="Отчеты"),
]
