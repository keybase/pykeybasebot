import json

from typing import Dict  # , List, Optional

# from .types import chat1


class TeamClient:
    def __init__(self, bot):
        self.bot = bot

    async def list_self_memberships(self):
        pass

    async def list_team_memberships(self, team: str):
        pass

    async def list_user_memberships(self, user: str):
        pass

    async def create(self, name: str):
        pass

    async def add_member(self, name: str):
        pass

    async def edit_member(self, user: str, role: str):
        pass

    async def remove_member(self, user: str):
        pass

    async def rename_subteam(self, old_name: str, new_name: str):
        pass

    async def leave(self, team: str):
        pass

    async def execute(self, command) -> Dict[str, str]:
        resp = await self.bot.submit("team api", json.dumps(command).encode("utf-8"))
        return resp["result"]
