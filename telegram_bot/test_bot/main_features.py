from sqlalchemy import select
from datetime import datetime
from keyboard import render_yes_now_keyboard
from constants import bot
from models import Users_todo
from db import Session

DB_FILE_TODOS = "db/all_todos"


def csv_viewing(user_id):
    date_today = datetime.date(datetime.now())
    str_today = date_today.strftime("%d.%m.%Y")


def user_date(message, todo_text):
    user_id = message.from_user.id
    message_date = message.text
    question = f'Задание: {todo_text}, дата: {message_date}'
    render_yes_now_keyboard(user_id, question, "reg")
    session = Session()
    add_todo = Users_todo(users_id=user_id, user_todo=todo_text, todo_date=message_date)
    session.add(add_todo)
    session.commit()
    session.close()


def to_do(message):
    user_id = message.from_user.id
    todo_text = message.text
    bot.send_message(user_id, "Введите дату:")
    bot.register_next_step_handler(message, user_date, todo_text)


def check_todo_table(user_id):
    date_today = datetime.date(datetime.now())
    str_today = date_today.strftime("%d.%m.%Y")
    session = Session()
    todos = session.execute(
        select(Users_todo).where(Users_todo.users_id == user_id, Users_todo.todo_date == str_today)
        )
    send_message = "Ваши задачи на сегодня\n"
    for index, i in enumerate(todos.fetchall(), start=1):
        send_message += f"{index}. {i[0]}\n"
    bot.send_message(user_id, send_message)