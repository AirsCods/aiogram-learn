from aiogram import Dispatcher

from .admins import AdminFilter
from .forworded_message import IsForwarded
from .group_chat import IsGroup
from .private_chat import IsPrivate


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsForwarded)
