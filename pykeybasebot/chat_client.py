import json

from .types import chat1


class ChatClient:
    def __init__(self, bot):
        self.bot = bot

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
