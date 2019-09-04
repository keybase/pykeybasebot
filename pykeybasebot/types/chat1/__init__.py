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

from mashumaro import DataClassJSONMixin
from typing_extensions import Literal

import gregor1
import keybase1
import stellar1


@dataclass
class RateLimitRes(DataClassJSONMixin):
    tank: str
    capacity: int
    reset: int
    gas: int


@dataclass
class ChatChannel(DataClassJSONMixin):
    name: str
    public: bool
    members_type: str
    topic_type: Optional[str]
    topic_name: Optional[str]


@dataclass
class ChatMessage(DataClassJSONMixin):
    body: str


@dataclass
class MsgSender(DataClassJSONMixin):
    uid: str
    username: Optional[str]
    device_id: str
    device_name: Optional[str]


@dataclass
class UIPagination(DataClassJSONMixin):
    next: str
    previous: str
    num: int
    last: bool


@dataclass
class UnverifiedInboxUIItemMetadata(DataClassJSONMixin):
    channel_name: str
    headline: str
    headline_decorated: str
    snippet: str
    snippet_decoration: str
    writer_names: List[str]
    reset_participants: List[str]


class UIParticipantType(Enum):
    NONE = "none"
    USER = "user"
    PHONENO = "phoneno"
    EMAIL = "email"


@dataclass
class UIChannelNameMention(DataClassJSONMixin):
    name: str
    conv_id: str


@dataclass
class UIAssetUrlInfo(DataClassJSONMixin):
    preview_url: str
    full_url: str
    full_url_cached: bool
    mime_type: str
    video_duration: Optional[str]
    inline_video_playable: bool


@dataclass
class UIPaymentInfo(DataClassJSONMixin):
    account_id: Optional[stellar1.AccountID]
    amount_description: str
    worth: str
    worth_at_send_time: str
    delta: stellar1.BalanceDelta
    note: str
    payment_id: stellar1.PaymentID
    status: stellar1.PaymentStatus
    status_description: str
    status_detail: str
    show_cancel: bool
    from_username: str
    to_username: str
    source_amount: str
    source_asset: stellar1.Asset
    issuer_description: str


@dataclass
class UIRequestInfo(DataClassJSONMixin):
    amount: str
    amount_description: str
    asset: Optional[stellar1.Asset]
    currency: Optional[stellar1.OutsideCurrencyCode]
    worth_at_request_time: str
    status: stellar1.RequestStatus


class MessageUnboxedState(Enum):
    VALID = "valid"
    ERROR = "error"
    OUTBOX = "outbox"
    PLACEHOLDER = "placeholder"


@dataclass
class UITeamMention(DataClassJSONMixin):
    in_team: bool
    open: bool
    description: Optional[str]
    num_members: Optional[int]
    public_admins: List[str]
    conv_id: Optional[str]


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


@dataclass
class UILinkDecoration(DataClassJSONMixin):
    display: str
    url: str


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


@dataclass
class UIChatPayment(DataClassJSONMixin):
    username: str
    full_name: str
    xlm_amount: str
    error: Optional[str]
    display_amount: Optional[str]


@dataclass
class GiphySearchResult(DataClassJSONMixin):
    target_url: str
    preview_url: str
    preview_width: int
    preview_height: int
    preview_is_video: bool


class UICoinFlipPhase(Enum):
    COMMITMENT = "commitment"
    REVEALS = "reveals"
    COMPLETE = "complete"
    ERROR = "error"


@dataclass
class UICoinFlipErrorParticipant(DataClassJSONMixin):
    user: str
    device: str


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


@dataclass
class UICoinFlipHand(DataClassJSONMixin):
    target: str
    hand: List[int]


@dataclass
class UICoinFlipParticipant(DataClassJSONMixin):
    uid: str
    device_id: str
    username: str
    device_name: str
    commitment: str
    reveal: Optional[str]


@dataclass
class UICommandMarkdown(DataClassJSONMixin):
    body: str
    title: Optional[str]


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


@dataclass
class ConversationCommand(DataClassJSONMixin):
    description: str
    name: str
    usage: str
    has_help_text: bool
    username: Optional[str]


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


@dataclass
class GlobalAppNotificationSettings(DataClassJSONMixin):
    settings: Dict[str, bool]


class ConversationStatus(Enum):
    UNFILED = "unfiled"
    FAVORITE = "favorite"
    IGNORED = "ignored"
    BLOCKED = "blocked"
    MUTED = "muted"
    REPORTED = "reported"


@dataclass
class KBFSPath(DataClassJSONMixin):
    start_index: int
    raw_path: str
    standard_path: str
    path_info: keybase1.KBFSPathInfo


class ConversationMemberStatus(Enum):
    ACTIVE = "active"
    REMOVED = "removed"
    LEFT = "left"
    PREVIEW = "preview"
    RESET = "reset"
    NEVER_JOINED = "never_joined"


@dataclass
class Pagination(DataClassJSONMixin):
    next: bytes
    previous: bytes
    num: int
    last: bool
    force_first_page: bool


@dataclass
class RateLimit(DataClassJSONMixin):
    name: str
    calls_remaining: int
    window_reset: int
    max_calls: int


@dataclass
class ConversationFinalizeInfo(DataClassJSONMixin):
    reset_user: str
    reset_date: str
    reset_full: str
    reset_timestamp: gregor1.Time


@dataclass
class ConversationResolveInfo(DataClassJSONMixin):
    new_tlf_name: str


@dataclass
class ConversationNotificationInfo(DataClassJSONMixin):
    channel_wide: bool
    settings: Dict[str, Dict[str, bool]]


@dataclass
class ConversationCreatorInfo(DataClassJSONMixin):
    ctime: gregor1.Time
    uid: gregor1.UID


@dataclass
class ConversationCreatorInfoLocal(DataClassJSONMixin):
    ctime: gregor1.Time
    username: str


@dataclass
class ConversationMinWriterRoleInfo(DataClassJSONMixin):
    uid: gregor1.UID
    role: keybase1.TeamRole


@dataclass
class MsgEphemeralMetadata(DataClassJSONMixin):
    l: gregor1.DurationSec
    g: keybase1.EkGeneration
    u: Optional[str]


