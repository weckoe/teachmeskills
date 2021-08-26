import os
import telebot

API_TOKEN = "1827046423:AAEtXx9tssHYBpsWn1fx11s_CKox538GeqU"
bot = telebot.TeleBot(API_TOKEN)

csv_dir = os.path.join("test_files", "csv")

FILE_PATH_2 = os.path.join(csv_dir, "todo.csv")
FILE_PATH_1 = os.path.join(csv_dir, "test.csv")

NAMES = ["user_id", "todo_text", "date"]