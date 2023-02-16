import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('TOKEN')

DOWNLOAD_PATH = os.getenv('DOWNLOAD_PATH')

admins = [
    os.getenv('ADMIN_ID')
]

allowed_users = [
    5280548835,
]

channels = [
    os.getenv('MY_CHANNEL')
]

ip = os.getenv('ip')

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