@dataclass
class EncryptedData(DataClassJSONMixin):
    v: int
    e: bytes
    n: bytes


@dataclass
class SignEncryptedData(DataClassJSONMixin):
    v: int
    e: bytes
    n: bytes


@dataclass
class SealedData(DataClassJSONMixin):
    v: int
    e: bytes
    n: bytes


@dataclass
class SignatureInfo(DataClassJSONMixin):
    v: int
    s: bytes
    k: bytes


@dataclass
class MerkleRoot(DataClassJSONMixin):
    seqno: int
    hash: bytes


class InboxResType(Enum):
    VERSIONHIT = "versionhit"
    FULL = "full"


class RetentionPolicyType(Enum):
    NONE = "none"
    RETAIN = "retain"
    EXPIRE = "expire"
    INHERIT = "inherit"
    EPHEMERAL = "ephemeral"


@dataclass
class RpRetain(DataClassJSONMixin):
    pass


@dataclass
class RpExpire(DataClassJSONMixin):
    age: gregor1.DurationSec


@dataclass
class RpInherit(DataClassJSONMixin):
    pass


@dataclass
class RpEphemeral(DataClassJSONMixin):
    age: gregor1.DurationSec


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


@dataclass
class EmptyStruct(DataClassJSONMixin):
    pass


@dataclass
class ChatSearchMatch(DataClassJSONMixin):
    start_index: int
    end_index: int
    match: str


@dataclass
class ChatSearchInboxDone(DataClassJSONMixin):
    num_hits: int
    num_convs: int
    percent_indexed: int
    delegated: bool


@dataclass
class ChatSearchIndexStatus(DataClassJSONMixin):
    percent_indexed: int


@dataclass
class AssetMetadataImage(DataClassJSONMixin):
    width: int
    height: int


@dataclass
class AssetMetadataVideo(DataClassJSONMixin):
    width: int
    height: int
    duration_ms: int


@dataclass
class AssetMetadataAudio(DataClassJSONMixin):
    duration_ms: int


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


@dataclass
class TeamMember(DataClassJSONMixin):
    uid: gregor1.UID
    role: keybase1.TeamRole
    status: keybase1.TeamMemberStatus


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


@dataclass
class KnownUserMention(DataClassJSONMixin):
    text: str
    uid: gregor1.UID


@dataclass
class KnownTeamMention(DataClassJSONMixin):
    name: str
    channel: str


@dataclass
class MaybeMention(DataClassJSONMixin):
    name: str
    channel: str


@dataclass
class Coordinate(DataClassJSONMixin):
    lat: float
    lon: float
    accuracy: float


@dataclass
class LiveLocation(DataClassJSONMixin):
    end_time: gregor1.Time


@dataclass
class MessageConversationMetadata(DataClassJSONMixin):
    conversation_title: str


@dataclass
class MessageHeadline(DataClassJSONMixin):
    headline: str


class MessageSystemType(Enum):
    ADDEDTOTEAM = "addedtoteam"
    INVITEADDEDTOTEAM = "inviteaddedtoteam"
    COMPLEXTEAM = "complexteam"
    CREATETEAM = "createteam"
    GITPUSH = "gitpush"
    CHANGEAVATAR = "changeavatar"
    CHANGERETENTION = "changeretention"
    BULKADDTOCONV = "bulkaddtoconv"


@dataclass
class MessageSystemAddedToTeam(DataClassJSONMixin):
    team: str
    adder: str
    addee: str
    owners: List[str]
    admins: List[str]
    writers: List[str]
    readers: List[str]
    bots: List[str]
    restricted_bots: List[str]


@dataclass
class MessageSystemInviteAddedToTeam(DataClassJSONMixin):
    team: str
    inviter: str
    invitee: str
    adder: str
    invite_type: keybase1.TeamInviteCategory


@dataclass
class MessageSystemComplexTeam(DataClassJSONMixin):
    team: str


@dataclass
class MessageSystemCreateTeam(DataClassJSONMixin):
    team: str
    creator: str


@dataclass
class MessageSystemGitPush(DataClassJSONMixin):
    team: str
    pusher: str
    repo_name: str
    repo_id: keybase1.RepoID
    refs: List[keybase1.GitRefMetadata]
    push_type: keybase1.GitPushType
    previous_repo_name: str


@dataclass
class MessageSystemChangeAvatar(DataClassJSONMixin):
    team: str
    user: str


@dataclass
class MessageSystemBulkAddToConv(DataClassJSONMixin):
    usernames: List[str]


@dataclass
class MessageJoin(DataClassJSONMixin):
    joiners: List[str]
    leavers: List[str]


@dataclass
class MessageLeave(DataClassJSONMixin):
    pass


@dataclass
class MessageSendPayment(DataClassJSONMixin):
    payment_id: stellar1.PaymentID


@dataclass
class MessageRequestPayment(DataClassJSONMixin):
    request_id: stellar1.KeybaseRequestID
    note: str


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


@dataclass
class HeaderPlaintextMetaInfo(DataClassJSONMixin):
    crit: bool


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


@dataclass
class BodyPlaintextMetaInfo(DataClassJSONMixin):
    crit: bool


class MessageUnboxedErrorType(Enum):
    MISC = "misc"
    BADVERSION_CRITICAL = "badversion_critical"
    BADVERSION = "badversion"
    IDENTIFY = "identify"
    EPHEMERAL = "ephemeral"
    PAIRWISE_MISSING = "pairwise_missing"


@dataclass
class UnreadFirstNumLimit(DataClassJSONMixin):
    num_read: int
    at_least: int
    at_most: int


@dataclass
class ConversationLocalParticipant(DataClassJSONMixin):
    username: str
    fullname: Optional[str]
    contact_name: Optional[str]


class ConversationErrorType(Enum):
    PERMANENT = "permanent"
    MISSINGINFO = "missinginfo"
    SELFREKEYNEEDED = "selfrekeyneeded"
    OTHERREKEYNEEDED = "otherrekeyneeded"
    IDENTIFY = "identify"
    TRANSIENT = "transient"
    NONE = "none"


