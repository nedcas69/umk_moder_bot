import os # Импортируем библиотеку функций для работы с операционной системой

from dotenv import load_dotenv # Импортируем функцию load_dotenv

load_dotenv() # Запускаем функцию которая загружает переменное окружение из файла .env

# Получаем токен бота
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# Список администраторов бота
admins = [
    562847836
]


adm = [
    1005654596
]

chat_ids = -1001855063926



ip = os.getenv('ip')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASS'))
DATABASE = str(os.getenv('PG_DB'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'

