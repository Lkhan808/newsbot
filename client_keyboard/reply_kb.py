from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="ВЫБЕРИТЕ ОПЦИЮ ⤵⤵⤵⤵")
b1 = KeyboardButton(text="/allnews")
b2 = KeyboardButton(text="/freshnews")
reply_keyboard.row(b1, b2)