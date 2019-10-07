"""gregor.1

Auto-generated to Python types by avdl-compiler v1.4.4 (https://github.com/keybase/node-avdl-compiler)
Input files:
 - ../../go/src/github.com/keybase/client/protocol/avdl/gregor1/auth.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/gregor1/auth_internal.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/gregor1/auth_update.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/gregor1/common.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/gregor1/incoming.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/gregor1/outgoing.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/gregor1/remind.avdl
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Union

from dataclasses_json import DataClassJsonMixin, config
from typing_extensions import Literal

DurationMsec = int
DurationSec = int
Category = str
System = str
UID = str
MsgID = str
DeviceID = str
Body = str
Time = int
SessionID = str
SessionToken = str


@dataclass
class AuthResult(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    sid: SessionID = field(metadata=config(field_name="sid"))
    is_admin: bool = field(metadata=config(field_name="isAdmin"))


@dataclass
class TimeOrOffset(DataClassJsonMixin):
    time: Time = field(metadata=config(field_name="time"))
    offset: DurationMsec = field(metadata=config(field_name="offset"))


@dataclass
class Metadata(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    msg_id: MsgID = field(metadata=config(field_name="msgID"))
    ctime: Time = field(metadata=config(field_name="ctime"))
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    in_band_msg_type: int = field(metadata=config(field_name="inBandMsgType"))


@dataclass
class ReminderID(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    msg_id: MsgID = field(metadata=config(field_name="msgID"))
    seqno: int = field(metadata=config(field_name="seqno"))


@dataclass
class OutOfBandMessage(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    system: System = field(metadata=config(field_name="system"))
    body: Body = field(metadata=config(field_name="body"))


@dataclass
class ConnectedDevice(DataClassJsonMixin):
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    device_type: str = field(metadata=config(field_name="deviceType"))
    device_platform: str = field(metadata=config(field_name="devicePlatform"))
    user_agent: str = field(metadata=config(field_name="userAgent"))


@dataclass
class StateSyncMessage(DataClassJsonMixin):
    md: Metadata = field(metadata=config(field_name="md"))


@dataclass
class MsgRange(DataClassJsonMixin):
    end_time: TimeOrOffset = field(metadata=config(field_name="endTime"))
    category: Category = field(metadata=config(field_name="category"))
    skip_msg_i_ds: Optional[Optional[List[MsgID]]] = field(
        default=None, metadata=config(field_name="skipMsgIDs")
    )


@dataclass
class Item(DataClassJsonMixin):
    category: Category = field(metadata=config(field_name="category"))
    dtime: TimeOrOffset = field(metadata=config(field_name="dtime"))
    body: Body = field(metadata=config(field_name="body"))
    remind_times: Optional[Optional[List[TimeOrOffset]]] = field(
        default=None, metadata=config(field_name="remindTimes")
    )


@dataclass
class ConnectedUser(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    devices: Optional[Optional[List[ConnectedDevice]]] = field(
        default=None, metadata=config(field_name="devices")
    )


@dataclass
class Dismissal(DataClassJsonMixin):
    msg_i_ds: Optional[Optional[List[MsgID]]] = field(
        default=None, metadata=config(field_name="msgIDs")
    )
    ranges: Optional[Optional[List[MsgRange]]] = field(
        default=None, metadata=config(field_name="ranges")
    )


@dataclass
class ItemAndMetadata(DataClassJsonMixin):
    md: Optional[Metadata] = field(default=None, metadata=config(field_name="md"))
    item: Optional[Item] = field(default=None, metadata=config(field_name="item"))


@dataclass
class State(DataClassJsonMixin):
    items: Optional[Optional[List[ItemAndMetadata]]] = field(
        default=None, metadata=config(field_name="items")
    )


@dataclass
class StateUpdateMessage(DataClassJsonMixin):
    md: Metadata = field(metadata=config(field_name="md"))
    creation: Optional[Item] = field(
        default=None, metadata=config(field_name="creation")
    )
    dismissal: Optional[Dismissal] = field(
        default=None, metadata=config(field_name="dismissal")
    )


@dataclass
class Reminder(DataClassJsonMixin):
    item: ItemAndMetadata = field(metadata=config(field_name="item"))
    seqno: int = field(metadata=config(field_name="seqno"))
    remind_time: Time = field(metadata=config(field_name="remindTime"))


@dataclass
class InBandMessage(DataClassJsonMixin):
    state_update: Optional[StateUpdateMessage] = field(
        default=None, metadata=config(field_name="stateUpdate")
    )
    state_sync: Optional[StateSyncMessage] = field(
        default=None, metadata=config(field_name="stateSync")
    )


@dataclass
class ReminderSet(DataClassJsonMixin):
    more_reminders_ready: bool = field(metadata=config(field_name="moreRemindersReady"))
    reminders: Optional[Optional[List[Reminder]]] = field(
        default=None, metadata=config(field_name="reminders")
    )


@dataclass
class Message(DataClassJsonMixin):
    oobm: Optional[OutOfBandMessage] = field(
        default=None, metadata=config(field_name="oobm")
    )
    ibm: Optional[InBandMessage] = field(
        default=None, metadata=config(field_name="ibm")
    )


@dataclass
class SyncResult(DataClassJsonMixin):
    hash: str = field(metadata=config(field_name="hash"))
    msgs: Optional[Optional[List[InBandMessage]]] = field(
        default=None, metadata=config(field_name="msgs")
    )