@dataclass
class ConversationErrorRekey(DataClassJSONMixin):
    tlf_name: str
    tlf_public: bool
    rekeyers: List[str]
    writer_names: List[str]
    reader_names: List[str]


@dataclass
class ConversationMinWriterRoleInfoLocal(DataClassJSONMixin):
    changed_by: str
    cannot_write: bool
    role: keybase1.TeamRole


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


@dataclass
class UserBotExtendedDescription(DataClassJSONMixin):
    title: str
    desktop_body: str
    mobile_body: str


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


@dataclass
class TyperInfo(DataClassJSONMixin):
    uid: keybase1.UID
    username: str
    device_id: keybase1.DeviceID
    device_name: str
    device_type: str


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


@dataclass
class S3Params(DataClassJSONMixin):
    bucket: str
    object_key: str
    access_key: str
    acl: str
    region_name: str
    region_endpoint: str
    region_bucket_endpoint: str


@dataclass
class ServerCacheVers(DataClassJSONMixin):
    inbox_vers: int
    bodies_vers: int


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


@dataclass
class UnfurlVideo(DataClassJSONMixin):
    url: str
    mime_type: str
    height: int
    width: int


@dataclass
class UnfurlYoutubeRaw(DataClassJSONMixin):
    pass


@dataclass
class UnfurlYoutube(DataClassJSONMixin):
    pass


@dataclass
class UnfurlImageDisplay(DataClassJSONMixin):
    url: str
    height: int
    width: int
    is_video: bool


@dataclass
class UnfurlYoutubeDisplay(DataClassJSONMixin):
    pass


class UnfurlMode(Enum):
    ALWAYS = "always"
    NEVER = "never"
    WHITELISTED = "whitelisted"


@dataclass
class MsgFlipContent(DataClassJSONMixin):
    text: str
    game_id: str
    flip_conv_id: str
    user_mentions: List[KnownUserMention]
    team_mentions: List[KnownTeamMention]


@dataclass
class ConvSummary(DataClassJSONMixin):
    id: str
    channel: ChatChannel
    unread: bool
    active_at: int
    active_at_ms: int
    member_status: str
    reset_users: Optional[List[str]]
    finalize_info: Optional[ConversationFinalizeInfo]
    supersedes: Optional[List[str]]
    superseded_by: Optional[List[str]]
    error: Optional[str]


@dataclass
class SendRes(DataClassJSONMixin):
    message: str
    id: Optional[MessageID]
    outbox_id: Optional[OutboxID]
    identify_failures: Optional[List[keybase1.TLFIdentifyFailure]]
    ratelimits: Optional[List[RateLimitRes]]


@dataclass
class NewConvRes(DataClassJSONMixin):
    id: str
    identify_failures: Optional[List[keybase1.TLFIdentifyFailure]]
    ratelimits: Optional[List[RateLimitRes]]


@dataclass
class EmptyRes(DataClassJSONMixin):
    ratelimits: Optional[List[RateLimitRes]]


@dataclass
class UIParticipant(DataClassJSONMixin):
    type: UIParticipantType
    assertion: str
    full_name: Optional[str]
    contact_name: Optional[str]


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


@dataclass
class UIChatSearchConvHit(DataClassJSONMixin):
    conv_id: str
    team_type: TeamType
    name: str
    mtime: gregor1.Time


@dataclass
class UIChatPaymentSummary(DataClassJSONMixin):
    xlm_total: str
    display_total: str
    payments: List[UIChatPayment]


@dataclass
class GiphySearchResults(DataClassJSONMixin):
    results: List[GiphySearchResult]
    gallery_url: str


@dataclass
class UICoinFlipAbsenteeError(DataClassJSONMixin):
    absentees: List[UICoinFlipErrorParticipant]


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


@dataclass
class ConversationCommandGroupsCustom(DataClassJSONMixin):
    commands: List[ConversationCommand]


@dataclass
class InboxVersInfo(DataClassJSONMixin):
    uid: gregor1.UID
    vers: InboxVers


@dataclass
class ConversationMember(DataClassJSONMixin):
    uid: gregor1.UID
    conv_id: ConversationID
    topic_type: TopicType


@dataclass
class ConversationIDMessageIDPair(DataClassJSONMixin):
    conv_id: ConversationID
    msg_id: MessageID


@dataclass
class ChannelNameMention(DataClassJSONMixin):
    conv_id: ConversationID
    topic_name: str


@dataclass
class GetInboxQuery(DataClassJSONMixin):
    conv_id: Optional[ConversationID]
    topic_type: Optional[TopicType]
    tlf_id: Optional[TLFID]
    tlf_visibility: Optional[keybase1.TLFVisibility]
    before: Optional[gregor1.Time]
    after: Optional[gregor1.Time]
    one_chat_type_per_tlf: Optional[bool]
    topic_name: Optional[str]
    status: List[ConversationStatus]
    member_status: List[ConversationMemberStatus]
    existences: List[ConversationExistence]
    members_types: List[ConversationMembersType]
    conv_i_ds: List[ConversationID]
    unread_only: bool
    read_only: bool
    compute_active_list: bool
    summarize_max_msgs: bool
    skip_bg_loads: bool


@dataclass
class ConversationIDTriple(DataClassJSONMixin):
    tlfid: TLFID
    topic_type: TopicType
    topic_id: TopicID


@dataclass
class Expunge(DataClassJSONMixin):
    upto: MessageID
    basis: MessageID


@dataclass
class ConversationReaderInfo(DataClassJSONMixin):
    mtime: gregor1.Time
    read_msgid: MessageID
    max_msgid: MessageID
    status: ConversationMemberStatus


@dataclass
class ConversationSettings(DataClassJSONMixin):
    mwr: Optional[ConversationMinWriterRoleInfo]


@dataclass
class MessageSummary(DataClassJSONMixin):
    msg_id: MessageID
    message_type: MessageType
    tlf_name: str
    tlf_public: bool
    ctime: gregor1.Time


@dataclass
class Reaction(DataClassJSONMixin):
    ctime: gregor1.Time
    reaction_msg_id: MessageID


