"""chat.1

Auto-generated to Python types by avdl-compiler v1.4.4 (https://github.com/keybase/node-avdl-compiler)
Input files:
 - ../client/protocol/avdl/chat1/api.avdl
 - ../client/protocol/avdl/chat1/chat_ui.avdl
 - ../client/protocol/avdl/chat1/commands.avdl
 - ../client/protocol/avdl/chat1/common.avdl
 - ../client/protocol/avdl/chat1/gregor.avdl
 - ../client/protocol/avdl/chat1/local.avdl
 - ../client/protocol/avdl/chat1/notify.avdl
 - ../client/protocol/avdl/chat1/remote.avdl
 - ../client/protocol/avdl/chat1/unfurl.avdl
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Union

import pykeybasebot.types.gregor1 as gregor1
import pykeybasebot.types.keybase1 as keybase1
import pykeybasebot.types.stellar1 as stellar1
from dataclasses_json import DataClassJsonMixin, config
from typing_extensions import Literal


@dataclass
class RateLimitRes(DataClassJsonMixin):
    tank: str = field(metadata=config(field_name="tank"))
    capacity: int = field(metadata=config(field_name="capacity"))
    reset: int = field(metadata=config(field_name="reset"))
    gas: int = field(metadata=config(field_name="gas"))


@dataclass
class ChatChannel(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    public: Optional[bool] = field(default=None, metadata=config(field_name="public"))
    members_type: Optional[str] = field(
        default=None, metadata=config(field_name="members_type")
    )
    topic_type: Optional[str] = field(
        default=None, metadata=config(field_name="topic_type")
    )
    topic_name: Optional[str] = field(
        default=None, metadata=config(field_name="topic_name")
    )


@dataclass
class ChatMessage(DataClassJsonMixin):
    body: str = field(metadata=config(field_name="body"))


@dataclass
class MsgSender(DataClassJsonMixin):
    uid: str = field(metadata=config(field_name="uid"))
    device_id: str = field(metadata=config(field_name="device_id"))
    username: Optional[str] = field(
        default=None, metadata=config(field_name="username")
    )
    device_name: Optional[str] = field(
        default=None, metadata=config(field_name="device_name")
    )


@dataclass
class ResetConvMemberAPI(DataClassJsonMixin):
    conversation_id: str = field(metadata=config(field_name="conversationID"))
    username: str = field(metadata=config(field_name="username"))


@dataclass
class UIPagination(DataClassJsonMixin):
    next: str = field(metadata=config(field_name="next"))
    previous: str = field(metadata=config(field_name="previous"))
    num: int = field(metadata=config(field_name="num"))
    last: bool = field(metadata=config(field_name="last"))


@dataclass
class UIInboxSmallTeamRow(DataClassJsonMixin):
    conv_id: str = field(metadata=config(field_name="convID"))
    name: str = field(metadata=config(field_name="name"))
    time: gregor1.Time = field(metadata=config(field_name="time"))
    is_muted: bool = field(metadata=config(field_name="isMuted"))
    is_team: bool = field(metadata=config(field_name="isTeam"))
    snippet: Optional[str] = field(default=None, metadata=config(field_name="snippet"))
    snippet_decoration: Optional[str] = field(
        default=None, metadata=config(field_name="snippetDecoration")
    )
    draft: Optional[str] = field(default=None, metadata=config(field_name="draft"))


class UIInboxBigTeamRowTyp(Enum):
    LABEL = 1
    CHANNEL = 2


class UIInboxBigTeamRowTypStrings(Enum):
    LABEL = "label"
    CHANNEL = "channel"


@dataclass
class UIInboxBigTeamChannelRow(DataClassJsonMixin):
    conv_id: str = field(metadata=config(field_name="convID"))
    teamname: str = field(metadata=config(field_name="teamname"))
    channelname: str = field(metadata=config(field_name="channelname"))
    is_muted: bool = field(metadata=config(field_name="isMuted"))
    draft: Optional[str] = field(default=None, metadata=config(field_name="draft"))


@dataclass
class UnverifiedInboxUIItemMetadata(DataClassJsonMixin):
    channel_name: str = field(metadata=config(field_name="channelName"))
    headline: str = field(metadata=config(field_name="headline"))
    headline_decorated: str = field(metadata=config(field_name="headlineDecorated"))
    snippet: str = field(metadata=config(field_name="snippet"))
    snippet_decoration: str = field(metadata=config(field_name="snippetDecoration"))
    writer_names: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="writerNames")
    )
    reset_participants: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="resetParticipants")
    )


class UIParticipantType(Enum):
    NONE = 0
    USER = 1
    PHONENO = 2
    EMAIL = 3


class UIParticipantTypeStrings(Enum):
    NONE = "none"
    USER = "user"
    PHONENO = "phoneno"
    EMAIL = "email"


@dataclass
class UIChannelNameMention(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    conv_id: str = field(metadata=config(field_name="convID"))


@dataclass
class UIAssetUrlInfo(DataClassJsonMixin):
    preview_url: str = field(metadata=config(field_name="previewUrl"))
    full_url: str = field(metadata=config(field_name="fullUrl"))
    full_url_cached: bool = field(metadata=config(field_name="fullUrlCached"))
    mime_type: str = field(metadata=config(field_name="mimeType"))
    inline_video_playable: bool = field(
        metadata=config(field_name="inlineVideoPlayable")
    )
    video_duration: Optional[str] = field(
        default=None, metadata=config(field_name="videoDuration")
    )


@dataclass
class UIPaymentInfo(DataClassJsonMixin):
    amount_description: str = field(metadata=config(field_name="amountDescription"))
    worth: str = field(metadata=config(field_name="worth"))
    worth_at_send_time: str = field(metadata=config(field_name="worthAtSendTime"))
    delta: stellar1.BalanceDelta = field(metadata=config(field_name="delta"))
    note: str = field(metadata=config(field_name="note"))
    payment_id: stellar1.PaymentID = field(metadata=config(field_name="paymentID"))
    status: stellar1.PaymentStatus = field(metadata=config(field_name="status"))
    status_description: str = field(metadata=config(field_name="statusDescription"))
    status_detail: str = field(metadata=config(field_name="statusDetail"))
    show_cancel: bool = field(metadata=config(field_name="showCancel"))
    from_username: str = field(metadata=config(field_name="fromUsername"))
    to_username: str = field(metadata=config(field_name="toUsername"))
    source_amount: str = field(metadata=config(field_name="sourceAmount"))
    source_asset: stellar1.Asset = field(metadata=config(field_name="sourceAsset"))
    issuer_description: str = field(metadata=config(field_name="issuerDescription"))
    account_id: Optional[stellar1.AccountID] = field(
        default=None, metadata=config(field_name="accountID")
    )


@dataclass
class UIRequestInfo(DataClassJsonMixin):
    amount: str = field(metadata=config(field_name="amount"))
    amount_description: str = field(metadata=config(field_name="amountDescription"))
    worth_at_request_time: str = field(metadata=config(field_name="worthAtRequestTime"))
    status: stellar1.RequestStatus = field(metadata=config(field_name="status"))
    asset: Optional[stellar1.Asset] = field(
        default=None, metadata=config(field_name="asset")
    )
    currency: Optional[stellar1.OutsideCurrencyCode] = field(
        default=None, metadata=config(field_name="currency")
    )


class MessageUnboxedState(Enum):
    VALID = 1
    ERROR = 2
    OUTBOX = 3
    PLACEHOLDER = 4


class MessageUnboxedStateStrings(Enum):
    VALID = "valid"
    ERROR = "error"
    OUTBOX = "outbox"
    PLACEHOLDER = "placeholder"


@dataclass
class UITeamMention(DataClassJsonMixin):
    in_team: bool = field(metadata=config(field_name="inTeam"))
    open: bool = field(metadata=config(field_name="open"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    num_members: Optional[int] = field(
        default=None, metadata=config(field_name="numMembers")
    )
    public_admins: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="publicAdmins")
    )
    conv_id: Optional[str] = field(default=None, metadata=config(field_name="convID"))


class UITextDecorationTyp(Enum):
    PAYMENT = 0
    ATMENTION = 1
    CHANNELNAMEMENTION = 2
    MAYBEMENTION = 3
    LINK = 4
    MAILTO = 5
    KBFSPATH = 6


class UITextDecorationTypStrings(Enum):
    PAYMENT = "payment"
    ATMENTION = "atmention"
    CHANNELNAMEMENTION = "channelnamemention"
    MAYBEMENTION = "maybemention"
    LINK = "link"
    MAILTO = "mailto"
    KBFSPATH = "kbfspath"


class UIMaybeMentionStatus(Enum):
    UNKNOWN = 0
    USER = 1
    TEAM = 2
    NOTHING = 3


class UIMaybeMentionStatusStrings(Enum):
    UNKNOWN = "unknown"
    USER = "user"
    TEAM = "team"
    NOTHING = "nothing"


@dataclass
class UILinkDecoration(DataClassJsonMixin):
    display: str = field(metadata=config(field_name="display"))
    url: str = field(metadata=config(field_name="url"))


class UIChatThreadStatusTyp(Enum):
    NONE = 0
    SERVER = 1
    VALIDATING = 2
    VALIDATED = 3


class UIChatThreadStatusTypStrings(Enum):
    NONE = "none"
    SERVER = "server"
    VALIDATING = "validating"
    VALIDATED = "validated"


@dataclass
class UIChatThreadStatus__NONE(DataClassJsonMixin):
    typ: Literal[UIChatThreadStatusTypStrings.NONE]
    NONE: None


@dataclass
class UIChatThreadStatus__SERVER(DataClassJsonMixin):
    typ: Literal[UIChatThreadStatusTypStrings.SERVER]
    SERVER: None


@dataclass
class UIChatThreadStatus__VALIDATING(DataClassJsonMixin):
    typ: Literal[UIChatThreadStatusTypStrings.VALIDATING]
    VALIDATING: Optional[int]


@dataclass
class UIChatThreadStatus__VALIDATED(DataClassJsonMixin):
    typ: Literal[UIChatThreadStatusTypStrings.VALIDATED]
    VALIDATED: None


UIChatThreadStatus = Union[
    UIChatThreadStatus__NONE,
    UIChatThreadStatus__SERVER,
    UIChatThreadStatus__VALIDATING,
    UIChatThreadStatus__VALIDATED,
]


@dataclass
class UIChatPayment(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    full_name: str = field(metadata=config(field_name="fullName"))
    xlm_amount: str = field(metadata=config(field_name="xlmAmount"))
    error: Optional[str] = field(default=None, metadata=config(field_name="error"))
    display_amount: Optional[str] = field(
        default=None, metadata=config(field_name="displayAmount")
    )


@dataclass
class GiphySearchResult(DataClassJsonMixin):
    target_url: str = field(metadata=config(field_name="targetUrl"))
    preview_url: str = field(metadata=config(field_name="previewUrl"))
    preview_width: int = field(metadata=config(field_name="previewWidth"))
    preview_height: int = field(metadata=config(field_name="previewHeight"))
    preview_is_video: bool = field(metadata=config(field_name="previewIsVideo"))


class UICoinFlipPhase(Enum):
    COMMITMENT = 0
    REVEALS = 1
    COMPLETE = 2
    ERROR = 3


class UICoinFlipPhaseStrings(Enum):
    COMMITMENT = "commitment"
    REVEALS = "reveals"
    COMPLETE = "complete"
    ERROR = "error"


@dataclass
class UICoinFlipErrorParticipant(DataClassJsonMixin):
    user: str = field(metadata=config(field_name="user"))
    device: str = field(metadata=config(field_name="device"))


class UICoinFlipErrorTyp(Enum):
    GENERIC = 0
    ABSENTEE = 1
    TIMEOUT = 2
    ABORTED = 3
    DUPREG = 4
    DUPCOMMITCOMPLETE = 5
    DUPREVEAL = 6
    COMMITMISMATCH = 7


class UICoinFlipErrorTypStrings(Enum):
    GENERIC = "generic"
    ABSENTEE = "absentee"
    TIMEOUT = "timeout"
    ABORTED = "aborted"
    DUPREG = "dupreg"
    DUPCOMMITCOMPLETE = "dupcommitcomplete"
    DUPREVEAL = "dupreveal"
    COMMITMISMATCH = "commitmismatch"


class UICoinFlipResultTyp(Enum):
    NUMBER = 0
    SHUFFLE = 1
    DECK = 2
    HANDS = 3
    COIN = 4


class UICoinFlipResultTypStrings(Enum):
    NUMBER = "number"
    SHUFFLE = "shuffle"
    DECK = "deck"
    HANDS = "hands"
    COIN = "coin"


@dataclass
class UICoinFlipHand(DataClassJsonMixin):
    target: str = field(metadata=config(field_name="target"))
    hand: Optional[Optional[List[int]]] = field(
        default=None, metadata=config(field_name="hand")
    )


@dataclass
class UICoinFlipParticipant(DataClassJsonMixin):
    uid: str = field(metadata=config(field_name="uid"))
    device_id: str = field(metadata=config(field_name="deviceID"))
    username: str = field(metadata=config(field_name="username"))
    device_name: str = field(metadata=config(field_name="deviceName"))
    commitment: str = field(metadata=config(field_name="commitment"))
    reveal: Optional[str] = field(default=None, metadata=config(field_name="reveal"))


@dataclass
class UICommandMarkdown(DataClassJsonMixin):
    body: str = field(metadata=config(field_name="body"))
    title: Optional[str] = field(default=None, metadata=config(field_name="title"))


LocationWatchID = int


class UIWatchPositionPerm(Enum):
    BASE = 0
    ALWAYS = 1


class UIWatchPositionPermStrings(Enum):
    BASE = "base"
    ALWAYS = "always"


class UICommandStatusDisplayTyp(Enum):
    STATUS = 0
    WARNING = 1
    ERROR = 2


class UICommandStatusDisplayTypStrings(Enum):
    STATUS = "status"
    WARNING = "warning"
    ERROR = "error"


class UICommandStatusActionTyp(Enum):
    APPSETTINGS = 0


class UICommandStatusActionTypStrings(Enum):
    APPSETTINGS = "appsettings"


class UIBotCommandsUpdateStatus(Enum):
    UPTODATE = 0
    UPDATING = 1
    FAILED = 2
    BLANK = 3


class UIBotCommandsUpdateStatusStrings(Enum):
    UPTODATE = "uptodate"
    UPDATING = "updating"
    FAILED = "failed"
    BLANK = "blank"


@dataclass
class ConversationCommand(DataClassJsonMixin):
    description: str = field(metadata=config(field_name="description"))
    name: str = field(metadata=config(field_name="name"))
    usage: str = field(metadata=config(field_name="usage"))
    has_help_text: bool = field(metadata=config(field_name="hasHelpText"))
    username: Optional[str] = field(
        default=None, metadata=config(field_name="username")
    )


class ConversationCommandGroupsTyp(Enum):
    BUILTIN = 0
    CUSTOM = 1
    NONE = 2


class ConversationCommandGroupsTypStrings(Enum):
    BUILTIN = "builtin"
    CUSTOM = "custom"
    NONE = "none"


class ConversationBuiltinCommandTyp(Enum):
    NONE = 0
    ADHOC = 1
    SMALLTEAM = 2
    BIGTEAM = 3
    BIGTEAMGENERAL = 4


class ConversationBuiltinCommandTypStrings(Enum):
    NONE = "none"
    ADHOC = "adhoc"
    SMALLTEAM = "smallteam"
    BIGTEAM = "bigteam"
    BIGTEAMGENERAL = "bigteamgeneral"


ThreadID = str
MessageID = int
TLFConvOrdinal = int
TopicID = str
ConversationID = str
TLFID = str
Hash = str
InboxVers = int
LocalConversationVers = int
ConversationVers = int
OutboxID = str
TopicNameState = str
FlipGameID = str


class ConversationExistence(Enum):
    ACTIVE = 0
    ARCHIVED = 1
    DELETED = 2
    ABANDONED = 3


class ConversationExistenceStrings(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"
    ABANDONED = "abandoned"


class ConversationMembersType(Enum):
    KBFS = 0
    TEAM = 1
    IMPTEAMNATIVE = 2
    IMPTEAMUPGRADE = 3


class ConversationMembersTypeStrings(Enum):
    KBFS = "kbfs"
    TEAM = "team"
    IMPTEAMNATIVE = "impteamnative"
    IMPTEAMUPGRADE = "impteamupgrade"


class SyncInboxResType(Enum):
    CURRENT = 0
    INCREMENTAL = 1
    CLEAR = 2


class SyncInboxResTypeStrings(Enum):
    CURRENT = "current"
    INCREMENTAL = "incremental"
    CLEAR = "clear"


class MessageType(Enum):
    NONE = 0
    TEXT = 1
    ATTACHMENT = 2
    EDIT = 3
    DELETE = 4
    METADATA = 5
    TLFNAME = 6
    HEADLINE = 7
    ATTACHMENTUPLOADED = 8
    JOIN = 9
    LEAVE = 10
    SYSTEM = 11
    DELETEHISTORY = 12
    REACTION = 13
    SENDPAYMENT = 14
    REQUESTPAYMENT = 15
    UNFURL = 16
    FLIP = 17
    PIN = 18


class MessageTypeStrings(Enum):
    NONE = "none"
    TEXT = "text"
    ATTACHMENT = "attachment"
    EDIT = "edit"
    DELETE = "delete"
    METADATA = "metadata"
    TLFNAME = "tlfname"
    HEADLINE = "headline"
    ATTACHMENTUPLOADED = "attachmentuploaded"
    JOIN = "join"
    LEAVE = "leave"
    SYSTEM = "system"
    DELETEHISTORY = "deletehistory"
    REACTION = "reaction"
    SENDPAYMENT = "sendpayment"
    REQUESTPAYMENT = "requestpayment"
    UNFURL = "unfurl"
    FLIP = "flip"
    PIN = "pin"


class TopicType(Enum):
    NONE = 0
    CHAT = 1
    DEV = 2
    KBFSFILEEDIT = 3


class TopicTypeStrings(Enum):
    NONE = "none"
    CHAT = "chat"
    DEV = "dev"
    KBFSFILEEDIT = "kbfsfileedit"


class TeamType(Enum):
    NONE = 0
    SIMPLE = 1
    COMPLEX = 2


class TeamTypeStrings(Enum):
    NONE = "none"
    SIMPLE = "simple"
    COMPLEX = "complex"


class NotificationKind(Enum):
    GENERIC = 0
    ATMENTION = 1


class NotificationKindStrings(Enum):
    GENERIC = "generic"
    ATMENTION = "atmention"


class GlobalAppNotificationSetting(Enum):
    NEWMESSAGES = 0
    PLAINTEXTMOBILE = 1
    PLAINTEXTDESKTOP = 2
    DEFAULTSOUNDMOBILE = 3
    DISABLETYPING = 4


class GlobalAppNotificationSettingStrings(Enum):
    NEWMESSAGES = "newmessages"
    PLAINTEXTMOBILE = "plaintextmobile"
    PLAINTEXTDESKTOP = "plaintextdesktop"
    DEFAULTSOUNDMOBILE = "defaultsoundmobile"
    DISABLETYPING = "disabletyping"


@dataclass
class GlobalAppNotificationSettings(DataClassJsonMixin):
    settings: Dict[str, bool] = field(metadata=config(field_name="settings"))


class ConversationStatus(Enum):
    UNFILED = 0
    FAVORITE = 1
    IGNORED = 2
    BLOCKED = 3
    MUTED = 4
    REPORTED = 5


class ConversationStatusStrings(Enum):
    UNFILED = "unfiled"
    FAVORITE = "favorite"
    IGNORED = "ignored"
    BLOCKED = "blocked"
    MUTED = "muted"
    REPORTED = "reported"


@dataclass
class KBFSPath(DataClassJsonMixin):
    start_index: int = field(metadata=config(field_name="startIndex"))
    raw_path: str = field(metadata=config(field_name="rawPath"))
    standard_path: str = field(metadata=config(field_name="standardPath"))
    path_info: keybase1.KBFSPathInfo = field(metadata=config(field_name="pathInfo"))


class ConversationMemberStatus(Enum):
    ACTIVE = 0
    REMOVED = 1
    LEFT = 2
    PREVIEW = 3
    RESET = 4
    NEVER_JOINED = 5


class ConversationMemberStatusStrings(Enum):
    ACTIVE = "active"
    REMOVED = "removed"
    LEFT = "left"
    PREVIEW = "preview"
    RESET = "reset"
    NEVER_JOINED = "never_joined"


@dataclass
class Pagination(DataClassJsonMixin):
    num: int = field(metadata=config(field_name="num"))
    next: Optional[str] = field(default=None, metadata=config(field_name="next"))
    previous: Optional[str] = field(
        default=None, metadata=config(field_name="previous")
    )
    last: Optional[bool] = field(default=None, metadata=config(field_name="last"))
    force_first_page: Optional[bool] = field(
        default=None, metadata=config(field_name="forceFirstPage")
    )


@dataclass
class RateLimit(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    calls_remaining: int = field(metadata=config(field_name="callsRemaining"))
    window_reset: int = field(metadata=config(field_name="windowReset"))
    max_calls: int = field(metadata=config(field_name="maxCalls"))


@dataclass
class ConversationFinalizeInfo(DataClassJsonMixin):
    reset_user: str = field(metadata=config(field_name="resetUser"))
    reset_date: str = field(metadata=config(field_name="resetDate"))
    reset_full: str = field(metadata=config(field_name="resetFull"))
    reset_timestamp: gregor1.Time = field(metadata=config(field_name="resetTimestamp"))


@dataclass
class ConversationResolveInfo(DataClassJsonMixin):
    new_tlf_name: str = field(metadata=config(field_name="newTLFName"))


@dataclass
class ConversationNotificationInfo(DataClassJsonMixin):
    channel_wide: bool = field(metadata=config(field_name="channelWide"))
    settings: Dict[str, Dict[str, bool]] = field(metadata=config(field_name="settings"))


@dataclass
class ConversationCreatorInfo(DataClassJsonMixin):
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))
    uid: gregor1.UID = field(metadata=config(field_name="uid"))


@dataclass
class ConversationCreatorInfoLocal(DataClassJsonMixin):
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))
    username: str = field(metadata=config(field_name="username"))


@dataclass
class ConversationMinWriterRoleInfo(DataClassJsonMixin):
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    role: keybase1.TeamRole = field(metadata=config(field_name="role"))


@dataclass
class MsgEphemeralMetadata(DataClassJsonMixin):
    lifetime: gregor1.DurationSec = field(metadata=config(field_name="l"))
    generation: keybase1.EkGeneration = field(metadata=config(field_name="g"))
    exploded_by: Optional[str] = field(default=None, metadata=config(field_name="u"))


@dataclass
class EncryptedData(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    e: str = field(metadata=config(field_name="e"))
    n: str = field(metadata=config(field_name="n"))


@dataclass
class SignEncryptedData(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    e: str = field(metadata=config(field_name="e"))
    n: str = field(metadata=config(field_name="n"))


@dataclass
class SealedData(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    e: str = field(metadata=config(field_name="e"))
    n: str = field(metadata=config(field_name="n"))


@dataclass
class SignatureInfo(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    s: str = field(metadata=config(field_name="s"))
    k: str = field(metadata=config(field_name="k"))


@dataclass
class MerkleRoot(DataClassJsonMixin):
    seqno: int = field(metadata=config(field_name="seqno"))
    hash: str = field(metadata=config(field_name="hash"))


class InboxResType(Enum):
    VERSIONHIT = 0
    FULL = 1


class InboxResTypeStrings(Enum):
    VERSIONHIT = "versionhit"
    FULL = "full"


class RetentionPolicyType(Enum):
    NONE = 0
    RETAIN = 1
    EXPIRE = 2
    INHERIT = 3
    EPHEMERAL = 4


class RetentionPolicyTypeStrings(Enum):
    NONE = "none"
    RETAIN = "retain"
    EXPIRE = "expire"
    INHERIT = "inherit"
    EPHEMERAL = "ephemeral"


@dataclass
class RpRetain(DataClassJsonMixin):
    pass


@dataclass
class RpExpire(DataClassJsonMixin):
    age: gregor1.DurationSec = field(metadata=config(field_name="age"))


@dataclass
class RpInherit(DataClassJsonMixin):
    pass


@dataclass
class RpEphemeral(DataClassJsonMixin):
    age: gregor1.DurationSec = field(metadata=config(field_name="age"))


class GetThreadReason(Enum):
    GENERAL = 0
    PUSH = 1
    FOREGROUND = 2
    BACKGROUNDCONVLOAD = 3
    FIXRETRY = 4
    PREPARE = 5
    SEARCHER = 6
    INDEXED_SEARCH = 7
    KBFSFILEACTIVITY = 8
    COINFLIP = 9
    BOTCOMMANDS = 10


class GetThreadReasonStrings(Enum):
    GENERAL = "general"
    PUSH = "push"
    FOREGROUND = "foreground"
    BACKGROUNDCONVLOAD = "backgroundconvload"
    FIXRETRY = "fixretry"
    PREPARE = "prepare"
    SEARCHER = "searcher"
    INDEXED_SEARCH = "indexed_search"
    KBFSFILEACTIVITY = "kbfsfileactivity"
    COINFLIP = "coinflip"
    BOTCOMMANDS = "botcommands"


class ReIndexingMode(Enum):
    NONE = 0
    PRESEARCH_SYNC = 1
    POSTSEARCH_SYNC = 2


class ReIndexingModeStrings(Enum):
    NONE = "none"
    PRESEARCH_SYNC = "presearch_sync"
    POSTSEARCH_SYNC = "postsearch_sync"


@dataclass
class EmptyStruct(DataClassJsonMixin):
    pass


@dataclass
class ChatSearchMatch(DataClassJsonMixin):
    start_index: int = field(metadata=config(field_name="startIndex"))
    end_index: int = field(metadata=config(field_name="endIndex"))
    match: str = field(metadata=config(field_name="match"))


@dataclass
class ChatSearchInboxDone(DataClassJsonMixin):
    num_hits: int = field(metadata=config(field_name="numHits"))
    num_convs: int = field(metadata=config(field_name="numConvs"))
    percent_indexed: int = field(metadata=config(field_name="percentIndexed"))
    delegated: bool = field(metadata=config(field_name="delegated"))


@dataclass
class ChatSearchIndexStatus(DataClassJsonMixin):
    percent_indexed: int = field(metadata=config(field_name="percentIndexed"))


@dataclass
class AssetMetadataImage(DataClassJsonMixin):
    width: int = field(metadata=config(field_name="width"))
    height: int = field(metadata=config(field_name="height"))


@dataclass
class AssetMetadataVideo(DataClassJsonMixin):
    width: int = field(metadata=config(field_name="width"))
    height: int = field(metadata=config(field_name="height"))
    duration_ms: int = field(metadata=config(field_name="durationMs"))


@dataclass
class AssetMetadataAudio(DataClassJsonMixin):
    duration_ms: int = field(metadata=config(field_name="durationMs"))


class AssetMetadataType(Enum):
    NONE = 0
    IMAGE = 1
    VIDEO = 2
    AUDIO = 3


class AssetMetadataTypeStrings(Enum):
    NONE = "none"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"


class AssetTag(Enum):
    PRIMARY = 0


class AssetTagStrings(Enum):
    PRIMARY = "primary"


class BotCommandsAdvertisementTyp(Enum):
    PUBLIC = 0
    TLFID_MEMBERS = 1
    TLFID_CONVS = 2


class BotCommandsAdvertisementTypStrings(Enum):
    PUBLIC = "public"
    TLFID_MEMBERS = "tlfid_members"
    TLFID_CONVS = "tlfid_convs"


@dataclass
class TeamMember(DataClassJsonMixin):
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    role: keybase1.TeamRole = field(metadata=config(field_name="role"))
    status: keybase1.TeamMemberStatus = field(metadata=config(field_name="status"))


VersionKind = str


class TextPaymentResultTyp(Enum):
    SENT = 0
    ERROR = 1


class TextPaymentResultTypStrings(Enum):
    SENT = "sent"
    ERROR = "error"


@dataclass
class TextPaymentResult__ERROR(DataClassJsonMixin):
    resultTyp: Literal[TextPaymentResultTypStrings.ERROR]
    ERROR: Optional[str]


@dataclass
class TextPaymentResult__SENT(DataClassJsonMixin):
    resultTyp: Literal[TextPaymentResultTypStrings.SENT]
    SENT: Optional[stellar1.PaymentID]


TextPaymentResult = Union[TextPaymentResult__ERROR, TextPaymentResult__SENT]


@dataclass
class KnownUserMention(DataClassJsonMixin):
    text: str = field(metadata=config(field_name="text"))
    uid: gregor1.UID = field(metadata=config(field_name="uid"))


@dataclass
class KnownTeamMention(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    channel: str = field(metadata=config(field_name="channel"))


@dataclass
class MaybeMention(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    channel: str = field(metadata=config(field_name="channel"))


@dataclass
class Coordinate(DataClassJsonMixin):
    lat: float = field(metadata=config(field_name="lat"))
    lon: float = field(metadata=config(field_name="lon"))
    accuracy: float = field(metadata=config(field_name="accuracy"))


@dataclass
class LiveLocation(DataClassJsonMixin):
    end_time: gregor1.Time = field(metadata=config(field_name="endTime"))


@dataclass
class MessageConversationMetadata(DataClassJsonMixin):
    conversation_title: str = field(metadata=config(field_name="conversationTitle"))


@dataclass
class MessageHeadline(DataClassJsonMixin):
    headline: str = field(metadata=config(field_name="headline"))


class MessageSystemType(Enum):
    ADDEDTOTEAM = 0
    INVITEADDEDTOTEAM = 1
    COMPLEXTEAM = 2
    CREATETEAM = 3
    GITPUSH = 4
    CHANGEAVATAR = 5
    CHANGERETENTION = 6
    BULKADDTOCONV = 7
    SBSRESOLVE = 8


class MessageSystemTypeStrings(Enum):
    ADDEDTOTEAM = "addedtoteam"
    INVITEADDEDTOTEAM = "inviteaddedtoteam"
    COMPLEXTEAM = "complexteam"
    CREATETEAM = "createteam"
    GITPUSH = "gitpush"
    CHANGEAVATAR = "changeavatar"
    CHANGERETENTION = "changeretention"
    BULKADDTOCONV = "bulkaddtoconv"
    SBSRESOLVE = "sbsresolve"


@dataclass
class MessageSystemAddedToTeam(DataClassJsonMixin):
    team: str = field(metadata=config(field_name="team"))
    adder: str = field(metadata=config(field_name="adder"))
    addee: str = field(metadata=config(field_name="addee"))
    owners: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="owners")
    )
    admins: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="admins")
    )
    writers: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="writers")
    )
    readers: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="readers")
    )
    bots: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="bots")
    )
    restricted_bots: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="restrictedBots")
    )


@dataclass
class MessageSystemInviteAddedToTeam(DataClassJsonMixin):
    team: str = field(metadata=config(field_name="team"))
    inviter: str = field(metadata=config(field_name="inviter"))
    invitee: str = field(metadata=config(field_name="invitee"))
    adder: str = field(metadata=config(field_name="adder"))
    invite_type: keybase1.TeamInviteCategory = field(
        metadata=config(field_name="inviteType")
    )


@dataclass
class MessageSystemComplexTeam(DataClassJsonMixin):
    team: str = field(metadata=config(field_name="team"))


@dataclass
class MessageSystemCreateTeam(DataClassJsonMixin):
    team: str = field(metadata=config(field_name="team"))
    creator: str = field(metadata=config(field_name="creator"))


@dataclass
class MessageSystemGitPush(DataClassJsonMixin):
    team: str = field(metadata=config(field_name="team"))
    pusher: str = field(metadata=config(field_name="pusher"))
    repo_name: str = field(metadata=config(field_name="repoName"))
    repo_id: keybase1.RepoID = field(metadata=config(field_name="repoID"))
    push_type: keybase1.GitPushType = field(metadata=config(field_name="pushType"))
    previous_repo_name: str = field(metadata=config(field_name="previousRepoName"))
    refs: Optional[Optional[List[keybase1.GitRefMetadata]]] = field(
        default=None, metadata=config(field_name="refs")
    )


@dataclass
class MessageSystemChangeAvatar(DataClassJsonMixin):
    team: str = field(metadata=config(field_name="team"))
    user: str = field(metadata=config(field_name="user"))


@dataclass
class MessageSystemBulkAddToConv(DataClassJsonMixin):
    usernames: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="usernames")
    )


@dataclass
class MessageSystemSbsResolve(DataClassJsonMixin):
    assertion_service: str = field(metadata=config(field_name="assertionService"))
    assertion_username: str = field(metadata=config(field_name="assertionUsername"))
    prover: str = field(metadata=config(field_name="prover"))


@dataclass
class MessageJoin(DataClassJsonMixin):
    joiners: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="joiners")
    )
    leavers: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="leavers")
    )


@dataclass
class MessageLeave(DataClassJsonMixin):
    pass


@dataclass
class MessageSendPayment(DataClassJsonMixin):
    payment_id: stellar1.PaymentID = field(metadata=config(field_name="paymentID"))


@dataclass
class MessageRequestPayment(DataClassJsonMixin):
    request_id: stellar1.KeybaseRequestID = field(
        metadata=config(field_name="requestID")
    )
    note: str = field(metadata=config(field_name="note"))


class OutboxStateType(Enum):
    SENDING = 0
    ERROR = 1


class OutboxStateTypeStrings(Enum):
    SENDING = "sending"
    ERROR = "error"


class OutboxErrorType(Enum):
    MISC = 0
    OFFLINE = 1
    IDENTIFY = 2
    TOOLONG = 3
    DUPLICATE = 4
    EXPIRED = 5
    TOOMANYATTEMPTS = 6
    ALREADY_DELETED = 7
    UPLOADFAILED = 8
    RESTRICTEDBOT = 9


class OutboxErrorTypeStrings(Enum):
    MISC = "misc"
    OFFLINE = "offline"
    IDENTIFY = "identify"
    TOOLONG = "toolong"
    DUPLICATE = "duplicate"
    EXPIRED = "expired"
    TOOMANYATTEMPTS = "toomanyattempts"
    ALREADY_DELETED = "already_deleted"
    UPLOADFAILED = "uploadfailed"
    RESTRICTEDBOT = "restrictedbot"


class HeaderPlaintextVersion(Enum):
    V1 = 1
    V2 = 2
    V3 = 3
    V4 = 4
    V5 = 5
    V6 = 6
    V7 = 7
    V8 = 8
    V9 = 9
    V10 = 10


class HeaderPlaintextVersionStrings(Enum):
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"
    V4 = "v4"
    V5 = "v5"
    V6 = "v6"
    V7 = "v7"
    V8 = "v8"
    V9 = "v9"
    V10 = "v10"


@dataclass
class HeaderPlaintextMetaInfo(DataClassJsonMixin):
    crit: bool = field(metadata=config(field_name="crit"))


class BodyPlaintextVersion(Enum):
    V1 = 1
    V2 = 2
    V3 = 3
    V4 = 4
    V5 = 5
    V6 = 6
    V7 = 7
    V8 = 8
    V9 = 9
    V10 = 10


class BodyPlaintextVersionStrings(Enum):
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"
    V4 = "v4"
    V5 = "v5"
    V6 = "v6"
    V7 = "v7"
    V8 = "v8"
    V9 = "v9"
    V10 = "v10"


@dataclass
class BodyPlaintextMetaInfo(DataClassJsonMixin):
    crit: bool = field(metadata=config(field_name="crit"))


class MessageUnboxedErrorType(Enum):
    MISC = 0
    BADVERSION_CRITICAL = 1
    BADVERSION = 2
    IDENTIFY = 3
    EPHEMERAL = 4
    PAIRWISE_MISSING = 5


class MessageUnboxedErrorTypeStrings(Enum):
    MISC = "misc"
    BADVERSION_CRITICAL = "badversion_critical"
    BADVERSION = "badversion"
    IDENTIFY = "identify"
    EPHEMERAL = "ephemeral"
    PAIRWISE_MISSING = "pairwise_missing"


@dataclass
class UnreadFirstNumLimit(DataClassJsonMixin):
    num_read: int = field(metadata=config(field_name="NumRead"))
    at_least: int = field(metadata=config(field_name="AtLeast"))
    at_most: int = field(metadata=config(field_name="AtMost"))


@dataclass
class ConversationLocalParticipant(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    fullname: Optional[str] = field(
        default=None, metadata=config(field_name="fullname")
    )
    contact_name: Optional[str] = field(
        default=None, metadata=config(field_name="contactName")
    )


class ConversationErrorType(Enum):
    PERMANENT = 0
    MISSINGINFO = 1
    SELFREKEYNEEDED = 2
    OTHERREKEYNEEDED = 3
    IDENTIFY = 4
    TRANSIENT = 5
    NONE = 6


class ConversationErrorTypeStrings(Enum):
    PERMANENT = "permanent"
    MISSINGINFO = "missinginfo"
    SELFREKEYNEEDED = "selfrekeyneeded"
    OTHERREKEYNEEDED = "otherrekeyneeded"
    IDENTIFY = "identify"
    TRANSIENT = "transient"
    NONE = "none"


@dataclass
class ConversationErrorRekey(DataClassJsonMixin):
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    tlf_public: bool = field(metadata=config(field_name="tlfPublic"))
    rekeyers: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="rekeyers")
    )
    writer_names: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="writerNames")
    )
    reader_names: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="readerNames")
    )


@dataclass
class ConversationMinWriterRoleInfoLocal(DataClassJsonMixin):
    changed_by: str = field(metadata=config(field_name="changedBy"))
    cannot_write: bool = field(metadata=config(field_name="cannotWrite"))
    role: keybase1.TeamRole = field(metadata=config(field_name="role"))


class MessageIDControlMode(Enum):
    OLDERMESSAGES = 0
    NEWERMESSAGES = 1
    CENTERED = 2
    UNREADLINE = 3


class MessageIDControlModeStrings(Enum):
    OLDERMESSAGES = "oldermessages"
    NEWERMESSAGES = "newermessages"
    CENTERED = "centered"
    UNREADLINE = "unreadline"


class GetThreadNonblockCbMode(Enum):
    FULL = 0
    INCREMENTAL = 1


class GetThreadNonblockCbModeStrings(Enum):
    FULL = "full"
    INCREMENTAL = "incremental"


class GetThreadNonblockPgMode(Enum):
    DEFAULT = 0
    SERVER = 1


class GetThreadNonblockPgModeStrings(Enum):
    DEFAULT = "default"
    SERVER = "server"


class PreviewLocationTyp(Enum):
    URL = 0
    FILE = 1
    BYTES = 2


class PreviewLocationTypStrings(Enum):
    URL = "url"
    FILE = "file"
    BYTES = "bytes"


@dataclass
class PreviewLocation__URL(DataClassJsonMixin):
    ltyp: Literal[PreviewLocationTypStrings.URL]
    URL: Optional[str]


@dataclass
class PreviewLocation__FILE(DataClassJsonMixin):
    ltyp: Literal[PreviewLocationTypStrings.FILE]
    FILE: Optional[str]


@dataclass
class PreviewLocation__BYTES(DataClassJsonMixin):
    ltyp: Literal[PreviewLocationTypStrings.BYTES]
    BYTES: Optional[str]


PreviewLocation = Union[
    PreviewLocation__URL, PreviewLocation__FILE, PreviewLocation__BYTES
]


class UnfurlPromptAction(Enum):
    ALWAYS = 0
    NEVER = 1
    ACCEPT = 2
    NOTNOW = 3
    ONETIME = 4


class UnfurlPromptActionStrings(Enum):
    ALWAYS = "always"
    NEVER = "never"
    ACCEPT = "accept"
    NOTNOW = "notnow"
    ONETIME = "onetime"


@dataclass
class UnfurlPromptResult__ALWAYS(DataClassJsonMixin):
    actionType: Literal[UnfurlPromptActionStrings.ALWAYS]
    ALWAYS: None


@dataclass
class UnfurlPromptResult__NEVER(DataClassJsonMixin):
    actionType: Literal[UnfurlPromptActionStrings.NEVER]
    NEVER: None


@dataclass
class UnfurlPromptResult__NOTNOW(DataClassJsonMixin):
    actionType: Literal[UnfurlPromptActionStrings.NOTNOW]
    NOTNOW: None


@dataclass
class UnfurlPromptResult__ACCEPT(DataClassJsonMixin):
    actionType: Literal[UnfurlPromptActionStrings.ACCEPT]
    ACCEPT: Optional[str]


@dataclass
class UnfurlPromptResult__ONETIME(DataClassJsonMixin):
    actionType: Literal[UnfurlPromptActionStrings.ONETIME]
    ONETIME: Optional[str]


UnfurlPromptResult = Union[
    UnfurlPromptResult__ALWAYS,
    UnfurlPromptResult__NEVER,
    UnfurlPromptResult__NOTNOW,
    UnfurlPromptResult__ACCEPT,
    UnfurlPromptResult__ONETIME,
]


class GalleryItemTyp(Enum):
    MEDIA = 0
    LINK = 1
    DOC = 2


class GalleryItemTypStrings(Enum):
    MEDIA = "media"
    LINK = "link"
    DOC = "doc"


@dataclass
class UserBotExtendedDescription(DataClassJsonMixin):
    title: str = field(metadata=config(field_name="title"))
    desktop_body: str = field(metadata=config(field_name="desktop_body"))
    mobile_body: str = field(metadata=config(field_name="mobile_body"))


class ChatActivitySource(Enum):
    LOCAL = 0
    REMOTE = 1


class ChatActivitySourceStrings(Enum):
    LOCAL = "local"
    REMOTE = "remote"


class ChatActivityType(Enum):
    RESERVED = 0
    INCOMING_MESSAGE = 1
    READ_MESSAGE = 2
    NEW_CONVERSATION = 3
    SET_STATUS = 4
    FAILED_MESSAGE = 5
    MEMBERS_UPDATE = 6
    SET_APP_NOTIFICATION_SETTINGS = 7
    TEAMTYPE = 8
    EXPUNGE = 9
    EPHEMERAL_PURGE = 10
    REACTION_UPDATE = 11
    MESSAGES_UPDATED = 12


class ChatActivityTypeStrings(Enum):
    RESERVED = "reserved"
    INCOMING_MESSAGE = "incoming_message"
    READ_MESSAGE = "read_message"
    NEW_CONVERSATION = "new_conversation"
    SET_STATUS = "set_status"
    FAILED_MESSAGE = "failed_message"
    MEMBERS_UPDATE = "members_update"
    SET_APP_NOTIFICATION_SETTINGS = "set_app_notification_settings"
    TEAMTYPE = "teamtype"
    EXPUNGE = "expunge"
    EPHEMERAL_PURGE = "ephemeral_purge"
    REACTION_UPDATE = "reaction_update"
    MESSAGES_UPDATED = "messages_updated"


@dataclass
class TyperInfo(DataClassJsonMixin):
    uid: keybase1.UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    device_id: keybase1.DeviceID = field(metadata=config(field_name="deviceID"))
    device_name: str = field(metadata=config(field_name="deviceName"))
    device_type: str = field(metadata=config(field_name="deviceType"))


class StaleUpdateType(Enum):
    CLEAR = 0
    NEWACTIVITY = 1
    CONVUPDATE = 2


class StaleUpdateTypeStrings(Enum):
    CLEAR = "clear"
    NEWACTIVITY = "newactivity"
    CONVUPDATE = "convupdate"


class MessageBoxedVersion(Enum):
    VNONE = 0
    V1 = 1
    V2 = 2
    V3 = 3
    V4 = 4


class MessageBoxedVersionStrings(Enum):
    VNONE = "vnone"
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"
    V4 = "v4"


class ChannelMention(Enum):
    NONE = 0
    ALL = 1
    HERE = 2


class ChannelMentionStrings(Enum):
    NONE = "none"
    ALL = "all"
    HERE = "here"


@dataclass
class S3Params(DataClassJsonMixin):
    bucket: str = field(metadata=config(field_name="bucket"))
    object_key: str = field(metadata=config(field_name="objectKey"))
    access_key: str = field(metadata=config(field_name="accessKey"))
    acl: str = field(metadata=config(field_name="acl"))
    region_name: str = field(metadata=config(field_name="regionName"))
    region_endpoint: str = field(metadata=config(field_name="regionEndpoint"))
    region_bucket_endpoint: str = field(
        metadata=config(field_name="regionBucketEndpoint")
    )


@dataclass
class ServerCacheVers(DataClassJsonMixin):
    inbox_vers: int = field(metadata=config(field_name="inboxVers"))
    bodies_vers: int = field(metadata=config(field_name="bodiesVers"))


class SyncAllProtVers(Enum):
    V0 = 0
    V1 = 1


class SyncAllProtVersStrings(Enum):
    V0 = "v0"
    V1 = "v1"


class SyncAllNotificationType(Enum):
    STATE = 0
    INCREMENTAL = 1


class SyncAllNotificationTypeStrings(Enum):
    STATE = "state"
    INCREMENTAL = "incremental"


@dataclass
class SyncAllNotificationRes__STATE(DataClassJsonMixin):
    typ: Literal[SyncAllNotificationTypeStrings.STATE]
    STATE: Optional[gregor1.State]


@dataclass
class SyncAllNotificationRes__INCREMENTAL(DataClassJsonMixin):
    typ: Literal[SyncAllNotificationTypeStrings.INCREMENTAL]
    INCREMENTAL: Optional[gregor1.SyncResult]


SyncAllNotificationRes = Union[
    SyncAllNotificationRes__STATE, SyncAllNotificationRes__INCREMENTAL
]


class ExternalAPIKeyTyp(Enum):
    GOOGLEMAPS = 0
    GIPHY = 1


class ExternalAPIKeyTypStrings(Enum):
    GOOGLEMAPS = "googlemaps"
    GIPHY = "giphy"


@dataclass
class ExternalAPIKey__GOOGLEMAPS(DataClassJsonMixin):
    typ: Literal[ExternalAPIKeyTypStrings.GOOGLEMAPS]
    GOOGLEMAPS: Optional[str]


@dataclass
class ExternalAPIKey__GIPHY(DataClassJsonMixin):
    typ: Literal[ExternalAPIKeyTypStrings.GIPHY]
    GIPHY: Optional[str]


ExternalAPIKey = Union[ExternalAPIKey__GOOGLEMAPS, ExternalAPIKey__GIPHY]

CommandConvVers = int


class BotInfoResponseTyp(Enum):
    UPTODATE = 0
    INFO = 1


class BotInfoResponseTypStrings(Enum):
    UPTODATE = "uptodate"
    INFO = "info"


BotInfoHash = str


class UnfurlType(Enum):
    GENERIC = 0
    YOUTUBE = 1
    GIPHY = 2
    MAPS = 3


class UnfurlTypeStrings(Enum):
    GENERIC = "generic"
    YOUTUBE = "youtube"
    GIPHY = "giphy"
    MAPS = "maps"


@dataclass
class UnfurlVideo(DataClassJsonMixin):
    url: str = field(metadata=config(field_name="url"))
    mime_type: str = field(metadata=config(field_name="mimeType"))
    height: int = field(metadata=config(field_name="height"))
    width: int = field(metadata=config(field_name="width"))


@dataclass
class UnfurlYoutubeRaw(DataClassJsonMixin):
    pass


@dataclass
class UnfurlYoutube(DataClassJsonMixin):
    pass


@dataclass
class UnfurlImageDisplay(DataClassJsonMixin):
    url: str = field(metadata=config(field_name="url"))
    height: int = field(metadata=config(field_name="height"))
    width: int = field(metadata=config(field_name="width"))
    is_video: bool = field(metadata=config(field_name="isVideo"))


@dataclass
class UnfurlYoutubeDisplay(DataClassJsonMixin):
    pass


class UnfurlMode(Enum):
    ALWAYS = 0
    NEVER = 1
    WHITELISTED = 2


class UnfurlModeStrings(Enum):
    ALWAYS = "always"
    NEVER = "never"
    WHITELISTED = "whitelisted"


@dataclass
class MsgFlipContent(DataClassJsonMixin):
    text: str = field(metadata=config(field_name="text"))
    game_id: str = field(metadata=config(field_name="game_id"))
    flip_conv_id: str = field(metadata=config(field_name="flip_conv_id"))
    user_mentions: Optional[Optional[List[KnownUserMention]]] = field(
        default=None, metadata=config(field_name="user_mentions")
    )
    team_mentions: Optional[Optional[List[KnownTeamMention]]] = field(
        default=None, metadata=config(field_name="team_mentions")
    )


@dataclass
class ConvSummary(DataClassJsonMixin):
    id: str = field(metadata=config(field_name="id"))
    channel: ChatChannel = field(metadata=config(field_name="channel"))
    unread: bool = field(metadata=config(field_name="unread"))
    active_at: int = field(metadata=config(field_name="active_at"))
    active_at_ms: int = field(metadata=config(field_name="active_at_ms"))
    member_status: str = field(metadata=config(field_name="member_status"))
    reset_users: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="reset_users")
    )
    finalize_info: Optional[ConversationFinalizeInfo] = field(
        default=None, metadata=config(field_name="finalize_info")
    )
    supersedes: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="supersedes")
    )
    superseded_by: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="superseded_by")
    )
    error: Optional[str] = field(default=None, metadata=config(field_name="error"))


@dataclass
class SendRes(DataClassJsonMixin):
    message: str = field(metadata=config(field_name="message"))
    message_id: Optional[MessageID] = field(
        default=None, metadata=config(field_name="id")
    )
    outbox_id: Optional[OutboxID] = field(
        default=None, metadata=config(field_name="outbox_id")
    )
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identify_failures")
    )
    rate_limits: Optional[Optional[List[RateLimitRes]]] = field(
        default=None, metadata=config(field_name="ratelimits")
    )


@dataclass
class NewConvRes(DataClassJsonMixin):
    id: str = field(metadata=config(field_name="id"))
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identify_failures")
    )
    rate_limits: Optional[Optional[List[RateLimitRes]]] = field(
        default=None, metadata=config(field_name="ratelimits")
    )


@dataclass
class EmptyRes(DataClassJsonMixin):
    rate_limits: Optional[Optional[List[RateLimitRes]]] = field(
        default=None, metadata=config(field_name="ratelimits")
    )


@dataclass
class GetResetConvMembersRes(DataClassJsonMixin):
    members: Optional[Optional[List[ResetConvMemberAPI]]] = field(
        default=None, metadata=config(field_name="members")
    )
    rate_limits: Optional[Optional[List[RateLimitRes]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )


@dataclass
class UIInboxBigTeamRow__LABEL(DataClassJsonMixin):
    state: Literal[UIInboxBigTeamRowTypStrings.LABEL]
    LABEL: Optional[str]


@dataclass
class UIInboxBigTeamRow__CHANNEL(DataClassJsonMixin):
    state: Literal[UIInboxBigTeamRowTypStrings.CHANNEL]
    CHANNEL: Optional[UIInboxBigTeamChannelRow]


UIInboxBigTeamRow = Union[UIInboxBigTeamRow__LABEL, UIInboxBigTeamRow__CHANNEL]


@dataclass
class UIParticipant(DataClassJsonMixin):
    type: UIParticipantType = field(metadata=config(field_name="type"))
    assertion: str = field(metadata=config(field_name="assertion"))
    full_name: Optional[str] = field(
        default=None, metadata=config(field_name="fullName")
    )
    contact_name: Optional[str] = field(
        default=None, metadata=config(field_name="contactName")
    )


@dataclass
class UIMaybeMentionInfo__UNKNOWN(DataClassJsonMixin):
    status: Literal[UIMaybeMentionStatusStrings.UNKNOWN]
    UNKNOWN: None


@dataclass
class UIMaybeMentionInfo__USER(DataClassJsonMixin):
    status: Literal[UIMaybeMentionStatusStrings.USER]
    USER: None


@dataclass
class UIMaybeMentionInfo__TEAM(DataClassJsonMixin):
    status: Literal[UIMaybeMentionStatusStrings.TEAM]
    TEAM: Optional[UITeamMention]


@dataclass
class UIMaybeMentionInfo__NOTHING(DataClassJsonMixin):
    status: Literal[UIMaybeMentionStatusStrings.NOTHING]
    NOTHING: None


UIMaybeMentionInfo = Union[
    UIMaybeMentionInfo__UNKNOWN,
    UIMaybeMentionInfo__USER,
    UIMaybeMentionInfo__TEAM,
    UIMaybeMentionInfo__NOTHING,
]


@dataclass
class UIChatSearchConvHit(DataClassJsonMixin):
    conv_id: str = field(metadata=config(field_name="convID"))
    team_type: TeamType = field(metadata=config(field_name="teamType"))
    name: str = field(metadata=config(field_name="name"))
    mtime: gregor1.Time = field(metadata=config(field_name="mtime"))


@dataclass
class UIChatPaymentSummary(DataClassJsonMixin):
    xlm_total: str = field(metadata=config(field_name="xlmTotal"))
    display_total: str = field(metadata=config(field_name="displayTotal"))
    payments: Optional[Optional[List[UIChatPayment]]] = field(
        default=None, metadata=config(field_name="payments")
    )


@dataclass
class GiphySearchResults(DataClassJsonMixin):
    gallery_url: str = field(metadata=config(field_name="galleryUrl"))
    results: Optional[Optional[List[GiphySearchResult]]] = field(
        default=None, metadata=config(field_name="results")
    )


@dataclass
class UICoinFlipAbsenteeError(DataClassJsonMixin):
    absentees: Optional[Optional[List[UICoinFlipErrorParticipant]]] = field(
        default=None, metadata=config(field_name="absentees")
    )


@dataclass
class UICoinFlipResult__NUMBER(DataClassJsonMixin):
    typ: Literal[UICoinFlipResultTypStrings.NUMBER]
    NUMBER: Optional[str]


@dataclass
class UICoinFlipResult__SHUFFLE(DataClassJsonMixin):
    typ: Literal[UICoinFlipResultTypStrings.SHUFFLE]
    SHUFFLE: Optional[List[str]]


@dataclass
class UICoinFlipResult__DECK(DataClassJsonMixin):
    typ: Literal[UICoinFlipResultTypStrings.DECK]
    DECK: Optional[List[int]]


@dataclass
class UICoinFlipResult__HANDS(DataClassJsonMixin):
    typ: Literal[UICoinFlipResultTypStrings.HANDS]
    HANDS: Optional[List[UICoinFlipHand]]


@dataclass
class UICoinFlipResult__COIN(DataClassJsonMixin):
    typ: Literal[UICoinFlipResultTypStrings.COIN]
    COIN: Optional[bool]


UICoinFlipResult = Union[
    UICoinFlipResult__NUMBER,
    UICoinFlipResult__SHUFFLE,
    UICoinFlipResult__DECK,
    UICoinFlipResult__HANDS,
    UICoinFlipResult__COIN,
]


@dataclass
class ConversationCommandGroupsCustom(DataClassJsonMixin):
    commands: Optional[Optional[List[ConversationCommand]]] = field(
        default=None, metadata=config(field_name="commands")
    )


@dataclass
class InboxVersInfo(DataClassJsonMixin):
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    vers: InboxVers = field(metadata=config(field_name="vers"))


@dataclass
class ConversationMember(DataClassJsonMixin):
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))


@dataclass
class ConversationIDMessageIDPair(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    msg_id: MessageID = field(metadata=config(field_name="msgID"))


@dataclass
class ChannelNameMention(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    topic_name: str = field(metadata=config(field_name="topicName"))


@dataclass
class GetInboxQuery(DataClassJsonMixin):
    unread_only: bool = field(metadata=config(field_name="unreadOnly"))
    read_only: bool = field(metadata=config(field_name="readOnly"))
    compute_active_list: bool = field(metadata=config(field_name="computeActiveList"))
    summarize_max_msgs: bool = field(metadata=config(field_name="summarizeMaxMsgs"))
    skip_bg_loads: bool = field(metadata=config(field_name="skipBgLoads"))
    conv_id: Optional[ConversationID] = field(
        default=None, metadata=config(field_name="convID")
    )
    topic_type: Optional[TopicType] = field(
        default=None, metadata=config(field_name="topicType")
    )
    tlf_id: Optional[TLFID] = field(default=None, metadata=config(field_name="tlfID"))
    tlf_visibility: Optional[keybase1.TLFVisibility] = field(
        default=None, metadata=config(field_name="tlfVisibility")
    )
    before: Optional[gregor1.Time] = field(
        default=None, metadata=config(field_name="before")
    )
    after: Optional[gregor1.Time] = field(
        default=None, metadata=config(field_name="after")
    )
    one_chat_type_per_tlf: Optional[bool] = field(
        default=None, metadata=config(field_name="oneChatTypePerTLF")
    )
    topic_name: Optional[str] = field(
        default=None, metadata=config(field_name="topicName")
    )
    status: Optional[Optional[List[ConversationStatus]]] = field(
        default=None, metadata=config(field_name="status")
    )
    member_status: Optional[Optional[List[ConversationMemberStatus]]] = field(
        default=None, metadata=config(field_name="memberStatus")
    )
    existences: Optional[Optional[List[ConversationExistence]]] = field(
        default=None, metadata=config(field_name="existences")
    )
    members_types: Optional[Optional[List[ConversationMembersType]]] = field(
        default=None, metadata=config(field_name="membersTypes")
    )
    conv_i_ds: Optional[Optional[List[ConversationID]]] = field(
        default=None, metadata=config(field_name="convIDs")
    )


@dataclass
class ConversationIDTriple(DataClassJsonMixin):
    tlfid: TLFID = field(metadata=config(field_name="tlfid"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    topic_id: TopicID = field(metadata=config(field_name="topicID"))


@dataclass
class Expunge(DataClassJsonMixin):
    upto: MessageID = field(metadata=config(field_name="upto"))
    basis: MessageID = field(metadata=config(field_name="basis"))


@dataclass
class ConversationReaderInfo(DataClassJsonMixin):
    mtime: gregor1.Time = field(metadata=config(field_name="mtime"))
    read_msgid: MessageID = field(metadata=config(field_name="readMsgid"))
    max_msgid: MessageID = field(metadata=config(field_name="maxMsgid"))
    status: ConversationMemberStatus = field(metadata=config(field_name="status"))
    untrusted_team_role: keybase1.TeamRole = field(
        metadata=config(field_name="untrustedTeamRole")
    )


@dataclass
class ConversationSettings(DataClassJsonMixin):
    min_writer_role_info: Optional[ConversationMinWriterRoleInfo] = field(
        default=None, metadata=config(field_name="mwr")
    )


@dataclass
class MessageSummary(DataClassJsonMixin):
    msg_id: MessageID = field(metadata=config(field_name="msgID"))
    message_type: MessageType = field(metadata=config(field_name="messageType"))
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    tlf_public: bool = field(metadata=config(field_name="tlfPublic"))
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))


@dataclass
class Reaction(DataClassJsonMixin):
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))
    reaction_msg_id: MessageID = field(metadata=config(field_name="reactionMsgID"))


@dataclass
class MessageServerHeader(DataClassJsonMixin):
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    superseded_by: MessageID = field(metadata=config(field_name="supersededBy"))
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))
    now: gregor1.Time = field(metadata=config(field_name="n"))
    reaction_i_ds: Optional[Optional[List[MessageID]]] = field(
        default=None, metadata=config(field_name="r")
    )
    unfurl_i_ds: Optional[Optional[List[MessageID]]] = field(
        default=None, metadata=config(field_name="u")
    )
    replies: Optional[Optional[List[MessageID]]] = field(
        default=None, metadata=config(field_name="replies")
    )
    rtime: Optional[gregor1.Time] = field(
        default=None, metadata=config(field_name="rt")
    )


@dataclass
class MessagePreviousPointer(DataClassJsonMixin):
    id: MessageID = field(metadata=config(field_name="id"))
    hash: Hash = field(metadata=config(field_name="hash"))


@dataclass
class OutboxInfo(DataClassJsonMixin):
    prev: MessageID = field(metadata=config(field_name="prev"))
    compose_time: gregor1.Time = field(metadata=config(field_name="composeTime"))


@dataclass
class EphemeralPurgeInfo(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="c"))
    is_active: bool = field(metadata=config(field_name="a"))
    next_purge_time: gregor1.Time = field(metadata=config(field_name="n"))
    min_unexploded_id: MessageID = field(metadata=config(field_name="e"))


@dataclass
class RetentionPolicy__RETAIN(DataClassJsonMixin):
    typ: Literal[RetentionPolicyTypeStrings.RETAIN]
    RETAIN: Optional[RpRetain]


@dataclass
class RetentionPolicy__EXPIRE(DataClassJsonMixin):
    typ: Literal[RetentionPolicyTypeStrings.EXPIRE]
    EXPIRE: Optional[RpExpire]


@dataclass
class RetentionPolicy__INHERIT(DataClassJsonMixin):
    typ: Literal[RetentionPolicyTypeStrings.INHERIT]
    INHERIT: Optional[RpInherit]


@dataclass
class RetentionPolicy__EPHEMERAL(DataClassJsonMixin):
    typ: Literal[RetentionPolicyTypeStrings.EPHEMERAL]
    EPHEMERAL: Optional[RpEphemeral]


RetentionPolicy = Union[
    RetentionPolicy__RETAIN,
    RetentionPolicy__EXPIRE,
    RetentionPolicy__INHERIT,
    RetentionPolicy__EPHEMERAL,
]


@dataclass
class SearchOpts(DataClassJsonMixin):
    is_regex: bool = field(metadata=config(field_name="isRegex"))
    sent_by: str = field(metadata=config(field_name="sentBy"))
    sent_to: str = field(metadata=config(field_name="sentTo"))
    match_mentions: bool = field(metadata=config(field_name="matchMentions"))
    sent_before: gregor1.Time = field(metadata=config(field_name="sentBefore"))
    sent_after: gregor1.Time = field(metadata=config(field_name="sentAfter"))
    max_hits: int = field(metadata=config(field_name="maxHits"))
    max_messages: int = field(metadata=config(field_name="maxMessages"))
    before_context: int = field(metadata=config(field_name="beforeContext"))
    after_context: int = field(metadata=config(field_name="afterContext"))
    reindex_mode: ReIndexingMode = field(metadata=config(field_name="reindexMode"))
    max_convs_searched: int = field(metadata=config(field_name="maxConvsSearched"))
    max_convs_hit: int = field(metadata=config(field_name="maxConvsHit"))
    max_name_convs: int = field(metadata=config(field_name="maxNameConvs"))
    initial_pagination: Optional[Pagination] = field(
        default=None, metadata=config(field_name="initialPagination")
    )
    conv_id: Optional[ConversationID] = field(
        default=None, metadata=config(field_name="convID")
    )


@dataclass
class AssetMetadata__IMAGE(DataClassJsonMixin):
    assetType: Literal[AssetMetadataTypeStrings.IMAGE]
    IMAGE: Optional[AssetMetadataImage]


@dataclass
class AssetMetadata__VIDEO(DataClassJsonMixin):
    assetType: Literal[AssetMetadataTypeStrings.VIDEO]
    VIDEO: Optional[AssetMetadataVideo]


@dataclass
class AssetMetadata__AUDIO(DataClassJsonMixin):
    assetType: Literal[AssetMetadataTypeStrings.AUDIO]
    AUDIO: Optional[AssetMetadataAudio]


AssetMetadata = Union[AssetMetadata__IMAGE, AssetMetadata__VIDEO, AssetMetadata__AUDIO]


@dataclass
class UnreadUpdate(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    unread_messages: int = field(metadata=config(field_name="unreadMessages"))
    unread_notifying_messages: Dict[str, int] = field(
        metadata=config(field_name="unreadNotifyingMessages")
    )
    compat_unread_messages: int = field(metadata=config(field_name="UnreadMessages"))
    diff: bool = field(metadata=config(field_name="diff"))


@dataclass
class TLFFinalizeUpdate(DataClassJsonMixin):
    finalize_info: ConversationFinalizeInfo = field(
        metadata=config(field_name="finalizeInfo")
    )
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    conv_i_ds: Optional[Optional[List[ConversationID]]] = field(
        default=None, metadata=config(field_name="convIDs")
    )


@dataclass
class TLFResolveUpdate(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))


@dataclass
class RemoteUserTypingUpdate(DataClassJsonMixin):
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    device_id: gregor1.DeviceID = field(metadata=config(field_name="deviceID"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    typing: bool = field(metadata=config(field_name="typing"))


@dataclass
class ConversationUpdate(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    existence: ConversationExistence = field(metadata=config(field_name="existence"))


@dataclass
class TeamChannelUpdate(DataClassJsonMixin):
    team_id: TLFID = field(metadata=config(field_name="teamID"))


@dataclass
class KBFSImpteamUpgradeUpdate(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))


@dataclass
class SubteamRenameUpdate(DataClassJsonMixin):
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    conv_i_ds: Optional[Optional[List[ConversationID]]] = field(
        default=None, metadata=config(field_name="convIDs")
    )


@dataclass
class TextPayment(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    payment_text: str = field(metadata=config(field_name="paymentText"))
    result: TextPaymentResult = field(metadata=config(field_name="result"))


@dataclass
class MessageEdit(DataClassJsonMixin):
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    body: str = field(metadata=config(field_name="body"))
    user_mentions: Optional[Optional[List[KnownUserMention]]] = field(
        default=None, metadata=config(field_name="userMentions")
    )
    team_mentions: Optional[Optional[List[KnownTeamMention]]] = field(
        default=None, metadata=config(field_name="teamMentions")
    )


@dataclass
class MessageDelete(DataClassJsonMixin):
    message_i_ds: Optional[Optional[List[MessageID]]] = field(
        default=None, metadata=config(field_name="messageIDs")
    )


@dataclass
class MessageFlip(DataClassJsonMixin):
    text: str = field(metadata=config(field_name="text"))
    game_id: FlipGameID = field(metadata=config(field_name="gameID"))
    flip_conv_id: ConversationID = field(metadata=config(field_name="flipConvID"))
    user_mentions: Optional[Optional[List[KnownUserMention]]] = field(
        default=None, metadata=config(field_name="userMentions")
    )
    team_mentions: Optional[Optional[List[KnownTeamMention]]] = field(
        default=None, metadata=config(field_name="teamMentions")
    )


@dataclass
class MessagePin(DataClassJsonMixin):
    msg_id: MessageID = field(metadata=config(field_name="msgID"))


@dataclass
class MessageDeleteHistory(DataClassJsonMixin):
    upto: MessageID = field(metadata=config(field_name="upto"))


@dataclass
class MessageReaction(DataClassJsonMixin):
    message_id: MessageID = field(metadata=config(field_name="m"))
    body: str = field(metadata=config(field_name="b"))


@dataclass
class SenderPrepareOptions(DataClassJsonMixin):
    skip_topic_name_state: bool = field(
        metadata=config(field_name="skipTopicNameState")
    )
    reply_to: Optional[MessageID] = field(
        default=None, metadata=config(field_name="replyTo")
    )


@dataclass
class SenderSendOptions(DataClassJsonMixin):
    join_mentions_as: Optional[ConversationMemberStatus] = field(
        default=None, metadata=config(field_name="joinMentionsAs")
    )


@dataclass
class OutboxStateError(DataClassJsonMixin):
    message: str = field(metadata=config(field_name="message"))
    typ: OutboxErrorType = field(metadata=config(field_name="typ"))


@dataclass
class HeaderPlaintextUnsupported(DataClassJsonMixin):
    mi: HeaderPlaintextMetaInfo = field(metadata=config(field_name="mi"))


@dataclass
class BodyPlaintextUnsupported(DataClassJsonMixin):
    mi: BodyPlaintextMetaInfo = field(metadata=config(field_name="mi"))


@dataclass
class MessageUnboxedError(DataClassJsonMixin):
    err_type: MessageUnboxedErrorType = field(metadata=config(field_name="errType"))
    err_msg: str = field(metadata=config(field_name="errMsg"))
    internal_err_msg: str = field(metadata=config(field_name="internalErrMsg"))
    version_kind: VersionKind = field(metadata=config(field_name="versionKind"))
    version_number: int = field(metadata=config(field_name="versionNumber"))
    is_critical: bool = field(metadata=config(field_name="isCritical"))
    sender_username: str = field(metadata=config(field_name="senderUsername"))
    sender_device_name: str = field(metadata=config(field_name="senderDeviceName"))
    sender_device_type: str = field(metadata=config(field_name="senderDeviceType"))
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    message_type: MessageType = field(metadata=config(field_name="messageType"))
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))
    is_ephemeral: bool = field(metadata=config(field_name="isEphemeral"))
    is_ephemeral_expired: bool = field(metadata=config(field_name="isEphemeralExpired"))
    etime: gregor1.Time = field(metadata=config(field_name="etime"))


@dataclass
class MessageUnboxedPlaceholder(DataClassJsonMixin):
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    hidden: bool = field(metadata=config(field_name="hidden"))


@dataclass
class ConversationSettingsLocal(DataClassJsonMixin):
    min_writer_role_info: Optional[ConversationMinWriterRoleInfoLocal] = field(
        default=None, metadata=config(field_name="minWriterRoleInfo")
    )


@dataclass
class NonblockFetchRes(DataClassJsonMixin):
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identifyFailures")
    )


@dataclass
class MessageIDControl(DataClassJsonMixin):
    mode: MessageIDControlMode = field(metadata=config(field_name="mode"))
    num: int = field(metadata=config(field_name="num"))
    pivot: Optional[MessageID] = field(
        default=None, metadata=config(field_name="pivot")
    )


@dataclass
class UnreadlineRes(DataClassJsonMixin):
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identifyFailures")
    )
    unreadline_id: Optional[MessageID] = field(
        default=None, metadata=config(field_name="unreadlineID")
    )


@dataclass
class NameQuery(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    members_type: ConversationMembersType = field(
        metadata=config(field_name="membersType")
    )
    tlf_id: Optional[TLFID] = field(default=None, metadata=config(field_name="tlfID"))


@dataclass
class PostLocalRes(DataClassJsonMixin):
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identifyFailures")
    )


@dataclass
class PostLocalNonblockRes(DataClassJsonMixin):
    outbox_id: OutboxID = field(metadata=config(field_name="outboxID"))
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identifyFailures")
    )


@dataclass
class EditTarget(DataClassJsonMixin):
    message_id: Optional[MessageID] = field(
        default=None, metadata=config(field_name="messageID")
    )
    outbox_id: Optional[OutboxID] = field(
        default=None, metadata=config(field_name="outboxID")
    )


@dataclass
class SetConversationStatusLocalRes(DataClassJsonMixin):
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identifyFailures")
    )


@dataclass
class GetInboxSummaryForCLILocalQuery(DataClassJsonMixin):
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    after: str = field(metadata=config(field_name="after"))
    before: str = field(metadata=config(field_name="before"))
    visibility: keybase1.TLFVisibility = field(metadata=config(field_name="visibility"))
    unread_first: bool = field(metadata=config(field_name="unreadFirst"))
    unread_first_limit: UnreadFirstNumLimit = field(
        metadata=config(field_name="unreadFirstLimit")
    )
    activity_sorted_limit: int = field(
        metadata=config(field_name="activitySortedLimit")
    )
    status: Optional[Optional[List[ConversationStatus]]] = field(
        default=None, metadata=config(field_name="status")
    )
    conv_i_ds: Optional[Optional[List[ConversationID]]] = field(
        default=None, metadata=config(field_name="convIDs")
    )


@dataclass
class DownloadAttachmentLocalRes(DataClassJsonMixin):
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identifyFailures")
    )


@dataclass
class DownloadFileAttachmentLocalRes(DataClassJsonMixin):
    file_path: str = field(metadata=config(field_name="filePath"))
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identifyFailures")
    )


@dataclass
class MarkAsReadLocalRes(DataClassJsonMixin):
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )


@dataclass
class JoinLeaveConversationLocalRes(DataClassJsonMixin):
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )


@dataclass
class DeleteConversationLocalRes(DataClassJsonMixin):
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )


@dataclass
class SetAppNotificationSettingsLocalRes(DataClassJsonMixin):
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )


@dataclass
class AppNotificationSettingLocal(DataClassJsonMixin):
    device_type: keybase1.DeviceType = field(metadata=config(field_name="deviceType"))
    kind: NotificationKind = field(metadata=config(field_name="kind"))
    enabled: bool = field(metadata=config(field_name="enabled"))


@dataclass
class ResetConvMember(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    conv: ConversationID = field(metadata=config(field_name="conv"))


@dataclass
class ProfileSearchConvStats(DataClassJsonMixin):
    err: str = field(metadata=config(field_name="err"))
    conv_name: str = field(metadata=config(field_name="convName"))
    min_conv_id: MessageID = field(metadata=config(field_name="minConvID"))
    max_conv_id: MessageID = field(metadata=config(field_name="maxConvID"))
    num_missing: int = field(metadata=config(field_name="numMissing"))
    num_messages: int = field(metadata=config(field_name="numMessages"))
    index_size_disk: int = field(metadata=config(field_name="indexSizeDisk"))
    index_size_mem: int = field(metadata=config(field_name="indexSizeMem"))
    duration_msec: gregor1.DurationMsec = field(
        metadata=config(field_name="durationMsec")
    )
    percent_indexed: int = field(metadata=config(field_name="percentIndexed"))


@dataclass
class BuiltinCommandGroup(DataClassJsonMixin):
    typ: ConversationBuiltinCommandTyp = field(metadata=config(field_name="typ"))
    commands: Optional[Optional[List[ConversationCommand]]] = field(
        default=None, metadata=config(field_name="commands")
    )


@dataclass
class UserBotCommandOutput(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    description: str = field(metadata=config(field_name="description"))
    usage: str = field(metadata=config(field_name="usage"))
    username: str = field(metadata=config(field_name="username"))
    extended_description: Optional[UserBotExtendedDescription] = field(
        default=None, metadata=config(field_name="extended_description")
    )


@dataclass
class UserBotCommandInput(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    description: str = field(metadata=config(field_name="description"))
    usage: str = field(metadata=config(field_name="usage"))
    extended_description: Optional[UserBotExtendedDescription] = field(
        default=None, metadata=config(field_name="extended_description")
    )


@dataclass
class AdvertiseBotCommandsLocalRes(DataClassJsonMixin):
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )


@dataclass
class ClearBotCommandsLocalRes(DataClassJsonMixin):
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )


@dataclass
class PinMessageRes(DataClassJsonMixin):
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )


@dataclass
class SetAppNotificationSettingsInfo(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    settings: ConversationNotificationInfo = field(
        metadata=config(field_name="settings")
    )


@dataclass
class MemberInfo(DataClassJsonMixin):
    member: str = field(metadata=config(field_name="member"))
    status: ConversationMemberStatus = field(metadata=config(field_name="status"))


@dataclass
class ConvTypingUpdate(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    typers: Optional[Optional[List[TyperInfo]]] = field(
        default=None, metadata=config(field_name="typers")
    )


@dataclass
class ConversationStaleUpdate(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    update_type: StaleUpdateType = field(metadata=config(field_name="updateType"))


@dataclass
class NewConversationRemoteRes(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    created_complex_team: bool = field(metadata=config(field_name="createdComplexTeam"))
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class MarkAsReadRes(DataClassJsonMixin):
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class SetConversationStatusRes(DataClassJsonMixin):
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class GetUnreadlineRemoteRes(DataClassJsonMixin):
    unreadline_id: Optional[MessageID] = field(
        default=None, metadata=config(field_name="unreadlineID")
    )
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class JoinLeaveConversationRemoteRes(DataClassJsonMixin):
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class DeleteConversationRemoteRes(DataClassJsonMixin):
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class GetMessageBeforeRes(DataClassJsonMixin):
    msg_id: MessageID = field(metadata=config(field_name="msgID"))
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class SetAppNotificationSettingsRes(DataClassJsonMixin):
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class SetRetentionRes(DataClassJsonMixin):
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class SetConvMinWriterRoleRes(DataClassJsonMixin):
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class ServerNowRes(DataClassJsonMixin):
    now: gregor1.Time = field(metadata=config(field_name="now"))
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class RemoteBotCommandsAdvertisementPublic(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))


@dataclass
class RemoteBotCommandsAdvertisementTLFID(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    tlf_id: TLFID = field(metadata=config(field_name="tlfID"))


@dataclass
class BotCommandConv(DataClassJsonMixin):
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    vers: CommandConvVers = field(metadata=config(field_name="vers"))
    mtime: gregor1.Time = field(metadata=config(field_name="mtime"))


@dataclass
class AdvertiseBotCommandsRes(DataClassJsonMixin):
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class ClearBotCommandsRes(DataClassJsonMixin):
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class UnfurlGenericRaw(DataClassJsonMixin):
    title: str = field(metadata=config(field_name="title"))
    url: str = field(metadata=config(field_name="url"))
    site_name: str = field(metadata=config(field_name="siteName"))
    favicon_url: Optional[str] = field(
        default=None, metadata=config(field_name="faviconUrl")
    )
    image_url: Optional[str] = field(
        default=None, metadata=config(field_name="imageUrl")
    )
    video: Optional[UnfurlVideo] = field(
        default=None, metadata=config(field_name="video")
    )
    publish_time: Optional[int] = field(
        default=None, metadata=config(field_name="publishTime")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )


@dataclass
class UnfurlGiphyRaw(DataClassJsonMixin):
    image_url: Optional[str] = field(
        default=None, metadata=config(field_name="imageUrl")
    )
    video: Optional[UnfurlVideo] = field(
        default=None, metadata=config(field_name="video")
    )
    favicon_url: Optional[str] = field(
        default=None, metadata=config(field_name="faviconUrl")
    )


@dataclass
class UnfurlMapsRaw(DataClassJsonMixin):
    title: str = field(metadata=config(field_name="title"))
    url: str = field(metadata=config(field_name="url"))
    site_name: str = field(metadata=config(field_name="siteName"))
    image_url: str = field(metadata=config(field_name="imageUrl"))
    description: str = field(metadata=config(field_name="description"))
    coord: Coordinate = field(metadata=config(field_name="coord"))
    time: gregor1.Time = field(metadata=config(field_name="time"))
    live_location_done: bool = field(metadata=config(field_name="liveLocationDone"))
    history_image_url: Optional[str] = field(
        default=None, metadata=config(field_name="historyImageUrl")
    )
    live_location_end_time: Optional[gregor1.Time] = field(
        default=None, metadata=config(field_name="liveLocationEndTime")
    )


@dataclass
class UnfurlGenericMapInfo(DataClassJsonMixin):
    coord: Coordinate = field(metadata=config(field_name="coord"))
    time: gregor1.Time = field(metadata=config(field_name="time"))
    is_live_location_done: bool = field(
        metadata=config(field_name="isLiveLocationDone")
    )
    live_location_end_time: Optional[gregor1.Time] = field(
        default=None, metadata=config(field_name="liveLocationEndTime")
    )


@dataclass
class UnfurlGiphyDisplay(DataClassJsonMixin):
    favicon: Optional[UnfurlImageDisplay] = field(
        default=None, metadata=config(field_name="favicon")
    )
    image: Optional[UnfurlImageDisplay] = field(
        default=None, metadata=config(field_name="image")
    )
    video: Optional[UnfurlImageDisplay] = field(
        default=None, metadata=config(field_name="video")
    )


@dataclass
class UnfurlSettings(DataClassJsonMixin):
    mode: UnfurlMode = field(metadata=config(field_name="mode"))
    whitelist: Dict[str, bool] = field(metadata=config(field_name="whitelist"))


@dataclass
class UnfurlSettingsDisplay(DataClassJsonMixin):
    mode: UnfurlMode = field(metadata=config(field_name="mode"))
    whitelist: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="whitelist")
    )


@dataclass
class ChatList(DataClassJsonMixin):
    offline: bool = field(metadata=config(field_name="offline"))
    conversations: Optional[Optional[List[ConvSummary]]] = field(
        default=None, metadata=config(field_name="conversations")
    )
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identify_failures")
    )
    pagination: Optional[Pagination] = field(
        default=None, metadata=config(field_name="pagination")
    )
    rate_limits: Optional[Optional[List[RateLimitRes]]] = field(
        default=None, metadata=config(field_name="ratelimits")
    )


@dataclass
class ListCommandsRes(DataClassJsonMixin):
    commands: Optional[Optional[List[UserBotCommandOutput]]] = field(
        default=None, metadata=config(field_name="commands")
    )
    rate_limits: Optional[Optional[List[RateLimitRes]]] = field(
        default=None, metadata=config(field_name="ratelimits")
    )


@dataclass
class AdvertiseCommandAPIParam(DataClassJsonMixin):
    typ: str = field(metadata=config(field_name="type"))
    commands: Optional[Optional[List[UserBotCommandInput]]] = field(
        default=None, metadata=config(field_name="commands")
    )
    team_name: Optional[str] = field(
        default=None, metadata=config(field_name="team_name")
    )


@dataclass
class UIInboxLayout(DataClassJsonMixin):
    small_teams: Optional[Optional[List[UIInboxSmallTeamRow]]] = field(
        default=None, metadata=config(field_name="smallTeams")
    )
    big_teams: Optional[Optional[List[UIInboxBigTeamRow]]] = field(
        default=None, metadata=config(field_name="bigTeams")
    )


@dataclass
class UITextDecoration__PAYMENT(DataClassJsonMixin):
    typ: Literal[UITextDecorationTypStrings.PAYMENT]
    PAYMENT: Optional[TextPayment]


@dataclass
class UITextDecoration__ATMENTION(DataClassJsonMixin):
    typ: Literal[UITextDecorationTypStrings.ATMENTION]
    ATMENTION: Optional[str]


@dataclass
class UITextDecoration__CHANNELNAMEMENTION(DataClassJsonMixin):
    typ: Literal[UITextDecorationTypStrings.CHANNELNAMEMENTION]
    CHANNELNAMEMENTION: Optional[UIChannelNameMention]


@dataclass
class UITextDecoration__MAYBEMENTION(DataClassJsonMixin):
    typ: Literal[UITextDecorationTypStrings.MAYBEMENTION]
    MAYBEMENTION: Optional[MaybeMention]


@dataclass
class UITextDecoration__LINK(DataClassJsonMixin):
    typ: Literal[UITextDecorationTypStrings.LINK]
    LINK: Optional[UILinkDecoration]


@dataclass
class UITextDecoration__MAILTO(DataClassJsonMixin):
    typ: Literal[UITextDecorationTypStrings.MAILTO]
    MAILTO: Optional[UILinkDecoration]


@dataclass
class UITextDecoration__KBFSPATH(DataClassJsonMixin):
    typ: Literal[UITextDecorationTypStrings.KBFSPATH]
    KBFSPATH: Optional[KBFSPath]


UITextDecoration = Union[
    UITextDecoration__PAYMENT,
    UITextDecoration__ATMENTION,
    UITextDecoration__CHANNELNAMEMENTION,
    UITextDecoration__MAYBEMENTION,
    UITextDecoration__LINK,
    UITextDecoration__MAILTO,
    UITextDecoration__KBFSPATH,
]


@dataclass
class UIChatSearchConvHits(DataClassJsonMixin):
    unread_matches: bool = field(metadata=config(field_name="unreadMatches"))
    hits: Optional[Optional[List[UIChatSearchConvHit]]] = field(
        default=None, metadata=config(field_name="hits")
    )


@dataclass
class UICoinFlipError__GENERIC(DataClassJsonMixin):
    typ: Literal[UICoinFlipErrorTypStrings.GENERIC]
    GENERIC: Optional[str]


@dataclass
class UICoinFlipError__ABSENTEE(DataClassJsonMixin):
    typ: Literal[UICoinFlipErrorTypStrings.ABSENTEE]
    ABSENTEE: Optional[UICoinFlipAbsenteeError]


@dataclass
class UICoinFlipError__TIMEOUT(DataClassJsonMixin):
    typ: Literal[UICoinFlipErrorTypStrings.TIMEOUT]
    TIMEOUT: None


@dataclass
class UICoinFlipError__ABORTED(DataClassJsonMixin):
    typ: Literal[UICoinFlipErrorTypStrings.ABORTED]
    ABORTED: None


@dataclass
class UICoinFlipError__DUPREG(DataClassJsonMixin):
    typ: Literal[UICoinFlipErrorTypStrings.DUPREG]
    DUPREG: Optional[UICoinFlipErrorParticipant]


@dataclass
class UICoinFlipError__DUPCOMMITCOMPLETE(DataClassJsonMixin):
    typ: Literal[UICoinFlipErrorTypStrings.DUPCOMMITCOMPLETE]
    DUPCOMMITCOMPLETE: Optional[UICoinFlipErrorParticipant]


@dataclass
class UICoinFlipError__DUPREVEAL(DataClassJsonMixin):
    typ: Literal[UICoinFlipErrorTypStrings.DUPREVEAL]
    DUPREVEAL: Optional[UICoinFlipErrorParticipant]


@dataclass
class UICoinFlipError__COMMITMISMATCH(DataClassJsonMixin):
    typ: Literal[UICoinFlipErrorTypStrings.COMMITMISMATCH]
    COMMITMISMATCH: Optional[UICoinFlipErrorParticipant]


UICoinFlipError = Union[
    UICoinFlipError__GENERIC,
    UICoinFlipError__ABSENTEE,
    UICoinFlipError__TIMEOUT,
    UICoinFlipError__ABORTED,
    UICoinFlipError__DUPREG,
    UICoinFlipError__DUPCOMMITCOMPLETE,
    UICoinFlipError__DUPREVEAL,
    UICoinFlipError__COMMITMISMATCH,
]


@dataclass
class ConversationCommandGroups__BUILTIN(DataClassJsonMixin):
    typ: Literal[ConversationCommandGroupsTypStrings.BUILTIN]
    BUILTIN: Optional[ConversationBuiltinCommandTyp]


@dataclass
class ConversationCommandGroups__CUSTOM(DataClassJsonMixin):
    typ: Literal[ConversationCommandGroupsTypStrings.CUSTOM]
    CUSTOM: Optional[ConversationCommandGroupsCustom]


@dataclass
class ConversationCommandGroups__NONE(DataClassJsonMixin):
    typ: Literal[ConversationCommandGroupsTypStrings.NONE]
    NONE: None


ConversationCommandGroups = Union[
    ConversationCommandGroups__BUILTIN,
    ConversationCommandGroups__CUSTOM,
    ConversationCommandGroups__NONE,
]


@dataclass
class ConversationIDMessageIDPairs(DataClassJsonMixin):
    pairs: Optional[Optional[List[ConversationIDMessageIDPair]]] = field(
        default=None, metadata=config(field_name="pairs")
    )


@dataclass
class ReactionMap(DataClassJsonMixin):
    reactions: Dict[str, Dict[str, Reaction]] = field(
        metadata=config(field_name="reactions")
    )


@dataclass
class MessageClientHeader(DataClassJsonMixin):
    conv: ConversationIDTriple = field(metadata=config(field_name="conv"))
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    tlf_public: bool = field(metadata=config(field_name="tlfPublic"))
    message_type: MessageType = field(metadata=config(field_name="messageType"))
    supersedes: MessageID = field(metadata=config(field_name="supersedes"))
    sender: gregor1.UID = field(metadata=config(field_name="sender"))
    sender_device: gregor1.DeviceID = field(metadata=config(field_name="senderDevice"))
    pairwise_macs: Dict[str, str] = field(metadata=config(field_name="pm"))
    kbfs_crypt_keys_used: Optional[bool] = field(
        default=None, metadata=config(field_name="kbfsCryptKeysUsed")
    )
    deletes: Optional[Optional[List[MessageID]]] = field(
        default=None, metadata=config(field_name="deletes")
    )
    prev: Optional[Optional[List[MessagePreviousPointer]]] = field(
        default=None, metadata=config(field_name="prev")
    )
    delete_history: Optional[MessageDeleteHistory] = field(
        default=None, metadata=config(field_name="deleteHistory")
    )
    merkle_root: Optional[MerkleRoot] = field(
        default=None, metadata=config(field_name="merkleRoot")
    )
    outbox_id: Optional[OutboxID] = field(
        default=None, metadata=config(field_name="outboxID")
    )
    outbox_info: Optional[OutboxInfo] = field(
        default=None, metadata=config(field_name="outboxInfo")
    )
    ephemeral_metadata: Optional[MsgEphemeralMetadata] = field(
        default=None, metadata=config(field_name="em")
    )
    bot_uid: Optional[gregor1.UID] = field(
        default=None, metadata=config(field_name="b")
    )


@dataclass
class MessageClientHeaderVerified(DataClassJsonMixin):
    conv: ConversationIDTriple = field(metadata=config(field_name="conv"))
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    tlf_public: bool = field(metadata=config(field_name="tlfPublic"))
    message_type: MessageType = field(metadata=config(field_name="messageType"))
    sender: gregor1.UID = field(metadata=config(field_name="sender"))
    sender_device: gregor1.DeviceID = field(metadata=config(field_name="senderDevice"))
    rtime: gregor1.Time = field(metadata=config(field_name="rt"))
    has_pairwise_macs: bool = field(metadata=config(field_name="pm"))
    prev: Optional[Optional[List[MessagePreviousPointer]]] = field(
        default=None, metadata=config(field_name="prev")
    )
    kbfs_crypt_keys_used: Optional[bool] = field(
        default=None, metadata=config(field_name="kbfsCryptKeysUsed")
    )
    merkle_root: Optional[MerkleRoot] = field(
        default=None, metadata=config(field_name="merkleRoot")
    )
    outbox_id: Optional[OutboxID] = field(
        default=None, metadata=config(field_name="outboxID")
    )
    outbox_info: Optional[OutboxInfo] = field(
        default=None, metadata=config(field_name="outboxInfo")
    )
    ephemeral_metadata: Optional[MsgEphemeralMetadata] = field(
        default=None, metadata=config(field_name="em")
    )
    bot_uid: Optional[gregor1.UID] = field(
        default=None, metadata=config(field_name="b")
    )


@dataclass
class Asset(DataClassJsonMixin):
    filename: str = field(metadata=config(field_name="filename"))
    region: str = field(metadata=config(field_name="region"))
    endpoint: str = field(metadata=config(field_name="endpoint"))
    bucket: str = field(metadata=config(field_name="bucket"))
    path: str = field(metadata=config(field_name="path"))
    size: int = field(metadata=config(field_name="size"))
    mime_type: str = field(metadata=config(field_name="mimeType"))
    enc_hash: Hash = field(metadata=config(field_name="encHash"))
    key: str = field(metadata=config(field_name="key"))
    verify_key: str = field(metadata=config(field_name="verifyKey"))
    title: str = field(metadata=config(field_name="title"))
    nonce: str = field(metadata=config(field_name="nonce"))
    metadata: AssetMetadata = field(metadata=config(field_name="metadata"))
    tag: AssetTag = field(metadata=config(field_name="tag"))


@dataclass
class GenericPayload(DataClassJsonMixin):
    action: str = field(metadata=config(field_name="Action"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        default=None, metadata=config(field_name="unreadUpdate")
    )


@dataclass
class NewConversationPayload(DataClassJsonMixin):
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        default=None, metadata=config(field_name="unreadUpdate")
    )


@dataclass
class ReadMessagePayload(DataClassJsonMixin):
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    msg_id: MessageID = field(metadata=config(field_name="msgID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        default=None, metadata=config(field_name="unreadUpdate")
    )


@dataclass
class SetStatusPayload(DataClassJsonMixin):
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    status: ConversationStatus = field(metadata=config(field_name="status"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        default=None, metadata=config(field_name="unreadUpdate")
    )


@dataclass
class TeamTypePayload(DataClassJsonMixin):
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    team_type: TeamType = field(metadata=config(field_name="teamType"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        default=None, metadata=config(field_name="unreadUpdate")
    )


@dataclass
class SetAppNotificationSettingsPayload(DataClassJsonMixin):
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    settings: ConversationNotificationInfo = field(
        metadata=config(field_name="settings")
    )
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        default=None, metadata=config(field_name="unreadUpdate")
    )


@dataclass
class ExpungePayload(DataClassJsonMixin):
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    expunge: Expunge = field(metadata=config(field_name="expunge"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    max_msgs: Optional[Optional[List[MessageSummary]]] = field(
        default=None, metadata=config(field_name="maxMsgs")
    )
    unread_update: Optional[UnreadUpdate] = field(
        default=None, metadata=config(field_name="unreadUpdate")
    )


@dataclass
class UpdateConversationMembership(DataClassJsonMixin):
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    joined: Optional[Optional[List[ConversationMember]]] = field(
        default=None, metadata=config(field_name="joined")
    )
    removed: Optional[Optional[List[ConversationMember]]] = field(
        default=None, metadata=config(field_name="removed")
    )
    reset: Optional[Optional[List[ConversationMember]]] = field(
        default=None, metadata=config(field_name="reset")
    )
    previewed: Optional[Optional[List[ConversationID]]] = field(
        default=None, metadata=config(field_name="previewed")
    )
    unread_update: Optional[UnreadUpdate] = field(
        default=None, metadata=config(field_name="unreadUpdate")
    )
    unread_updates: Optional[Optional[List[UnreadUpdate]]] = field(
        default=None, metadata=config(field_name="unreadUpdates")
    )


@dataclass
class UpdateConversations(DataClassJsonMixin):
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    conv_updates: Optional[Optional[List[ConversationUpdate]]] = field(
        default=None, metadata=config(field_name="convUpdates")
    )


@dataclass
class SetConvRetentionUpdate(DataClassJsonMixin):
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    policy: RetentionPolicy = field(metadata=config(field_name="policy"))


@dataclass
class SetTeamRetentionUpdate(DataClassJsonMixin):
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    team_id: keybase1.TeamID = field(metadata=config(field_name="teamID"))
    policy: RetentionPolicy = field(metadata=config(field_name="policy"))


@dataclass
class SetConvSettingsUpdate(DataClassJsonMixin):
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    conv_settings: Optional[ConversationSettings] = field(
        default=None, metadata=config(field_name="convSettings")
    )


@dataclass
class MessageText(DataClassJsonMixin):
    body: str = field(metadata=config(field_name="body"))
    payments: Optional[Optional[List[TextPayment]]] = field(
        default=None, metadata=config(field_name="payments")
    )
    reply_to: Optional[MessageID] = field(
        default=None, metadata=config(field_name="replyTo")
    )
    reply_to_uid: Optional[gregor1.UID] = field(
        default=None, metadata=config(field_name="replyToUID")
    )
    user_mentions: Optional[Optional[List[KnownUserMention]]] = field(
        default=None, metadata=config(field_name="userMentions")
    )
    team_mentions: Optional[Optional[List[KnownTeamMention]]] = field(
        default=None, metadata=config(field_name="teamMentions")
    )
    live_location: Optional[LiveLocation] = field(
        default=None, metadata=config(field_name="liveLocation")
    )


@dataclass
class MessageSystemChangeRetention(DataClassJsonMixin):
    is_team: bool = field(metadata=config(field_name="isTeam"))
    is_inherit: bool = field(metadata=config(field_name="isInherit"))
    members_type: ConversationMembersType = field(
        metadata=config(field_name="membersType")
    )
    policy: RetentionPolicy = field(metadata=config(field_name="policy"))
    user: str = field(metadata=config(field_name="user"))


@dataclass
class OutboxState__SENDING(DataClassJsonMixin):
    state: Literal[OutboxStateTypeStrings.SENDING]
    SENDING: Optional[int]


@dataclass
class OutboxState__ERROR(DataClassJsonMixin):
    state: Literal[OutboxStateTypeStrings.ERROR]
    ERROR: Optional[OutboxStateError]


OutboxState = Union[OutboxState__SENDING, OutboxState__ERROR]


@dataclass
class HeaderPlaintextV1(DataClassJsonMixin):
    conv: ConversationIDTriple = field(metadata=config(field_name="conv"))
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    tlf_public: bool = field(metadata=config(field_name="tlfPublic"))
    message_type: MessageType = field(metadata=config(field_name="messageType"))
    sender: gregor1.UID = field(metadata=config(field_name="sender"))
    sender_device: gregor1.DeviceID = field(metadata=config(field_name="senderDevice"))
    body_hash: Hash = field(metadata=config(field_name="bodyHash"))
    prev: Optional[Optional[List[MessagePreviousPointer]]] = field(
        default=None, metadata=config(field_name="prev")
    )
    kbfs_crypt_keys_used: Optional[bool] = field(
        default=None, metadata=config(field_name="kbfsCryptKeysUsed")
    )
    outbox_info: Optional[OutboxInfo] = field(
        default=None, metadata=config(field_name="outboxInfo")
    )
    outbox_id: Optional[OutboxID] = field(
        default=None, metadata=config(field_name="outboxID")
    )
    header_signature: Optional[SignatureInfo] = field(
        default=None, metadata=config(field_name="headerSignature")
    )
    merkle_root: Optional[MerkleRoot] = field(
        default=None, metadata=config(field_name="merkleRoot")
    )
    ephemeral_metadata: Optional[MsgEphemeralMetadata] = field(
        default=None, metadata=config(field_name="em")
    )
    bot_uid: Optional[gregor1.UID] = field(
        default=None, metadata=config(field_name="b")
    )


@dataclass
class GetThreadQuery(DataClassJsonMixin):
    mark_as_read: bool = field(metadata=config(field_name="markAsRead"))
    disable_resolve_supersedes: bool = field(
        metadata=config(field_name="disableResolveSupersedes")
    )
    enable_delete_placeholders: bool = field(
        metadata=config(field_name="enableDeletePlaceholders")
    )
    disable_post_process_thread: bool = field(
        metadata=config(field_name="disablePostProcessThread")
    )
    message_types: Optional[Optional[List[MessageType]]] = field(
        default=None, metadata=config(field_name="messageTypes")
    )
    before: Optional[gregor1.Time] = field(
        default=None, metadata=config(field_name="before")
    )
    after: Optional[gregor1.Time] = field(
        default=None, metadata=config(field_name="after")
    )
    message_id_control: Optional[MessageIDControl] = field(
        default=None, metadata=config(field_name="messageIDControl")
    )


@dataclass
class GetInboxLocalQuery(DataClassJsonMixin):
    unread_only: bool = field(metadata=config(field_name="unreadOnly"))
    read_only: bool = field(metadata=config(field_name="readOnly"))
    compute_active_list: bool = field(metadata=config(field_name="computeActiveList"))
    name: Optional[NameQuery] = field(default=None, metadata=config(field_name="name"))
    topic_name: Optional[str] = field(
        default=None, metadata=config(field_name="topicName")
    )
    conv_i_ds: Optional[Optional[List[ConversationID]]] = field(
        default=None, metadata=config(field_name="convIDs")
    )
    topic_type: Optional[TopicType] = field(
        default=None, metadata=config(field_name="topicType")
    )
    tlf_visibility: Optional[keybase1.TLFVisibility] = field(
        default=None, metadata=config(field_name="tlfVisibility")
    )
    before: Optional[gregor1.Time] = field(
        default=None, metadata=config(field_name="before")
    )
    after: Optional[gregor1.Time] = field(
        default=None, metadata=config(field_name="after")
    )
    one_chat_type_per_tlf: Optional[bool] = field(
        default=None, metadata=config(field_name="oneChatTypePerTLF")
    )
    status: Optional[Optional[List[ConversationStatus]]] = field(
        default=None, metadata=config(field_name="status")
    )
    member_status: Optional[Optional[List[ConversationMemberStatus]]] = field(
        default=None, metadata=config(field_name="memberStatus")
    )


@dataclass
class MakePreviewRes(DataClassJsonMixin):
    mime_type: str = field(metadata=config(field_name="mimeType"))
    preview_mime_type: Optional[str] = field(
        default=None, metadata=config(field_name="previewMimeType")
    )
    location: Optional[PreviewLocation] = field(
        default=None, metadata=config(field_name="location")
    )
    metadata: Optional[AssetMetadata] = field(
        default=None, metadata=config(field_name="metadata")
    )
    base_metadata: Optional[AssetMetadata] = field(
        default=None, metadata=config(field_name="baseMetadata")
    )


@dataclass
class GetAllResetConvMembersRes(DataClassJsonMixin):
    members: Optional[Optional[List[ResetConvMember]]] = field(
        default=None, metadata=config(field_name="members")
    )
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )


@dataclass
class StaticConfig(DataClassJsonMixin):
    deletable_by_delete_history: Optional[Optional[List[MessageType]]] = field(
        default=None, metadata=config(field_name="deletableByDeleteHistory")
    )
    builtin_commands: Optional[Optional[List[BuiltinCommandGroup]]] = field(
        default=None, metadata=config(field_name="builtinCommands")
    )


@dataclass
class AdvertiseCommandsParam(DataClassJsonMixin):
    typ: BotCommandsAdvertisementTyp = field(metadata=config(field_name="typ"))
    commands: Optional[Optional[List[UserBotCommandInput]]] = field(
        default=None, metadata=config(field_name="commands")
    )
    team_name: Optional[str] = field(
        default=None, metadata=config(field_name="teamName")
    )


@dataclass
class ListBotCommandsLocalRes(DataClassJsonMixin):
    commands: Optional[Optional[List[UserBotCommandOutput]]] = field(
        default=None, metadata=config(field_name="commands")
    )
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )


@dataclass
class MembersUpdateInfo(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    members: Optional[Optional[List[MemberInfo]]] = field(
        default=None, metadata=config(field_name="members")
    )


@dataclass
class ExpungeInfo(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    expunge: Expunge = field(metadata=config(field_name="expunge"))


@dataclass
class PostRemoteRes(DataClassJsonMixin):
    msg_header: MessageServerHeader = field(metadata=config(field_name="msgHeader"))
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class UnreadUpdateFull(DataClassJsonMixin):
    ignore: bool = field(metadata=config(field_name="ignore"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    inbox_sync_status: SyncInboxResType = field(
        metadata=config(field_name="inboxSyncStatus")
    )
    updates: Optional[Optional[List[UnreadUpdate]]] = field(
        default=None, metadata=config(field_name="updates")
    )


@dataclass
class SweepRes(DataClassJsonMixin):
    found_task: bool = field(metadata=config(field_name="foundTask"))
    deleted_messages: bool = field(metadata=config(field_name="deletedMessages"))
    expunge: Expunge = field(metadata=config(field_name="expunge"))


@dataclass
class RemoteBotCommandsAdvertisement__PUBLIC(DataClassJsonMixin):
    typ: Literal[BotCommandsAdvertisementTypStrings.PUBLIC]
    PUBLIC: Optional[RemoteBotCommandsAdvertisementPublic]


@dataclass
class RemoteBotCommandsAdvertisement__TLFID_MEMBERS(DataClassJsonMixin):
    typ: Literal[BotCommandsAdvertisementTypStrings.TLFID_MEMBERS]
    TLFID_MEMBERS: Optional[RemoteBotCommandsAdvertisementTLFID]


@dataclass
class RemoteBotCommandsAdvertisement__TLFID_CONVS(DataClassJsonMixin):
    typ: Literal[BotCommandsAdvertisementTypStrings.TLFID_CONVS]
    TLFID_CONVS: Optional[RemoteBotCommandsAdvertisementTLFID]


RemoteBotCommandsAdvertisement = Union[
    RemoteBotCommandsAdvertisement__PUBLIC,
    RemoteBotCommandsAdvertisement__TLFID_MEMBERS,
    RemoteBotCommandsAdvertisement__TLFID_CONVS,
]


@dataclass
class BotInfo(DataClassJsonMixin):
    command_convs: Optional[Optional[List[BotCommandConv]]] = field(
        default=None, metadata=config(field_name="commandConvs")
    )


@dataclass
class UnfurlRaw__GENERIC(DataClassJsonMixin):
    unfurlType: Literal[UnfurlTypeStrings.GENERIC]
    GENERIC: Optional[UnfurlGenericRaw]


@dataclass
class UnfurlRaw__YOUTUBE(DataClassJsonMixin):
    unfurlType: Literal[UnfurlTypeStrings.YOUTUBE]
    YOUTUBE: Optional[UnfurlYoutubeRaw]


@dataclass
class UnfurlRaw__GIPHY(DataClassJsonMixin):
    unfurlType: Literal[UnfurlTypeStrings.GIPHY]
    GIPHY: Optional[UnfurlGiphyRaw]


@dataclass
class UnfurlRaw__MAPS(DataClassJsonMixin):
    unfurlType: Literal[UnfurlTypeStrings.MAPS]
    MAPS: Optional[UnfurlMapsRaw]


UnfurlRaw = Union[
    UnfurlRaw__GENERIC, UnfurlRaw__YOUTUBE, UnfurlRaw__GIPHY, UnfurlRaw__MAPS
]


@dataclass
class UnfurlGenericDisplay(DataClassJsonMixin):
    title: str = field(metadata=config(field_name="title"))
    url: str = field(metadata=config(field_name="url"))
    site_name: str = field(metadata=config(field_name="siteName"))
    favicon: Optional[UnfurlImageDisplay] = field(
        default=None, metadata=config(field_name="favicon")
    )
    media: Optional[UnfurlImageDisplay] = field(
        default=None, metadata=config(field_name="media")
    )
    publish_time: Optional[int] = field(
        default=None, metadata=config(field_name="publishTime")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    map_info: Optional[UnfurlGenericMapInfo] = field(
        default=None, metadata=config(field_name="mapInfo")
    )


@dataclass
class UICoinFlipStatus(DataClassJsonMixin):
    game_id: str = field(metadata=config(field_name="gameID"))
    phase: UICoinFlipPhase = field(metadata=config(field_name="phase"))
    progress_text: str = field(metadata=config(field_name="progressText"))
    result_text: str = field(metadata=config(field_name="resultText"))
    commitment_visualization: str = field(
        metadata=config(field_name="commitmentVisualization")
    )
    reveal_visualization: str = field(metadata=config(field_name="revealVisualization"))
    participants: Optional[Optional[List[UICoinFlipParticipant]]] = field(
        default=None, metadata=config(field_name="participants")
    )
    error_info: Optional[UICoinFlipError] = field(
        default=None, metadata=config(field_name="errorInfo")
    )
    result_info: Optional[UICoinFlipResult] = field(
        default=None, metadata=config(field_name="resultInfo")
    )


@dataclass
class MessageSystem__ADDEDTOTEAM(DataClassJsonMixin):
    systemType: Literal[MessageSystemTypeStrings.ADDEDTOTEAM]
    ADDEDTOTEAM: Optional[MessageSystemAddedToTeam]


@dataclass
class MessageSystem__INVITEADDEDTOTEAM(DataClassJsonMixin):
    systemType: Literal[MessageSystemTypeStrings.INVITEADDEDTOTEAM]
    INVITEADDEDTOTEAM: Optional[MessageSystemInviteAddedToTeam]


@dataclass
class MessageSystem__COMPLEXTEAM(DataClassJsonMixin):
    systemType: Literal[MessageSystemTypeStrings.COMPLEXTEAM]
    COMPLEXTEAM: Optional[MessageSystemComplexTeam]


@dataclass
class MessageSystem__CREATETEAM(DataClassJsonMixin):
    systemType: Literal[MessageSystemTypeStrings.CREATETEAM]
    CREATETEAM: Optional[MessageSystemCreateTeam]


@dataclass
class MessageSystem__GITPUSH(DataClassJsonMixin):
    systemType: Literal[MessageSystemTypeStrings.GITPUSH]
    GITPUSH: Optional[MessageSystemGitPush]


@dataclass
class MessageSystem__CHANGEAVATAR(DataClassJsonMixin):
    systemType: Literal[MessageSystemTypeStrings.CHANGEAVATAR]
    CHANGEAVATAR: Optional[MessageSystemChangeAvatar]


@dataclass
class MessageSystem__CHANGERETENTION(DataClassJsonMixin):
    systemType: Literal[MessageSystemTypeStrings.CHANGERETENTION]
    CHANGERETENTION: Optional[MessageSystemChangeRetention]


@dataclass
class MessageSystem__BULKADDTOCONV(DataClassJsonMixin):
    systemType: Literal[MessageSystemTypeStrings.BULKADDTOCONV]
    BULKADDTOCONV: Optional[MessageSystemBulkAddToConv]


@dataclass
class MessageSystem__SBSRESOLVE(DataClassJsonMixin):
    systemType: Literal[MessageSystemTypeStrings.SBSRESOLVE]
    SBSRESOLVE: Optional[MessageSystemSbsResolve]


MessageSystem = Union[
    MessageSystem__ADDEDTOTEAM,
    MessageSystem__INVITEADDEDTOTEAM,
    MessageSystem__COMPLEXTEAM,
    MessageSystem__CREATETEAM,
    MessageSystem__GITPUSH,
    MessageSystem__CHANGEAVATAR,
    MessageSystem__CHANGERETENTION,
    MessageSystem__BULKADDTOCONV,
    MessageSystem__SBSRESOLVE,
]


@dataclass
class MessageAttachment(DataClassJsonMixin):
    object: Asset = field(metadata=config(field_name="object"))
    metadata: str = field(metadata=config(field_name="metadata"))
    uploaded: bool = field(metadata=config(field_name="uploaded"))
    preview: Optional[Asset] = field(
        default=None, metadata=config(field_name="preview")
    )
    previews: Optional[Optional[List[Asset]]] = field(
        default=None, metadata=config(field_name="previews")
    )


@dataclass
class MessageAttachmentUploaded(DataClassJsonMixin):
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    object: Asset = field(metadata=config(field_name="object"))
    metadata: str = field(metadata=config(field_name="metadata"))
    previews: Optional[Optional[List[Asset]]] = field(
        default=None, metadata=config(field_name="previews")
    )


@dataclass
class HeaderPlaintext__V1(DataClassJsonMixin):
    version: Literal[HeaderPlaintextVersionStrings.V1]
    V1: Optional[HeaderPlaintextV1]


@dataclass
class HeaderPlaintext__V2(DataClassJsonMixin):
    version: Literal[HeaderPlaintextVersionStrings.V2]
    V2: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V3(DataClassJsonMixin):
    version: Literal[HeaderPlaintextVersionStrings.V3]
    V3: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V4(DataClassJsonMixin):
    version: Literal[HeaderPlaintextVersionStrings.V4]
    V4: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V5(DataClassJsonMixin):
    version: Literal[HeaderPlaintextVersionStrings.V5]
    V5: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V6(DataClassJsonMixin):
    version: Literal[HeaderPlaintextVersionStrings.V6]
    V6: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V7(DataClassJsonMixin):
    version: Literal[HeaderPlaintextVersionStrings.V7]
    V7: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V8(DataClassJsonMixin):
    version: Literal[HeaderPlaintextVersionStrings.V8]
    V8: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V9(DataClassJsonMixin):
    version: Literal[HeaderPlaintextVersionStrings.V9]
    V9: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V10(DataClassJsonMixin):
    version: Literal[HeaderPlaintextVersionStrings.V10]
    V10: Optional[HeaderPlaintextUnsupported]


HeaderPlaintext = Union[
    HeaderPlaintext__V1,
    HeaderPlaintext__V2,
    HeaderPlaintext__V3,
    HeaderPlaintext__V4,
    HeaderPlaintext__V5,
    HeaderPlaintext__V6,
    HeaderPlaintext__V7,
    HeaderPlaintext__V8,
    HeaderPlaintext__V9,
    HeaderPlaintext__V10,
]


@dataclass
class PostFileAttachmentArg(DataClassJsonMixin):
    conversation_id: ConversationID = field(
        metadata=config(field_name="conversationID")
    )
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    visibility: keybase1.TLFVisibility = field(metadata=config(field_name="visibility"))
    filename: str = field(metadata=config(field_name="filename"))
    title: str = field(metadata=config(field_name="title"))
    metadata: str = field(metadata=config(field_name="metadata"))
    identify_behavior: keybase1.TLFIdentifyBehavior = field(
        metadata=config(field_name="identifyBehavior")
    )
    caller_preview: Optional[MakePreviewRes] = field(
        default=None, metadata=config(field_name="callerPreview")
    )
    outbox_id: Optional[OutboxID] = field(
        default=None, metadata=config(field_name="outboxID")
    )
    ephemeral_lifetime: Optional[gregor1.DurationSec] = field(
        default=None, metadata=config(field_name="ephemeralLifetime")
    )


@dataclass
class ReactionUpdate(DataClassJsonMixin):
    reactions: ReactionMap = field(metadata=config(field_name="reactions"))
    target_msg_id: MessageID = field(metadata=config(field_name="targetMsgID"))


@dataclass
class MessageBoxed(DataClassJsonMixin):
    version: MessageBoxedVersion = field(metadata=config(field_name="version"))
    client_header: MessageClientHeader = field(
        metadata=config(field_name="clientHeader")
    )
    header_ciphertext: SealedData = field(
        metadata=config(field_name="headerCiphertext")
    )
    body_ciphertext: EncryptedData = field(metadata=config(field_name="bodyCiphertext"))
    verify_key: str = field(metadata=config(field_name="verifyKey"))
    key_generation: int = field(metadata=config(field_name="keyGeneration"))
    server_header: Optional[MessageServerHeader] = field(
        default=None, metadata=config(field_name="serverHeader")
    )


@dataclass
class BotInfoResponse__UPTODATE(DataClassJsonMixin):
    typ: Literal[BotInfoResponseTypStrings.UPTODATE]
    UPTODATE: None


@dataclass
class BotInfoResponse__INFO(DataClassJsonMixin):
    typ: Literal[BotInfoResponseTypStrings.INFO]
    INFO: Optional[BotInfo]


BotInfoResponse = Union[BotInfoResponse__UPTODATE, BotInfoResponse__INFO]


@dataclass
class UnfurlGeneric(DataClassJsonMixin):
    title: str = field(metadata=config(field_name="title"))
    url: str = field(metadata=config(field_name="url"))
    site_name: str = field(metadata=config(field_name="siteName"))
    favicon: Optional[Asset] = field(
        default=None, metadata=config(field_name="favicon")
    )
    image: Optional[Asset] = field(default=None, metadata=config(field_name="image"))
    publish_time: Optional[int] = field(
        default=None, metadata=config(field_name="publishTime")
    )
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    map_info: Optional[UnfurlGenericMapInfo] = field(
        default=None, metadata=config(field_name="mapInfo")
    )


@dataclass
class UnfurlGiphy(DataClassJsonMixin):
    favicon: Optional[Asset] = field(
        default=None, metadata=config(field_name="favicon")
    )
    image: Optional[Asset] = field(default=None, metadata=config(field_name="image"))
    video: Optional[Asset] = field(default=None, metadata=config(field_name="video"))


@dataclass
class UnfurlDisplay__GENERIC(DataClassJsonMixin):
    unfurlType: Literal[UnfurlTypeStrings.GENERIC]
    GENERIC: Optional[UnfurlGenericDisplay]


@dataclass
class UnfurlDisplay__YOUTUBE(DataClassJsonMixin):
    unfurlType: Literal[UnfurlTypeStrings.YOUTUBE]
    YOUTUBE: Optional[UnfurlYoutubeDisplay]


@dataclass
class UnfurlDisplay__GIPHY(DataClassJsonMixin):
    unfurlType: Literal[UnfurlTypeStrings.GIPHY]
    GIPHY: Optional[UnfurlGiphyDisplay]


UnfurlDisplay = Union[
    UnfurlDisplay__GENERIC, UnfurlDisplay__YOUTUBE, UnfurlDisplay__GIPHY
]


@dataclass
class UIMessageUnfurlInfo(DataClassJsonMixin):
    unfurl_message_id: MessageID = field(metadata=config(field_name="unfurlMessageID"))
    url: str = field(metadata=config(field_name="url"))
    unfurl: UnfurlDisplay = field(metadata=config(field_name="unfurl"))
    is_collapsed: bool = field(metadata=config(field_name="isCollapsed"))


@dataclass
class NewMessagePayload(DataClassJsonMixin):
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    message: MessageBoxed = field(metadata=config(field_name="message"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        default=None, metadata=config(field_name="unreadUpdate")
    )
    max_msgs: Optional[Optional[List[MessageSummary]]] = field(
        default=None, metadata=config(field_name="maxMsgs")
    )


@dataclass
class LoadFlipRes(DataClassJsonMixin):
    status: UICoinFlipStatus = field(metadata=config(field_name="status"))
    rate_limits: Optional[Optional[List[RateLimit]]] = field(
        default=None, metadata=config(field_name="rateLimits")
    )
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identifyFailures")
    )


@dataclass
class ReactionUpdateNotif(DataClassJsonMixin):
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    user_reacjis: keybase1.UserReacjis = field(
        metadata=config(field_name="userReacjis")
    )
    reaction_updates: Optional[Optional[List[ReactionUpdate]]] = field(
        default=None, metadata=config(field_name="reactionUpdates")
    )


@dataclass
class ThreadViewBoxed(DataClassJsonMixin):
    messages: Optional[Optional[List[MessageBoxed]]] = field(
        default=None, metadata=config(field_name="messages")
    )
    pagination: Optional[Pagination] = field(
        default=None, metadata=config(field_name="pagination")
    )


@dataclass
class GetMessagesRemoteRes(DataClassJsonMixin):
    msgs: Optional[Optional[List[MessageBoxed]]] = field(
        default=None, metadata=config(field_name="msgs")
    )
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class GetBotInfoRes(DataClassJsonMixin):
    response: BotInfoResponse = field(metadata=config(field_name="response"))
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class Unfurl__GENERIC(DataClassJsonMixin):
    unfurlType: Literal[UnfurlTypeStrings.GENERIC]
    GENERIC: Optional[UnfurlGeneric]


@dataclass
class Unfurl__YOUTUBE(DataClassJsonMixin):
    unfurlType: Literal[UnfurlTypeStrings.YOUTUBE]
    YOUTUBE: Optional[UnfurlYoutube]


@dataclass
class Unfurl__GIPHY(DataClassJsonMixin):
    unfurlType: Literal[UnfurlTypeStrings.GIPHY]
    GIPHY: Optional[UnfurlGiphy]


Unfurl = Union[Unfurl__GENERIC, Unfurl__YOUTUBE, Unfurl__GIPHY]


@dataclass
class GetThreadRemoteRes(DataClassJsonMixin):
    thread: ThreadViewBoxed = field(metadata=config(field_name="thread"))
    members_type: ConversationMembersType = field(
        metadata=config(field_name="membersType")
    )
    visibility: keybase1.TLFVisibility = field(metadata=config(field_name="visibility"))
    rate_limit: Optional[RateLimit] = field(
        default=None, metadata=config(field_name="rateLimit")
    )


@dataclass
class UnfurlResult(DataClassJsonMixin):
    unfurl: Unfurl = field(metadata=config(field_name="unfurl"))
    url: str = field(metadata=config(field_name="url"))


@dataclass
class MessageUnfurl(DataClassJsonMixin):
    unfurl: UnfurlResult = field(metadata=config(field_name="unfurl"))
    message_id: MessageID = field(metadata=config(field_name="messageID"))


@dataclass
class MsgContent(DataClassJsonMixin):
    type_name: str = field(metadata=config(field_name="type"))
    text: Optional[MessageText] = field(
        default=None, metadata=config(field_name="text")
    )
    attachment: Optional[MessageAttachment] = field(
        default=None, metadata=config(field_name="attachment")
    )
    edit: Optional[MessageEdit] = field(
        default=None, metadata=config(field_name="edit")
    )
    reaction: Optional[MessageReaction] = field(
        default=None, metadata=config(field_name="reaction")
    )
    delete: Optional[MessageDelete] = field(
        default=None, metadata=config(field_name="delete")
    )
    metadata: Optional[MessageConversationMetadata] = field(
        default=None, metadata=config(field_name="metadata")
    )
    headline: Optional[MessageHeadline] = field(
        default=None, metadata=config(field_name="headline")
    )
    attachment_uploaded: Optional[MessageAttachmentUploaded] = field(
        default=None, metadata=config(field_name="attachment_uploaded")
    )
    system: Optional[MessageSystem] = field(
        default=None, metadata=config(field_name="system")
    )
    send_payment: Optional[MessageSendPayment] = field(
        default=None, metadata=config(field_name="send_payment")
    )
    request_payment: Optional[MessageRequestPayment] = field(
        default=None, metadata=config(field_name="request_payment")
    )
    unfurl: Optional[MessageUnfurl] = field(
        default=None, metadata=config(field_name="unfurl")
    )
    flip: Optional[MsgFlipContent] = field(
        default=None, metadata=config(field_name="flip")
    )


@dataclass
class MessageBody__TEXT(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.TEXT]
    TEXT: Optional[MessageText]


@dataclass
class MessageBody__ATTACHMENT(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.ATTACHMENT]
    ATTACHMENT: Optional[MessageAttachment]


@dataclass
class MessageBody__EDIT(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.EDIT]
    EDIT: Optional[MessageEdit]


@dataclass
class MessageBody__DELETE(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.DELETE]
    DELETE: Optional[MessageDelete]


@dataclass
class MessageBody__METADATA(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.METADATA]
    METADATA: Optional[MessageConversationMetadata]


@dataclass
class MessageBody__HEADLINE(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.HEADLINE]
    HEADLINE: Optional[MessageHeadline]


@dataclass
class MessageBody__ATTACHMENTUPLOADED(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.ATTACHMENTUPLOADED]
    ATTACHMENTUPLOADED: Optional[MessageAttachmentUploaded]


@dataclass
class MessageBody__JOIN(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.JOIN]
    JOIN: Optional[MessageJoin]


@dataclass
class MessageBody__LEAVE(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.LEAVE]
    LEAVE: Optional[MessageLeave]


@dataclass
class MessageBody__SYSTEM(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.SYSTEM]
    SYSTEM: Optional[MessageSystem]


@dataclass
class MessageBody__DELETEHISTORY(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.DELETEHISTORY]
    DELETEHISTORY: Optional[MessageDeleteHistory]


@dataclass
class MessageBody__REACTION(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.REACTION]
    REACTION: Optional[MessageReaction]


@dataclass
class MessageBody__SENDPAYMENT(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.SENDPAYMENT]
    SENDPAYMENT: Optional[MessageSendPayment]


@dataclass
class MessageBody__REQUESTPAYMENT(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.REQUESTPAYMENT]
    REQUESTPAYMENT: Optional[MessageRequestPayment]


@dataclass
class MessageBody__UNFURL(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.UNFURL]
    UNFURL: Optional[MessageUnfurl]


@dataclass
class MessageBody__FLIP(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.FLIP]
    FLIP: Optional[MessageFlip]


@dataclass
class MessageBody__PIN(DataClassJsonMixin):
    messageType: Literal[MessageTypeStrings.PIN]
    PIN: Optional[MessagePin]


MessageBody = Union[
    MessageBody__TEXT,
    MessageBody__ATTACHMENT,
    MessageBody__EDIT,
    MessageBody__DELETE,
    MessageBody__METADATA,
    MessageBody__HEADLINE,
    MessageBody__ATTACHMENTUPLOADED,
    MessageBody__JOIN,
    MessageBody__LEAVE,
    MessageBody__SYSTEM,
    MessageBody__DELETEHISTORY,
    MessageBody__REACTION,
    MessageBody__SENDPAYMENT,
    MessageBody__REQUESTPAYMENT,
    MessageBody__UNFURL,
    MessageBody__FLIP,
    MessageBody__PIN,
]


@dataclass
class MsgSummary(DataClassJsonMixin):
    id: MessageID = field(metadata=config(field_name="id"))
    conv_id: str = field(metadata=config(field_name="conversation_id"))
    channel: ChatChannel = field(metadata=config(field_name="channel"))
    sender: MsgSender = field(metadata=config(field_name="sender"))
    sent_at: int = field(metadata=config(field_name="sent_at"))
    sent_at_ms: int = field(metadata=config(field_name="sent_at_ms"))
    content: MsgContent = field(metadata=config(field_name="content"))
    unread: bool = field(metadata=config(field_name="unread"))
    prev: Optional[Optional[List[MessagePreviousPointer]]] = field(
        default=None, metadata=config(field_name="prev")
    )
    revoked_device: Optional[bool] = field(
        default=None, metadata=config(field_name="revoked_device")
    )
    offline: Optional[bool] = field(default=None, metadata=config(field_name="offline"))
    kbfs_encrypted: Optional[bool] = field(
        default=None, metadata=config(field_name="kbfs_encrypted")
    )
    is_ephemeral: Optional[bool] = field(
        default=None, metadata=config(field_name="is_ephemeral")
    )
    is_ephemeral_expired: Optional[bool] = field(
        default=None, metadata=config(field_name="is_ephemeral_expired")
    )
    e_time: Optional[gregor1.Time] = field(
        default=None, metadata=config(field_name="e_time")
    )
    reactions: Optional[ReactionMap] = field(
        default=None, metadata=config(field_name="reactions")
    )
    has_pairwise_macs: Optional[bool] = field(
        default=None, metadata=config(field_name="has_pairwise_macs")
    )
    at_mention_usernames: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="at_mention_usernames")
    )
    channel_mention: Optional[str] = field(
        default=None, metadata=config(field_name="channel_mention")
    )
    channel_name_mentions: Optional[Optional[List[UIChannelNameMention]]] = field(
        default=None, metadata=config(field_name="channel_name_mentions")
    )
    bot_uid: Optional[str] = field(default=None, metadata=config(field_name="bot_uid"))


@dataclass
class BodyPlaintextV1(DataClassJsonMixin):
    message_body: MessageBody = field(metadata=config(field_name="messageBody"))


@dataclass
class BodyPlaintextV2(DataClassJsonMixin):
    message_body: MessageBody = field(metadata=config(field_name="messageBody"))
    mi: BodyPlaintextMetaInfo = field(metadata=config(field_name="mi"))


@dataclass
class MessagePlaintext(DataClassJsonMixin):
    client_header: MessageClientHeader = field(
        metadata=config(field_name="clientHeader")
    )
    message_body: MessageBody = field(metadata=config(field_name="messageBody"))
    supersedes_outbox_id: Optional[OutboxID] = field(
        default=None, metadata=config(field_name="supersedesOutboxID")
    )


@dataclass
class Message(DataClassJsonMixin):
    msg: Optional[MsgSummary] = field(default=None, metadata=config(field_name="msg"))
    error: Optional[str] = field(default=None, metadata=config(field_name="error"))


@dataclass
class MsgNotification(DataClassJsonMixin):
    type: str = field(metadata=config(field_name="type"))
    source: str = field(metadata=config(field_name="source"))
    msg: Optional[MsgSummary] = field(default=None, metadata=config(field_name="msg"))
    error: Optional[str] = field(default=None, metadata=config(field_name="error"))
    pagination: Optional[UIPagination] = field(
        default=None, metadata=config(field_name="pagination")
    )


@dataclass
class BodyPlaintext__V1(DataClassJsonMixin):
    version: Literal[BodyPlaintextVersionStrings.V1]
    V1: Optional[BodyPlaintextV1]


@dataclass
class BodyPlaintext__V2(DataClassJsonMixin):
    version: Literal[BodyPlaintextVersionStrings.V2]
    V2: Optional[BodyPlaintextV2]


@dataclass
class BodyPlaintext__V3(DataClassJsonMixin):
    version: Literal[BodyPlaintextVersionStrings.V3]
    V3: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V4(DataClassJsonMixin):
    version: Literal[BodyPlaintextVersionStrings.V4]
    V4: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V5(DataClassJsonMixin):
    version: Literal[BodyPlaintextVersionStrings.V5]
    V5: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V6(DataClassJsonMixin):
    version: Literal[BodyPlaintextVersionStrings.V6]
    V6: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V7(DataClassJsonMixin):
    version: Literal[BodyPlaintextVersionStrings.V7]
    V7: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V8(DataClassJsonMixin):
    version: Literal[BodyPlaintextVersionStrings.V8]
    V8: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V9(DataClassJsonMixin):
    version: Literal[BodyPlaintextVersionStrings.V9]
    V9: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V10(DataClassJsonMixin):
    version: Literal[BodyPlaintextVersionStrings.V10]
    V10: Optional[BodyPlaintextUnsupported]


BodyPlaintext = Union[
    BodyPlaintext__V1,
    BodyPlaintext__V2,
    BodyPlaintext__V3,
    BodyPlaintext__V4,
    BodyPlaintext__V5,
    BodyPlaintext__V6,
    BodyPlaintext__V7,
    BodyPlaintext__V8,
    BodyPlaintext__V9,
    BodyPlaintext__V10,
]


@dataclass
class Thread(DataClassJsonMixin):
    messages: Optional[Optional[List[Message]]] = field(
        default=None, metadata=config(field_name="messages")
    )
    pagination: Optional[Pagination] = field(
        default=None, metadata=config(field_name="pagination")
    )
    offline: Optional[bool] = field(default=None, metadata=config(field_name="offline"))
    identify_failures: Optional[Optional[List[keybase1.TLFIdentifyFailure]]] = field(
        default=None, metadata=config(field_name="identify_failures")
    )
    rate_limits: Optional[Optional[List[RateLimitRes]]] = field(
        default=None, metadata=config(field_name="ratelimits")
    )
