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

# aiogram.redis = {
#     'host': ip,
# }
#
# redis = {
#     'address': (ip, 6379),
#     'encoding': 'utf8'
# }