@dataclass
class MessageServerHeader(DataClassJSONMixin):
    message_id: MessageID
    superseded_by: MessageID
    r: List[MessageID]
    u: List[MessageID]
    replies: List[MessageID]
    ctime: gregor1.Time
    n: gregor1.Time
    rt: Optional[gregor1.Time]


@dataclass
class MessagePreviousPointer(DataClassJSONMixin):
    id: MessageID
    hash: Hash


@dataclass
class OutboxInfo(DataClassJSONMixin):
    prev: MessageID
    compose_time: gregor1.Time


@dataclass
class EphemeralPurgeInfo(DataClassJSONMixin):
    c: ConversationID
    a: bool
    n: gregor1.Time
    e: MessageID


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


@dataclass
class SearchOpts(DataClassJSONMixin):
    is_regex: bool
    sent_by: str
    sent_to: str
    match_mentions: bool
    sent_before: gregor1.Time
    sent_after: gregor1.Time
    max_hits: int
    max_messages: int
    before_context: int
    after_context: int
    initial_pagination: Optional[Pagination]
    reindex_mode: ReIndexingMode
    max_convs_searched: int
    max_convs_hit: int
    conv_id: Optional[ConversationID]
    max_name_convs: int


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


@dataclass
class UnreadUpdate(DataClassJSONMixin):
    conv_id: ConversationID
    unread_messages: int
    unread_notifying_messages: Dict[str, int]
    diff: bool


@dataclass
class TLFFinalizeUpdate(DataClassJSONMixin):
    finalize_info: ConversationFinalizeInfo
    conv_i_ds: List[ConversationID]
    inbox_vers: InboxVers


@dataclass
class TLFResolveUpdate(DataClassJSONMixin):
    conv_id: ConversationID
    inbox_vers: InboxVers


@dataclass
class RemoteUserTypingUpdate(DataClassJSONMixin):
    uid: gregor1.UID
    device_id: gregor1.DeviceID
    conv_id: ConversationID
    typing: bool


@dataclass
class ConversationUpdate(DataClassJSONMixin):
    conv_id: ConversationID
    existence: ConversationExistence


@dataclass
class TeamChannelUpdate(DataClassJSONMixin):
    team_id: TLFID


@dataclass
class KBFSImpteamUpgradeUpdate(DataClassJSONMixin):
    conv_id: ConversationID
    inbox_vers: InboxVers
    topic_type: TopicType


@dataclass
class SubteamRenameUpdate(DataClassJSONMixin):
    conv_i_ds: List[ConversationID]
    inbox_vers: InboxVers


@dataclass
class TextPayment(DataClassJSONMixin):
    username: str
    payment_text: str
    result: TextPaymentResult


@dataclass
class MessageEdit(DataClassJSONMixin):
    message_id: MessageID
    body: str
    user_mentions: List[KnownUserMention]
    team_mentions: List[KnownTeamMention]


@dataclass
class MessageDelete(DataClassJSONMixin):
    message_i_ds: List[MessageID]


@dataclass
class MessageFlip(DataClassJSONMixin):
    text: str
    game_id: FlipGameID
    flip_conv_id: ConversationID
    user_mentions: List[KnownUserMention]
    team_mentions: List[KnownTeamMention]


@dataclass
class MessagePin(DataClassJSONMixin):
    msg_id: MessageID


@dataclass
class MessageDeleteHistory(DataClassJSONMixin):
    upto: MessageID


@dataclass
class MessageReaction(DataClassJSONMixin):
    m: MessageID
    b: str


@dataclass
class SenderPrepareOptions(DataClassJSONMixin):
    skip_topic_name_state: bool
    reply_to: Optional[MessageID]


@dataclass
class SenderSendOptions(DataClassJSONMixin):
    join_mentions_as: Optional[ConversationMemberStatus]


@dataclass
class OutboxStateError(DataClassJSONMixin):
    message: str
    typ: OutboxErrorType


@dataclass
class HeaderPlaintextUnsupported(DataClassJSONMixin):
    mi: HeaderPlaintextMetaInfo


@dataclass
class BodyPlaintextUnsupported(DataClassJSONMixin):
    mi: BodyPlaintextMetaInfo


@dataclass
class MessageUnboxedError(DataClassJSONMixin):
    err_type: MessageUnboxedErrorType
    err_msg: str
    internal_err_msg: str
    version_kind: VersionKind
    version_number: int
    is_critical: bool
    sender_username: str
    sender_device_name: str
    sender_device_type: str
    message_id: MessageID
    message_type: MessageType
    ctime: gregor1.Time
    is_ephemeral: bool
    is_ephemeral_expired: bool
    etime: gregor1.Time


@dataclass
class MessageUnboxedPlaceholder(DataClassJSONMixin):
    message_id: MessageID
    hidden: bool


@dataclass
class ConversationSettingsLocal(DataClassJSONMixin):
    min_writer_role_info: Optional[ConversationMinWriterRoleInfoLocal]


@dataclass
class NonblockFetchRes(DataClassJSONMixin):
    offline: bool
    rate_limits: List[RateLimit]
    identify_failures: List[keybase1.TLFIdentifyFailure]


@dataclass
class MessageIDControl(DataClassJSONMixin):
    pivot: Optional[MessageID]
    mode: MessageIDControlMode
    num: int


@dataclass
class UnreadlineRes(DataClassJSONMixin):
    offline: bool
    rate_limits: List[RateLimit]
    identify_failures: List[keybase1.TLFIdentifyFailure]
    unreadline_id: Optional[MessageID]


@dataclass
class NameQuery(DataClassJSONMixin):
    name: str
    tlf_id: Optional[TLFID]
    members_type: ConversationMembersType


@dataclass
class PostLocalRes(DataClassJSONMixin):
    rate_limits: List[RateLimit]
    message_id: MessageID
    identify_failures: List[keybase1.TLFIdentifyFailure]


@dataclass
class PostLocalNonblockRes(DataClassJSONMixin):
    rate_limits: List[RateLimit]
    outbox_id: OutboxID
    identify_failures: List[keybase1.TLFIdentifyFailure]


