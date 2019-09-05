from dataclasses import dataclass
from enum import Enum
from typing import Any, List, Optional

import pykeybasebot.types.chat1 as chat1
import pykeybasebot.types.stellar1 as stellar1
from dataclasses_json import dataclass_json


class EventType(Enum):
    CHAT = "chat"
    DEV = "dev"
    WALLET = "wallet"


class Source(Enum):
    REMOTE = "remote"
    LOCAL = "local"
    PAYMENT_STATUS = "payment_status"
    PAYMENT = "payment"


@dataclass_json
@dataclass
class KbEvent:
    type: EventType
    source: Source
    pagination: Optional[chat1.UIPagination] = None
    msg: Optional[chat1.MsgSummary] = None
    notification: Optional[stellar1.PaymentDetailsLocal] = None


# class MembersType(Enum):
#     KBFS = "kbfs"
#     TEAM = "team"
#     IMPTEAMNATIVE = "impteamnative"
#     IMPTEAMUPGRADE = "impteamupgrade"


# class TopicType(Enum):
#     NONE = "none"
#     CHAT = "chat"
#     DEV = "dev"
#     KBFSFILEEDIT = "kbfsfileedit"


# @dataclass
# class Sender(DataClassJSONMixin):
#     uid: str
#     username: str
#     device_id: str
#     device_name: str


# @dataclass
# class Channel(DataClassJSONMixin):
#     name: str
#     public: bool
#     members_type: MembersType
#     topic_type: TopicType
#     topic_name: Optional[str] = None

#     def replyable_dict(self):
#         # Channels that come from the chat event stream are formatted
#         # a little bit differently from how channels need to be structured for
#         # API Send commands. This method converts from the former to the latter.
#         running_dict = {"name": self.name}
#         if self.members_type == MembersType.IMPTEAMNATIVE:
#             return running_dict
#         if self.public:
#             running_dict["public"] = True
#         running_dict["members_type"] = self.members_type.value
#         running_dict["topic_name"] = self.topic_name
#         return running_dict


# class ContentType(Enum):
#     # https://github.com/keybase/client/blob/master/go/protocol/chat1/common.go
#     NONE = "none"
#     TEXT = "text"
#     ATTACHMENT = "attachment"
#     EDIT = "edit"
#     DELETE = "delete"
#     METADATA = "metadata"
#     TLFNAME = "tlfname"
#     HEADLINE = "headline"
#     ATTACHMENTUPLOADED = "attachmentuploaded"
#     JOIN = "join"
#     LEAVE = "leave"
#     SYSTEM = "system"
#     DELETEHISTORY = "deletehistory"
#     REACTION = "reaction"
#     SENDPAYMENT = "sendpayment"
#     REQUESTPAYMENT = "requestpayment"
#     UNFURL = "unfurl"
#     FLIP = "flip"


# @dataclass
# class PaymentResult(DataClassJSONMixin):
#     resultTyp: int
#     error: str


# @dataclass
# class Payment(DataClassJSONMixin):
#     username: str
#     paymentText: str
#     result: PaymentResult


# @dataclass
# class UserMention(DataClassJSONMixin):
#     text: str
#     uid: str


# @dataclass
# class TeamMention(DataClassJSONMixin):
#     name: str
#     channel: str


# @dataclass
# class ContentText(DataClassJSONMixin):
#     body: str
#     payments: List[Payment]
#     userMentions: List[UserMention]
#     teamMentions: List[TeamMention]
#     at_mention_usernames: Optional[List[str]] = None


# @dataclass
# class Reaction(DataClassJSONMixin):
#     m: int  # message id to react to
#     b: str  # reaction (or text), e.g. :mag:


# @dataclass
# class Content(DataClassJSONMixin):
#     type: ContentType
#     text: Optional[ContentText] = None
#     reaction: Optional[Reaction] = None
#     unfurl: Optional[Any] = None
#     edit: Optional[Any] = None
#     flip: Optional[Any] = None


# @dataclass
# class ChannelNameMention(DataClassJSONMixin):
#     name: str
#     conv_id: str


# @dataclass
# class Message(DataClassJSONMixin):
#     id: int
#     channel: Channel
#     sender: Sender
#     sent_at: int
#     sent_at_ms: int
#     content: Content
#     conversation_id: Optional[str] = None
#     prev: Optional[str] = None
#     unread: Optional[bool] = None
#     channel_mention: Optional[str] = None
#     channel_name_mention: Optional[List[ChannelNameMention]] = None


# @dataclass
# class Pagination(DataClassJSONMixin):
#     next: str
#     previous: str
#     num: int
#     last: bool


# class PaymentStatusStr(Enum):
#     NONE = "none"
#     PENDING = "pending"
#     CLAIMABLE = "claimable"
#     COMPLETED = "completed"
#     ERROR = "error"
#     UNKNOWN = "unknown"
#     CANCELED = "canceled"


# class PaymentStatusInt(Enum):
#     NONE = 0
#     PENDING = 1
#     CLAIMABLE = 2
#     COMPLETED = 3
#     ERROR = 4
#     UNKNOWN = 5
#     CANCELED = 6


# @dataclass
# class SourceAsset(DataClassJSONMixin):
#     type: str
#     code: str
#     issuer: str
#     verifiedDomain: str
#     issuerName: str
#     desc: str
#     infoUrl: str


# @dataclass
# class Notification(DataClassJSONMixin):
#     id: str
#     txID: str
#     time: int
#     statusSimplified: PaymentStatusInt
#     statusDescription: PaymentStatusStr
#     statusDetail: str
#     showCancel: bool
#     amountDescription: str
#     delta: int
#     worth: str
#     worthAtSendTime: str
#     issuerDescription: str
#     fromType: int
#     toType: int
#     fromAccountID: str
#     fromAccountName: str
#     fromUsername: str
#     toAccountID: str
#     toAccountName: str
#     toUsername: str
#     toAssertion: str
#     originalToAssertion: str
#     note: str
#     noteErr: str
#     sourceAmountMax: str
#     sourceAmountActual: str
#     sourceAsset: SourceAsset
#     publicNote: str
#     publicNoteType: str
#     externalTxURL: str
#     batchID: str
#     fromAirdrop: bool
#     isInflation: bool


# @dataclass
# class KbEvent(DataClassJSONMixin):
#     type: EventType
#     source: Source
#     pagination: Optional[Pagination] = None
#     msg: Optional[Message] = None
#     notification: Optional[Notification] = None
