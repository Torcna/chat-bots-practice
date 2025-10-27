import bot.databaseClient

from bot.handlers.handler import Handler


class DatabaseLogger(Handler):

    def can_handle(self, update: dict) -> bool:
        return True

    def handle(self, update: dict) -> bool:
        bot.databaseClient.persistUpdate(update)
        return True