@dataclass
class EditTarget(DataClassJSONMixin):
    message_id: Optional[MessageID]
    outbox_id: Optional[OutboxID]


@dataclass
class SetConversationStatusLocalRes(DataClassJSONMixin):
    rate_limits: List[RateLimit]
    identify_failures: List[keybase1.TLFIdentifyFailure]


@dataclass
class GetInboxSummaryForCLILocalQuery(DataClassJSONMixin):
    topic_type: TopicType
    after: str
    before: str
    visibility: keybase1.TLFVisibility
    status: List[ConversationStatus]
    unread_first: bool
    unread_first_limit: UnreadFirstNumLimit
    activity_sorted_limit: int


@dataclass
class DownloadAttachmentLocalRes(DataClassJSONMixin):
    rate_limits: List[RateLimit]
    identify_failures: List[keybase1.TLFIdentifyFailure]


@dataclass
class DownloadFileAttachmentLocalRes(DataClassJSONMixin):
    filename: str
    rate_limits: List[RateLimit]
    identify_failures: List[keybase1.TLFIdentifyFailure]


@dataclass
class MarkAsReadLocalRes(DataClassJSONMixin):
    offline: bool
    rate_limits: List[RateLimit]


@dataclass
class JoinLeaveConversationLocalRes(DataClassJSONMixin):
    offline: bool
    rate_limits: List[RateLimit]


@dataclass
class DeleteConversationLocalRes(DataClassJSONMixin):
    offline: bool
    rate_limits: List[RateLimit]


@dataclass
class SetAppNotificationSettingsLocalRes(DataClassJSONMixin):
    offline: bool
    rate_limits: List[RateLimit]


@dataclass
class AppNotificationSettingLocal(DataClassJSONMixin):
    device_type: keybase1.DeviceType
    kind: NotificationKind
    enabled: bool


@dataclass
class ProfileSearchConvStats(DataClassJSONMixin):
    err: str
    conv_name: str
    min_conv_id: MessageID
    max_conv_id: MessageID
    num_missing: int
    num_messages: int
    index_size_disk: int
    index_size_mem: int
    duration_msec: gregor1.DurationMsec
    percent_indexed: int


@dataclass
class BuiltinCommandGroup(DataClassJSONMixin):
    typ: ConversationBuiltinCommandTyp
    commands: List[ConversationCommand]


@dataclass
class UserBotCommandOutput(DataClassJSONMixin):
    name: str
    description: str
    usage: str
    extended_description: Optional[UserBotExtendedDescription]
    username: str


@dataclass
class UserBotCommandInput(DataClassJSONMixin):
    name: str
    description: str
    usage: str
    extended_description: Optional[UserBotExtendedDescription]


@dataclass
class AdvertiseBotCommandsLocalRes(DataClassJSONMixin):
    rate_limits: List[RateLimit]


@dataclass
class ClearBotCommandsLocalRes(DataClassJSONMixin):
    rate_limits: List[RateLimit]


@dataclass
class PinMessageRes(DataClassJSONMixin):
    rate_limits: List[RateLimit]


@dataclass
class SetAppNotificationSettingsInfo(DataClassJSONMixin):
    conv_id: ConversationID
    settings: ConversationNotificationInfo


@dataclass
class MemberInfo(DataClassJSONMixin):
    member: str
    status: ConversationMemberStatus


@dataclass
class ConvTypingUpdate(DataClassJSONMixin):
    conv_id: ConversationID
    typers: List[TyperInfo]


@dataclass
class ConversationStaleUpdate(DataClassJSONMixin):
    conv_id: ConversationID
    update_type: StaleUpdateType


@dataclass
class NewConversationRemoteRes(DataClassJSONMixin):
    conv_id: ConversationID
    created_complex_team: bool
    rate_limit: Optional[RateLimit]


@dataclass
class MarkAsReadRes(DataClassJSONMixin):
    rate_limit: Optional[RateLimit]


@dataclass
class SetConversationStatusRes(DataClassJSONMixin):
    rate_limit: Optional[RateLimit]


@dataclass
class GetUnreadlineRemoteRes(DataClassJSONMixin):
    unreadline_id: Optional[MessageID]
    rate_limit: Optional[RateLimit]


@dataclass
class JoinLeaveConversationRemoteRes(DataClassJSONMixin):
    rate_limit: Optional[RateLimit]


@dataclass
class DeleteConversationRemoteRes(DataClassJSONMixin):
    rate_limit: Optional[RateLimit]


@dataclass
class GetMessageBeforeRes(DataClassJSONMixin):
    msg_id: MessageID
    rate_limit: Optional[RateLimit]


@dataclass
class SetAppNotificationSettingsRes(DataClassJSONMixin):
    rate_limit: Optional[RateLimit]


@dataclass
class SetRetentionRes(DataClassJSONMixin):
    rate_limit: Optional[RateLimit]


@dataclass
class SetConvMinWriterRoleRes(DataClassJSONMixin):
    rate_limit: Optional[RateLimit]


@dataclass
class ServerNowRes(DataClassJSONMixin):
    rate_limit: Optional[RateLimit]
    now: gregor1.Time


@dataclass
class RemoteBotCommandsAdvertisementPublic(DataClassJSONMixin):
    conv_id: ConversationID


@dataclass
class RemoteBotCommandsAdvertisementTLFID(DataClassJSONMixin):
    conv_id: ConversationID
    tlf_id: TLFID


@dataclass
class BotCommandConv(DataClassJSONMixin):
    uid: gregor1.UID
    conv_id: ConversationID
    vers: CommandConvVers
    mtime: gregor1.Time


@dataclass
class AdvertiseBotCommandsRes(DataClassJSONMixin):
    rate_limit: Optional[RateLimit]


@dataclass
class ClearBotCommandsRes(DataClassJSONMixin):
    rate_limit: Optional[RateLimit]


@dataclass
class UnfurlGenericRaw(DataClassJSONMixin):
    title: str
    url: str
    site_name: str
    favicon_url: Optional[str]
    image_url: Optional[str]
    video: Optional[UnfurlVideo]
    publish_time: Optional[int]
    description: Optional[str]


