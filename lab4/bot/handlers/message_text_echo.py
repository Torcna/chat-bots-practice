from bot.handler import Handler
import bot.tgClient


class MessageEcho(Handler):
    def can_handle(self, update: dict) -> bool:
        if update.get("message"):
            return "message" in update and "text" in update["message"]

        return False

    def handle(self, update: dict) -> bool:
        print("there is text")
        bot.tgClient.sendMessage(
            chat_id=update["message"]["chat"]["id"], text=update["message"]["text"]
        )

        return False
