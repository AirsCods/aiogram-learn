import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get('TOKEN')
admins = [

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
