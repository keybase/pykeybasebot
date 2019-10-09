from dataclasses import dataclass
from enum import Enum
from typing import Optional

from dataclasses_json import DataClassJsonMixin

from .types import chat1, stellar1


class EventType(Enum):
    CHAT = "chat"
    DEV = "dev"
    WALLET = "wallet"


class Source(Enum):
    REMOTE = "remote"
    LOCAL = "local"
    PAYMENT_STATUS = "payment_status"
    PAYMENT = "payment"


@dataclass
class KbEvent(DataClassJsonMixin):
    type: EventType
    source: Source
    pagination: Optional[chat1.UIPagination] = None
    msg: Optional[chat1.MsgSummary] = None
    notification: Optional[stellar1.PaymentDetailsLocal] = None