@dataclass
class UnfurlGiphyRaw(DataClassJSONMixin):
    image_url: Optional[str]
    video: Optional[UnfurlVideo]
    favicon_url: Optional[str]


@dataclass
class UnfurlMapsRaw(DataClassJSONMixin):
    title: str
    url: str
    site_name: str
    image_url: str
    history_image_url: Optional[str]
    description: str
    coord: Coordinate
    time: gregor1.Time
    live_location_end_time: Optional[gregor1.Time]
    live_location_done: bool


@dataclass
class UnfurlGenericMapInfo(DataClassJSONMixin):
    coord: Coordinate
    time: gregor1.Time
    live_location_end_time: Optional[gregor1.Time]
    is_live_location_done: bool


@dataclass
class UnfurlGiphyDisplay(DataClassJSONMixin):
    favicon: Optional[UnfurlImageDisplay]
    image: Optional[UnfurlImageDisplay]
    video: Optional[UnfurlImageDisplay]


@dataclass
class UnfurlSettings(DataClassJSONMixin):
    mode: UnfurlMode
    whitelist: Dict[str, bool]


@dataclass
class UnfurlSettingsDisplay(DataClassJSONMixin):
    mode: UnfurlMode
    whitelist: List[str]


@dataclass
class ChatList(DataClassJSONMixin):
    conversations: List[ConvSummary]
    offline: bool
    identify_failures: Optional[List[keybase1.TLFIdentifyFailure]]
    pagination: Optional[Pagination]
    ratelimits: Optional[List[RateLimitRes]]


@dataclass
class ListCommandsRes(DataClassJSONMixin):
    commands: List[UserBotCommandOutput]
    ratelimits: Optional[List[RateLimitRes]]


@dataclass
class AdvertiseCommandAPIParam(DataClassJSONMixin):
    type: str
    commands: List[UserBotCommandInput]
    team_name: Optional[str]


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


@dataclass
class UIChatSearchConvHits(DataClassJSONMixin):
    hits: List[UIChatSearchConvHit]
    unread_matches: bool


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


@dataclass
class ConversationIDMessageIDPairs(DataClassJSONMixin):
    pairs: List[ConversationIDMessageIDPair]


@dataclass
class ReactionMap(DataClassJSONMixin):
    reactions: Dict[str, Dict[str, Reaction]]


@dataclass
class MessageClientHeader(DataClassJSONMixin):
    conv: ConversationIDTriple
    tlf_name: str
    tlf_public: bool
    message_type: MessageType
    supersedes: MessageID
    kbfs_crypt_keys_used: Optional[bool]
    deletes: List[MessageID]
    prev: List[MessagePreviousPointer]
    delete_history: Optional[MessageDeleteHistory]
    sender: gregor1.UID
    sender_device: gregor1.DeviceID
    merkle_root: Optional[MerkleRoot]
    outbox_id: Optional[OutboxID]
    outbox_info: Optional[OutboxInfo]
    em: Optional[MsgEphemeralMetadata]
    pm: Dict[str, bytes]
    b: Optional[gregor1.UID]


@dataclass
class MessageClientHeaderVerified(DataClassJSONMixin):
    conv: ConversationIDTriple
    tlf_name: str
    tlf_public: bool
    message_type: MessageType
    prev: List[MessagePreviousPointer]
    sender: gregor1.UID
    sender_device: gregor1.DeviceID
    kbfs_crypt_keys_used: Optional[bool]
    merkle_root: Optional[MerkleRoot]
    outbox_id: Optional[OutboxID]
    outbox_info: Optional[OutboxInfo]
    em: Optional[MsgEphemeralMetadata]
    rt: gregor1.Time
    pm: bool
    b: Optional[gregor1.UID]


@dataclass
class Asset(DataClassJSONMixin):
    filename: str
    region: str
    endpoint: str
    bucket: str
    path: str
    size: int
    mime_type: str
    enc_hash: Hash
    key: bytes
    verify_key: bytes
    title: str
    nonce: bytes
    metadata: AssetMetadata
    tag: AssetTag


@dataclass
class GenericPayload(DataClassJSONMixin):
    action: str
    inbox_vers: InboxVers
    conv_id: ConversationID
    topic_type: TopicType
    unread_update: Optional[UnreadUpdate]


@dataclass
class NewConversationPayload(DataClassJSONMixin):
    action: str
    conv_id: ConversationID
    inbox_vers: InboxVers
    topic_type: TopicType
    unread_update: Optional[UnreadUpdate]


@dataclass
class ReadMessagePayload(DataClassJSONMixin):
    action: str
    conv_id: ConversationID
    msg_id: MessageID
    inbox_vers: InboxVers
    topic_type: TopicType
    unread_update: Optional[UnreadUpdate]


@dataclass
class SetStatusPayload(DataClassJSONMixin):
    action: str
    conv_id: ConversationID
    status: ConversationStatus
    inbox_vers: InboxVers
    topic_type: TopicType
    unread_update: Optional[UnreadUpdate]


@dataclass
class TeamTypePayload(DataClassJSONMixin):
    action: str
    conv_id: ConversationID
    team_type: TeamType
    inbox_vers: InboxVers
    topic_type: TopicType
    unread_update: Optional[UnreadUpdate]


@dataclass
class SetAppNotificationSettingsPayload(DataClassJSONMixin):
    action: str
    conv_id: ConversationID
    inbox_vers: InboxVers
    settings: ConversationNotificationInfo
    topic_type: TopicType
    unread_update: Optional[UnreadUpdate]


@dataclass
class ExpungePayload(DataClassJSONMixin):
    action: str
    conv_id: ConversationID
    inbox_vers: InboxVers
    expunge: Expunge
    max_msgs: List[MessageSummary]
    topic_type: TopicType
    unread_update: Optional[UnreadUpdate]


@dataclass
class UpdateConversationMembership(DataClassJSONMixin):
    inbox_vers: InboxVers
    joined: List[ConversationMember]
    removed: List[ConversationMember]
    reset: List[ConversationMember]
    previewed: List[ConversationID]
    unread_update: Optional[UnreadUpdate]
    unread_updates: List[UnreadUpdate]


