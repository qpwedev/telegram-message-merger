from pyrogram import Client, filters
import os
from datetime import datetime, timedelta
from typing import List
from pyrogram.types import Message

from dotenv import load_dotenv
load_dotenv()

API_ID, API_HASH, MY_ID = \
    os.getenv("API_ID"), \
    os.getenv("API_HASH"), \
    int(os.getenv("MY_ID"))

if "<YOUR_VALUE>" in [API_ID, API_HASH, MY_ID]:
    print("Please enter your API ID and API HASH in the config.json file.")
    exit(1)

app = Client("my_account", int(API_ID), API_HASH)


async def get_last_burst_messages(chat_id: int) -> List[Message]:
    last_messages = []

    async for message in app.get_chat_history(chat_id, limit=5):

        if message.from_user.id != MY_ID:
            break

        last_messages.append(message)

    return last_messages


def unify_message_text(messages: List[Message]) -> str:
    text = ""
    for message in messages[::-1]:
        text += message.text + "\n\n"

    return text


async def delete_unused_messages(messages: List[Message], chat_id: int) -> None:
    message_ids = [message.id for message in messages[:-1]]

    try:
        await app.delete_messages(
            chat_id=chat_id,
            message_ids=message_ids,
            revoke=True
        )

    except Exception as e:
        print(e)


async def edit_first_message(messages: List[Message]):
    first_message = messages[-1]
    text = unify_message_text(messages)

    try:
        await first_message.edit(text=text)
    except Exception as e:
        print(e)


def validate_timerange(messages: List[Message]) -> bool:
    first_message = messages[-1]
    last_message = messages[0]

    first_message_datetime = datetime.strptime(
        first_message.date, "%Y-%m-%d %H:%M:%S"
    )

    last_message_datetime = datetime.strptime(
        last_message.date, "%Y-%m-%d %H:%M:%S"
    )

    if last_message_datetime - first_message_datetime > timedelta(seconds=30):
        return False

    return True


def filter_messages_by_timerange(messages: List[Message]) -> List[Message]:
    first_message_datetime = messages[0].date
    filtered_messages = []

    for message in messages:
        if first_message_datetime - message.date < timedelta(seconds=30):
            filtered_messages.append(message)

    return filtered_messages


@app.on_message(filters.text & filters.private & filters.me)
async def messsage_forwarder(_, message):
    if message.reply_to_message:
        return

    print("hello world", message.chat.id, message.text)

    last_messages = await get_last_burst_messages(message.chat.id)

    filtered_last_messages = filter_messages_by_timerange(
        last_messages
    )

    if len(filtered_last_messages) < 2:
        return

    await delete_unused_messages(
        filtered_last_messages,
        message.chat.id
    )

    await edit_first_message(
        filtered_last_messages
    )


if __name__ == "__main__":
    app.run()
