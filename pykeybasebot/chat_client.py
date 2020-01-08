import json
from typing import Dict, List, Optional

from .errors import ChatClientError
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
        return chat_list.conversations or []

    async def read(
        self, channel: chat1.ChatChannel, pagination: Optional[chat1.Pagination]
    ) -> List[Optional[chat1.MsgSummary]]:
        """
        Reads the messages in a channel.
        """
        await self.bot.ensure_initialized()
        read_options = {"channel": channel.to_dict()}
        if pagination is not None:
            read_options["pagination"] = pagination.to_dict()
        read_request = {"method": "read", "params": {"options": read_options}}
        res = await self.execute(read_request)
        thread = chat1.Thread.from_dict(res)
        return [message.msg for message in (thread.messages or [])]

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

    async def execute(self, command) -> Dict[str, str]:
        resp = await self.bot.submit("chat api", json.dumps(command).encode("utf-8"))
        try:
            return resp["result"]
        except (TypeError, KeyError):
            # this could happen if the running keybase client has an unexpected issue
            raise ChatClientError(json.dumps(resp))
