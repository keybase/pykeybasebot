import json
from typing import Any, Dict, Union

from .errors import disambiguate_error
from .types import keybase1


class KVStoreClient:
    def __init__(self, bot):
        self.bot = bot

    async def put(
        self,
        namespace: str,
        entry_key: str,
        entry_value: str,
        revision: Union[int, None] = None,
        team: Union[str, None] = None,
    ) -> keybase1.KVPutResult:
        await self.bot.ensure_initialized()
        args: Dict[str, Any] = {
            "method": "put",
            "params": {
                "options": {
                    "team": team,
                    "namespace": namespace,
                    "entryKey": entry_key,
                    "entryValue": entry_value,
                    "revision": revision,
                }
            },
        }
        try:
            res = await self.execute(args)
            return keybase1.KVPutResult.from_dict(res)
        except Exception as e:
            raise disambiguate_error(e)

    async def delete(
        self,
        namespace: str,
        entry_key: str,
        revision: Union[int, None] = None,
        team: Union[str, None] = None,
    ) -> keybase1.KVDeleteEntryResult:
        await self.bot.ensure_initialized()
        args: Dict[str, Any] = {
            "method": "del",
            "params": {
                "options": {
                    "team": team,
                    "namespace": namespace,
                    "entryKey": entry_key,
                    "revision": revision,
                }
            },
        }
        try:
            res = await self.execute(args)
            return keybase1.KVDeleteEntryResult.from_dict(res)
        except Exception as e:
            raise disambiguate_error(e)

    async def get(
        self, namespace: str, entry_key: str, team: Union[str, None] = None
    ) -> keybase1.KVGetResult:
        await self.bot.ensure_initialized()
        args: Dict[str, Any] = {
            "method": "get",
            "params": {
                "options": {"team": team, "namespace": namespace, "entryKey": entry_key}
            },
        }
        res = await self.execute(args)
        return keybase1.KVGetResult.from_dict(res)

    async def list_namespaces(
        self, team: Union[str, None] = None
    ) -> keybase1.KVListNamespaceResult:
        await self.bot.ensure_initialized()
        args: Dict[str, Any] = {
            "team": team,
            "method": "list",
            "params": {"options": {"team": team}},
        }
        res = await self.execute(args)
        return keybase1.KVListNamespaceResult.from_dict(res)

    async def list_entrykeys(
        self, namespace: str, team: Union[str, None] = None
    ) -> keybase1.KVListEntryResult:
        await self.bot.ensure_initialized()
        args: Dict[str, Any] = {
            "method": "list",
            "params": {"options": {"team": team, "namespace": namespace}},
        }
        res = await self.execute(args)
        return keybase1.KVListEntryResult.from_dict(res)

    def is_deleted(self, res: keybase1.KVGetResult) -> bool:
        return res.revision > 0 and res.entry_value == ""

    def is_present(self, res: keybase1.KVGetResult) -> bool:
        return res.revision > 0 and res.entry_value != ""

    async def execute(self, command):
        resp = await self.bot.submit("kvstore api", json.dumps(command).encode("utf-8"))
        return resp["result"]
