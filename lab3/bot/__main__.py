import time
import bot.databaseClient
import bot.tgClient


def main() -> None:
    offsetCounter = 0
    try:
        while True:
            updates = bot.tgClient.getUpdates(offsetCounter)
            bot.databaseClient.persist_updates(updates)
            for upd in updates:
                offsetCounter = max(offsetCounter, upd["update_id"] + 1)
                msg = upd.get("message")
                if not msg:
                    continue

                chat_id = msg.get("chat", {}).get("id")
                text = msg.get("text")

                if text:
                    print("there is text")
                    bot.tgClient.sendMessage(chat_id=chat_id, text=text)
                else:
                    print("there is NO text")
                    bot.tgClient.sendMessage(
                        chat_id=chat_id,
                        text="Cannot echo this type of messages, sr",
                    )
                print(".", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStop")


if __name__ == "__main__":
    main()
