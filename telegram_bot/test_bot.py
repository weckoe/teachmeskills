import telebot
from telebot import types

API_TOKEN = "1827046423:AAEtXx9tssHYBpsWn1fx11s_CKox538GeqU"

bot = telebot.TeleBot(API_TOKEN)

users = {}


def is_valid_name_surname(name_surname):
    return not (" " in name_surname or len(name_surname) < 2)


@bot.message_handler(content_types=["text"])
def start(message):
    user_id = message.from_user.id
    if message.text == "Регистрация":
        # create empty user
        users[user_id] = {}
        remove_initial_keyboard(user_id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == "Логин":
        remove_initial_keyboard(user_id, "Логин я сделаю дома :)")
    else:
        render_initial_keyboard(user_id)


def get_name(message):
    user_id = message.from_user.id
    name = message.text.title()
    if is_valid_name_surname(name):
        users[user_id]["name"] = name.title()
        bot.send_message(user_id, "Какая у тебя фамилия?")
        bot.register_next_step_handler(message, get_surname)
    else:
        bot.send_message(user_id, "Введите корректное имя")
        bot.register_next_step_handler(message, get_name)


def get_surname(message):
    surname = message.text
    user_id = message.from_user.id
    if is_valid_name_surname(surname):
        users[user_id]["surname"] = surname.title()
        bot.send_message(user_id, "Сколько тебе лет?")
        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(user_id, "Введите корректную фамилию")
        bot.register_next_step_handler(message, get_surname)


def get_age(message):
    age_text = message.text
    user_id = message.from_user.id
    if age_text.isdigit():
        age = int(age_text)
        if not 10 <= age <= 100:
            bot.send_message(user_id, "Введите реальный возраст, пожалуйста")
            bot.register_next_step_handler(message, get_age)
        else:
            users[user_id]["age"] = int(age)
            name = users[user_id]["name"]
            surname = users[user_id]["surname"]
            question = f"Тебе {age} лет и тебя зовут {name} {surname}?"
            render_yes_now_keyboard(user_id, question, "reg")
    else:
        bot.send_message(user_id, "Введите цифрами, пожалуйста")
        bot.register_next_step_handler(message, get_age)


@bot.callback_query_handler(func=lambda call: call.data.startswith("reg_"))
def callback_worker(call):
    user_id = call.from_user.id
    if call.data == "reg_yes":
        bot.send_message(user_id, "Спасибо, я запомню!")
        # pretend that we save in database
    elif call.data == "reg_no":
        # remove user
        users.pop(user_id, None)
        render_initial_keyboard(user_id)


def render_yes_now_keyboard(user_id: int, question: str, prefix: str):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Да", callback_data=f"{prefix}_yes")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="Нет", callback_data=f"{prefix}_no")
    keyboard.add(key_no)
    bot.send_message(user_id, text=question, reply_markup=keyboard)


def render_initial_keyboard(user_id: int):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    register_button = types.KeyboardButton("Регистрация")
    login_button = types.KeyboardButton("Логин")
    keyboard.add(register_button, login_button)
    bot.send_message(user_id, "Выберите действие", reply_markup=keyboard)


def remove_initial_keyboard(user_id: int, message: str):
    keyboard = types.ReplyKeyboardRemove()
    bot.send_message(user_id, message, reply_markup=keyboard)


if __name__ == "__main__":
    bot.polling(none_stop=True)
