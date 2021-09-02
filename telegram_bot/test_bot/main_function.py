
import sqlite3
import csv

from main_features import to_do, check_todo_file
from keyboard import render_yes_now_keyboard, render_initial_keyboard, remove_initial_keyboard
from constants import bot

DB_FILE_USERS = "db/all_users"

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
    elif message.text == "Создание ToDo":
        remove_initial_keyboard(user_id, "Введите название задания:")
        bot.register_next_step_handler(message, to_do)
    elif message.text == "ToDo на сегодня":
        check_todo_file(user_id)
        render_initial_keyboard(user_id)
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
        if not 10 <= age <= 300:
            bot.send_message(user_id, "Введите реальный возраст, пожалуйста")
            bot.register_next_step_handler(message, get_age)
        else:
            users[user_id]["age"] = int(age)
            name = users[user_id]["name"]
            surname = users[user_id]["surname"]
            question = f"Тебе {age} лет и тебя зовут {name} {surname}?"
            render_yes_now_keyboard(user_id, question, "reg")
            making_db()
            with sqlite3.connect(DB_FILE_USERS) as conn:
                cursor = conn.cursor()
                cursor.execute(f"""
                    INSERT INTO users(user_id, user_name, user_surname, age)
                    VALUES ('{user_id}', '{name}', '{surname}', '{age}')
                """)
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


def making_db():
    with sqlite3.connect(DB_FILE_USERS) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            user_name VARCHAR(15) NOT NULL,
            user_surname VARCHAR(15) NOT NULL UNIQUE,
            age INTEGER
            )
        """)

# 18:32 40

if __name__ == "__main__":
    bot.polling(none_stop=True)
