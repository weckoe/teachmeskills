import csv
import os
import sqlite3



from datetime import datetime
from keyboard import render_yes_now_keyboard
from constants import FILE_PATH_2, NAMES, bot

DB_FILE_TODOS = "db/all_todos"

def check_todo_file(user_id):
    if not os.path.exists(FILE_PATH_2):
        bot.send_message(user_id, "Задач на сегодня нет")
    else:
        csv_viewing(user_id)
        # list_of_todos = csv_viewing(user_id)
        # bot.send_message(user_id, list_of_todos)

def csv_viewing(user_id):
    user_todos = []
    user_ids = []
    date_today = datetime.date(datetime.now())
    str_today = date_today.strftime("%d.%m.%Y")
    with sqlite3.connect(DB_FILE_TODOS) as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT user_todo FROM "users_todo"
            WHERE todo_date = '{str_today}'
         """)
        text_with_todos = f"Ваши задачи на сегодня: {cursor.fetchall()}"
    bot.send_message(user_id, text_with_todos)
    # with open(FILE_PATH_2, "r") as csv_file:
    #     reader = csv.DictReader(csv_file)
    #     for row in reader:
    #         user_ids.append(user_id)
    #         for i in user_ids:
    #             if user_id not in user_ids:
    #                 continue
    #             date_today = datetime.date(datetime.now())
    #             str_today = date_today.strftime("%d.%m.%Y")
    #         if row["date"] == str_today:
    #             user_todos.append(row["todo_text"])
    # if not user_todos:
    #     bot.send_message(user_id, "На сегодня для вас задач нет((")
    # else:
    #     enumerated_todos = []
    #     for index, todo in enumerate(user_todos, start=1):
    #         enumerated_todos.append(f"{index}. {todo}")
    #         todos_for_today = f"Ваши задачи на сегодня: \n"
    #         todos = "\n".join(enumerated_todos)
    #         message_to_user = f"{todos_for_today}{todos}"
    #     return message_to_user


def user_date(message, todo_text):
    making_todo_bd()
    user_id = message.from_user.id
    message_date = message.text
    question = f'Задание: {todo_text}, дата: {message_date}'
    render_yes_now_keyboard(user_id, question, "reg")
    with sqlite3.connect(DB_FILE_TODOS) as conn:
        cursor = conn.cursor()
        cursor.execute(f""" 
        INSERT INTO "users_todo"(id, user_todo, todo_date)
        VALUES ('{user_id}', '{todo_text}', '{message_date}')
        """)
    # with open(FILE_PATH_2, "a") as csv_file:
    #     writer = csv.DictWriter(csv_file, fieldnames=NAMES)
    #     writer.writeheader()
    #     writer.writerow({"user_id": user_id, "todo_text": todo_text, "date": message_date})
    # with open(FILE_PATH_2, "r") as csv_file:
    #     reader = csv.DictReader(csv_file)
    #     for row in reader:
    #         question = f'Задание: {row["todo_text"]}, дата: {row["date"]}'


def to_do(message):
    user_id = message.from_user.id
    todo_text = message.text
    bot.send_message(user_id, "Введите дату:")
    bot.register_next_step_handler(message, user_date, todo_text)


def making_todo_bd():
    with sqlite3.connect(DB_FILE_TODOS) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS "users_todo"(
            id INTEGER NOT NULL,
            user_todo VARCHAR(30) NOT NULL,
            todo_date TEXT
            )
                     """)




