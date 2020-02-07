import json
from typing import Dict, List, Optional, Tuple, Union

from .errors import ChatClientError
from .types import chat1


class ChatClient:
    def __init__(self, bot):
        self.bot = bot

    def _channel_or_conv_id(self, channel: Union[chat1.ChatChannel, chat1.ConvIDStr]) -> Tuple[str, Union[str, dict]]:
        if isinstance(channel, chat1.ChatChannel):
            return "channel", channel.to_dict()
        return "conversation_id", str(channel)

    async def list(self) -> List[chat1.ConvSummary]:
        """
        Lists your chats, with info on which ones have unread messages.
        """
        await self.bot.ensure_initialized()
        res = await self.execute({"method": "list"})
        chat_list = chat1.ChatList.from_dict(res)
        return chat_list.conversations or []

    async def read(
        self, channel: Union[chat1.ChatChannel, chat1.ConvIDStr], pagination: Optional[chat1.Pagination]
    ) -> List[Optional[chat1.MsgSummary]]:
        """
        Reads the messages in a channel.
        """
        await self.bot.ensure_initialized()
        ch_key, ch_val = self._channel_or_conv_id(channel)
        read_options = {ch_key: ch_val}
        if pagination is not None:
            read_options["pagination"] = pagination.to_dict()
        read_request = {"method": "read", "params": {"options": read_options}}
        res = await self.execute(read_request)
        thread = chat1.Thread.from_dict(res)
        return [message.msg for message in (thread.messages or [])]

    async def send(self, channel: Union[chat1.ChatChannel, chat1.ConvIDStr], message: str) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        ch_key, ch_val = self._channel_or_conv_id(channel)
        res = await self.execute(
            {
                "method": "send",
                "params": {
                    "options": {
                        ch_key: ch_val,
                        "message": {"body": message},
                    }
                },
            }
        )
        return chat1.SendRes.from_dict(res)

    async def react(
        self, channel: Union[chat1.ChatChannel, chat1.ConvIDStr], message_id: chat1.MessageID, reaction: str
    ) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        ch_key, ch_val = self._channel_or_conv_id(channel)
        res = await self.execute(
            {
                "method": "reaction",
                "params": {
                    "options": {
                        ch_key: ch_val,
                        "message_id": message_id,
                        "message": {"body": reaction},
                    }
                },
            }
        )
        return chat1.SendRes.from_dict(res)

    async def edit(
        self, channel: Union[chat1.ChatChannel, chat1.ConvIDStr], message_id: chat1.MessageID, message: str
    ) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        ch_key, ch_val = self._channel_or_conv_id(channel)
        res = await self.execute(
            {
                "method": "edit",
                "params": {
                    "options": {
                        ch_key: ch_val,
                        "message_id": message_id,
                        "message": {"body": message},
                    }
                },
            }
        )
        return chat1.SendRes.from_dict(res)

    async def attach(
        self, channel: Union[chat1.ChatChannel, chat1.ConvIDStr], filename: str, title: str
    ) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        ch_key, ch_val = self._channel_or_conv_id(channel)
        res = await self.execute(
            {
                "method": "attach",
                "params": {
                    "options": {
                        ch_key: ch_val,
                        "filename": filename,
                        "title": title,
                    }
                },
            }
        )
        return chat1.SendRes.from_dict(res)

    async def download(
        self, channel: Union[chat1.ChatChannel, chat1.ConvIDStr], message_id: int, output: str
    ) -> chat1.SendRes:
        await self.bot.ensure_initialized()
        ch_key, ch_val = self._channel_or_conv_id(channel)
        res = await self.execute(
            {
                "method": "download",
                "params": {
                    "options": {
                        ch_key: ch_val,
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