@dataclass
class UpdateConversations(DataClassJSONMixin):
    inbox_vers: InboxVers
    conv_updates: List[ConversationUpdate]


@dataclass
class SetConvRetentionUpdate(DataClassJSONMixin):
    inbox_vers: InboxVers
    conv_id: ConversationID
    policy: RetentionPolicy


@dataclass
class SetTeamRetentionUpdate(DataClassJSONMixin):
    inbox_vers: InboxVers
    team_id: keybase1.TeamID
    policy: RetentionPolicy


@dataclass
class SetConvSettingsUpdate(DataClassJSONMixin):
    inbox_vers: InboxVers
    conv_id: ConversationID
    conv_settings: Optional[ConversationSettings]


@dataclass
class MessageText(DataClassJSONMixin):
    body: str
    payments: List[TextPayment]
    reply_to: Optional[MessageID]
    reply_to_uid: Optional[gregor1.UID]
    user_mentions: List[KnownUserMention]
    team_mentions: List[KnownTeamMention]
    live_location: Optional[LiveLocation]


@dataclass
class MessageSystemChangeRetention(DataClassJSONMixin):
    is_team: bool
    is_inherit: bool
    members_type: ConversationMembersType
    policy: RetentionPolicy
    user: str


@dataclass
class OutboxState__SENDING:
    state: Literal[OutboxStateType.SENDING]
    SENDING: Optional[int]


@dataclass
class OutboxState__ERROR:
    state: Literal[OutboxStateType.ERROR]
    ERROR: Optional[OutboxStateError]


OutboxState = Union[OutboxState__SENDING, OutboxState__ERROR]


@dataclass
class HeaderPlaintextV1(DataClassJSONMixin):
    conv: ConversationIDTriple
    tlf_name: str
    tlf_public: bool
    message_type: MessageType
    prev: List[MessagePreviousPointer]
    sender: gregor1.UID
    sender_device: gregor1.DeviceID
    kbfs_crypt_keys_used: Optional[bool]
    body_hash: Hash
    outbox_info: Optional[OutboxInfo]
    outbox_id: Optional[OutboxID]
    header_signature: Optional[SignatureInfo]
    merkle_root: Optional[MerkleRoot]
    em: Optional[MsgEphemeralMetadata]
    b: Optional[gregor1.UID]


@dataclass
class GetThreadQuery(DataClassJSONMixin):
    mark_as_read: bool
    message_types: List[MessageType]
    disable_resolve_supersedes: bool
    enable_delete_placeholders: bool
    disable_post_process_thread: bool
    before: Optional[gregor1.Time]
    after: Optional[gregor1.Time]
    message_id_control: Optional[MessageIDControl]


@dataclass
class GetInboxLocalQuery(DataClassJSONMixin):
    name: Optional[NameQuery]
    topic_name: Optional[str]
    conv_i_ds: List[ConversationID]
    topic_type: Optional[TopicType]
    tlf_visibility: Optional[keybase1.TLFVisibility]
    before: Optional[gregor1.Time]
    after: Optional[gregor1.Time]
    one_chat_type_per_tlf: Optional[bool]
    status: List[ConversationStatus]
    member_status: List[ConversationMemberStatus]
    unread_only: bool
    read_only: bool
    compute_active_list: bool


@dataclass
class MakePreviewRes(DataClassJSONMixin):
    mime_type: str
    preview_mime_type: Optional[str]
    location: Optional[PreviewLocation]
    metadata: Optional[AssetMetadata]
    base_metadata: Optional[AssetMetadata]


@dataclass
class StaticConfig(DataClassJSONMixin):
    deletable_by_delete_history: List[MessageType]
    builtin_commands: List[BuiltinCommandGroup]


@dataclass
class AdvertiseCommandsParam(DataClassJSONMixin):
    typ: BotCommandsAdvertisementTyp
    commands: List[UserBotCommandInput]
    team_name: Optional[str]


@dataclass
class ListBotCommandsLocalRes(DataClassJSONMixin):
    commands: List[UserBotCommandOutput]
    rate_limits: List[RateLimit]


@dataclass
class MembersUpdateInfo(DataClassJSONMixin):
    conv_id: ConversationID
    members: List[MemberInfo]


@dataclass
class ExpungeInfo(DataClassJSONMixin):
    conv_id: ConversationID
    expunge: Expunge


@dataclass
class PostRemoteRes(DataClassJSONMixin):
    msg_header: MessageServerHeader
    rate_limit: Optional[RateLimit]


@dataclass
class UnreadUpdateFull(DataClassJSONMixin):
    ignore: bool
    inbox_vers: InboxVers
    inbox_sync_status: SyncInboxResType
    updates: List[UnreadUpdate]


@dataclass
class SweepRes(DataClassJSONMixin):
    found_task: bool
    deleted_messages: bool
    expunge: Expunge


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


@dataclass
class BotInfo(DataClassJSONMixin):
    command_convs: List[BotCommandConv]


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


@dataclass
class UnfurlGenericDisplay(DataClassJSONMixin):
    title: str
    url: str
    site_name: str
    favicon: Optional[UnfurlImageDisplay]
    media: Optional[UnfurlImageDisplay]
    publish_time: Optional[int]
    description: Optional[str]
    map_info: Optional[UnfurlGenericMapInfo]


@dataclass
class UICoinFlipStatus(DataClassJSONMixin):
    game_id: str
    phase: UICoinFlipPhase
    progress_text: str
    result_text: str
    commitment_visualization: str
    reveal_visualization: str
    participants: List[UICoinFlipParticipant]
    error_info: Optional[UICoinFlipError]
    result_info: Optional[UICoinFlipResult]


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


@dataclass
class MessageAttachment(DataClassJSONMixin):
    object: Asset
    preview: Optional[Asset]
    previews: List[Asset]
    metadata: bytes
    uploaded: bool


@dataclass
class MessageAttachmentUploaded(DataClassJSONMixin):
    message_id: MessageID
    object: Asset
    previews: List[Asset]
    metadata: bytes


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


