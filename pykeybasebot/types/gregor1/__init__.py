"""gregor.1

Auto-generated to Python types by avdl-compiler v1.4.1 (https://github.com/keybase/node-avdl-compiler)
Input files:
 - ../client/protocol/avdl/gregor1/auth.avdl
 - ../client/protocol/avdl/gregor1/auth_internal.avdl
 - ../client/protocol/avdl/gregor1/auth_update.avdl
 - ../client/protocol/avdl/gregor1/common.avdl
 - ../client/protocol/avdl/gregor1/incoming.avdl
 - ../client/protocol/avdl/gregor1/outgoing.avdl
 - ../client/protocol/avdl/gregor1/remind.avdl
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union

from mashumaro import DataClassJSONMixin
from typing_extensions import Literal

DurationMsec = int
DurationSec = int
Category = str
System = str
UID = bytes
MsgID = bytes
DeviceID = bytes
Body = bytes
Time = int
SessionID = str
SessionToken = str


@dataclass
class AuthResult(DataClassJSONMixin):
    uid: UID
    username: str
    sid: SessionID
    is_admin: bool


@dataclass
class TimeOrOffset(DataClassJSONMixin):
    time: Time
    offset: DurationMsec


@dataclass
class Metadata(DataClassJSONMixin):
    uid: UID
    msg_id: MsgID
    ctime: Time
    device_id: DeviceID
    in_band_msg_type: int


@dataclass
class ReminderID(DataClassJSONMixin):
    uid: UID
    msg_id: MsgID
    seqno: int


@dataclass
class OutOfBandMessage(DataClassJSONMixin):
    uid: UID
    system: System
    body: Body


@dataclass
class ConnectedDevice(DataClassJSONMixin):
    device_id: DeviceID
    device_type: str
    device_platform: str
    user_agent: str


@dataclass
class StateSyncMessage(DataClassJSONMixin):
    md: Metadata


@dataclass
class MsgRange(DataClassJSONMixin):
    end_time: TimeOrOffset
    category: Category
    skip_msg_i_ds: List[MsgID]


@dataclass
class Item(DataClassJSONMixin):
    category: Category
    dtime: TimeOrOffset
    remind_times: List[TimeOrOffset]
    body: Body


@dataclass
class ConnectedUser(DataClassJSONMixin):
    uid: UID
    devices: List[ConnectedDevice]


@dataclass
class Dismissal(DataClassJSONMixin):
    msg_i_ds: List[MsgID]
    ranges: List[MsgRange]


@dataclass
class ItemAndMetadata(DataClassJSONMixin):
    md: Optional[Metadata]
    item: Optional[Item]


@dataclass
class State(DataClassJSONMixin):
    items: List[ItemAndMetadata]


@dataclass
class StateUpdateMessage(DataClassJSONMixin):
    md: Metadata
    creation: Optional[Item]
    dismissal: Optional[Dismissal]


@dataclass
class Reminder(DataClassJSONMixin):
    item: ItemAndMetadata
    seqno: int
    remind_time: Time


@dataclass
class InBandMessage(DataClassJSONMixin):
    state_update: Optional[StateUpdateMessage]
    state_sync: Optional[StateSyncMessage]


@dataclass
class ReminderSet(DataClassJSONMixin):
    reminders: List[Reminder]
    more_reminders_ready: bool


@dataclass
class Message(DataClassJSONMixin):
    oobm: Optional[OutOfBandMessage]
    ibm: Optional[InBandMessage]


@dataclass
class SyncResult(DataClassJSONMixin):
    msgs: List[InBandMessage]
    hash: bytes
