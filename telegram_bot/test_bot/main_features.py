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
    date_today = datetime.date(datetime.now())
    str_today = date_today.strftime("%d.%m.%Y")
    with sqlite3.connect(DB_FILE_TODOS) as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT user_todo FROM "users_todo"
            WHERE todo_date = '{str_today}'
            AND user_id = '{user_id}';
         """)
        text_with_todos = f"Ваши задачи на сегодня: {cursor.fetchall()}"
    bot.send_message(user_id, text_with_todos)



def user_date(message, todo_text):
    making_todo_bd()
    user_id = message.from_user.id
    message_date = message.text
    question = f'Задание: {todo_text}, дата: {message_date}'
    render_yes_now_keyboard(user_id, question, "reg")
    with sqlite3.connect(DB_FILE_TODOS) as conn:
        cursor = conn.cursor()
        cursor.execute(f""" 
        INSERT INTO users_todo(user_id, user_todo, todo_date)
        VALUES ('{user_id}', '{todo_text}', '{message_date}')
        """)

def to_do(message):
    user_id = message.from_user.id
    todo_text = message.text
    bot.send_message(user_id, "Введите дату:")
    bot.register_next_step_handler(message, user_date, todo_text)

def making_todo_bd():
    with sqlite3.connect(DB_FILE_TODOS) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = 1")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users_todo(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            user_todo VARCHAR(30) NOT NULL,
            todo_date TEXT,
            
            FOREIGN KEY (user_id)
            REFERENCES users(user_id) ON DELETE CASCADE 
            )
                     """)




