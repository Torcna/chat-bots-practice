import urllib.request
import json
import os

from dotenv import load_dotenv

load_dotenv()


def makeRequest(method: str, **params) -> dict:
    jsonData = json.dumps(params).encode("utf-8")
    print(jsonData)
    request = urllib.request.Request(
        method="POST",
        url=f"{os.getenv('TELEGRAM_BASE_URI')}{os.getenv('TOKEN')}/{method}",
        data=jsonData,
        headers={
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request) as response:
        responseBody = response.read().decode("utf-8")
        responseJSON = json.loads(responseBody)
        if responseJSON["ok"] == True:
            return responseJSON["result"]
        else:
            print("not ok")


def getUpdates(offset: int) -> dict:
    return makeRequest("getUpdates", offset=offset)


def sendMessage(chat_id: int, text: str) -> dict:
    return makeRequest("sendMessage", chat_id=chat_id, text=text)


def getMe() -> dict:
    return makeRequest("getMe")
