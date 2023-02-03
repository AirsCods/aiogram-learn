import logging

from aiogram.types import Update

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exception handler. Catches exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return:
    """
    from aiogram.utils.exceptions import (Unauthorized, InvalidQueryID, TelegramAPIError,
                                          CantDemoteChatCreator, MessageNotModified, MessageToDeleteNotFound,
                                          MessageTextIsEmpty, RetryAfter, BadRequest,
                                          CantParseEntities, MessageCantBeDeleted)

    if isinstance(exception, CantDemoteChatCreator):
        logging.debug('Can\'t demote chat creator')
        return True

    if isinstance(exception, MessageNotModified):
        logging.debug('Message is not modified')
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.debug('Message can\'t be deleted')
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.debug('Message to delete not found')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.debug('Message text is empty')
        return True

    if isinstance(exception, Unauthorized):
        logging.debug(f'Unauthorized: {exception}')
        return True

    if isinstance(exception, InvalidQueryID):
        logging.debug(f'Invalid query ID: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, CantParseEntities):
        await Update.get_current().message.answer(f'Попало в эррор хендлер. Can\'t parser entities: {exception.args}')
        return True

    if isinstance(exception, RetryAfter):
        logging.debug(f'Retry after: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, BadRequest):
        logging.debug(f'Bad request: {exception} \nUpdate: {update}')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.debug(f'Telegram API error: {exception} \nUpdate: {update}')
        return True

    logging.exception(f'Update: {update} \n{exception}')
