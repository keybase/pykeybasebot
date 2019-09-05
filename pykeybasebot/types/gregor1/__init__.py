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

from dataclasses_json import config, dataclass_json
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


@dataclass_json
@dataclass
class AuthResult:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    sid: SessionID = field(metadata=config(field_name="sid"))
    is_admin: bool = field(metadata=config(field_name="isAdmin"))


@dataclass_json
@dataclass
class TimeOrOffset:
    time: Time = field(metadata=config(field_name="time"))
    offset: DurationMsec = field(metadata=config(field_name="offset"))


@dataclass_json
@dataclass
class Metadata:
    uid: UID = field(metadata=config(field_name="uid"))
    msg_id: MsgID = field(metadata=config(field_name="msgID"))
    ctime: Time = field(metadata=config(field_name="ctime"))
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    in_band_msg_type: int = field(metadata=config(field_name="inBandMsgType"))


@dataclass_json
@dataclass
class ReminderID:
    uid: UID = field(metadata=config(field_name="uid"))
    msg_id: MsgID = field(metadata=config(field_name="msgID"))
    seqno: int = field(metadata=config(field_name="seqno"))


@dataclass_json
@dataclass
class OutOfBandMessage:
    uid: UID = field(metadata=config(field_name="uid"))
    system: System = field(metadata=config(field_name="system"))
    body: Body = field(metadata=config(field_name="body"))


@dataclass_json
@dataclass
class ConnectedDevice:
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    device_type: str = field(metadata=config(field_name="deviceType"))
    device_platform: str = field(metadata=config(field_name="devicePlatform"))
    user_agent: str = field(metadata=config(field_name="userAgent"))


@dataclass_json
@dataclass
class StateSyncMessage:
    md: Metadata = field(metadata=config(field_name="md"))


@dataclass_json
@dataclass
class MsgRange:
    end_time: TimeOrOffset = field(metadata=config(field_name="endTime"))
    category: Category = field(metadata=config(field_name="category"))
    skip_msg_i_ds: List[MsgID] = field(metadata=config(field_name="skipMsgIDs"))


@dataclass_json
@dataclass
class Item:
    category: Category = field(metadata=config(field_name="category"))
    dtime: TimeOrOffset = field(metadata=config(field_name="dtime"))
    remind_times: List[TimeOrOffset] = field(metadata=config(field_name="remindTimes"))
    body: Body = field(metadata=config(field_name="body"))


@dataclass_json
@dataclass
class ConnectedUser:
    uid: UID = field(metadata=config(field_name="uid"))
    devices: List[ConnectedDevice] = field(metadata=config(field_name="devices"))


@dataclass_json
@dataclass
class Dismissal:
    msg_i_ds: List[MsgID] = field(metadata=config(field_name="msgIDs"))
    ranges: List[MsgRange] = field(metadata=config(field_name="ranges"))


@dataclass_json
@dataclass
class ItemAndMetadata:
    md: Optional[Metadata] = field(metadata=config(field_name="md"))
    item: Optional[Item] = field(metadata=config(field_name="item"))


@dataclass_json
@dataclass
class State:
    items: List[ItemAndMetadata] = field(metadata=config(field_name="items"))


@dataclass_json
@dataclass
class StateUpdateMessage:
    md: Metadata = field(metadata=config(field_name="md"))
    creation: Optional[Item] = field(metadata=config(field_name="creation"))
    dismissal: Optional[Dismissal] = field(metadata=config(field_name="dismissal"))


@dataclass_json
@dataclass
class Reminder:
    item: ItemAndMetadata = field(metadata=config(field_name="item"))
    seqno: int = field(metadata=config(field_name="seqno"))
    remind_time: Time = field(metadata=config(field_name="remindTime"))


@dataclass_json
@dataclass
class InBandMessage:
    state_update: Optional[StateUpdateMessage] = field(
        metadata=config(field_name="stateUpdate")
    )
    state_sync: Optional[StateSyncMessage] = field(
        metadata=config(field_name="stateSync")
    )


@dataclass_json
@dataclass
class ReminderSet:
    reminders: List[Reminder] = field(metadata=config(field_name="reminders"))
    more_reminders_ready: bool = field(metadata=config(field_name="moreRemindersReady"))


@dataclass_json
@dataclass
class Message:
    oobm: Optional[OutOfBandMessage] = field(metadata=config(field_name="oobm"))
    ibm: Optional[InBandMessage] = field(metadata=config(field_name="ibm"))


@dataclass_json
@dataclass
class SyncResult:
    msgs: List[InBandMessage] = field(metadata=config(field_name="msgs"))
    hash: bytes = field(metadata=config(field_name="hash"))
