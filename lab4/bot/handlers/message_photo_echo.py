import bot.tgClient
from bot.handler import Handler


class MessagePhotoEcho(Handler):
    def can_handle(self, update: dict) -> bool:
        return "message" in update and "photo" in update["message"]

    def handle(self, update: dict) -> bool:
        msg = update["message"]
        chat_id = msg["chat"]["id"]
        file_id = msg["photo"][-1]["file_id"]
        bot.tgClient.sendPhoto(chat_id, file_id)
        return False
