"""chat.1

Auto-generated to Python types by avdl-compiler v1.4.1 (https://github.com/keybase/node-avdl-compiler)
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

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union

from dataclasses_json import config, dataclass_json
from typing_extensions import Literal

import gregor1
import keybase1
import stellar1


@dataclass_json
@dataclass
class RateLimitRes:
    tank: str = field(metadata=config(field_name="tank"))
    capacity: int = field(metadata=config(field_name="capacity"))
    reset: int = field(metadata=config(field_name="reset"))
    gas: int = field(metadata=config(field_name="gas"))


@dataclass_json
@dataclass
class ChatChannel:
    name: str = field(metadata=config(field_name="name"))
    public: bool = field(metadata=config(field_name="public"))
    members_type: str = field(metadata=config(field_name="members_type"))
    topic_type: Optional[str] = field(metadata=config(field_name="topic_type"))
    topic_name: Optional[str] = field(metadata=config(field_name="topic_name"))


@dataclass_json
@dataclass
class ChatMessage:
    body: str = field(metadata=config(field_name="body"))


@dataclass_json
@dataclass
class MsgSender:
    uid: str = field(metadata=config(field_name="uid"))
    username: Optional[str] = field(metadata=config(field_name="username"))
    device_id: str = field(metadata=config(field_name="device_id"))
    device_name: Optional[str] = field(metadata=config(field_name="device_name"))


@dataclass_json
@dataclass
class UIPagination:
    next: str = field(metadata=config(field_name="next"))
    previous: str = field(metadata=config(field_name="previous"))
    num: int = field(metadata=config(field_name="num"))
    last: bool = field(metadata=config(field_name="last"))


@dataclass_json
@dataclass
class UnverifiedInboxUIItemMetadata:
    channel_name: str = field(metadata=config(field_name="channelName"))
    headline: str = field(metadata=config(field_name="headline"))
    headline_decorated: str = field(metadata=config(field_name="headlineDecorated"))
    snippet: str = field(metadata=config(field_name="snippet"))
    snippet_decoration: str = field(metadata=config(field_name="snippetDecoration"))
    writer_names: List[str] = field(metadata=config(field_name="writerNames"))
    reset_participants: List[str] = field(
        metadata=config(field_name="resetParticipants")
    )


class UIParticipantType(Enum):
    NONE = "none"
    USER = "user"
    PHONENO = "phoneno"
    EMAIL = "email"


@dataclass_json
@dataclass
class UIChannelNameMention:
    name: str = field(metadata=config(field_name="name"))
    conv_id: str = field(metadata=config(field_name="convID"))


@dataclass_json
@dataclass
class UIAssetUrlInfo:
    preview_url: str = field(metadata=config(field_name="previewUrl"))
    full_url: str = field(metadata=config(field_name="fullUrl"))
    full_url_cached: bool = field(metadata=config(field_name="fullUrlCached"))
    mime_type: str = field(metadata=config(field_name="mimeType"))
    video_duration: Optional[str] = field(metadata=config(field_name="videoDuration"))
    inline_video_playable: bool = field(
        metadata=config(field_name="inlineVideoPlayable")
    )


@dataclass_json
@dataclass
class UIPaymentInfo:
    account_id: Optional[stellar1.AccountID] = field(
        metadata=config(field_name="accountID")
    )
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


@dataclass_json
@dataclass
class UIRequestInfo:
    amount: str = field(metadata=config(field_name="amount"))
    amount_description: str = field(metadata=config(field_name="amountDescription"))
    asset: Optional[stellar1.Asset] = field(metadata=config(field_name="asset"))
    currency: Optional[stellar1.OutsideCurrencyCode] = field(
        metadata=config(field_name="currency")
    )
    worth_at_request_time: str = field(metadata=config(field_name="worthAtRequestTime"))
    status: stellar1.RequestStatus = field(metadata=config(field_name="status"))


class MessageUnboxedState(Enum):
    VALID = "valid"
    ERROR = "error"
    OUTBOX = "outbox"
    PLACEHOLDER = "placeholder"


@dataclass_json
@dataclass
class UITeamMention:
    in_team: bool = field(metadata=config(field_name="inTeam"))
    open: bool = field(metadata=config(field_name="open"))
    description: Optional[str] = field(metadata=config(field_name="description"))
    num_members: Optional[int] = field(metadata=config(field_name="numMembers"))
    public_admins: List[str] = field(metadata=config(field_name="publicAdmins"))
    conv_id: Optional[str] = field(metadata=config(field_name="convID"))


class UITextDecorationTyp(Enum):
    PAYMENT = "payment"
    ATMENTION = "atmention"
    CHANNELNAMEMENTION = "channelnamemention"
    MAYBEMENTION = "maybemention"
    LINK = "link"
    MAILTO = "mailto"
    KBFSPATH = "kbfspath"


class UIMaybeMentionStatus(Enum):
    UNKNOWN = "unknown"
    USER = "user"
    TEAM = "team"
    NOTHING = "nothing"


@dataclass_json
@dataclass
class UILinkDecoration:
    display: str = field(metadata=config(field_name="display"))
    url: str = field(metadata=config(field_name="url"))


class UIChatThreadStatusTyp(Enum):
    NONE = "none"
    SERVER = "server"
    VALIDATING = "validating"
    VALIDATED = "validated"


@dataclass
class UIChatThreadStatus__NONE:
    typ: Literal[UIChatThreadStatusTyp.NONE]
    NONE: None


@dataclass
class UIChatThreadStatus__SERVER:
    typ: Literal[UIChatThreadStatusTyp.SERVER]
    SERVER: None


@dataclass
class UIChatThreadStatus__VALIDATING:
    typ: Literal[UIChatThreadStatusTyp.VALIDATING]
    VALIDATING: Optional[int]


@dataclass
class UIChatThreadStatus__VALIDATED:
    typ: Literal[UIChatThreadStatusTyp.VALIDATED]
    VALIDATED: None


UIChatThreadStatus = Union[
    UIChatThreadStatus__NONE,
    UIChatThreadStatus__SERVER,
    UIChatThreadStatus__VALIDATING,
    UIChatThreadStatus__VALIDATED,
]


@dataclass_json
@dataclass
class UIChatPayment:
    username: str = field(metadata=config(field_name="username"))
    full_name: str = field(metadata=config(field_name="fullName"))
    xlm_amount: str = field(metadata=config(field_name="xlmAmount"))
    error: Optional[str] = field(metadata=config(field_name="error"))
    display_amount: Optional[str] = field(metadata=config(field_name="displayAmount"))


@dataclass_json
@dataclass
class GiphySearchResult:
    target_url: str = field(metadata=config(field_name="targetUrl"))
    preview_url: str = field(metadata=config(field_name="previewUrl"))
    preview_width: int = field(metadata=config(field_name="previewWidth"))
    preview_height: int = field(metadata=config(field_name="previewHeight"))
    preview_is_video: bool = field(metadata=config(field_name="previewIsVideo"))


class UICoinFlipPhase(Enum):
    COMMITMENT = "commitment"
    REVEALS = "reveals"
    COMPLETE = "complete"
    ERROR = "error"


@dataclass_json
@dataclass
class UICoinFlipErrorParticipant:
    user: str = field(metadata=config(field_name="user"))
    device: str = field(metadata=config(field_name="device"))


class UICoinFlipErrorTyp(Enum):
    GENERIC = "generic"
    ABSENTEE = "absentee"
    TIMEOUT = "timeout"
    ABORTED = "aborted"
    DUPREG = "dupreg"
    DUPCOMMITCOMPLETE = "dupcommitcomplete"
    DUPREVEAL = "dupreveal"
    COMMITMISMATCH = "commitmismatch"


class UICoinFlipResultTyp(Enum):
    NUMBER = "number"
    SHUFFLE = "shuffle"
    DECK = "deck"
    HANDS = "hands"
    COIN = "coin"


@dataclass_json
@dataclass
class UICoinFlipHand:
    target: str = field(metadata=config(field_name="target"))
    hand: List[int] = field(metadata=config(field_name="hand"))


@dataclass_json
@dataclass
class UICoinFlipParticipant:
    uid: str = field(metadata=config(field_name="uid"))
    device_id: str = field(metadata=config(field_name="deviceID"))
    username: str = field(metadata=config(field_name="username"))
    device_name: str = field(metadata=config(field_name="deviceName"))
    commitment: str = field(metadata=config(field_name="commitment"))
    reveal: Optional[str] = field(metadata=config(field_name="reveal"))


@dataclass_json
@dataclass
class UICommandMarkdown:
    body: str = field(metadata=config(field_name="body"))
    title: Optional[str] = field(metadata=config(field_name="title"))


LocationWatchID = int


class UICommandStatusDisplayTyp(Enum):
    STATUS = "status"
    WARNING = "warning"
    ERROR = "error"


class UICommandStatusActionTyp(Enum):
    APPSETTINGS = "appsettings"


class UIBotCommandsUpdateStatus(Enum):
    UPTODATE = "uptodate"
    UPDATING = "updating"
    FAILED = "failed"
    BLANK = "blank"


@dataclass_json
@dataclass
class ConversationCommand:
    description: str = field(metadata=config(field_name="description"))
    name: str = field(metadata=config(field_name="name"))
    usage: str = field(metadata=config(field_name="usage"))
    has_help_text: bool = field(metadata=config(field_name="hasHelpText"))
    username: Optional[str] = field(metadata=config(field_name="username"))


class ConversationCommandGroupsTyp(Enum):
    BUILTIN = "builtin"
    CUSTOM = "custom"
    NONE = "none"


class ConversationBuiltinCommandTyp(Enum):
    NONE = "none"
    ADHOC = "adhoc"
    SMALLTEAM = "smallteam"
    BIGTEAM = "bigteam"
    BIGTEAMGENERAL = "bigteamgeneral"


ThreadID = bytes
MessageID = int
TLFConvOrdinal = int
TopicID = bytes
ConversationID = bytes
TLFID = bytes
Hash = bytes
InboxVers = int
LocalConversationVers = int
ConversationVers = int
OutboxID = bytes
TopicNameState = bytes
FlipGameID = bytes


class ConversationExistence(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"
    ABANDONED = "abandoned"


class ConversationMembersType(Enum):
    KBFS = "kbfs"
    TEAM = "team"
    IMPTEAMNATIVE = "impteamnative"
    IMPTEAMUPGRADE = "impteamupgrade"


class SyncInboxResType(Enum):
    CURRENT = "current"
    INCREMENTAL = "incremental"
    CLEAR = "clear"


class MessageType(Enum):
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
    NONE = "none"
    CHAT = "chat"
    DEV = "dev"
    KBFSFILEEDIT = "kbfsfileedit"


class TeamType(Enum):
    NONE = "none"
    SIMPLE = "simple"
    COMPLEX = "complex"


class NotificationKind(Enum):
    GENERIC = "generic"
    ATMENTION = "atmention"


class GlobalAppNotificationSetting(Enum):
    NEWMESSAGES = "newmessages"
    PLAINTEXTMOBILE = "plaintextmobile"
    PLAINTEXTDESKTOP = "plaintextdesktop"
    DEFAULTSOUNDMOBILE = "defaultsoundmobile"
    DISABLETYPING = "disabletyping"


@dataclass_json
@dataclass
class GlobalAppNotificationSettings:
    settings: Dict[str, bool] = field(metadata=config(field_name="settings"))


class ConversationStatus(Enum):
    UNFILED = "unfiled"
    FAVORITE = "favorite"
    IGNORED = "ignored"
    BLOCKED = "blocked"
    MUTED = "muted"
    REPORTED = "reported"


@dataclass_json
@dataclass
class KBFSPath:
    start_index: int = field(metadata=config(field_name="startIndex"))
    raw_path: str = field(metadata=config(field_name="rawPath"))
    standard_path: str = field(metadata=config(field_name="standardPath"))
    path_info: keybase1.KBFSPathInfo = field(metadata=config(field_name="pathInfo"))


class ConversationMemberStatus(Enum):
    ACTIVE = "active"
    REMOVED = "removed"
    LEFT = "left"
    PREVIEW = "preview"
    RESET = "reset"
    NEVER_JOINED = "never_joined"


@dataclass_json
@dataclass
class Pagination:
    next: bytes = field(metadata=config(field_name="next"))
    previous: bytes = field(metadata=config(field_name="previous"))
    num: int = field(metadata=config(field_name="num"))
    last: bool = field(metadata=config(field_name="last"))
    force_first_page: bool = field(metadata=config(field_name="forceFirstPage"))


@dataclass_json
@dataclass
class RateLimit:
    name: str = field(metadata=config(field_name="name"))
    calls_remaining: int = field(metadata=config(field_name="callsRemaining"))
    window_reset: int = field(metadata=config(field_name="windowReset"))
    max_calls: int = field(metadata=config(field_name="maxCalls"))


@dataclass_json
@dataclass
class ConversationFinalizeInfo:
    reset_user: str = field(metadata=config(field_name="resetUser"))
    reset_date: str = field(metadata=config(field_name="resetDate"))
    reset_full: str = field(metadata=config(field_name="resetFull"))
    reset_timestamp: gregor1.Time = field(metadata=config(field_name="resetTimestamp"))


@dataclass_json
@dataclass
class ConversationResolveInfo:
    new_tlf_name: str = field(metadata=config(field_name="newTLFName"))


@dataclass_json
@dataclass
class ConversationNotificationInfo:
    channel_wide: bool = field(metadata=config(field_name="channelWide"))
    settings: Dict[str, Dict[str, bool]] = field(metadata=config(field_name="settings"))


@dataclass_json
@dataclass
class ConversationCreatorInfo:
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))
    uid: gregor1.UID = field(metadata=config(field_name="uid"))


@dataclass_json
@dataclass
class ConversationCreatorInfoLocal:
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))
    username: str = field(metadata=config(field_name="username"))


@dataclass_json
@dataclass
class ConversationMinWriterRoleInfo:
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    role: keybase1.TeamRole = field(metadata=config(field_name="role"))


@dataclass_json
@dataclass
class MsgEphemeralMetadata:
    lifetime: gregor1.DurationSec = field(metadata=config(field_name="l"))
    generation: keybase1.EkGeneration = field(metadata=config(field_name="g"))
    exploded_by: Optional[str] = field(metadata=config(field_name="u"))


@dataclass_json
@dataclass
class EncryptedData:
    v: int = field(metadata=config(field_name="v"))
    e: bytes = field(metadata=config(field_name="e"))
    n: bytes = field(metadata=config(field_name="n"))


@dataclass_json
@dataclass
class SignEncryptedData:
    v: int = field(metadata=config(field_name="v"))
    e: bytes = field(metadata=config(field_name="e"))
    n: bytes = field(metadata=config(field_name="n"))


@dataclass_json
@dataclass
class SealedData:
    v: int = field(metadata=config(field_name="v"))
    e: bytes = field(metadata=config(field_name="e"))
    n: bytes = field(metadata=config(field_name="n"))


@dataclass_json
@dataclass
class SignatureInfo:
    v: int = field(metadata=config(field_name="v"))
    s: bytes = field(metadata=config(field_name="s"))
    k: bytes = field(metadata=config(field_name="k"))


@dataclass_json
@dataclass
class MerkleRoot:
    seqno: int = field(metadata=config(field_name="seqno"))
    hash: bytes = field(metadata=config(field_name="hash"))


class InboxResType(Enum):
    VERSIONHIT = "versionhit"
    FULL = "full"


class RetentionPolicyType(Enum):
    NONE = "none"
    RETAIN = "retain"
    EXPIRE = "expire"
    INHERIT = "inherit"
    EPHEMERAL = "ephemeral"


@dataclass_json
@dataclass
class RpRetain:
    pass


@dataclass_json
@dataclass
class RpExpire:
    age: gregor1.DurationSec = field(metadata=config(field_name="age"))


@dataclass_json
@dataclass
class RpInherit:
    pass


@dataclass_json
@dataclass
class RpEphemeral:
    age: gregor1.DurationSec = field(metadata=config(field_name="age"))


class GetThreadReason(Enum):
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
    NONE = "none"
    PRESEARCH_SYNC = "presearch_sync"
    POSTSEARCH_SYNC = "postsearch_sync"


@dataclass_json
@dataclass
class EmptyStruct:
    pass


@dataclass_json
@dataclass
class ChatSearchMatch:
    start_index: int = field(metadata=config(field_name="startIndex"))
    end_index: int = field(metadata=config(field_name="endIndex"))
    match: str = field(metadata=config(field_name="match"))


@dataclass_json
@dataclass
class ChatSearchInboxDone:
    num_hits: int = field(metadata=config(field_name="numHits"))
    num_convs: int = field(metadata=config(field_name="numConvs"))
    percent_indexed: int = field(metadata=config(field_name="percentIndexed"))
    delegated: bool = field(metadata=config(field_name="delegated"))


@dataclass_json
@dataclass
class ChatSearchIndexStatus:
    percent_indexed: int = field(metadata=config(field_name="percentIndexed"))


@dataclass_json
@dataclass
class AssetMetadataImage:
    width: int = field(metadata=config(field_name="width"))
    height: int = field(metadata=config(field_name="height"))


@dataclass_json
@dataclass
class AssetMetadataVideo:
    width: int = field(metadata=config(field_name="width"))
    height: int = field(metadata=config(field_name="height"))
    duration_ms: int = field(metadata=config(field_name="durationMs"))


@dataclass_json
@dataclass
class AssetMetadataAudio:
    duration_ms: int = field(metadata=config(field_name="durationMs"))


class AssetMetadataType(Enum):
    NONE = "none"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"


class AssetTag(Enum):
    PRIMARY = "primary"


class BotCommandsAdvertisementTyp(Enum):
    PUBLIC = "public"
    TLFID_MEMBERS = "tlfid_members"
    TLFID_CONVS = "tlfid_convs"


@dataclass_json
@dataclass
class TeamMember:
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    role: keybase1.TeamRole = field(metadata=config(field_name="role"))
    status: keybase1.TeamMemberStatus = field(metadata=config(field_name="status"))


VersionKind = str


class TextPaymentResultTyp(Enum):
    SENT = "sent"
    ERROR = "error"


@dataclass
class TextPaymentResult__ERROR:
    resultTyp: Literal[TextPaymentResultTyp.ERROR]
    ERROR: Optional[str]


@dataclass
class TextPaymentResult__SENT:
    resultTyp: Literal[TextPaymentResultTyp.SENT]
    SENT: Optional[stellar1.PaymentID]


TextPaymentResult = Union[TextPaymentResult__ERROR, TextPaymentResult__SENT]


@dataclass_json
@dataclass
class KnownUserMention:
    text: str = field(metadata=config(field_name="text"))
    uid: gregor1.UID = field(metadata=config(field_name="uid"))


@dataclass_json
@dataclass
class KnownTeamMention:
    name: str = field(metadata=config(field_name="name"))
    channel: str = field(metadata=config(field_name="channel"))


@dataclass_json
@dataclass
class MaybeMention:
    name: str = field(metadata=config(field_name="name"))
    channel: str = field(metadata=config(field_name="channel"))


@dataclass_json
@dataclass
class Coordinate:
    lat: float = field(metadata=config(field_name="lat"))
    lon: float = field(metadata=config(field_name="lon"))
    accuracy: float = field(metadata=config(field_name="accuracy"))


@dataclass_json
@dataclass
class LiveLocation:
    end_time: gregor1.Time = field(metadata=config(field_name="endTime"))


@dataclass_json
@dataclass
class MessageConversationMetadata:
    conversation_title: str = field(metadata=config(field_name="conversationTitle"))


@dataclass_json
@dataclass
class MessageHeadline:
    headline: str = field(metadata=config(field_name="headline"))


class MessageSystemType(Enum):
    ADDEDTOTEAM = "addedtoteam"
    INVITEADDEDTOTEAM = "inviteaddedtoteam"
    COMPLEXTEAM = "complexteam"
    CREATETEAM = "createteam"
    GITPUSH = "gitpush"
    CHANGEAVATAR = "changeavatar"
    CHANGERETENTION = "changeretention"
    BULKADDTOCONV = "bulkaddtoconv"


@dataclass_json
@dataclass
class MessageSystemAddedToTeam:
    team: str = field(metadata=config(field_name="team"))
    adder: str = field(metadata=config(field_name="adder"))
    addee: str = field(metadata=config(field_name="addee"))
    owners: List[str] = field(metadata=config(field_name="owners"))
    admins: List[str] = field(metadata=config(field_name="admins"))
    writers: List[str] = field(metadata=config(field_name="writers"))
    readers: List[str] = field(metadata=config(field_name="readers"))
    bots: List[str] = field(metadata=config(field_name="bots"))
    restricted_bots: List[str] = field(metadata=config(field_name="restrictedBots"))


@dataclass_json
@dataclass
class MessageSystemInviteAddedToTeam:
    team: str = field(metadata=config(field_name="team"))
    inviter: str = field(metadata=config(field_name="inviter"))
    invitee: str = field(metadata=config(field_name="invitee"))
    adder: str = field(metadata=config(field_name="adder"))
    invite_type: keybase1.TeamInviteCategory = field(
        metadata=config(field_name="inviteType")
    )


@dataclass_json
@dataclass
class MessageSystemComplexTeam:
    team: str = field(metadata=config(field_name="team"))


@dataclass_json
@dataclass
class MessageSystemCreateTeam:
    team: str = field(metadata=config(field_name="team"))
    creator: str = field(metadata=config(field_name="creator"))


@dataclass_json
@dataclass
class MessageSystemGitPush:
    team: str = field(metadata=config(field_name="team"))
    pusher: str = field(metadata=config(field_name="pusher"))
    repo_name: str = field(metadata=config(field_name="repoName"))
    repo_id: keybase1.RepoID = field(metadata=config(field_name="repoID"))
    refs: List[keybase1.GitRefMetadata] = field(metadata=config(field_name="refs"))
    push_type: keybase1.GitPushType = field(metadata=config(field_name="pushType"))
    previous_repo_name: str = field(metadata=config(field_name="previousRepoName"))


@dataclass_json
@dataclass
class MessageSystemChangeAvatar:
    team: str = field(metadata=config(field_name="team"))
    user: str = field(metadata=config(field_name="user"))


@dataclass_json
@dataclass
class MessageSystemBulkAddToConv:
    usernames: List[str] = field(metadata=config(field_name="usernames"))


@dataclass_json
@dataclass
class MessageJoin:
    joiners: List[str] = field(metadata=config(field_name="joiners"))
    leavers: List[str] = field(metadata=config(field_name="leavers"))


@dataclass_json
@dataclass
class MessageLeave:
    pass


@dataclass_json
@dataclass
class MessageSendPayment:
    payment_id: stellar1.PaymentID = field(metadata=config(field_name="paymentID"))


@dataclass_json
@dataclass
class MessageRequestPayment:
    request_id: stellar1.KeybaseRequestID = field(
        metadata=config(field_name="requestID")
    )
    note: str = field(metadata=config(field_name="note"))


class OutboxStateType(Enum):
    SENDING = "sending"
    ERROR = "error"


class OutboxErrorType(Enum):
    MISC = "misc"
    OFFLINE = "offline"
    IDENTIFY = "identify"
    TOOLONG = "toolong"
    DUPLICATE = "duplicate"
    EXPIRED = "expired"
    TOOMANYATTEMPTS = "toomanyattempts"
    ALREADY_DELETED = "already_deleted"
    UPLOADFAILED = "uploadfailed"


class HeaderPlaintextVersion(Enum):
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


@dataclass_json
@dataclass
class HeaderPlaintextMetaInfo:
    crit: bool = field(metadata=config(field_name="crit"))


class BodyPlaintextVersion(Enum):
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


@dataclass_json
@dataclass
class BodyPlaintextMetaInfo:
    crit: bool = field(metadata=config(field_name="crit"))


class MessageUnboxedErrorType(Enum):
    MISC = "misc"
    BADVERSION_CRITICAL = "badversion_critical"
    BADVERSION = "badversion"
    IDENTIFY = "identify"
    EPHEMERAL = "ephemeral"
    PAIRWISE_MISSING = "pairwise_missing"


@dataclass_json
@dataclass
class UnreadFirstNumLimit:
    num_read: int = field(metadata=config(field_name="NumRead"))
    at_least: int = field(metadata=config(field_name="AtLeast"))
    at_most: int = field(metadata=config(field_name="AtMost"))


@dataclass_json
@dataclass
class ConversationLocalParticipant:
    username: str = field(metadata=config(field_name="username"))
    fullname: Optional[str] = field(metadata=config(field_name="fullname"))
    contact_name: Optional[str] = field(metadata=config(field_name="contactName"))


class ConversationErrorType(Enum):
    PERMANENT = "permanent"
    MISSINGINFO = "missinginfo"
    SELFREKEYNEEDED = "selfrekeyneeded"
    OTHERREKEYNEEDED = "otherrekeyneeded"
    IDENTIFY = "identify"
    TRANSIENT = "transient"
    NONE = "none"


@dataclass_json
@dataclass
class ConversationErrorRekey:
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    tlf_public: bool = field(metadata=config(field_name="tlfPublic"))
    rekeyers: List[str] = field(metadata=config(field_name="rekeyers"))
    writer_names: List[str] = field(metadata=config(field_name="writerNames"))
    reader_names: List[str] = field(metadata=config(field_name="readerNames"))


@dataclass_json
@dataclass
class ConversationMinWriterRoleInfoLocal:
    changed_by: str = field(metadata=config(field_name="changedBy"))
    cannot_write: bool = field(metadata=config(field_name="cannotWrite"))
    role: keybase1.TeamRole = field(metadata=config(field_name="role"))


class MessageIDControlMode(Enum):
    OLDERMESSAGES = "oldermessages"
    NEWERMESSAGES = "newermessages"
    CENTERED = "centered"
    UNREADLINE = "unreadline"


class GetThreadNonblockCbMode(Enum):
    FULL = "full"
    INCREMENTAL = "incremental"


class GetThreadNonblockPgMode(Enum):
    DEFAULT = "default"
    SERVER = "server"


class PreviewLocationTyp(Enum):
    URL = "url"
    FILE = "file"
    BYTES = "bytes"


@dataclass
class PreviewLocation__URL:
    ltyp: Literal[PreviewLocationTyp.URL]
    URL: Optional[str]


@dataclass
class PreviewLocation__FILE:
    ltyp: Literal[PreviewLocationTyp.FILE]
    FILE: Optional[str]


@dataclass
class PreviewLocation__BYTES:
    ltyp: Literal[PreviewLocationTyp.BYTES]
    BYTES: Optional[bytes]


PreviewLocation = Union[
    PreviewLocation__URL, PreviewLocation__FILE, PreviewLocation__BYTES
]


class UnfurlPromptAction(Enum):
    ALWAYS = "always"
    NEVER = "never"
    ACCEPT = "accept"
    NOTNOW = "notnow"
    ONETIME = "onetime"


@dataclass
class UnfurlPromptResult__ALWAYS:
    actionType: Literal[UnfurlPromptAction.ALWAYS]
    ALWAYS: None


@dataclass
class UnfurlPromptResult__NEVER:
    actionType: Literal[UnfurlPromptAction.NEVER]
    NEVER: None


@dataclass
class UnfurlPromptResult__NOTNOW:
    actionType: Literal[UnfurlPromptAction.NOTNOW]
    NOTNOW: None


@dataclass
class UnfurlPromptResult__ACCEPT:
    actionType: Literal[UnfurlPromptAction.ACCEPT]
    ACCEPT: Optional[str]


@dataclass
class UnfurlPromptResult__ONETIME:
    actionType: Literal[UnfurlPromptAction.ONETIME]
    ONETIME: Optional[str]


UnfurlPromptResult = Union[
    UnfurlPromptResult__ALWAYS,
    UnfurlPromptResult__NEVER,
    UnfurlPromptResult__NOTNOW,
    UnfurlPromptResult__ACCEPT,
    UnfurlPromptResult__ONETIME,
]


class GalleryItemTyp(Enum):
    MEDIA = "media"
    LINK = "link"
    DOC = "doc"


@dataclass_json
@dataclass
class UserBotExtendedDescription:
    title: str = field(metadata=config(field_name="title"))
    desktop_body: str = field(metadata=config(field_name="desktop_body"))
    mobile_body: str = field(metadata=config(field_name="mobile_body"))


class ChatActivitySource(Enum):
    LOCAL = "local"
    REMOTE = "remote"


class ChatActivityType(Enum):
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


@dataclass_json
@dataclass
class TyperInfo:
    uid: keybase1.UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    device_id: keybase1.DeviceID = field(metadata=config(field_name="deviceID"))
    device_name: str = field(metadata=config(field_name="deviceName"))
    device_type: str = field(metadata=config(field_name="deviceType"))


class StaleUpdateType(Enum):
    CLEAR = "clear"
    NEWACTIVITY = "newactivity"
    CONVUPDATE = "convupdate"


class MessageBoxedVersion(Enum):
    VNONE = "vnone"
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"
    V4 = "v4"


class ChannelMention(Enum):
    NONE = "none"
    ALL = "all"
    HERE = "here"


@dataclass_json
@dataclass
class S3Params:
    bucket: str = field(metadata=config(field_name="bucket"))
    object_key: str = field(metadata=config(field_name="objectKey"))
    access_key: str = field(metadata=config(field_name="accessKey"))
    acl: str = field(metadata=config(field_name="acl"))
    region_name: str = field(metadata=config(field_name="regionName"))
    region_endpoint: str = field(metadata=config(field_name="regionEndpoint"))
    region_bucket_endpoint: str = field(
        metadata=config(field_name="regionBucketEndpoint")
    )


@dataclass_json
@dataclass
class ServerCacheVers:
    inbox_vers: int = field(metadata=config(field_name="inboxVers"))
    bodies_vers: int = field(metadata=config(field_name="bodiesVers"))


class SyncAllProtVers(Enum):
    V0 = "v0"
    V1 = "v1"


class SyncAllNotificationType(Enum):
    STATE = "state"
    INCREMENTAL = "incremental"


@dataclass
class SyncAllNotificationRes__STATE:
    typ: Literal[SyncAllNotificationType.STATE]
    STATE: Optional[gregor1.State]


@dataclass
class SyncAllNotificationRes__INCREMENTAL:
    typ: Literal[SyncAllNotificationType.INCREMENTAL]
    INCREMENTAL: Optional[gregor1.SyncResult]


SyncAllNotificationRes = Union[
    SyncAllNotificationRes__STATE, SyncAllNotificationRes__INCREMENTAL
]


class ExternalAPIKeyTyp(Enum):
    GOOGLEMAPS = "googlemaps"
    GIPHY = "giphy"


@dataclass
class ExternalAPIKey__GOOGLEMAPS:
    typ: Literal[ExternalAPIKeyTyp.GOOGLEMAPS]
    GOOGLEMAPS: Optional[str]


@dataclass
class ExternalAPIKey__GIPHY:
    typ: Literal[ExternalAPIKeyTyp.GIPHY]
    GIPHY: Optional[str]


ExternalAPIKey = Union[ExternalAPIKey__GOOGLEMAPS, ExternalAPIKey__GIPHY]

CommandConvVers = int


class BotInfoResponseTyp(Enum):
    UPTODATE = "uptodate"
    INFO = "info"


BotInfoHash = bytes


class UnfurlType(Enum):
    GENERIC = "generic"
    YOUTUBE = "youtube"
    GIPHY = "giphy"
    MAPS = "maps"


@dataclass_json
@dataclass
class UnfurlVideo:
    url: str = field(metadata=config(field_name="url"))
    mime_type: str = field(metadata=config(field_name="mimeType"))
    height: int = field(metadata=config(field_name="height"))
    width: int = field(metadata=config(field_name="width"))


@dataclass_json
@dataclass
class UnfurlYoutubeRaw:
    pass


@dataclass_json
@dataclass
class UnfurlYoutube:
    pass


@dataclass_json
@dataclass
class UnfurlImageDisplay:
    url: str = field(metadata=config(field_name="url"))
    height: int = field(metadata=config(field_name="height"))
    width: int = field(metadata=config(field_name="width"))
    is_video: bool = field(metadata=config(field_name="isVideo"))


@dataclass_json
@dataclass
class UnfurlYoutubeDisplay:
    pass


class UnfurlMode(Enum):
    ALWAYS = "always"
    NEVER = "never"
    WHITELISTED = "whitelisted"


@dataclass_json
@dataclass
class MsgFlipContent:
    text: str = field(metadata=config(field_name="text"))
    game_id: str = field(metadata=config(field_name="game_id"))
    flip_conv_id: str = field(metadata=config(field_name="flip_conv_id"))
    user_mentions: List[KnownUserMention] = field(
        metadata=config(field_name="user_mentions")
    )
    team_mentions: List[KnownTeamMention] = field(
        metadata=config(field_name="team_mentions")
    )


@dataclass_json
@dataclass
class ConvSummary:
    id: str = field(metadata=config(field_name="id"))
    channel: ChatChannel = field(metadata=config(field_name="channel"))
    unread: bool = field(metadata=config(field_name="unread"))
    active_at: int = field(metadata=config(field_name="active_at"))
    active_at_ms: int = field(metadata=config(field_name="active_at_ms"))
    member_status: str = field(metadata=config(field_name="member_status"))
    reset_users: Optional[List[str]] = field(metadata=config(field_name="reset_users"))
    finalize_info: Optional[ConversationFinalizeInfo] = field(
        metadata=config(field_name="finalize_info")
    )
    supersedes: Optional[List[str]] = field(metadata=config(field_name="supersedes"))
    superseded_by: Optional[List[str]] = field(
        metadata=config(field_name="superseded_by")
    )
    error: Optional[str] = field(metadata=config(field_name="error"))


@dataclass_json
@dataclass
class SendRes:
    message: str = field(metadata=config(field_name="message"))
    message_id: Optional[MessageID] = field(metadata=config(field_name="id"))
    outbox_id: Optional[OutboxID] = field(metadata=config(field_name="outbox_id"))
    identify_failures: Optional[List[keybase1.TLFIdentifyFailure]] = field(
        metadata=config(field_name="identify_failures")
    )
    rate_limits: Optional[List[RateLimitRes]] = field(
        metadata=config(field_name="ratelimits")
    )


@dataclass_json
@dataclass
class NewConvRes:
    id: str = field(metadata=config(field_name="id"))
    identify_failures: Optional[List[keybase1.TLFIdentifyFailure]] = field(
        metadata=config(field_name="identify_failures")
    )
    rate_limits: Optional[List[RateLimitRes]] = field(
        metadata=config(field_name="ratelimits")
    )


@dataclass_json
@dataclass
class EmptyRes:
    rate_limits: Optional[List[RateLimitRes]] = field(
        metadata=config(field_name="ratelimits")
    )


@dataclass_json
@dataclass
class UIParticipant:
    type: UIParticipantType = field(metadata=config(field_name="type"))
    assertion: str = field(metadata=config(field_name="assertion"))
    full_name: Optional[str] = field(metadata=config(field_name="fullName"))
    contact_name: Optional[str] = field(metadata=config(field_name="contactName"))


@dataclass
class UIMaybeMentionInfo__UNKNOWN:
    status: Literal[UIMaybeMentionStatus.UNKNOWN]
    UNKNOWN: None


@dataclass
class UIMaybeMentionInfo__USER:
    status: Literal[UIMaybeMentionStatus.USER]
    USER: None


@dataclass
class UIMaybeMentionInfo__TEAM:
    status: Literal[UIMaybeMentionStatus.TEAM]
    TEAM: Optional[UITeamMention]


@dataclass
class UIMaybeMentionInfo__NOTHING:
    status: Literal[UIMaybeMentionStatus.NOTHING]
    NOTHING: None


UIMaybeMentionInfo = Union[
    UIMaybeMentionInfo__UNKNOWN,
    UIMaybeMentionInfo__USER,
    UIMaybeMentionInfo__TEAM,
    UIMaybeMentionInfo__NOTHING,
]


@dataclass_json
@dataclass
class UIChatSearchConvHit:
    conv_id: str = field(metadata=config(field_name="convID"))
    team_type: TeamType = field(metadata=config(field_name="teamType"))
    name: str = field(metadata=config(field_name="name"))
    mtime: gregor1.Time = field(metadata=config(field_name="mtime"))


@dataclass_json
@dataclass
class UIChatPaymentSummary:
    xlm_total: str = field(metadata=config(field_name="xlmTotal"))
    display_total: str = field(metadata=config(field_name="displayTotal"))
    payments: List[UIChatPayment] = field(metadata=config(field_name="payments"))


@dataclass_json
@dataclass
class GiphySearchResults:
    results: List[GiphySearchResult] = field(metadata=config(field_name="results"))
    gallery_url: str = field(metadata=config(field_name="galleryUrl"))


@dataclass_json
@dataclass
class UICoinFlipAbsenteeError:
    absentees: List[UICoinFlipErrorParticipant] = field(
        metadata=config(field_name="absentees")
    )


@dataclass
class UICoinFlipResult__NUMBER:
    typ: Literal[UICoinFlipResultTyp.NUMBER]
    NUMBER: Optional[str]


@dataclass
class UICoinFlipResult__SHUFFLE:
    typ: Literal[UICoinFlipResultTyp.SHUFFLE]
    SHUFFLE: Optional[List[str]]


@dataclass
class UICoinFlipResult__DECK:
    typ: Literal[UICoinFlipResultTyp.DECK]
    DECK: Optional[List[int]]


@dataclass
class UICoinFlipResult__HANDS:
    typ: Literal[UICoinFlipResultTyp.HANDS]
    HANDS: Optional[List[UICoinFlipHand]]


@dataclass
class UICoinFlipResult__COIN:
    typ: Literal[UICoinFlipResultTyp.COIN]
    COIN: Optional[bool]


UICoinFlipResult = Union[
    UICoinFlipResult__NUMBER,
    UICoinFlipResult__SHUFFLE,
    UICoinFlipResult__DECK,
    UICoinFlipResult__HANDS,
    UICoinFlipResult__COIN,
]


@dataclass_json
@dataclass
class ConversationCommandGroupsCustom:
    commands: List[ConversationCommand] = field(metadata=config(field_name="commands"))


@dataclass_json
@dataclass
class InboxVersInfo:
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    vers: InboxVers = field(metadata=config(field_name="vers"))


@dataclass_json
@dataclass
class ConversationMember:
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))


@dataclass_json
@dataclass
class ConversationIDMessageIDPair:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    msg_id: MessageID = field(metadata=config(field_name="msgID"))


@dataclass_json
@dataclass
class ChannelNameMention:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    topic_name: str = field(metadata=config(field_name="topicName"))


@dataclass_json
@dataclass
class GetInboxQuery:
    conv_id: Optional[ConversationID] = field(metadata=config(field_name="convID"))
    topic_type: Optional[TopicType] = field(metadata=config(field_name="topicType"))
    tlf_id: Optional[TLFID] = field(metadata=config(field_name="tlfID"))
    tlf_visibility: Optional[keybase1.TLFVisibility] = field(
        metadata=config(field_name="tlfVisibility")
    )
    before: Optional[gregor1.Time] = field(metadata=config(field_name="before"))
    after: Optional[gregor1.Time] = field(metadata=config(field_name="after"))
    one_chat_type_per_tlf: Optional[bool] = field(
        metadata=config(field_name="oneChatTypePerTLF")
    )
    topic_name: Optional[str] = field(metadata=config(field_name="topicName"))
    status: List[ConversationStatus] = field(metadata=config(field_name="status"))
    member_status: List[ConversationMemberStatus] = field(
        metadata=config(field_name="memberStatus")
    )
    existences: List[ConversationExistence] = field(
        metadata=config(field_name="existences")
    )
    members_types: List[ConversationMembersType] = field(
        metadata=config(field_name="membersTypes")
    )
    conv_i_ds: List[ConversationID] = field(metadata=config(field_name="convIDs"))
    unread_only: bool = field(metadata=config(field_name="unreadOnly"))
    read_only: bool = field(metadata=config(field_name="readOnly"))
    compute_active_list: bool = field(metadata=config(field_name="computeActiveList"))
    summarize_max_msgs: bool = field(metadata=config(field_name="summarizeMaxMsgs"))
    skip_bg_loads: bool = field(metadata=config(field_name="skipBgLoads"))


@dataclass_json
@dataclass
class ConversationIDTriple:
    tlfid: TLFID = field(metadata=config(field_name="tlfid"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    topic_id: TopicID = field(metadata=config(field_name="topicID"))


@dataclass_json
@dataclass
class Expunge:
    upto: MessageID = field(metadata=config(field_name="upto"))
    basis: MessageID = field(metadata=config(field_name="basis"))


@dataclass_json
@dataclass
class ConversationReaderInfo:
    mtime: gregor1.Time = field(metadata=config(field_name="mtime"))
    read_msgid: MessageID = field(metadata=config(field_name="readMsgid"))
    max_msgid: MessageID = field(metadata=config(field_name="maxMsgid"))
    status: ConversationMemberStatus = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class ConversationSettings:
    min_writer_role_info: Optional[ConversationMinWriterRoleInfo] = field(
        metadata=config(field_name="mwr")
    )


@dataclass_json
@dataclass
class MessageSummary:
    msg_id: MessageID = field(metadata=config(field_name="msgID"))
    message_type: MessageType = field(metadata=config(field_name="messageType"))
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    tlf_public: bool = field(metadata=config(field_name="tlfPublic"))
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))


@dataclass_json
@dataclass
class Reaction:
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))
    reaction_msg_id: MessageID = field(metadata=config(field_name="reactionMsgID"))


@dataclass_json
@dataclass
class MessageServerHeader:
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    superseded_by: MessageID = field(metadata=config(field_name="supersededBy"))
    reaction_i_ds: List[MessageID] = field(metadata=config(field_name="r"))
    unfurl_i_ds: List[MessageID] = field(metadata=config(field_name="u"))
    replies: List[MessageID] = field(metadata=config(field_name="replies"))
    ctime: gregor1.Time = field(metadata=config(field_name="ctime"))
    now: gregor1.Time = field(metadata=config(field_name="n"))
    rtime: Optional[gregor1.Time] = field(metadata=config(field_name="rt"))


@dataclass_json
@dataclass
class MessagePreviousPointer:
    id: MessageID = field(metadata=config(field_name="id"))
    hash: Hash = field(metadata=config(field_name="hash"))


@dataclass_json
@dataclass
class OutboxInfo:
    prev: MessageID = field(metadata=config(field_name="prev"))
    compose_time: gregor1.Time = field(metadata=config(field_name="composeTime"))


@dataclass_json
@dataclass
class EphemeralPurgeInfo:
    conv_id: ConversationID = field(metadata=config(field_name="c"))
    is_active: bool = field(metadata=config(field_name="a"))
    next_purge_time: gregor1.Time = field(metadata=config(field_name="n"))
    min_unexploded_id: MessageID = field(metadata=config(field_name="e"))


@dataclass
class RetentionPolicy__RETAIN:
    typ: Literal[RetentionPolicyType.RETAIN]
    RETAIN: Optional[RpRetain]


@dataclass
class RetentionPolicy__EXPIRE:
    typ: Literal[RetentionPolicyType.EXPIRE]
    EXPIRE: Optional[RpExpire]


@dataclass
class RetentionPolicy__INHERIT:
    typ: Literal[RetentionPolicyType.INHERIT]
    INHERIT: Optional[RpInherit]


@dataclass
class RetentionPolicy__EPHEMERAL:
    typ: Literal[RetentionPolicyType.EPHEMERAL]
    EPHEMERAL: Optional[RpEphemeral]


RetentionPolicy = Union[
    RetentionPolicy__RETAIN,
    RetentionPolicy__EXPIRE,
    RetentionPolicy__INHERIT,
    RetentionPolicy__EPHEMERAL,
]


@dataclass_json
@dataclass
class SearchOpts:
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
    initial_pagination: Optional[Pagination] = field(
        metadata=config(field_name="initialPagination")
    )
    reindex_mode: ReIndexingMode = field(metadata=config(field_name="reindexMode"))
    max_convs_searched: int = field(metadata=config(field_name="maxConvsSearched"))
    max_convs_hit: int = field(metadata=config(field_name="maxConvsHit"))
    conv_id: Optional[ConversationID] = field(metadata=config(field_name="convID"))
    max_name_convs: int = field(metadata=config(field_name="maxNameConvs"))


@dataclass
class AssetMetadata__IMAGE:
    assetType: Literal[AssetMetadataType.IMAGE]
    IMAGE: Optional[AssetMetadataImage]


@dataclass
class AssetMetadata__VIDEO:
    assetType: Literal[AssetMetadataType.VIDEO]
    VIDEO: Optional[AssetMetadataVideo]


@dataclass
class AssetMetadata__AUDIO:
    assetType: Literal[AssetMetadataType.AUDIO]
    AUDIO: Optional[AssetMetadataAudio]


AssetMetadata = Union[AssetMetadata__IMAGE, AssetMetadata__VIDEO, AssetMetadata__AUDIO]


@dataclass_json
@dataclass
class UnreadUpdate:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    unread_messages: int = field(metadata=config(field_name="unreadMessages"))
    unread_notifying_messages: Dict[str, int] = field(
        metadata=config(field_name="unreadNotifyingMessages")
    )
    compat_unread_messages: int = field(metadata=config(field_name="UnreadMessages"))
    diff: bool = field(metadata=config(field_name="diff"))


@dataclass_json
@dataclass
class TLFFinalizeUpdate:
    finalize_info: ConversationFinalizeInfo = field(
        metadata=config(field_name="finalizeInfo")
    )
    conv_i_ds: List[ConversationID] = field(metadata=config(field_name="convIDs"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))


@dataclass_json
@dataclass
class TLFResolveUpdate:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))


@dataclass_json
@dataclass
class RemoteUserTypingUpdate:
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    device_id: gregor1.DeviceID = field(metadata=config(field_name="deviceID"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    typing: bool = field(metadata=config(field_name="typing"))


@dataclass_json
@dataclass
class ConversationUpdate:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    existence: ConversationExistence = field(metadata=config(field_name="existence"))


@dataclass_json
@dataclass
class TeamChannelUpdate:
    team_id: TLFID = field(metadata=config(field_name="teamID"))


@dataclass_json
@dataclass
class KBFSImpteamUpgradeUpdate:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))


@dataclass_json
@dataclass
class SubteamRenameUpdate:
    conv_i_ds: List[ConversationID] = field(metadata=config(field_name="convIDs"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))


@dataclass_json
@dataclass
class TextPayment:
    username: str = field(metadata=config(field_name="username"))
    payment_text: str = field(metadata=config(field_name="paymentText"))
    result: TextPaymentResult = field(metadata=config(field_name="result"))


@dataclass_json
@dataclass
class MessageEdit:
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    body: str = field(metadata=config(field_name="body"))
    user_mentions: List[KnownUserMention] = field(
        metadata=config(field_name="userMentions")
    )
    team_mentions: List[KnownTeamMention] = field(
        metadata=config(field_name="teamMentions")
    )


@dataclass_json
@dataclass
class MessageDelete:
    message_i_ds: List[MessageID] = field(metadata=config(field_name="messageIDs"))


@dataclass_json
@dataclass
class MessageFlip:
    text: str = field(metadata=config(field_name="text"))
    game_id: FlipGameID = field(metadata=config(field_name="gameID"))
    flip_conv_id: ConversationID = field(metadata=config(field_name="flipConvID"))
    user_mentions: List[KnownUserMention] = field(
        metadata=config(field_name="userMentions")
    )
    team_mentions: List[KnownTeamMention] = field(
        metadata=config(field_name="teamMentions")
    )


@dataclass_json
@dataclass
class MessagePin:
    msg_id: MessageID = field(metadata=config(field_name="msgID"))


@dataclass_json
@dataclass
class MessageDeleteHistory:
    upto: MessageID = field(metadata=config(field_name="upto"))


@dataclass_json
@dataclass
class MessageReaction:
    message_id: MessageID = field(metadata=config(field_name="m"))
    body: str = field(metadata=config(field_name="b"))


@dataclass_json
@dataclass
class SenderPrepareOptions:
    skip_topic_name_state: bool = field(
        metadata=config(field_name="skipTopicNameState")
    )
    reply_to: Optional[MessageID] = field(metadata=config(field_name="replyTo"))


@dataclass_json
@dataclass
class SenderSendOptions:
    join_mentions_as: Optional[ConversationMemberStatus] = field(
        metadata=config(field_name="joinMentionsAs")
    )


@dataclass_json
@dataclass
class OutboxStateError:
    message: str = field(metadata=config(field_name="message"))
    typ: OutboxErrorType = field(metadata=config(field_name="typ"))


@dataclass_json
@dataclass
class HeaderPlaintextUnsupported:
    mi: HeaderPlaintextMetaInfo = field(metadata=config(field_name="mi"))


@dataclass_json
@dataclass
class BodyPlaintextUnsupported:
    mi: BodyPlaintextMetaInfo = field(metadata=config(field_name="mi"))


@dataclass_json
@dataclass
class MessageUnboxedError:
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


@dataclass_json
@dataclass
class MessageUnboxedPlaceholder:
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    hidden: bool = field(metadata=config(field_name="hidden"))


@dataclass_json
@dataclass
class ConversationSettingsLocal:
    min_writer_role_info: Optional[ConversationMinWriterRoleInfoLocal] = field(
        metadata=config(field_name="minWriterRoleInfo")
    )


@dataclass_json
@dataclass
class NonblockFetchRes:
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))
    identify_failures: List[keybase1.TLFIdentifyFailure] = field(
        metadata=config(field_name="identifyFailures")
    )


@dataclass_json
@dataclass
class MessageIDControl:
    pivot: Optional[MessageID] = field(metadata=config(field_name="pivot"))
    mode: MessageIDControlMode = field(metadata=config(field_name="mode"))
    num: int = field(metadata=config(field_name="num"))


@dataclass_json
@dataclass
class UnreadlineRes:
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))
    identify_failures: List[keybase1.TLFIdentifyFailure] = field(
        metadata=config(field_name="identifyFailures")
    )
    unreadline_id: Optional[MessageID] = field(
        metadata=config(field_name="unreadlineID")
    )


@dataclass_json
@dataclass
class NameQuery:
    name: str = field(metadata=config(field_name="name"))
    tlf_id: Optional[TLFID] = field(metadata=config(field_name="tlfID"))
    members_type: ConversationMembersType = field(
        metadata=config(field_name="membersType")
    )


@dataclass_json
@dataclass
class PostLocalRes:
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    identify_failures: List[keybase1.TLFIdentifyFailure] = field(
        metadata=config(field_name="identifyFailures")
    )


@dataclass_json
@dataclass
class PostLocalNonblockRes:
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))
    outbox_id: OutboxID = field(metadata=config(field_name="outboxID"))
    identify_failures: List[keybase1.TLFIdentifyFailure] = field(
        metadata=config(field_name="identifyFailures")
    )


@dataclass_json
@dataclass
class EditTarget:
    message_id: Optional[MessageID] = field(metadata=config(field_name="messageID"))
    outbox_id: Optional[OutboxID] = field(metadata=config(field_name="outboxID"))


@dataclass_json
@dataclass
class SetConversationStatusLocalRes:
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))
    identify_failures: List[keybase1.TLFIdentifyFailure] = field(
        metadata=config(field_name="identifyFailures")
    )


@dataclass_json
@dataclass
class GetInboxSummaryForCLILocalQuery:
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    after: str = field(metadata=config(field_name="after"))
    before: str = field(metadata=config(field_name="before"))
    visibility: keybase1.TLFVisibility = field(metadata=config(field_name="visibility"))
    status: List[ConversationStatus] = field(metadata=config(field_name="status"))
    unread_first: bool = field(metadata=config(field_name="unreadFirst"))
    unread_first_limit: UnreadFirstNumLimit = field(
        metadata=config(field_name="unreadFirstLimit")
    )
    activity_sorted_limit: int = field(
        metadata=config(field_name="activitySortedLimit")
    )


@dataclass_json
@dataclass
class DownloadAttachmentLocalRes:
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))
    identify_failures: List[keybase1.TLFIdentifyFailure] = field(
        metadata=config(field_name="identifyFailures")
    )


@dataclass_json
@dataclass
class DownloadFileAttachmentLocalRes:
    filename: str = field(metadata=config(field_name="filename"))
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))
    identify_failures: List[keybase1.TLFIdentifyFailure] = field(
        metadata=config(field_name="identifyFailures")
    )


@dataclass_json
@dataclass
class MarkAsReadLocalRes:
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))


@dataclass_json
@dataclass
class JoinLeaveConversationLocalRes:
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))


@dataclass_json
@dataclass
class DeleteConversationLocalRes:
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))


@dataclass_json
@dataclass
class SetAppNotificationSettingsLocalRes:
    offline: bool = field(metadata=config(field_name="offline"))
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))


@dataclass_json
@dataclass
class AppNotificationSettingLocal:
    device_type: keybase1.DeviceType = field(metadata=config(field_name="deviceType"))
    kind: NotificationKind = field(metadata=config(field_name="kind"))
    enabled: bool = field(metadata=config(field_name="enabled"))


@dataclass_json
@dataclass
class ProfileSearchConvStats:
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


@dataclass_json
@dataclass
class BuiltinCommandGroup:
    typ: ConversationBuiltinCommandTyp = field(metadata=config(field_name="typ"))
    commands: List[ConversationCommand] = field(metadata=config(field_name="commands"))


@dataclass_json
@dataclass
class UserBotCommandOutput:
    name: str = field(metadata=config(field_name="name"))
    description: str = field(metadata=config(field_name="description"))
    usage: str = field(metadata=config(field_name="usage"))
    extended_description: Optional[UserBotExtendedDescription] = field(
        metadata=config(field_name="extended_description")
    )
    username: str = field(metadata=config(field_name="username"))


@dataclass_json
@dataclass
class UserBotCommandInput:
    name: str = field(metadata=config(field_name="name"))
    description: str = field(metadata=config(field_name="description"))
    usage: str = field(metadata=config(field_name="usage"))
    extended_description: Optional[UserBotExtendedDescription] = field(
        metadata=config(field_name="extended_description")
    )


@dataclass_json
@dataclass
class AdvertiseBotCommandsLocalRes:
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))


@dataclass_json
@dataclass
class ClearBotCommandsLocalRes:
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))


@dataclass_json
@dataclass
class PinMessageRes:
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))


@dataclass_json
@dataclass
class SetAppNotificationSettingsInfo:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    settings: ConversationNotificationInfo = field(
        metadata=config(field_name="settings")
    )


@dataclass_json
@dataclass
class MemberInfo:
    member: str = field(metadata=config(field_name="member"))
    status: ConversationMemberStatus = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class ConvTypingUpdate:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    typers: List[TyperInfo] = field(metadata=config(field_name="typers"))


@dataclass_json
@dataclass
class ConversationStaleUpdate:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    update_type: StaleUpdateType = field(metadata=config(field_name="updateType"))


@dataclass_json
@dataclass
class NewConversationRemoteRes:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    created_complex_team: bool = field(metadata=config(field_name="createdComplexTeam"))
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class MarkAsReadRes:
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class SetConversationStatusRes:
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class GetUnreadlineRemoteRes:
    unreadline_id: Optional[MessageID] = field(
        metadata=config(field_name="unreadlineID")
    )
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class JoinLeaveConversationRemoteRes:
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class DeleteConversationRemoteRes:
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class GetMessageBeforeRes:
    msg_id: MessageID = field(metadata=config(field_name="msgID"))
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class SetAppNotificationSettingsRes:
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class SetRetentionRes:
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class SetConvMinWriterRoleRes:
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class ServerNowRes:
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))
    now: gregor1.Time = field(metadata=config(field_name="now"))


@dataclass_json
@dataclass
class RemoteBotCommandsAdvertisementPublic:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))


@dataclass_json
@dataclass
class RemoteBotCommandsAdvertisementTLFID:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    tlf_id: TLFID = field(metadata=config(field_name="tlfID"))


@dataclass_json
@dataclass
class BotCommandConv:
    uid: gregor1.UID = field(metadata=config(field_name="uid"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    vers: CommandConvVers = field(metadata=config(field_name="vers"))
    mtime: gregor1.Time = field(metadata=config(field_name="mtime"))


@dataclass_json
@dataclass
class AdvertiseBotCommandsRes:
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class ClearBotCommandsRes:
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class UnfurlGenericRaw:
    title: str = field(metadata=config(field_name="title"))
    url: str = field(metadata=config(field_name="url"))
    site_name: str = field(metadata=config(field_name="siteName"))
    favicon_url: Optional[str] = field(metadata=config(field_name="faviconUrl"))
    image_url: Optional[str] = field(metadata=config(field_name="imageUrl"))
    video: Optional[UnfurlVideo] = field(metadata=config(field_name="video"))
    publish_time: Optional[int] = field(metadata=config(field_name="publishTime"))
    description: Optional[str] = field(metadata=config(field_name="description"))


@dataclass_json
@dataclass
class UnfurlGiphyRaw:
    image_url: Optional[str] = field(metadata=config(field_name="imageUrl"))
    video: Optional[UnfurlVideo] = field(metadata=config(field_name="video"))
    favicon_url: Optional[str] = field(metadata=config(field_name="faviconUrl"))


@dataclass_json
@dataclass
class UnfurlMapsRaw:
    title: str = field(metadata=config(field_name="title"))
    url: str = field(metadata=config(field_name="url"))
    site_name: str = field(metadata=config(field_name="siteName"))
    image_url: str = field(metadata=config(field_name="imageUrl"))
    history_image_url: Optional[str] = field(
        metadata=config(field_name="historyImageUrl")
    )
    description: str = field(metadata=config(field_name="description"))
    coord: Coordinate = field(metadata=config(field_name="coord"))
    time: gregor1.Time = field(metadata=config(field_name="time"))
    live_location_end_time: Optional[gregor1.Time] = field(
        metadata=config(field_name="liveLocationEndTime")
    )
    live_location_done: bool = field(metadata=config(field_name="liveLocationDone"))


@dataclass_json
@dataclass
class UnfurlGenericMapInfo:
    coord: Coordinate = field(metadata=config(field_name="coord"))
    time: gregor1.Time = field(metadata=config(field_name="time"))
    live_location_end_time: Optional[gregor1.Time] = field(
        metadata=config(field_name="liveLocationEndTime")
    )
    is_live_location_done: bool = field(
        metadata=config(field_name="isLiveLocationDone")
    )


@dataclass_json
@dataclass
class UnfurlGiphyDisplay:
    favicon: Optional[UnfurlImageDisplay] = field(metadata=config(field_name="favicon"))
    image: Optional[UnfurlImageDisplay] = field(metadata=config(field_name="image"))
    video: Optional[UnfurlImageDisplay] = field(metadata=config(field_name="video"))


@dataclass_json
@dataclass
class UnfurlSettings:
    mode: UnfurlMode = field(metadata=config(field_name="mode"))
    whitelist: Dict[str, bool] = field(metadata=config(field_name="whitelist"))


@dataclass_json
@dataclass
class UnfurlSettingsDisplay:
    mode: UnfurlMode = field(metadata=config(field_name="mode"))
    whitelist: List[str] = field(metadata=config(field_name="whitelist"))


@dataclass_json
@dataclass
class ChatList:
    conversations: List[ConvSummary] = field(
        metadata=config(field_name="conversations")
    )
    offline: bool = field(metadata=config(field_name="offline"))
    identify_failures: Optional[List[keybase1.TLFIdentifyFailure]] = field(
        metadata=config(field_name="identify_failures")
    )
    pagination: Optional[Pagination] = field(metadata=config(field_name="pagination"))
    rate_limits: Optional[List[RateLimitRes]] = field(
        metadata=config(field_name="ratelimits")
    )


@dataclass_json
@dataclass
class ListCommandsRes:
    commands: List[UserBotCommandOutput] = field(metadata=config(field_name="commands"))
    rate_limits: Optional[List[RateLimitRes]] = field(
        metadata=config(field_name="ratelimits")
    )


@dataclass_json
@dataclass
class AdvertiseCommandAPIParam:
    typ: str = field(metadata=config(field_name="type"))
    commands: List[UserBotCommandInput] = field(metadata=config(field_name="commands"))
    team_name: Optional[str] = field(metadata=config(field_name="team_name"))


@dataclass
class UITextDecoration__PAYMENT:
    typ: Literal[UITextDecorationTyp.PAYMENT]
    PAYMENT: Optional[TextPayment]


@dataclass
class UITextDecoration__ATMENTION:
    typ: Literal[UITextDecorationTyp.ATMENTION]
    ATMENTION: Optional[str]


@dataclass
class UITextDecoration__CHANNELNAMEMENTION:
    typ: Literal[UITextDecorationTyp.CHANNELNAMEMENTION]
    CHANNELNAMEMENTION: Optional[UIChannelNameMention]


@dataclass
class UITextDecoration__MAYBEMENTION:
    typ: Literal[UITextDecorationTyp.MAYBEMENTION]
    MAYBEMENTION: Optional[MaybeMention]


@dataclass
class UITextDecoration__LINK:
    typ: Literal[UITextDecorationTyp.LINK]
    LINK: Optional[UILinkDecoration]


@dataclass
class UITextDecoration__MAILTO:
    typ: Literal[UITextDecorationTyp.MAILTO]
    MAILTO: Optional[UILinkDecoration]


@dataclass
class UITextDecoration__KBFSPATH:
    typ: Literal[UITextDecorationTyp.KBFSPATH]
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


@dataclass_json
@dataclass
class UIChatSearchConvHits:
    hits: List[UIChatSearchConvHit] = field(metadata=config(field_name="hits"))
    unread_matches: bool = field(metadata=config(field_name="unreadMatches"))


@dataclass
class UICoinFlipError__GENERIC:
    typ: Literal[UICoinFlipErrorTyp.GENERIC]
    GENERIC: Optional[str]


@dataclass
class UICoinFlipError__ABSENTEE:
    typ: Literal[UICoinFlipErrorTyp.ABSENTEE]
    ABSENTEE: Optional[UICoinFlipAbsenteeError]


@dataclass
class UICoinFlipError__TIMEOUT:
    typ: Literal[UICoinFlipErrorTyp.TIMEOUT]
    TIMEOUT: None


@dataclass
class UICoinFlipError__ABORTED:
    typ: Literal[UICoinFlipErrorTyp.ABORTED]
    ABORTED: None


@dataclass
class UICoinFlipError__DUPREG:
    typ: Literal[UICoinFlipErrorTyp.DUPREG]
    DUPREG: Optional[UICoinFlipErrorParticipant]


@dataclass
class UICoinFlipError__DUPCOMMITCOMPLETE:
    typ: Literal[UICoinFlipErrorTyp.DUPCOMMITCOMPLETE]
    DUPCOMMITCOMPLETE: Optional[UICoinFlipErrorParticipant]


@dataclass
class UICoinFlipError__DUPREVEAL:
    typ: Literal[UICoinFlipErrorTyp.DUPREVEAL]
    DUPREVEAL: Optional[UICoinFlipErrorParticipant]


@dataclass
class UICoinFlipError__COMMITMISMATCH:
    typ: Literal[UICoinFlipErrorTyp.COMMITMISMATCH]
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
class ConversationCommandGroups__BUILTIN:
    typ: Literal[ConversationCommandGroupsTyp.BUILTIN]
    BUILTIN: Optional[ConversationBuiltinCommandTyp]


@dataclass
class ConversationCommandGroups__CUSTOM:
    typ: Literal[ConversationCommandGroupsTyp.CUSTOM]
    CUSTOM: Optional[ConversationCommandGroupsCustom]


@dataclass
class ConversationCommandGroups__NONE:
    typ: Literal[ConversationCommandGroupsTyp.NONE]
    NONE: None


ConversationCommandGroups = Union[
    ConversationCommandGroups__BUILTIN,
    ConversationCommandGroups__CUSTOM,
    ConversationCommandGroups__NONE,
]


@dataclass_json
@dataclass
class ConversationIDMessageIDPairs:
    pairs: List[ConversationIDMessageIDPair] = field(
        metadata=config(field_name="pairs")
    )


@dataclass_json
@dataclass
class ReactionMap:
    reactions: Dict[str, Dict[str, Reaction]] = field(
        metadata=config(field_name="reactions")
    )


@dataclass_json
@dataclass
class MessageClientHeader:
    conv: ConversationIDTriple = field(metadata=config(field_name="conv"))
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    tlf_public: bool = field(metadata=config(field_name="tlfPublic"))
    message_type: MessageType = field(metadata=config(field_name="messageType"))
    supersedes: MessageID = field(metadata=config(field_name="supersedes"))
    kbfs_crypt_keys_used: Optional[bool] = field(
        metadata=config(field_name="kbfsCryptKeysUsed")
    )
    deletes: List[MessageID] = field(metadata=config(field_name="deletes"))
    prev: List[MessagePreviousPointer] = field(metadata=config(field_name="prev"))
    delete_history: Optional[MessageDeleteHistory] = field(
        metadata=config(field_name="deleteHistory")
    )
    sender: gregor1.UID = field(metadata=config(field_name="sender"))
    sender_device: gregor1.DeviceID = field(metadata=config(field_name="senderDevice"))
    merkle_root: Optional[MerkleRoot] = field(metadata=config(field_name="merkleRoot"))
    outbox_id: Optional[OutboxID] = field(metadata=config(field_name="outboxID"))
    outbox_info: Optional[OutboxInfo] = field(metadata=config(field_name="outboxInfo"))
    ephemeral_metadata: Optional[MsgEphemeralMetadata] = field(
        metadata=config(field_name="em")
    )
    pairwise_macs: Dict[str, bytes] = field(metadata=config(field_name="pm"))
    bot_uid: Optional[gregor1.UID] = field(metadata=config(field_name="b"))


@dataclass_json
@dataclass
class MessageClientHeaderVerified:
    conv: ConversationIDTriple = field(metadata=config(field_name="conv"))
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    tlf_public: bool = field(metadata=config(field_name="tlfPublic"))
    message_type: MessageType = field(metadata=config(field_name="messageType"))
    prev: List[MessagePreviousPointer] = field(metadata=config(field_name="prev"))
    sender: gregor1.UID = field(metadata=config(field_name="sender"))
    sender_device: gregor1.DeviceID = field(metadata=config(field_name="senderDevice"))
    kbfs_crypt_keys_used: Optional[bool] = field(
        metadata=config(field_name="kbfsCryptKeysUsed")
    )
    merkle_root: Optional[MerkleRoot] = field(metadata=config(field_name="merkleRoot"))
    outbox_id: Optional[OutboxID] = field(metadata=config(field_name="outboxID"))
    outbox_info: Optional[OutboxInfo] = field(metadata=config(field_name="outboxInfo"))
    ephemeral_metadata: Optional[MsgEphemeralMetadata] = field(
        metadata=config(field_name="em")
    )
    rtime: gregor1.Time = field(metadata=config(field_name="rt"))
    has_pairwise_macs: bool = field(metadata=config(field_name="pm"))
    bot_uid: Optional[gregor1.UID] = field(metadata=config(field_name="b"))


@dataclass_json
@dataclass
class Asset:
    filename: str = field(metadata=config(field_name="filename"))
    region: str = field(metadata=config(field_name="region"))
    endpoint: str = field(metadata=config(field_name="endpoint"))
    bucket: str = field(metadata=config(field_name="bucket"))
    path: str = field(metadata=config(field_name="path"))
    size: int = field(metadata=config(field_name="size"))
    mime_type: str = field(metadata=config(field_name="mimeType"))
    enc_hash: Hash = field(metadata=config(field_name="encHash"))
    key: bytes = field(metadata=config(field_name="key"))
    verify_key: bytes = field(metadata=config(field_name="verifyKey"))
    title: str = field(metadata=config(field_name="title"))
    nonce: bytes = field(metadata=config(field_name="nonce"))
    metadata: AssetMetadata = field(metadata=config(field_name="metadata"))
    tag: AssetTag = field(metadata=config(field_name="tag"))


@dataclass_json
@dataclass
class GenericPayload:
    action: str = field(metadata=config(field_name="Action"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        metadata=config(field_name="unreadUpdate")
    )


@dataclass_json
@dataclass
class NewConversationPayload:
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        metadata=config(field_name="unreadUpdate")
    )


@dataclass_json
@dataclass
class ReadMessagePayload:
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    msg_id: MessageID = field(metadata=config(field_name="msgID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        metadata=config(field_name="unreadUpdate")
    )


@dataclass_json
@dataclass
class SetStatusPayload:
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    status: ConversationStatus = field(metadata=config(field_name="status"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        metadata=config(field_name="unreadUpdate")
    )


@dataclass_json
@dataclass
class TeamTypePayload:
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    team_type: TeamType = field(metadata=config(field_name="teamType"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        metadata=config(field_name="unreadUpdate")
    )


@dataclass_json
@dataclass
class SetAppNotificationSettingsPayload:
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    settings: ConversationNotificationInfo = field(
        metadata=config(field_name="settings")
    )
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        metadata=config(field_name="unreadUpdate")
    )


@dataclass_json
@dataclass
class ExpungePayload:
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    expunge: Expunge = field(metadata=config(field_name="expunge"))
    max_msgs: List[MessageSummary] = field(metadata=config(field_name="maxMsgs"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        metadata=config(field_name="unreadUpdate")
    )


@dataclass_json
@dataclass
class UpdateConversationMembership:
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    joined: List[ConversationMember] = field(metadata=config(field_name="joined"))
    removed: List[ConversationMember] = field(metadata=config(field_name="removed"))
    reset: List[ConversationMember] = field(metadata=config(field_name="reset"))
    previewed: List[ConversationID] = field(metadata=config(field_name="previewed"))
    unread_update: Optional[UnreadUpdate] = field(
        metadata=config(field_name="unreadUpdate")
    )
    unread_updates: List[UnreadUpdate] = field(
        metadata=config(field_name="unreadUpdates")
    )


@dataclass_json
@dataclass
class UpdateConversations:
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    conv_updates: List[ConversationUpdate] = field(
        metadata=config(field_name="convUpdates")
    )


@dataclass_json
@dataclass
class SetConvRetentionUpdate:
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    policy: RetentionPolicy = field(metadata=config(field_name="policy"))


@dataclass_json
@dataclass
class SetTeamRetentionUpdate:
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    team_id: keybase1.TeamID = field(metadata=config(field_name="teamID"))
    policy: RetentionPolicy = field(metadata=config(field_name="policy"))


@dataclass_json
@dataclass
class SetConvSettingsUpdate:
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    conv_settings: Optional[ConversationSettings] = field(
        metadata=config(field_name="convSettings")
    )


@dataclass_json
@dataclass
class MessageText:
    body: str = field(metadata=config(field_name="body"))
    payments: List[TextPayment] = field(metadata=config(field_name="payments"))
    reply_to: Optional[MessageID] = field(metadata=config(field_name="replyTo"))
    reply_to_uid: Optional[gregor1.UID] = field(
        metadata=config(field_name="replyToUID")
    )
    user_mentions: List[KnownUserMention] = field(
        metadata=config(field_name="userMentions")
    )
    team_mentions: List[KnownTeamMention] = field(
        metadata=config(field_name="teamMentions")
    )
    live_location: Optional[LiveLocation] = field(
        metadata=config(field_name="liveLocation")
    )


@dataclass_json
@dataclass
class MessageSystemChangeRetention:
    is_team: bool = field(metadata=config(field_name="isTeam"))
    is_inherit: bool = field(metadata=config(field_name="isInherit"))
    members_type: ConversationMembersType = field(
        metadata=config(field_name="membersType")
    )
    policy: RetentionPolicy = field(metadata=config(field_name="policy"))
    user: str = field(metadata=config(field_name="user"))


@dataclass
class OutboxState__SENDING:
    state: Literal[OutboxStateType.SENDING]
    SENDING: Optional[int]


@dataclass
class OutboxState__ERROR:
    state: Literal[OutboxStateType.ERROR]
    ERROR: Optional[OutboxStateError]


OutboxState = Union[OutboxState__SENDING, OutboxState__ERROR]


@dataclass_json
@dataclass
class HeaderPlaintextV1:
    conv: ConversationIDTriple = field(metadata=config(field_name="conv"))
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    tlf_public: bool = field(metadata=config(field_name="tlfPublic"))
    message_type: MessageType = field(metadata=config(field_name="messageType"))
    prev: List[MessagePreviousPointer] = field(metadata=config(field_name="prev"))
    sender: gregor1.UID = field(metadata=config(field_name="sender"))
    sender_device: gregor1.DeviceID = field(metadata=config(field_name="senderDevice"))
    kbfs_crypt_keys_used: Optional[bool] = field(
        metadata=config(field_name="kbfsCryptKeysUsed")
    )
    body_hash: Hash = field(metadata=config(field_name="bodyHash"))
    outbox_info: Optional[OutboxInfo] = field(metadata=config(field_name="outboxInfo"))
    outbox_id: Optional[OutboxID] = field(metadata=config(field_name="outboxID"))
    header_signature: Optional[SignatureInfo] = field(
        metadata=config(field_name="headerSignature")
    )
    merkle_root: Optional[MerkleRoot] = field(metadata=config(field_name="merkleRoot"))
    ephemeral_metadata: Optional[MsgEphemeralMetadata] = field(
        metadata=config(field_name="em")
    )
    bot_uid: Optional[gregor1.UID] = field(metadata=config(field_name="b"))


@dataclass_json
@dataclass
class GetThreadQuery:
    mark_as_read: bool = field(metadata=config(field_name="markAsRead"))
    message_types: List[MessageType] = field(metadata=config(field_name="messageTypes"))
    disable_resolve_supersedes: bool = field(
        metadata=config(field_name="disableResolveSupersedes")
    )
    enable_delete_placeholders: bool = field(
        metadata=config(field_name="enableDeletePlaceholders")
    )
    disable_post_process_thread: bool = field(
        metadata=config(field_name="disablePostProcessThread")
    )
    before: Optional[gregor1.Time] = field(metadata=config(field_name="before"))
    after: Optional[gregor1.Time] = field(metadata=config(field_name="after"))
    message_id_control: Optional[MessageIDControl] = field(
        metadata=config(field_name="messageIDControl")
    )


@dataclass_json
@dataclass
class GetInboxLocalQuery:
    name: Optional[NameQuery] = field(metadata=config(field_name="name"))
    topic_name: Optional[str] = field(metadata=config(field_name="topicName"))
    conv_i_ds: List[ConversationID] = field(metadata=config(field_name="convIDs"))
    topic_type: Optional[TopicType] = field(metadata=config(field_name="topicType"))
    tlf_visibility: Optional[keybase1.TLFVisibility] = field(
        metadata=config(field_name="tlfVisibility")
    )
    before: Optional[gregor1.Time] = field(metadata=config(field_name="before"))
    after: Optional[gregor1.Time] = field(metadata=config(field_name="after"))
    one_chat_type_per_tlf: Optional[bool] = field(
        metadata=config(field_name="oneChatTypePerTLF")
    )
    status: List[ConversationStatus] = field(metadata=config(field_name="status"))
    member_status: List[ConversationMemberStatus] = field(
        metadata=config(field_name="memberStatus")
    )
    unread_only: bool = field(metadata=config(field_name="unreadOnly"))
    read_only: bool = field(metadata=config(field_name="readOnly"))
    compute_active_list: bool = field(metadata=config(field_name="computeActiveList"))


@dataclass_json
@dataclass
class MakePreviewRes:
    mime_type: str = field(metadata=config(field_name="mimeType"))
    preview_mime_type: Optional[str] = field(
        metadata=config(field_name="previewMimeType")
    )
    location: Optional[PreviewLocation] = field(metadata=config(field_name="location"))
    metadata: Optional[AssetMetadata] = field(metadata=config(field_name="metadata"))
    base_metadata: Optional[AssetMetadata] = field(
        metadata=config(field_name="baseMetadata")
    )


@dataclass_json
@dataclass
class StaticConfig:
    deletable_by_delete_history: List[MessageType] = field(
        metadata=config(field_name="deletableByDeleteHistory")
    )
    builtin_commands: List[BuiltinCommandGroup] = field(
        metadata=config(field_name="builtinCommands")
    )


@dataclass_json
@dataclass
class AdvertiseCommandsParam:
    typ: BotCommandsAdvertisementTyp = field(metadata=config(field_name="typ"))
    commands: List[UserBotCommandInput] = field(metadata=config(field_name="commands"))
    team_name: Optional[str] = field(metadata=config(field_name="teamName"))


@dataclass_json
@dataclass
class ListBotCommandsLocalRes:
    commands: List[UserBotCommandOutput] = field(metadata=config(field_name="commands"))
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))


@dataclass_json
@dataclass
class MembersUpdateInfo:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    members: List[MemberInfo] = field(metadata=config(field_name="members"))


@dataclass_json
@dataclass
class ExpungeInfo:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    expunge: Expunge = field(metadata=config(field_name="expunge"))


@dataclass_json
@dataclass
class PostRemoteRes:
    msg_header: MessageServerHeader = field(metadata=config(field_name="msgHeader"))
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class UnreadUpdateFull:
    ignore: bool = field(metadata=config(field_name="ignore"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    inbox_sync_status: SyncInboxResType = field(
        metadata=config(field_name="inboxSyncStatus")
    )
    updates: List[UnreadUpdate] = field(metadata=config(field_name="updates"))


@dataclass_json
@dataclass
class SweepRes:
    found_task: bool = field(metadata=config(field_name="foundTask"))
    deleted_messages: bool = field(metadata=config(field_name="deletedMessages"))
    expunge: Expunge = field(metadata=config(field_name="expunge"))


@dataclass
class RemoteBotCommandsAdvertisement__PUBLIC:
    typ: Literal[BotCommandsAdvertisementTyp.PUBLIC]
    PUBLIC: Optional[RemoteBotCommandsAdvertisementPublic]


@dataclass
class RemoteBotCommandsAdvertisement__TLFID_MEMBERS:
    typ: Literal[BotCommandsAdvertisementTyp.TLFID_MEMBERS]
    TLFID_MEMBERS: Optional[RemoteBotCommandsAdvertisementTLFID]


@dataclass
class RemoteBotCommandsAdvertisement__TLFID_CONVS:
    typ: Literal[BotCommandsAdvertisementTyp.TLFID_CONVS]
    TLFID_CONVS: Optional[RemoteBotCommandsAdvertisementTLFID]


RemoteBotCommandsAdvertisement = Union[
    RemoteBotCommandsAdvertisement__PUBLIC,
    RemoteBotCommandsAdvertisement__TLFID_MEMBERS,
    RemoteBotCommandsAdvertisement__TLFID_CONVS,
]


@dataclass_json
@dataclass
class BotInfo:
    command_convs: List[BotCommandConv] = field(
        metadata=config(field_name="commandConvs")
    )


@dataclass
class UnfurlRaw__GENERIC:
    unfurlType: Literal[UnfurlType.GENERIC]
    GENERIC: Optional[UnfurlGenericRaw]


@dataclass
class UnfurlRaw__YOUTUBE:
    unfurlType: Literal[UnfurlType.YOUTUBE]
    YOUTUBE: Optional[UnfurlYoutubeRaw]


@dataclass
class UnfurlRaw__GIPHY:
    unfurlType: Literal[UnfurlType.GIPHY]
    GIPHY: Optional[UnfurlGiphyRaw]


@dataclass
class UnfurlRaw__MAPS:
    unfurlType: Literal[UnfurlType.MAPS]
    MAPS: Optional[UnfurlMapsRaw]


UnfurlRaw = Union[
    UnfurlRaw__GENERIC, UnfurlRaw__YOUTUBE, UnfurlRaw__GIPHY, UnfurlRaw__MAPS
]


@dataclass_json
@dataclass
class UnfurlGenericDisplay:
    title: str = field(metadata=config(field_name="title"))
    url: str = field(metadata=config(field_name="url"))
    site_name: str = field(metadata=config(field_name="siteName"))
    favicon: Optional[UnfurlImageDisplay] = field(metadata=config(field_name="favicon"))
    media: Optional[UnfurlImageDisplay] = field(metadata=config(field_name="media"))
    publish_time: Optional[int] = field(metadata=config(field_name="publishTime"))
    description: Optional[str] = field(metadata=config(field_name="description"))
    map_info: Optional[UnfurlGenericMapInfo] = field(
        metadata=config(field_name="mapInfo")
    )


@dataclass_json
@dataclass
class UICoinFlipStatus:
    game_id: str = field(metadata=config(field_name="gameID"))
    phase: UICoinFlipPhase = field(metadata=config(field_name="phase"))
    progress_text: str = field(metadata=config(field_name="progressText"))
    result_text: str = field(metadata=config(field_name="resultText"))
    commitment_visualization: str = field(
        metadata=config(field_name="commitmentVisualization")
    )
    reveal_visualization: str = field(metadata=config(field_name="revealVisualization"))
    participants: List[UICoinFlipParticipant] = field(
        metadata=config(field_name="participants")
    )
    error_info: Optional[UICoinFlipError] = field(
        metadata=config(field_name="errorInfo")
    )
    result_info: Optional[UICoinFlipResult] = field(
        metadata=config(field_name="resultInfo")
    )


@dataclass
class MessageSystem__ADDEDTOTEAM:
    systemType: Literal[MessageSystemType.ADDEDTOTEAM]
    ADDEDTOTEAM: Optional[MessageSystemAddedToTeam]


@dataclass
class MessageSystem__INVITEADDEDTOTEAM:
    systemType: Literal[MessageSystemType.INVITEADDEDTOTEAM]
    INVITEADDEDTOTEAM: Optional[MessageSystemInviteAddedToTeam]


@dataclass
class MessageSystem__COMPLEXTEAM:
    systemType: Literal[MessageSystemType.COMPLEXTEAM]
    COMPLEXTEAM: Optional[MessageSystemComplexTeam]


@dataclass
class MessageSystem__CREATETEAM:
    systemType: Literal[MessageSystemType.CREATETEAM]
    CREATETEAM: Optional[MessageSystemCreateTeam]


@dataclass
class MessageSystem__GITPUSH:
    systemType: Literal[MessageSystemType.GITPUSH]
    GITPUSH: Optional[MessageSystemGitPush]


@dataclass
class MessageSystem__CHANGEAVATAR:
    systemType: Literal[MessageSystemType.CHANGEAVATAR]
    CHANGEAVATAR: Optional[MessageSystemChangeAvatar]


@dataclass
class MessageSystem__CHANGERETENTION:
    systemType: Literal[MessageSystemType.CHANGERETENTION]
    CHANGERETENTION: Optional[MessageSystemChangeRetention]


@dataclass
class MessageSystem__BULKADDTOCONV:
    systemType: Literal[MessageSystemType.BULKADDTOCONV]
    BULKADDTOCONV: Optional[MessageSystemBulkAddToConv]


MessageSystem = Union[
    MessageSystem__ADDEDTOTEAM,
    MessageSystem__INVITEADDEDTOTEAM,
    MessageSystem__COMPLEXTEAM,
    MessageSystem__CREATETEAM,
    MessageSystem__GITPUSH,
    MessageSystem__CHANGEAVATAR,
    MessageSystem__CHANGERETENTION,
    MessageSystem__BULKADDTOCONV,
]


@dataclass_json
@dataclass
class MessageAttachment:
    object: Asset = field(metadata=config(field_name="object"))
    preview: Optional[Asset] = field(metadata=config(field_name="preview"))
    previews: List[Asset] = field(metadata=config(field_name="previews"))
    metadata: bytes = field(metadata=config(field_name="metadata"))
    uploaded: bool = field(metadata=config(field_name="uploaded"))


@dataclass_json
@dataclass
class MessageAttachmentUploaded:
    message_id: MessageID = field(metadata=config(field_name="messageID"))
    object: Asset = field(metadata=config(field_name="object"))
    previews: List[Asset] = field(metadata=config(field_name="previews"))
    metadata: bytes = field(metadata=config(field_name="metadata"))


@dataclass
class HeaderPlaintext__V1:
    version: Literal[HeaderPlaintextVersion.V1]
    V1: Optional[HeaderPlaintextV1]


@dataclass
class HeaderPlaintext__V2:
    version: Literal[HeaderPlaintextVersion.V2]
    V2: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V3:
    version: Literal[HeaderPlaintextVersion.V3]
    V3: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V4:
    version: Literal[HeaderPlaintextVersion.V4]
    V4: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V5:
    version: Literal[HeaderPlaintextVersion.V5]
    V5: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V6:
    version: Literal[HeaderPlaintextVersion.V6]
    V6: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V7:
    version: Literal[HeaderPlaintextVersion.V7]
    V7: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V8:
    version: Literal[HeaderPlaintextVersion.V8]
    V8: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V9:
    version: Literal[HeaderPlaintextVersion.V9]
    V9: Optional[HeaderPlaintextUnsupported]


@dataclass
class HeaderPlaintext__V10:
    version: Literal[HeaderPlaintextVersion.V10]
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


@dataclass_json
@dataclass
class PostFileAttachmentArg:
    conversation_id: ConversationID = field(
        metadata=config(field_name="conversationID")
    )
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    visibility: keybase1.TLFVisibility = field(metadata=config(field_name="visibility"))
    filename: str = field(metadata=config(field_name="filename"))
    title: str = field(metadata=config(field_name="title"))
    metadata: bytes = field(metadata=config(field_name="metadata"))
    identify_behavior: keybase1.TLFIdentifyBehavior = field(
        metadata=config(field_name="identifyBehavior")
    )
    caller_preview: Optional[MakePreviewRes] = field(
        metadata=config(field_name="callerPreview")
    )
    outbox_id: Optional[OutboxID] = field(metadata=config(field_name="outboxID"))
    ephemeral_lifetime: Optional[gregor1.DurationSec] = field(
        metadata=config(field_name="ephemeralLifetime")
    )


@dataclass_json
@dataclass
class ReactionUpdate:
    reactions: ReactionMap = field(metadata=config(field_name="reactions"))
    target_msg_id: MessageID = field(metadata=config(field_name="targetMsgID"))


@dataclass_json
@dataclass
class MessageBoxed:
    version: MessageBoxedVersion = field(metadata=config(field_name="version"))
    server_header: Optional[MessageServerHeader] = field(
        metadata=config(field_name="serverHeader")
    )
    client_header: MessageClientHeader = field(
        metadata=config(field_name="clientHeader")
    )
    header_ciphertext: SealedData = field(
        metadata=config(field_name="headerCiphertext")
    )
    body_ciphertext: EncryptedData = field(metadata=config(field_name="bodyCiphertext"))
    verify_key: bytes = field(metadata=config(field_name="verifyKey"))
    key_generation: int = field(metadata=config(field_name="keyGeneration"))


@dataclass
class BotInfoResponse__UPTODATE:
    typ: Literal[BotInfoResponseTyp.UPTODATE]
    UPTODATE: None


@dataclass
class BotInfoResponse__INFO:
    typ: Literal[BotInfoResponseTyp.INFO]
    INFO: Optional[BotInfo]


BotInfoResponse = Union[BotInfoResponse__UPTODATE, BotInfoResponse__INFO]


@dataclass_json
@dataclass
class UnfurlGeneric:
    title: str = field(metadata=config(field_name="title"))
    url: str = field(metadata=config(field_name="url"))
    site_name: str = field(metadata=config(field_name="siteName"))
    favicon: Optional[Asset] = field(metadata=config(field_name="favicon"))
    image: Optional[Asset] = field(metadata=config(field_name="image"))
    publish_time: Optional[int] = field(metadata=config(field_name="publishTime"))
    description: Optional[str] = field(metadata=config(field_name="description"))
    map_info: Optional[UnfurlGenericMapInfo] = field(
        metadata=config(field_name="mapInfo")
    )


@dataclass_json
@dataclass
class UnfurlGiphy:
    favicon: Optional[Asset] = field(metadata=config(field_name="favicon"))
    image: Optional[Asset] = field(metadata=config(field_name="image"))
    video: Optional[Asset] = field(metadata=config(field_name="video"))


@dataclass
class UnfurlDisplay__GENERIC:
    unfurlType: Literal[UnfurlType.GENERIC]
    GENERIC: Optional[UnfurlGenericDisplay]


@dataclass
class UnfurlDisplay__YOUTUBE:
    unfurlType: Literal[UnfurlType.YOUTUBE]
    YOUTUBE: Optional[UnfurlYoutubeDisplay]


@dataclass
class UnfurlDisplay__GIPHY:
    unfurlType: Literal[UnfurlType.GIPHY]
    GIPHY: Optional[UnfurlGiphyDisplay]


UnfurlDisplay = Union[
    UnfurlDisplay__GENERIC, UnfurlDisplay__YOUTUBE, UnfurlDisplay__GIPHY
]


@dataclass_json
@dataclass
class UIMessageUnfurlInfo:
    unfurl_message_id: MessageID = field(metadata=config(field_name="unfurlMessageID"))
    url: str = field(metadata=config(field_name="url"))
    unfurl: UnfurlDisplay = field(metadata=config(field_name="unfurl"))
    is_collapsed: bool = field(metadata=config(field_name="isCollapsed"))


@dataclass_json
@dataclass
class NewMessagePayload:
    action: str = field(metadata=config(field_name="Action"))
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    message: MessageBoxed = field(metadata=config(field_name="message"))
    inbox_vers: InboxVers = field(metadata=config(field_name="inboxVers"))
    topic_type: TopicType = field(metadata=config(field_name="topicType"))
    unread_update: Optional[UnreadUpdate] = field(
        metadata=config(field_name="unreadUpdate")
    )
    max_msgs: List[MessageSummary] = field(metadata=config(field_name="maxMsgs"))


@dataclass_json
@dataclass
class LoadFlipRes:
    status: UICoinFlipStatus = field(metadata=config(field_name="status"))
    rate_limits: List[RateLimit] = field(metadata=config(field_name="rateLimits"))
    identify_failures: List[keybase1.TLFIdentifyFailure] = field(
        metadata=config(field_name="identifyFailures")
    )


@dataclass_json
@dataclass
class ReactionUpdateNotif:
    conv_id: ConversationID = field(metadata=config(field_name="convID"))
    user_reacjis: keybase1.UserReacjis = field(
        metadata=config(field_name="userReacjis")
    )
    reaction_updates: List[ReactionUpdate] = field(
        metadata=config(field_name="reactionUpdates")
    )


@dataclass_json
@dataclass
class ThreadViewBoxed:
    messages: List[MessageBoxed] = field(metadata=config(field_name="messages"))
    pagination: Optional[Pagination] = field(metadata=config(field_name="pagination"))


@dataclass_json
@dataclass
class GetMessagesRemoteRes:
    msgs: List[MessageBoxed] = field(metadata=config(field_name="msgs"))
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class GetBotInfoRes:
    response: BotInfoResponse = field(metadata=config(field_name="response"))
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass
class Unfurl__GENERIC:
    unfurlType: Literal[UnfurlType.GENERIC]
    GENERIC: Optional[UnfurlGeneric]


@dataclass
class Unfurl__YOUTUBE:
    unfurlType: Literal[UnfurlType.YOUTUBE]
    YOUTUBE: Optional[UnfurlYoutube]


@dataclass
class Unfurl__GIPHY:
    unfurlType: Literal[UnfurlType.GIPHY]
    GIPHY: Optional[UnfurlGiphy]


Unfurl = Union[Unfurl__GENERIC, Unfurl__YOUTUBE, Unfurl__GIPHY]


@dataclass_json
@dataclass
class GetThreadRemoteRes:
    thread: ThreadViewBoxed = field(metadata=config(field_name="thread"))
    members_type: ConversationMembersType = field(
        metadata=config(field_name="membersType")
    )
    visibility: keybase1.TLFVisibility = field(metadata=config(field_name="visibility"))
    rate_limit: Optional[RateLimit] = field(metadata=config(field_name="rateLimit"))


@dataclass_json
@dataclass
class UnfurlResult:
    unfurl: Unfurl = field(metadata=config(field_name="unfurl"))
    url: str = field(metadata=config(field_name="url"))


@dataclass_json
@dataclass
class MessageUnfurl:
    unfurl: UnfurlResult = field(metadata=config(field_name="unfurl"))
    message_id: MessageID = field(metadata=config(field_name="messageID"))


@dataclass_json
@dataclass
class MsgContent:
    type_name: str = field(metadata=config(field_name="type"))
    text: Optional[MessageText] = field(metadata=config(field_name="text"))
    attachment: Optional[MessageAttachment] = field(
        metadata=config(field_name="attachment")
    )
    edit: Optional[MessageEdit] = field(metadata=config(field_name="edit"))
    reaction: Optional[MessageReaction] = field(metadata=config(field_name="reaction"))
    delete: Optional[MessageDelete] = field(metadata=config(field_name="delete"))
    metadata: Optional[MessageConversationMetadata] = field(
        metadata=config(field_name="metadata")
    )
    headline: Optional[MessageHeadline] = field(metadata=config(field_name="headline"))
    attachment_uploaded: Optional[MessageAttachmentUploaded] = field(
        metadata=config(field_name="attachment_uploaded")
    )
    system: Optional[MessageSystem] = field(metadata=config(field_name="system"))
    send_payment: Optional[MessageSendPayment] = field(
        metadata=config(field_name="send_payment")
    )
    request_payment: Optional[MessageRequestPayment] = field(
        metadata=config(field_name="request_payment")
    )
    unfurl: Optional[MessageUnfurl] = field(metadata=config(field_name="unfurl"))
    flip: Optional[MsgFlipContent] = field(metadata=config(field_name="flip"))


@dataclass
class MessageBody__TEXT:
    messageType: Literal[MessageType.TEXT]
    TEXT: Optional[MessageText]


@dataclass
class MessageBody__ATTACHMENT:
    messageType: Literal[MessageType.ATTACHMENT]
    ATTACHMENT: Optional[MessageAttachment]


@dataclass
class MessageBody__EDIT:
    messageType: Literal[MessageType.EDIT]
    EDIT: Optional[MessageEdit]


@dataclass
class MessageBody__DELETE:
    messageType: Literal[MessageType.DELETE]
    DELETE: Optional[MessageDelete]


@dataclass
class MessageBody__METADATA:
    messageType: Literal[MessageType.METADATA]
    METADATA: Optional[MessageConversationMetadata]


@dataclass
class MessageBody__HEADLINE:
    messageType: Literal[MessageType.HEADLINE]
    HEADLINE: Optional[MessageHeadline]


@dataclass
class MessageBody__ATTACHMENTUPLOADED:
    messageType: Literal[MessageType.ATTACHMENTUPLOADED]
    ATTACHMENTUPLOADED: Optional[MessageAttachmentUploaded]


@dataclass
class MessageBody__JOIN:
    messageType: Literal[MessageType.JOIN]
    JOIN: Optional[MessageJoin]


@dataclass
class MessageBody__LEAVE:
    messageType: Literal[MessageType.LEAVE]
    LEAVE: Optional[MessageLeave]


@dataclass
class MessageBody__SYSTEM:
    messageType: Literal[MessageType.SYSTEM]
    SYSTEM: Optional[MessageSystem]


@dataclass
class MessageBody__DELETEHISTORY:
    messageType: Literal[MessageType.DELETEHISTORY]
    DELETEHISTORY: Optional[MessageDeleteHistory]


@dataclass
class MessageBody__REACTION:
    messageType: Literal[MessageType.REACTION]
    REACTION: Optional[MessageReaction]


@dataclass
class MessageBody__SENDPAYMENT:
    messageType: Literal[MessageType.SENDPAYMENT]
    SENDPAYMENT: Optional[MessageSendPayment]


@dataclass
class MessageBody__REQUESTPAYMENT:
    messageType: Literal[MessageType.REQUESTPAYMENT]
    REQUESTPAYMENT: Optional[MessageRequestPayment]


@dataclass
class MessageBody__UNFURL:
    messageType: Literal[MessageType.UNFURL]
    UNFURL: Optional[MessageUnfurl]


@dataclass
class MessageBody__FLIP:
    messageType: Literal[MessageType.FLIP]
    FLIP: Optional[MessageFlip]


@dataclass
class MessageBody__PIN:
    messageType: Literal[MessageType.PIN]
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


@dataclass_json
@dataclass
class MsgSummary:
    id: MessageID = field(metadata=config(field_name="id"))
    conv_id: str = field(metadata=config(field_name="conversation_id"))
    channel: ChatChannel = field(metadata=config(field_name="channel"))
    sender: MsgSender = field(metadata=config(field_name="sender"))
    sent_at: int = field(metadata=config(field_name="sent_at"))
    sent_at_ms: int = field(metadata=config(field_name="sent_at_ms"))
    content: MsgContent = field(metadata=config(field_name="content"))
    prev: List[MessagePreviousPointer] = field(metadata=config(field_name="prev"))
    unread: bool = field(metadata=config(field_name="unread"))
    revoked_device: Optional[bool] = field(metadata=config(field_name="revoked_device"))
    offline: Optional[bool] = field(metadata=config(field_name="offline"))
    kbfs_encrypted: Optional[bool] = field(metadata=config(field_name="kbfs_encrypted"))
    is_ephemeral: Optional[bool] = field(metadata=config(field_name="is_ephemeral"))
    is_ephemeral_expired: Optional[bool] = field(
        metadata=config(field_name="is_ephemeral_expired")
    )
    e_time: Optional[gregor1.Time] = field(metadata=config(field_name="e_time"))
    reactions: Optional[ReactionMap] = field(metadata=config(field_name="reactions"))
    has_pairwise_macs: Optional[bool] = field(
        metadata=config(field_name="has_pairwise_macs")
    )
    at_mention_usernames: Optional[List[str]] = field(
        metadata=config(field_name="at_mention_usernames")
    )
    channel_mention: Optional[str] = field(
        metadata=config(field_name="channel_mention")
    )
    channel_name_mentions: Optional[List[UIChannelNameMention]] = field(
        metadata=config(field_name="channel_name_mentions")
    )


@dataclass_json
@dataclass
class BodyPlaintextV1:
    message_body: MessageBody = field(metadata=config(field_name="messageBody"))


@dataclass_json
@dataclass
class BodyPlaintextV2:
    message_body: MessageBody = field(metadata=config(field_name="messageBody"))
    mi: BodyPlaintextMetaInfo = field(metadata=config(field_name="mi"))


@dataclass_json
@dataclass
class MessagePlaintext:
    client_header: MessageClientHeader = field(
        metadata=config(field_name="clientHeader")
    )
    message_body: MessageBody = field(metadata=config(field_name="messageBody"))
    supersedes_outbox_id: Optional[OutboxID] = field(
        metadata=config(field_name="supersedesOutboxID")
    )


@dataclass_json
@dataclass
class Message:
    msg: Optional[MsgSummary] = field(metadata=config(field_name="msg"))
    error: Optional[str] = field(metadata=config(field_name="error"))


@dataclass_json
@dataclass
class MsgNotification:
    type: str = field(metadata=config(field_name="type"))
    source: str = field(metadata=config(field_name="source"))
    msg: Optional[MsgSummary] = field(metadata=config(field_name="msg"))
    error: Optional[str] = field(metadata=config(field_name="error"))
    pagination: Optional[UIPagination] = field(metadata=config(field_name="pagination"))


@dataclass
class BodyPlaintext__V1:
    version: Literal[BodyPlaintextVersion.V1]
    V1: Optional[BodyPlaintextV1]


@dataclass
class BodyPlaintext__V2:
    version: Literal[BodyPlaintextVersion.V2]
    V2: Optional[BodyPlaintextV2]


@dataclass
class BodyPlaintext__V3:
    version: Literal[BodyPlaintextVersion.V3]
    V3: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V4:
    version: Literal[BodyPlaintextVersion.V4]
    V4: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V5:
    version: Literal[BodyPlaintextVersion.V5]
    V5: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V6:
    version: Literal[BodyPlaintextVersion.V6]
    V6: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V7:
    version: Literal[BodyPlaintextVersion.V7]
    V7: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V8:
    version: Literal[BodyPlaintextVersion.V8]
    V8: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V9:
    version: Literal[BodyPlaintextVersion.V9]
    V9: Optional[BodyPlaintextUnsupported]


@dataclass
class BodyPlaintext__V10:
    version: Literal[BodyPlaintextVersion.V10]
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


@dataclass_json
@dataclass
class Thread:
    messages: List[Message] = field(metadata=config(field_name="messages"))
    pagination: Optional[Pagination] = field(metadata=config(field_name="pagination"))
    offline: Optional[bool] = field(metadata=config(field_name="offline"))
    identify_failures: Optional[List[keybase1.TLFIdentifyFailure]] = field(
        metadata=config(field_name="identify_failures")
    )
    rate_limits: Optional[List[RateLimitRes]] = field(
        metadata=config(field_name="ratelimits")
    )
