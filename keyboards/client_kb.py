from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


AccountMenu_kb = ReplyKeyboardMarkup(row_width=1)
SubscribeAccount = KeyboardButton(text='Написать достижение 💌')
AccountMenu_kb.add(SubscribeAccount)


AccountMenu = ReplyKeyboardMarkup(row_width=1)
SubscribeAccoun = KeyboardButton(text='Посмотреть достижения 🤩')
X = KeyboardButton(text='Удалить достижения ❌')
AccountMenu.add(SubscribeAccoun, X)


Yes_No_kb = ReplyKeyboardMarkup(row_width=2)
Yes = KeyboardButton(text='Да!', callback_data='Yes')
No = KeyboardButton(text='Нет', callback_data='No')
Yes_No_kb.add(Yes, No)
