import json
from typing import List

from .types import chat1


class ChatClient:
    def __init__(self, bot):
        self.bot = bot

    async def list(self) -> List[chat1.ConvSummary]:
        """
        Lists your chats, with info on which ones have unread messages.
        """
        await self.bot.ensure_initialized()
        res = await self.execute({"method": "list"})
        chat_list = chat1.ChatList.from_dict(res)
        return chat_list.converastions or []

    async def read(self, channel: chat1.ChatChannel) -> List[chat1.MsgSummary]:
        """
        Reads the messages in a channel. You can read with or without marking as read.
        """
        await self.bot.ensure_initialized()
        res = await self.execute(
            {"method": "read", "params": {"options": {"channel": channel.to_dict()}}}
        )
        thread = chat1.Thread.from_dict(res)
        if thread.messages is None:
            return []
        messages = []
        for message in thread.messages:
            messages.append(message.msg)
        return messages

    async def send(self, channel: chat1.ChatChannel, message: str) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        res = await self.execute(
            {
                "method": "send",
                "params": {
                    "options": {
                        "channel": channel.to_dict(),
                        "message": {"body": message},
                    }
                },
            }
        )
        return chat1.SendRes.from_dict(res)

    async def react(
        self, channel: chat1.ChatChannel, message_id: chat1.MessageID, reaction: str
    ) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        res = await self.execute(
            {
                "method": "reaction",
                "params": {
                    "options": {
                        "channel": channel.to_dict(),
                        "message_id": message_id,
                        "message": {"body": reaction},
                    }
                },
            }
        )
        return chat1.SendRes.from_dict(res)

    async def edit(
        self, channel: chat1.ChatChannel, message_id: chat1.MessageID, message: str
    ) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        res = await self.execute(
            {
                "method": "edit",
                "params": {
                    "options": {
                        "channel": channel.to_dict(),
                        "message_id": message_id,
                        "message": {"body": message},
                    }
                },
            }
        )
        return chat1.SendRes.from_dict(res)

    async def attach(
        self, channel: chat1.ChatChannel, filename: str, title: str
    ) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        res = await self.execute(
            {
                "method": "attach",
                "params": {
                    "options": {
                        "channel": channel.to_dict(),
                        "filename": filename,
                        "title": title,
                    }
                },
            }
        )
        return chat1.SendRes.from_dict(res)

    async def download(
        self, channel: chat1.ChatChannel, message_id: int, output: str
    ) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        res = await self.execute(
            {
                "method": "download",
                "params": {
                    "options": {
                        "channel": channel.to_dict(),
                        "message_id": message_id,
                        "output": output,
                    }
                },
            }
        )
        return chat1.SendRes.from_dict(res)

    async def execute(self, command):
        resp = await self.bot.submit("chat api", json.dumps(command).encode("utf-8"))
        return resp["result"]