@dataclass
class PostFileAttachmentArg(DataClassJSONMixin):
    conversation_id: ConversationID
    tlf_name: str
    visibility: keybase1.TLFVisibility
    filename: str
    title: str
    metadata: bytes
    identify_behavior: keybase1.TLFIdentifyBehavior
    caller_preview: Optional[MakePreviewRes]
    outbox_id: Optional[OutboxID]
    ephemeral_lifetime: Optional[gregor1.DurationSec]


@dataclass
class ReactionUpdate(DataClassJSONMixin):
    reactions: ReactionMap
    target_msg_id: MessageID


@dataclass
class MessageBoxed(DataClassJSONMixin):
    version: MessageBoxedVersion
    server_header: Optional[MessageServerHeader]
    client_header: MessageClientHeader
    header_ciphertext: SealedData
    body_ciphertext: EncryptedData
    verify_key: bytes
    key_generation: int


@dataclass
class BotInfoResponse__UPTODATE:
    typ: Literal[BotInfoResponseTyp.UPTODATE]
    UPTODATE: None


@dataclass
class BotInfoResponse__INFO:
    typ: Literal[BotInfoResponseTyp.INFO]
    INFO: Optional[BotInfo]


BotInfoResponse = Union[BotInfoResponse__UPTODATE, BotInfoResponse__INFO]


@dataclass
class UnfurlGeneric(DataClassJSONMixin):
    title: str
    url: str
    site_name: str
    favicon: Optional[Asset]
    image: Optional[Asset]
    publish_time: Optional[int]
    description: Optional[str]
    map_info: Optional[UnfurlGenericMapInfo]


@dataclass
class UnfurlGiphy(DataClassJSONMixin):
    favicon: Optional[Asset]
    image: Optional[Asset]
    video: Optional[Asset]


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


@dataclass
class UIMessageUnfurlInfo(DataClassJSONMixin):
    unfurl_message_id: MessageID
    url: str
    unfurl: UnfurlDisplay
    is_collapsed: bool


@dataclass
class NewMessagePayload(DataClassJSONMixin):
    action: str
    conv_id: ConversationID
    message: MessageBoxed
    inbox_vers: InboxVers
    topic_type: TopicType
    unread_update: Optional[UnreadUpdate]
    max_msgs: List[MessageSummary]


@dataclass
class LoadFlipRes(DataClassJSONMixin):
    status: UICoinFlipStatus
    rate_limits: List[RateLimit]
    identify_failures: List[keybase1.TLFIdentifyFailure]


@dataclass
class ReactionUpdateNotif(DataClassJSONMixin):
    conv_id: ConversationID
    user_reacjis: keybase1.UserReacjis
    reaction_updates: List[ReactionUpdate]


@dataclass
class ThreadViewBoxed(DataClassJSONMixin):
    messages: List[MessageBoxed]
    pagination: Optional[Pagination]


@dataclass
class GetMessagesRemoteRes(DataClassJSONMixin):
    msgs: List[MessageBoxed]
    rate_limit: Optional[RateLimit]


@dataclass
class GetBotInfoRes(DataClassJSONMixin):
    response: BotInfoResponse
    rate_limit: Optional[RateLimit]


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


@dataclass
class GetThreadRemoteRes(DataClassJSONMixin):
    thread: ThreadViewBoxed
    members_type: ConversationMembersType
    visibility: keybase1.TLFVisibility
    rate_limit: Optional[RateLimit]


@dataclass
class UnfurlResult(DataClassJSONMixin):
    unfurl: Unfurl
    url: str


@dataclass
class MessageUnfurl(DataClassJSONMixin):
    unfurl: UnfurlResult
    message_id: MessageID


@dataclass
class MsgContent(DataClassJSONMixin):
    type: str
    text: Optional[MessageText]
    attachment: Optional[MessageAttachment]
    edit: Optional[MessageEdit]
    reaction: Optional[MessageReaction]
    delete: Optional[MessageDelete]
    metadata: Optional[MessageConversationMetadata]
    headline: Optional[MessageHeadline]
    attachment_uploaded: Optional[MessageAttachmentUploaded]
    system: Optional[MessageSystem]
    send_payment: Optional[MessageSendPayment]
    request_payment: Optional[MessageRequestPayment]
    unfurl: Optional[MessageUnfurl]
    flip: Optional[MsgFlipContent]


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


@dataclass
class MsgSummary(DataClassJSONMixin):
    id: MessageID
    conversation_id: str
    channel: ChatChannel
    sender: MsgSender
    sent_at: int
    sent_at_ms: int
    content: MsgContent
    prev: List[MessagePreviousPointer]
    unread: bool
    revoked_device: Optional[bool]
    offline: Optional[bool]
    kbfs_encrypted: Optional[bool]
    is_ephemeral: Optional[bool]
    is_ephemeral_expired: Optional[bool]
    e_time: Optional[gregor1.Time]
    reactions: Optional[ReactionMap]
    has_pairwise_macs: Optional[bool]
    at_mention_usernames: Optional[List[str]]
    channel_mention: Optional[str]
    channel_name_mentions: Optional[List[UIChannelNameMention]]


@dataclass
class BodyPlaintextV1(DataClassJSONMixin):
    message_body: MessageBody


@dataclass
class BodyPlaintextV2(DataClassJSONMixin):
    message_body: MessageBody
    mi: BodyPlaintextMetaInfo


@dataclass
class MessagePlaintext(DataClassJSONMixin):
    client_header: MessageClientHeader
    message_body: MessageBody
    supersedes_outbox_id: Optional[OutboxID]


@dataclass
class Message(DataClassJSONMixin):
    msg: Optional[MsgSummary]
    error: Optional[str]


@dataclass
class MsgNotification(DataClassJSONMixin):
    type: str
    source: str
    msg: Optional[MsgSummary]
    error: Optional[str]
    pagination: Optional[UIPagination]


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


@dataclass
class Thread(DataClassJSONMixin):
    messages: List[Message]
    pagination: Optional[Pagination]
    offline: Optional[bool]
    identify_failures: Optional[List[keybase1.TLFIdentifyFailure]]
    ratelimits: Optional[List[RateLimitRes]]
