import json

from .bot import Bot
from .types import chat1, stellar1


class ChatClient:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def send(self, channel: chat1.ChatChannel, message: str) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        return await self.execute(
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

    async def react(
        self, channel: chat1.ChatChannel, message_id: chat1.MessageID, reaction: str
    ) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        return await self.execute(
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

    async def edit(
        self, channel: chat1.ChatChannel, message_id: chat1.MessageID, message: str
    ):
        await self.bot.ensure_initialized()
        return await self.execute(
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

    async def execute(self, command):
        return await self.bot.submit("chat api", json.dumps(command).encode("utf-8"))
