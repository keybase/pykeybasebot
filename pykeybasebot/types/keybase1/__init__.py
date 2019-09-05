"""keybase.1

Auto-generated to Python types by avdl-compiler v1.4.1 (https://github.com/keybase/node-avdl-compiler)
Input files:
 - ../client/protocol/avdl/keybase1/account.avdl
 - ../client/protocol/avdl/keybase1/apiserver.avdl
 - ../client/protocol/avdl/keybase1/appstate.avdl
 - ../client/protocol/avdl/keybase1/audit.avdl
 - ../client/protocol/avdl/keybase1/avatars.avdl
 - ../client/protocol/avdl/keybase1/backend_common.avdl
 - ../client/protocol/avdl/keybase1/badger.avdl
 - ../client/protocol/avdl/keybase1/block.avdl
 - ../client/protocol/avdl/keybase1/btc.avdl
 - ../client/protocol/avdl/keybase1/common.avdl
 - ../client/protocol/avdl/keybase1/config.avdl
 - ../client/protocol/avdl/keybase1/constants.avdl
 - ../client/protocol/avdl/keybase1/contacts.avdl
 - ../client/protocol/avdl/keybase1/crypto.avdl
 - ../client/protocol/avdl/keybase1/cryptocurrency.avdl
 - ../client/protocol/avdl/keybase1/ctl.avdl
 - ../client/protocol/avdl/keybase1/debugging.avdl
 - ../client/protocol/avdl/keybase1/delegate_ui_ctl.avdl
 - ../client/protocol/avdl/keybase1/device.avdl
 - ../client/protocol/avdl/keybase1/emails.avdl
 - ../client/protocol/avdl/keybase1/ephemeral.avdl
 - ../client/protocol/avdl/keybase1/favorite.avdl
 - ../client/protocol/avdl/keybase1/fs.avdl
 - ../client/protocol/avdl/keybase1/git.avdl
 - ../client/protocol/avdl/keybase1/gpg_common.avdl
 - ../client/protocol/avdl/keybase1/gpg_ui.avdl
 - ../client/protocol/avdl/keybase1/gregor.avdl
 - ../client/protocol/avdl/keybase1/gregor_ui.avdl
 - ../client/protocol/avdl/keybase1/home.avdl
 - ../client/protocol/avdl/keybase1/home_ui.avdl
 - ../client/protocol/avdl/keybase1/identify.avdl
 - ../client/protocol/avdl/keybase1/identify3.avdl
 - ../client/protocol/avdl/keybase1/identify3_common.avdl
 - ../client/protocol/avdl/keybase1/identify3_ui.avdl
 - ../client/protocol/avdl/keybase1/identify_common.avdl
 - ../client/protocol/avdl/keybase1/identify_ui.avdl
 - ../client/protocol/avdl/keybase1/implicit_team_migration.avdl
 - ../client/protocol/avdl/keybase1/install.avdl
 - ../client/protocol/avdl/keybase1/kbfs.avdl
 - ../client/protocol/avdl/keybase1/kbfs_common.avdl
 - ../client/protocol/avdl/keybase1/kbfs_git.avdl
 - ../client/protocol/avdl/keybase1/kbfsmount.avdl
 - ../client/protocol/avdl/keybase1/kex2provisionee.avdl
 - ../client/protocol/avdl/keybase1/kex2provisionee2.avdl
 - ../client/protocol/avdl/keybase1/kex2provisioner.avdl
 - ../client/protocol/avdl/keybase1/log.avdl
 - ../client/protocol/avdl/keybase1/log_ui.avdl
 - ../client/protocol/avdl/keybase1/login.avdl
 - ../client/protocol/avdl/keybase1/login_ui.avdl
 - ../client/protocol/avdl/keybase1/logsend.avdl
 - ../client/protocol/avdl/keybase1/merkle.avdl
 - ../client/protocol/avdl/keybase1/merkle_store.avdl
 - ../client/protocol/avdl/keybase1/metadata.avdl
 - ../client/protocol/avdl/keybase1/metadata_update.avdl
 - ../client/protocol/avdl/keybase1/notify_app.avdl
 - ../client/protocol/avdl/keybase1/notify_audit.avdl
 - ../client/protocol/avdl/keybase1/notify_badges.avdl
 - ../client/protocol/avdl/keybase1/notify_can_user_perform.avdl
 - ../client/protocol/avdl/keybase1/notify_ctl.avdl
 - ../client/protocol/avdl/keybase1/notify_device_clone.avdl
 - ../client/protocol/avdl/keybase1/notify_email.avdl
 - ../client/protocol/avdl/keybase1/notify_ephemeral.avdl
 - ../client/protocol/avdl/keybase1/notify_favorites.avdl
 - ../client/protocol/avdl/keybase1/notify_fs.avdl
 - ../client/protocol/avdl/keybase1/notify_fs_request.avdl
 - ../client/protocol/avdl/keybase1/notify_keyfamily.avdl
 - ../client/protocol/avdl/keybase1/notify_paperkey.avdl
 - ../client/protocol/avdl/keybase1/notify_pgp.avdl
 - ../client/protocol/avdl/keybase1/notify_phone.avdl
 - ../client/protocol/avdl/keybase1/notify_runtimestats.avdl
 - ../client/protocol/avdl/keybase1/notify_service.avdl
 - ../client/protocol/avdl/keybase1/notify_session.avdl
 - ../client/protocol/avdl/keybase1/notify_team.avdl
 - ../client/protocol/avdl/keybase1/notify_teambot.avdl
 - ../client/protocol/avdl/keybase1/notify_tracking.avdl
 - ../client/protocol/avdl/keybase1/notify_unverified_team_list.avdl
 - ../client/protocol/avdl/keybase1/notify_users.avdl
 - ../client/protocol/avdl/keybase1/os.avdl
 - ../client/protocol/avdl/keybase1/paperprovision.avdl
 - ../client/protocol/avdl/keybase1/passphrase_common.avdl
 - ../client/protocol/avdl/keybase1/pgp.avdl
 - ../client/protocol/avdl/keybase1/pgp_ui.avdl
 - ../client/protocol/avdl/keybase1/phone_numbers.avdl
 - ../client/protocol/avdl/keybase1/pprof.avdl
 - ../client/protocol/avdl/keybase1/process.avdl
 - ../client/protocol/avdl/keybase1/prove.avdl
 - ../client/protocol/avdl/keybase1/prove_common.avdl
 - ../client/protocol/avdl/keybase1/prove_ui.avdl
 - ../client/protocol/avdl/keybase1/provision_ui.avdl
 - ../client/protocol/avdl/keybase1/quota.avdl
 - ../client/protocol/avdl/keybase1/reachability.avdl
 - ../client/protocol/avdl/keybase1/rekey.avdl
 - ../client/protocol/avdl/keybase1/rekey_ui.avdl
 - ../client/protocol/avdl/keybase1/reset.avdl
 - ../client/protocol/avdl/keybase1/revoke.avdl
 - ../client/protocol/avdl/keybase1/saltpack.avdl
 - ../client/protocol/avdl/keybase1/saltpack_ui.avdl
 - ../client/protocol/avdl/keybase1/scanproofs.avdl
 - ../client/protocol/avdl/keybase1/secret_ui.avdl
 - ../client/protocol/avdl/keybase1/secretkeys.avdl
 - ../client/protocol/avdl/keybase1/selfprovision.avdl
 - ../client/protocol/avdl/keybase1/session.avdl
 - ../client/protocol/avdl/keybase1/signup.avdl
 - ../client/protocol/avdl/keybase1/sigs.avdl
 - ../client/protocol/avdl/keybase1/simple_fs.avdl
 - ../client/protocol/avdl/keybase1/stream_ui.avdl
 - ../client/protocol/avdl/keybase1/teambot.avdl
 - ../client/protocol/avdl/keybase1/teams.avdl
 - ../client/protocol/avdl/keybase1/teams_ui.avdl
 - ../client/protocol/avdl/keybase1/test.avdl
 - ../client/protocol/avdl/keybase1/tlf.avdl
 - ../client/protocol/avdl/keybase1/tlf_keys.avdl
 - ../client/protocol/avdl/keybase1/track.avdl
 - ../client/protocol/avdl/keybase1/ui.avdl
 - ../client/protocol/avdl/keybase1/upk.avdl
 - ../client/protocol/avdl/keybase1/user.avdl
 - ../client/protocol/avdl/keybase1/usersearch.avdl
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union

from dataclasses_json import config, dataclass_json
from typing_extensions import Literal

import gregor1


@dataclass_json
@dataclass
class HasServerKeysRes:
    has_server_keys: bool = field(metadata=config(field_name="hasServerKeys"))


@dataclass_json
@dataclass
class APIRes:
    status: str = field(metadata=config(field_name="status"))
    body: str = field(metadata=config(field_name="body"))
    http_status: int = field(metadata=config(field_name="httpStatus"))
    app_status: str = field(metadata=config(field_name="appStatus"))


class MobileAppState(Enum):
    FOREGROUND = "foreground"
    BACKGROUND = "background"
    INACTIVE = "inactive"
    BACKGROUNDACTIVE = "backgroundactive"


class MobileNetworkState(Enum):
    NONE = "none"
    WIFI = "wifi"
    CELLULAR = "cellular"
    UNKNOWN = "unknown"
    NOTAVAILABLE = "notavailable"


class BoxAuditAttemptResult(Enum):
    FAILURE_RETRYABLE = "failure_retryable"
    FAILURE_MALICIOUS_SERVER = "failure_malicious_server"
    OK_VERIFIED = "ok_verified"
    OK_NOT_ATTEMPTED_ROLE = "ok_not_attempted_role"
    OK_NOT_ATTEMPTED_OPENTEAM = "ok_not_attempted_openteam"
    OK_NOT_ATTEMPTED_SUBTEAM = "ok_not_attempted_subteam"


AvatarUrl = str
AvatarFormat = str


class BlockType(Enum):
    DATA = "data"
    MD = "md"
    GIT = "git"


@dataclass_json
@dataclass
class ChallengeInfo:
    now: int = field(metadata=config(field_name="now"))
    challenge: str = field(metadata=config(field_name="challenge"))


class BlockStatus(Enum):
    UNKNOWN = "unknown"
    LIVE = "live"
    ARCHIVED = "archived"


BlockRefNonce = Optional[str]


@dataclass_json
@dataclass
class BlockPingResponse:
    pass


Time = int
UnixTime = int
DurationSec = float


@dataclass_json
@dataclass
class StringKVPair:
    key: str = field(metadata=config(field_name="key"))
    value: str = field(metadata=config(field_name="value"))


UID = str
DeviceID = str
SigID = str
LeaseID = str
KID = str
PhoneNumber = str
RawPhoneNumber = str
RegionCode = str
LinkID = str
BinaryLinkID = bytes
BinaryKID = bytes
TLFID = str
TeamID = str
UserOrTeamID = str
GitRepoName = str
HashMeta = bytes


class TeamType(Enum):
    NONE = "none"
    LEGACY = "legacy"
    MODERN = "modern"


class TLFVisibility(Enum):
    ANY = "any"
    PUBLIC = "public"
    PRIVATE = "private"


Seqno = int


class SeqType(Enum):
    NONE = "none"
    PUBLIC = "public"
    PRIVATE = "private"
    SEMIPRIVATE = "semiprivate"
    USER_PRIVATE_HIDDEN = "user_private_hidden"
    TEAM_PRIVATE_HIDDEN = "team_private_hidden"


Bytes32 = Optional[str]


@dataclass_json
@dataclass
class Text:
    data: str = field(metadata=config(field_name="data"))
    markup: bool = field(metadata=config(field_name="markup"))


@dataclass_json
@dataclass
class PGPIdentity:
    username: str = field(metadata=config(field_name="username"))
    comment: str = field(metadata=config(field_name="comment"))
    email: str = field(metadata=config(field_name="email"))


class DeviceType(Enum):
    DESKTOP = "desktop"
    MOBILE = "mobile"


@dataclass_json
@dataclass
class Stream:
    fd: int = field(metadata=config(field_name="fd"))


class LogLevel(Enum):
    NONE = "none"
    DEBUG = "debug"
    INFO = "info"
    NOTICE = "notice"
    WARN = "warn"
    ERROR = "error"
    CRITICAL = "critical"
    FATAL = "fatal"


class ClientType(Enum):
    NONE = "none"
    CLI = "cli"
    GUI_MAIN = "gui_main"
    KBFS = "kbfs"
    GUI_HELPER = "gui_helper"


@dataclass_json
@dataclass
class KBFSPathInfo:
    standard_path: str = field(metadata=config(field_name="standardPath"))
    deeplink_path: str = field(metadata=config(field_name="deeplinkPath"))
    platform_after_mount_path: str = field(
        metadata=config(field_name="platformAfterMountPath")
    )


PerUserKeyGeneration = int


class UserOrTeamResult(Enum):
    USER = "user"
    TEAM = "team"


class MerkleTreeID(Enum):
    MASTER = "master"
    KBFS_PUBLIC = "kbfs_public"
    KBFS_PRIVATE = "kbfs_private"
    KBFS_PRIVATETEAM = "kbfs_privateteam"


SocialAssertionService = str
FullName = str


class FullNamePackageVersion(Enum):
    V0 = "v0"
    V1 = "v1"
    V2 = "v2"


@dataclass_json
@dataclass
class ImageCropRect:
    x_0: int = field(metadata=config(field_name="x0"))
    y_0: int = field(metadata=config(field_name="y0"))
    x_1: int = field(metadata=config(field_name="x1"))
    y_1: int = field(metadata=config(field_name="y1"))


class IdentityVisibility(Enum):
    PRIVATE = "private"
    PUBLIC = "public"


@dataclass_json
@dataclass
class SizedImage:
    path: str = field(metadata=config(field_name="path"))
    width: int = field(metadata=config(field_name="width"))


class OfflineAvailability(Enum):
    NONE = "none"
    BEST_EFFORT = "best_effort"


ReacjiSkinTone = int


@dataclass_json
@dataclass
class SessionStatus:
    session_for: str = field(metadata=config(field_name="SessionFor"))
    loaded: bool = field(metadata=config(field_name="Loaded"))
    cleared: bool = field(metadata=config(field_name="Cleared"))
    salt_only: bool = field(metadata=config(field_name="SaltOnly"))
    expired: bool = field(metadata=config(field_name="Expired"))


@dataclass_json
@dataclass
class PlatformInfo:
    os: str = field(metadata=config(field_name="os"))
    os_version: str = field(metadata=config(field_name="osVersion"))
    arch: str = field(metadata=config(field_name="arch"))
    go_version: str = field(metadata=config(field_name="goVersion"))


@dataclass_json
@dataclass
class LoadDeviceErr:
    where: str = field(metadata=config(field_name="where"))
    desc: str = field(metadata=config(field_name="desc"))


@dataclass_json
@dataclass
class DirSizeInfo:
    num_files: int = field(metadata=config(field_name="numFiles"))
    name: str = field(metadata=config(field_name="name"))
    human_size: str = field(metadata=config(field_name="humanSize"))


@dataclass_json
@dataclass
class KbClientStatus:
    version: str = field(metadata=config(field_name="version"))


@dataclass_json
@dataclass
class KbServiceStatus:
    version: str = field(metadata=config(field_name="version"))
    running: bool = field(metadata=config(field_name="running"))
    pid: str = field(metadata=config(field_name="pid"))
    log: str = field(metadata=config(field_name="log"))
    ek_log: str = field(metadata=config(field_name="ekLog"))


@dataclass_json
@dataclass
class KBFSStatus:
    version: str = field(metadata=config(field_name="version"))
    installed_version: str = field(metadata=config(field_name="installedVersion"))
    running: bool = field(metadata=config(field_name="running"))
    pid: str = field(metadata=config(field_name="pid"))
    log: str = field(metadata=config(field_name="log"))
    mount: str = field(metadata=config(field_name="mount"))


@dataclass_json
@dataclass
class DesktopStatus:
    version: str = field(metadata=config(field_name="version"))
    running: bool = field(metadata=config(field_name="running"))
    log: str = field(metadata=config(field_name="log"))


@dataclass_json
@dataclass
class UpdaterStatus:
    log: str = field(metadata=config(field_name="log"))


@dataclass_json
@dataclass
class StartStatus:
    log: str = field(metadata=config(field_name="log"))


@dataclass_json
@dataclass
class GitStatus:
    log: str = field(metadata=config(field_name="log"))


LogSendID = str


@dataclass_json
@dataclass
class AllProvisionedUsernames:
    default_username: str = field(metadata=config(field_name="defaultUsername"))
    provisioned_usernames: List[str] = field(
        metadata=config(field_name="provisionedUsernames")
    )
    has_provisioned_user: bool = field(metadata=config(field_name="hasProvisionedUser"))


class ForkType(Enum):
    NONE = "none"
    AUTO = "auto"
    WATCHDOG = "watchdog"
    LAUNCHD = "launchd"
    SYSTEMD = "systemd"


@dataclass_json
@dataclass
class ConfigValue:
    is_null: bool = field(metadata=config(field_name="isNull"))
    b: Optional[bool] = field(metadata=config(field_name="b"))
    i: Optional[int] = field(metadata=config(field_name="i"))
    s: Optional[str] = field(metadata=config(field_name="s"))
    o: Optional[str] = field(metadata=config(field_name="o"))


@dataclass_json
@dataclass
class OutOfDateInfo:
    upgrade_to: str = field(metadata=config(field_name="upgradeTo"))
    upgrade_uri: str = field(metadata=config(field_name="upgradeURI"))
    custom_message: str = field(metadata=config(field_name="customMessage"))
    critical_clock_skew: int = field(metadata=config(field_name="criticalClockSkew"))


class UpdateInfoStatus(Enum):
    UP_TO_DATE = "up_to_date"
    NEED_UPDATE = "need_update"
    CRITICALLY_OUT_OF_DATE = "critically_out_of_date"


class UpdateInfoStatus2(Enum):
    OK = "ok"
    SUGGESTED = "suggested"
    CRITICAL = "critical"


@dataclass_json
@dataclass
class UpdateDetails:
    message: str = field(metadata=config(field_name="message"))


class ProxyType(Enum):
    No_Proxy = "no_proxy"
    HTTP_Connect = "http_connect"
    Socks = "socks"


class StatusCode(Enum):
    SCOk = "scok"
    SCInputError = "scinputerror"
    SCLoginRequired = "scloginrequired"
    SCBadSession = "scbadsession"
    SCBadLoginUserNotFound = "scbadloginusernotfound"
    SCBadLoginPassword = "scbadloginpassword"
    SCNotFound = "scnotfound"
    SCThrottleControl = "scthrottlecontrol"
    SCDeleted = "scdeleted"
    SCGeneric = "scgeneric"
    SCAlreadyLoggedIn = "scalreadyloggedin"
    SCExists = "scexists"
    SCCanceled = "sccanceled"
    SCInputCanceled = "scinputcanceled"
    SCBadUsername = "scbadusername"
    SCOffline = "scoffline"
    SCReloginRequired = "screloginrequired"
    SCResolutionFailed = "scresolutionfailed"
    SCProfileNotPublic = "scprofilenotpublic"
    SCIdentifyFailed = "scidentifyfailed"
    SCTrackingBroke = "sctrackingbroke"
    SCWrongCryptoFormat = "scwrongcryptoformat"
    SCDecryptionError = "scdecryptionerror"
    SCInvalidAddress = "scinvalidaddress"
    SCNoSession = "scnosession"
    SCAccountReset = "scaccountreset"
    SCIdentifiesFailed = "scidentifiesfailed"
    SCNoSpaceOnDevice = "scnospaceondevice"
    SCMerkleClientError = "scmerkleclienterror"
    SCBadEmail = "scbademail"
    SCRateLimit = "scratelimit"
    SCBadSignupUsernameTaken = "scbadsignupusernametaken"
    SCBadInvitationCode = "scbadinvitationcode"
    SCBadSignupTeamName = "scbadsignupteamname"
    SCFeatureFlag = "scfeatureflag"
    SCEmailTaken = "scemailtaken"
    SCEmailAlreadyAdded = "scemailalreadyadded"
    SCEmailLimitExceeded = "scemaillimitexceeded"
    SCEmailCannotDeletePrimary = "scemailcannotdeleteprimary"
    SCEmailUnknown = "scemailunknown"
    SCMissingResult = "scmissingresult"
    SCKeyNotFound = "sckeynotfound"
    SCKeyCorrupted = "sckeycorrupted"
    SCKeyInUse = "sckeyinuse"
    SCKeyBadGen = "sckeybadgen"
    SCKeyNoSecret = "sckeynosecret"
    SCKeyBadUIDs = "sckeybaduids"
    SCKeyNoActive = "sckeynoactive"
    SCKeyNoSig = "sckeynosig"
    SCKeyBadSig = "sckeybadsig"
    SCKeyBadEldest = "sckeybadeldest"
    SCKeyNoEldest = "sckeynoeldest"
    SCKeyDuplicateUpdate = "sckeyduplicateupdate"
    SCSibkeyAlreadyExists = "scsibkeyalreadyexists"
    SCDecryptionKeyNotFound = "scdecryptionkeynotfound"
    SCKeyNoPGPEncryption = "sckeynopgpencryption"
    SCKeyNoNaClEncryption = "sckeynonaclencryption"
    SCKeySyncedPGPNotFound = "sckeysyncedpgpnotfound"
    SCKeyNoMatchingGPG = "sckeynomatchinggpg"
    SCKeyRevoked = "sckeyrevoked"
    SCSigCannotVerify = "scsigcannotverify"
    SCSigWrongKey = "scsigwrongkey"
    SCSigOldSeqno = "scsigoldseqno"
    SCSigCreationDisallowed = "scsigcreationdisallowed"
    SCSigMissingRatchet = "scsigmissingratchet"
    SCSigBadTotalOrder = "scsigbadtotalorder"
    SCBadTrackSession = "scbadtracksession"
    SCDeviceBadName = "scdevicebadname"
    SCDeviceNameInUse = "scdevicenameinuse"
    SCDeviceNotFound = "scdevicenotfound"
    SCDeviceMismatch = "scdevicemismatch"
    SCDeviceRequired = "scdevicerequired"
    SCDevicePrevProvisioned = "scdeviceprevprovisioned"
    SCDeviceNoProvision = "scdevicenoprovision"
    SCDeviceProvisionViaDevice = "scdeviceprovisionviadevice"
    SCRevokeCurrentDevice = "screvokecurrentdevice"
    SCRevokeLastDevice = "screvokelastdevice"
    SCDeviceProvisionOffline = "scdeviceprovisionoffline"
    SCRevokeLastDevicePGP = "screvokelastdevicepgp"
    SCStreamExists = "scstreamexists"
    SCStreamNotFound = "scstreamnotfound"
    SCStreamWrongKind = "scstreamwrongkind"
    SCStreamEOF = "scstreameof"
    SCGenericAPIError = "scgenericapierror"
    SCAPINetworkError = "scapinetworkerror"
    SCTimeout = "sctimeout"
    SCProofError = "scprooferror"
    SCIdentificationExpired = "scidentificationexpired"
    SCSelfNotFound = "scselfnotfound"
    SCBadKexPhrase = "scbadkexphrase"
    SCNoUIDelegation = "scnouidelegation"
    SCNoUI = "scnoui"
    SCGPGUnavailable = "scgpgunavailable"
    SCInvalidVersionError = "scinvalidversionerror"
    SCOldVersionError = "scoldversionerror"
    SCInvalidLocationError = "scinvalidlocationerror"
    SCServiceStatusError = "scservicestatuserror"
    SCInstallError = "scinstallerror"
    SCLoadKextError = "scloadkexterror"
    SCLoadKextPermError = "scloadkextpermerror"
    SCGitInternal = "scgitinternal"
    SCGitRepoAlreadyExists = "scgitrepoalreadyexists"
    SCGitInvalidRepoName = "scgitinvalidreponame"
    SCGitCannotDelete = "scgitcannotdelete"
    SCGitRepoDoesntExist = "scgitrepodoesntexist"
    SCLoginStateTimeout = "scloginstatetimeout"
    SCChatInternal = "scchatinternal"
    SCChatRateLimit = "scchatratelimit"
    SCChatConvExists = "scchatconvexists"
    SCChatUnknownTLFID = "scchatunknowntlfid"
    SCChatNotInConv = "scchatnotinconv"
    SCChatBadMsg = "scchatbadmsg"
    SCChatBroadcast = "scchatbroadcast"
    SCChatAlreadySuperseded = "scchatalreadysuperseded"
    SCChatAlreadyDeleted = "scchatalreadydeleted"
    SCChatTLFFinalized = "scchattlffinalized"
    SCChatCollision = "scchatcollision"
    SCIdentifySummaryError = "scidentifysummaryerror"
    SCNeedSelfRekey = "scneedselfrekey"
    SCNeedOtherRekey = "scneedotherrekey"
    SCChatMessageCollision = "scchatmessagecollision"
    SCChatDuplicateMessage = "scchatduplicatemessage"
    SCChatClientError = "scchatclienterror"
    SCChatNotInTeam = "scchatnotinteam"
    SCChatStalePreviousState = "scchatstalepreviousstate"
    SCChatEphemeralRetentionPolicyViolatedError = (
        "scchatephemeralretentionpolicyviolatederror"
    )
    SCTeamBadMembership = "scteambadmembership"
    SCTeamSelfNotOwner = "scteamselfnotowner"
    SCTeamNotFound = "scteamnotfound"
    SCTeamExists = "scteamexists"
    SCTeamReadError = "scteamreaderror"
    SCTeamWritePermDenied = "scteamwritepermdenied"
    SCTeamBadGeneration = "scteambadgeneration"
    SCNoOp = "scnoop"
    SCTeamInviteBadToken = "scteaminvitebadtoken"
    SCTeamTarDuplicate = "scteamtarduplicate"
    SCTeamTarNotFound = "scteamtarnotfound"
    SCTeamMemberExists = "scteammemberexists"
    SCTeamNotReleased = "scteamnotreleased"
    SCTeamPermanentlyLeft = "scteampermanentlyleft"
    SCTeamNeedRootId = "scteamneedrootid"
    SCTeamHasLiveChildren = "scteamhaslivechildren"
    SCTeamDeleteError = "scteamdeleteerror"
    SCTeamBadRootTeam = "scteambadrootteam"
    SCTeamNameConflictsWithUser = "scteamnameconflictswithuser"
    SCTeamDeleteNoUpPointer = "scteamdeletenouppointer"
    SCTeamNeedOwner = "scteamneedowner"
    SCTeamNoOwnerAllowed = "scteamnoownerallowed"
    SCTeamImplicitNoNonSbs = "scteamimplicitnononsbs"
    SCTeamImplicitBadHash = "scteamimplicitbadhash"
    SCTeamImplicitBadName = "scteamimplicitbadname"
    SCTeamImplicitClash = "scteamimplicitclash"
    SCTeamImplicitDuplicate = "scteamimplicitduplicate"
    SCTeamImplicitBadOp = "scteamimplicitbadop"
    SCTeamImplicitBadRole = "scteamimplicitbadrole"
    SCTeamImplicitNotFound = "scteamimplicitnotfound"
    SCTeamBadAdminSeqnoType = "scteambadadminseqnotype"
    SCTeamImplicitBadAdd = "scteamimplicitbadadd"
    SCTeamImplicitBadRemove = "scteamimplicitbadremove"
    SCTeamInviteTokenReused = "scteaminvitetokenreused"
    SCTeamKeyMaskNotFound = "scteamkeymasknotfound"
    SCTeamBanned = "scteambanned"
    SCTeamInvalidBan = "scteaminvalidban"
    SCTeamShowcasePermDenied = "scteamshowcasepermdenied"
    SCTeamProvisionalCanKey = "scteamprovisionalcankey"
    SCTeamProvisionalCannotKey = "scteamprovisionalcannotkey"
    SCTeamFTLOutdated = "scteamftloutdated"
    SCEphemeralKeyBadGeneration = "scephemeralkeybadgeneration"
    SCEphemeralKeyUnexpectedBox = "scephemeralkeyunexpectedbox"
    SCEphemeralKeyMissingBox = "scephemeralkeymissingbox"
    SCEphemeralKeyWrongNumberOfKeys = "scephemeralkeywrongnumberofkeys"
    SCEphemeralKeyMismatchedKey = "scephemeralkeymismatchedkey"
    SCEphemeralPairwiseMACsMissingUIDs = "scephemeralpairwisemacsmissinguids"
    SCEphemeralDeviceAfterEK = "scephemeraldeviceafterek"
    SCEphemeralMemberAfterEK = "scephemeralmemberafterek"
    SCEphemeralDeviceStale = "scephemeraldevicestale"
    SCEphemeralUserStale = "scephemeraluserstale"
    SCStellarError = "scstellarerror"
    SCStellarBadInput = "scstellarbadinput"
    SCStellarWrongRevision = "scstellarwrongrevision"
    SCStellarMissingBundle = "scstellarmissingbundle"
    SCStellarBadPuk = "scstellarbadpuk"
    SCStellarMissingAccount = "scstellarmissingaccount"
    SCStellarBadPrev = "scstellarbadprev"
    SCStellarWrongPrimary = "scstellarwrongprimary"
    SCStellarUnsupportedCurrency = "scstellarunsupportedcurrency"
    SCStellarNeedDisclaimer = "scstellarneeddisclaimer"
    SCStellarDeviceNotMobile = "scstellardevicenotmobile"
    SCStellarMobileOnlyPurgatory = "scstellarmobileonlypurgatory"
    SCStellarIncompatibleVersion = "scstellarincompatibleversion"
    SCNISTWrongSize = "scnistwrongsize"
    SCNISTBadMode = "scnistbadmode"
    SCNISTHashWrongSize = "scnisthashwrongsize"
    SCNISTSigWrongSize = "scnistsigwrongsize"
    SCNISTSigBadInput = "scnistsigbadinput"
    SCNISTSigBadUID = "scnistsigbaduid"
    SCNISTSigBadDeviceID = "scnistsigbaddeviceid"
    SCNISTSigBadNonce = "scnistsigbadnonce"
    SCNISTNoSigOrHash = "scnistnosigorhash"
    SCNISTExpired = "scnistexpired"
    SCNISTSigRevoked = "scnistsigrevoked"
    SCNISTKeyRevoked = "scnistkeyrevoked"
    SCNISTUserDeleted = "scnistuserdeleted"
    SCNISTNoDevice = "scnistnodevice"
    SCNISTSigCannot_verify = "scnistsigcannot_verify"
    SCNISTReplay = "scnistreplay"
    SCNISTSigBadLifetime = "scnistsigbadlifetime"
    SCNISTNotFound = "scnistnotfound"
    SCNISTBadClock = "scnistbadclock"
    SCNISTSigBadCtime = "scnistsigbadctime"
    SCBadSignupUsernameDeleted = "scbadsignupusernamedeleted"
    SCPhoneNumberUnknown = "scphonenumberunknown"
    SCPhoneNumberAlreadyVerified = "scphonenumberalreadyverified"
    SCPhoneNumberVerificationCodeExpired = "scphonenumberverificationcodeexpired"
    SCPhoneNumberWrongVerificationCode = "scphonenumberwrongverificationcode"
    SCPhoneNumberLimitExceeded = "scphonenumberlimitexceeded"
    SCNoPaperKeys = "scnopaperkeys"
    SCTeambotKeyGenerationExists = "scteambotkeygenerationexists"
    SCTeambotKeyOldBoxedGeneration = "scteambotkeyoldboxedgeneration"
    SCTeambotKeyBadGeneration = "scteambotkeybadgeneration"


ED25519PublicKey = Optional[str]
ED25519Signature = Optional[str]
EncryptedBytes32 = Optional[str]
BoxNonce = Optional[str]
BoxPublicKey = Optional[str]


@dataclass_json
@dataclass
class RegisterAddressRes:
    type: str = field(metadata=config(field_name="type"))
    family: str = field(metadata=config(field_name="family"))


class ExitCode(Enum):
    OK = "ok"
    NOTOK = "notok"
    RESTART = "restart"


class DbType(Enum):
    MAIN = "main"
    CHAT = "chat"
    FS_BLOCK_CACHE = "fs_block_cache"
    FS_BLOCK_CACHE_META = "fs_block_cache_meta"
    FS_SYNC_BLOCK_CACHE = "fs_sync_block_cache"
    FS_SYNC_BLOCK_CACHE_META = "fs_sync_block_cache_meta"


DbValue = bytes


@dataclass_json
@dataclass
class FirstStepResult:
    val_plus_two: int = field(metadata=config(field_name="valPlusTwo"))


EkGeneration = int


class TeamEphemeralKeyType(Enum):
    TEAM = "team"
    TEAMBOT = "teambot"


class FolderType(Enum):
    UNKNOWN = "unknown"
    PRIVATE = "private"
    PUBLIC = "public"
    TEAM = "team"


class FolderConflictType(Enum):
    NONE = "none"
    IN_CONFLICT = "in_conflict"
    IN_CONFLICT_AND_STUCK = "in_conflict_and_stuck"
    CLEARED_CONFLICT = "cleared_conflict"


class ConflictStateType(Enum):
    NormalView = "normalview"
    ManualResolvingLocalView = "manualresolvinglocalview"


@dataclass_json
@dataclass
class File:
    path: str = field(metadata=config(field_name="path"))


RepoID = str


class GitLocalMetadataVersion(Enum):
    V1 = "v1"


class GitPushType(Enum):
    DEFAULT = "default"
    CREATEREPO = "createrepo"
    RENAMEREPO = "renamerepo"


class GitRepoResultState(Enum):
    ERR = "err"
    OK = "ok"


@dataclass_json
@dataclass
class GitTeamRepoSettings:
    channel_name: Optional[str] = field(metadata=config(field_name="channelName"))
    chat_disabled: bool = field(metadata=config(field_name="chatDisabled"))


@dataclass_json
@dataclass
class SelectKeyRes:
    key_id: str = field(metadata=config(field_name="keyID"))
    do_secret_push: bool = field(metadata=config(field_name="doSecretPush"))


class PushReason(Enum):
    NONE = "none"
    RECONNECTED = "reconnected"
    NEW_DATA = "new_data"


HomeScreenItemID = str


class HomeScreenItemType(Enum):
    TODO = "todo"
    PEOPLE = "people"
    ANNOUNCEMENT = "announcement"


class AppLinkType(Enum):
    NONE = "none"
    PEOPLE = "people"
    CHAT = "chat"
    FILES = "files"
    WALLET = "wallet"
    GIT = "git"
    DEVICES = "devices"
    SETTINGS = "settings"
    TEAMS = "teams"


HomeScreenAnnouncementID = int
HomeScreenAnnouncementVersion = int


class HomeScreenTodoType(Enum):
    NONE = "none"
    BIO = "bio"
    PROOF = "proof"
    DEVICE = "device"
    FOLLOW = "follow"
    CHAT = "chat"
    PAPERKEY = "paperkey"
    TEAM = "team"
    FOLDER = "folder"
    GIT_REPO = "git_repo"
    TEAM_SHOWCASE = "team_showcase"
    AVATAR_USER = "avatar_user"
    AVATAR_TEAM = "avatar_team"
    ADD_PHONE_NUMBER = "add_phone_number"
    VERIFY_ALL_PHONE_NUMBER = "verify_all_phone_number"
    VERIFY_ALL_EMAIL = "verify_all_email"
    LEGACY_EMAIL_VISIBILITY = "legacy_email_visibility"
    ADD_EMAIL = "add_email"
    ANNONCEMENT_PLACEHOLDER = "annoncement_placeholder"


class HomeScreenPeopleNotificationType(Enum):
    FOLLOWED = "followed"
    FOLLOWED_MULTI = "followed_multi"


@dataclass_json
@dataclass
class Pics:
    square_40: str = field(metadata=config(field_name="square_40"))
    square_200: str = field(metadata=config(field_name="square_200"))
    square_360: str = field(metadata=config(field_name="square_360"))


Identify3Assertion = str
Identify3GUIID = str


class Identify3RowState(Enum):
    CHECKING = "checking"
    VALID = "valid"
    ERROR = "error"
    WARNING = "warning"
    REVOKED = "revoked"


class Identify3RowColor(Enum):
    BLUE = "blue"
    RED = "red"
    BLACK = "black"
    GREEN = "green"
    GRAY = "gray"
    YELLOW = "yellow"
    ORANGE = "orange"


class Identify3ResultType(Enum):
    OK = "ok"
    BROKEN = "broken"
    NEEDS_UPGRADE = "needs_upgrade"
    CANCELED = "canceled"


TrackToken = str
SigVersion = int


class TrackDiffType(Enum):
    NONE = "none"
    ERROR = "error"
    CLASH = "clash"
    REVOKED = "revoked"
    UPGRADED = "upgraded"
    NEW = "new"
    REMOTE_FAIL = "remote_fail"
    REMOTE_WORKING = "remote_working"
    REMOTE_CHANGED = "remote_changed"
    NEW_ELDEST = "new_eldest"
    NONE_VIA_TEMPORARY = "none_via_temporary"


class TrackStatus(Enum):
    """
    TrackStatus is a summary of this track before the track is approved by the
    user.
    NEW_*: New tracks
    UPDATE_*: Update to an existing track
    NEW_OK: Everything ok
    NEW_ZERO_PROOFS: User being tracked has no proofs
    NEW_FAIL_PROOFS: User being tracked has some failed proofs
    UPDATE_BROKEN: Previous tracking statement broken, this one will fix it.
    UPDATE_NEW_PROOFS: Previous tracking statement ok, but there are new proofs since previous tracking statement generated
    UPDATE_OK: No changes to previous tracking statement
    """

    NEW_OK = "new_ok"
    NEW_ZERO_PROOFS = "new_zero_proofs"
    NEW_FAIL_PROOFS = "new_fail_proofs"
    UPDATE_BROKEN_FAILED_PROOFS = "update_broken_failed_proofs"
    UPDATE_NEW_PROOFS = "update_new_proofs"
    UPDATE_OK = "update_ok"
    UPDATE_BROKEN_REVOKED = "update_broken_revoked"


class IdentifyReasonType(Enum):
    NONE = "none"
    ID = "id"
    TRACK = "track"
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    VERIFY = "verify"
    RESOURCE = "resource"
    BACKGROUND = "background"


@dataclass_json
@dataclass
class SigHint:
    remote_id: str = field(metadata=config(field_name="remoteId"))
    human_url: str = field(metadata=config(field_name="humanUrl"))
    api_url: str = field(metadata=config(field_name="apiUrl"))
    check_text: str = field(metadata=config(field_name="checkText"))


class CheckResultFreshness(Enum):
    FRESH = "fresh"
    AGED = "aged"
    RANCID = "rancid"


@dataclass_json
@dataclass
class ConfirmResult:
    identity_confirmed: bool = field(metadata=config(field_name="identityConfirmed"))
    remote_confirmed: bool = field(metadata=config(field_name="remoteConfirmed"))
    expiring_local: bool = field(metadata=config(field_name="expiringLocal"))
    auto_confirmed: bool = field(metadata=config(field_name="autoConfirmed"))


class DismissReasonType(Enum):
    NONE = "none"
    HANDLED_ELSEWHERE = "handled_elsewhere"


class InstallStatus(Enum):
    """
    Install status describes state of install for a component or service.
    """

    UNKNOWN = "unknown"
    ERROR = "error"
    NOT_INSTALLED = "not_installed"
    INSTALLED = "installed"


class InstallAction(Enum):
    UNKNOWN = "unknown"
    NONE = "none"
    UPGRADE = "upgrade"
    REINSTALL = "reinstall"
    INSTALL = "install"


@dataclass_json
@dataclass
class FuseMountInfo:
    path: str = field(metadata=config(field_name="path"))
    fstype: str = field(metadata=config(field_name="fstype"))
    output: str = field(metadata=config(field_name="output"))


class FSStatusCode(Enum):
    START = "start"
    FINISH = "finish"
    ERROR = "error"


class FSNotificationType(Enum):
    ENCRYPTING = "encrypting"
    DECRYPTING = "decrypting"
    SIGNING = "signing"
    VERIFYING = "verifying"
    REKEYING = "rekeying"
    CONNECTION = "connection"
    MD_READ_SUCCESS = "md_read_success"
    FILE_CREATED = "file_created"
    FILE_MODIFIED = "file_modified"
    FILE_DELETED = "file_deleted"
    FILE_RENAMED = "file_renamed"
    INITIALIZED = "initialized"
    SYNC_CONFIG_CHANGED = "sync_config_changed"


class FSErrorType(Enum):
    ACCESS_DENIED = "access_denied"
    USER_NOT_FOUND = "user_not_found"
    REVOKED_DATA_DETECTED = "revoked_data_detected"
    NOT_LOGGED_IN = "not_logged_in"
    TIMEOUT = "timeout"
    REKEY_NEEDED = "rekey_needed"
    BAD_FOLDER = "bad_folder"
    NOT_IMPLEMENTED = "not_implemented"
    OLD_VERSION = "old_version"
    OVER_QUOTA = "over_quota"
    NO_SIG_CHAIN = "no_sig_chain"
    TOO_MANY_FOLDERS = "too_many_folders"
    EXDEV_NOT_SUPPORTED = "exdev_not_supported"
    DISK_LIMIT_REACHED = "disk_limit_reached"
    DISK_CACHE_ERROR_LOG_SEND = "disk_cache_error_log_send"
    OFFLINE_ARCHIVED = "offline_archived"
    OFFLINE_UNSYNCED = "offline_unsynced"


@dataclass_json
@dataclass
class FSSyncStatusRequest:
    request_id: int = field(metadata=config(field_name="requestID"))


@dataclass_json
@dataclass
class PassphraseStream:
    passphrase_stream: bytes = field(metadata=config(field_name="passphraseStream"))
    generation: int = field(metadata=config(field_name="generation"))


SessionToken = str
CsrfToken = str
HelloRes = str


class ResetPromptType(Enum):
    COMPLETE = "complete"
    ENTER_NO_DEVICES = "enter_no_devices"
    ENTER_FORGOT_PW = "enter_forgot_pw"


class PassphraseRecoveryPromptType(Enum):
    ENCRYPTED_PGP_KEYS = "encrypted_pgp_keys"


KBFSRootHash = bytes
MerkleStoreSupportedVersion = int
MerkleStoreKitHash = str
MerkleStoreKit = str
MerkleStoreEntryString = str


@dataclass_json
@dataclass
class KeyBundle:
    version: int = field(metadata=config(field_name="version"))
    bundle: bytes = field(metadata=config(field_name="bundle"))


@dataclass_json
@dataclass
class MerkleRoot:
    version: int = field(metadata=config(field_name="version"))
    root: bytes = field(metadata=config(field_name="root"))


LockID = int
MDPriority = int


@dataclass_json
@dataclass
class RekeyRequest:
    folder_id: str = field(metadata=config(field_name="folderID"))
    revision: int = field(metadata=config(field_name="revision"))


ChatConversationID = bytes


@dataclass_json
@dataclass
class DeletedTeamInfo:
    team_name: str = field(metadata=config(field_name="teamName"))
    deleted_by: str = field(metadata=config(field_name="deletedBy"))
    id: gregor1.MsgID = field(metadata=config(field_name="id"))


@dataclass_json
@dataclass
class WalletAccountInfo:
    account_id: str = field(metadata=config(field_name="accountID"))
    num_unread: int = field(metadata=config(field_name="numUnread"))


@dataclass_json
@dataclass
class NotificationChannels:
    session: bool = field(metadata=config(field_name="session"))
    users: bool = field(metadata=config(field_name="users"))
    kbfs: bool = field(metadata=config(field_name="kbfs"))
    kbfsdesktop: bool = field(metadata=config(field_name="kbfsdesktop"))
    kbfslegacy: bool = field(metadata=config(field_name="kbfslegacy"))
    kbfssubscription: bool = field(metadata=config(field_name="kbfssubscription"))
    tracking: bool = field(metadata=config(field_name="tracking"))
    favorites: bool = field(metadata=config(field_name="favorites"))
    paperkeys: bool = field(metadata=config(field_name="paperkeys"))
    keyfamily: bool = field(metadata=config(field_name="keyfamily"))
    service: bool = field(metadata=config(field_name="service"))
    app: bool = field(metadata=config(field_name="app"))
    chat: bool = field(metadata=config(field_name="chat"))
    pgp: bool = field(metadata=config(field_name="pgp"))
    kbfsrequest: bool = field(metadata=config(field_name="kbfsrequest"))
    badges: bool = field(metadata=config(field_name="badges"))
    reachability: bool = field(metadata=config(field_name="reachability"))
    team: bool = field(metadata=config(field_name="team"))
    ephemeral: bool = field(metadata=config(field_name="ephemeral"))
    teambot: bool = field(metadata=config(field_name="teambot"))
    chatkbfsedits: bool = field(metadata=config(field_name="chatkbfsedits"))
    chatdev: bool = field(metadata=config(field_name="chatdev"))
    deviceclone: bool = field(metadata=config(field_name="deviceclone"))
    chatattachments: bool = field(metadata=config(field_name="chatattachments"))
    wallet: bool = field(metadata=config(field_name="wallet"))
    audit: bool = field(metadata=config(field_name="audit"))
    runtimestats: bool = field(metadata=config(field_name="runtimestats"))


class StatsSeverityLevel(Enum):
    NORMAL = "normal"
    WARNING = "warning"
    SEVERE = "severe"


class ProcessType(Enum):
    MAIN = "main"
    KBFS = "kbfs"


@dataclass_json
@dataclass
class HttpSrvInfo:
    address: str = field(metadata=config(field_name="address"))
    token: str = field(metadata=config(field_name="token"))


@dataclass_json
@dataclass
class TeamChangeSet:
    membership_changed: bool = field(metadata=config(field_name="membershipChanged"))
    key_rotated: bool = field(metadata=config(field_name="keyRotated"))
    renamed: bool = field(metadata=config(field_name="renamed"))
    misc: bool = field(metadata=config(field_name="misc"))


class AvatarUpdateType(Enum):
    NONE = "none"
    USER = "user"
    TEAM = "team"


class RuntimeGroup(Enum):
    UNKNOWN = "unknown"
    LINUXLIKE = "linuxlike"
    DARWINLIKE = "darwinlike"
    WINDOWSLIKE = "windowslike"


@dataclass_json
@dataclass
class Feature:
    allow: bool = field(metadata=config(field_name="allow"))
    default_value: bool = field(metadata=config(field_name="defaultValue"))
    readonly: bool = field(metadata=config(field_name="readonly"))
    label: str = field(metadata=config(field_name="label"))


class PassphraseType(Enum):
    NONE = "none"
    PAPER_KEY = "paper_key"
    PASS_PHRASE = "pass_phrase"
    VERIFY_PASS_PHRASE = "verify_pass_phrase"


@dataclass_json
@dataclass
class GetPassphraseRes:
    passphrase: str = field(metadata=config(field_name="passphrase"))
    store_secret: bool = field(metadata=config(field_name="storeSecret"))


class SignMode(Enum):
    ATTACHED = "attached"
    DETACHED = "detached"
    CLEAR = "clear"


@dataclass_json
@dataclass
class PGPEncryptOptions:
    recipients: List[str] = field(metadata=config(field_name="recipients"))
    no_sign: bool = field(metadata=config(field_name="noSign"))
    no_self: bool = field(metadata=config(field_name="noSelf"))
    binary_out: bool = field(metadata=config(field_name="binaryOut"))
    key_query: str = field(metadata=config(field_name="keyQuery"))


@dataclass_json
@dataclass
class PGPDecryptOptions:
    assert_signed: bool = field(metadata=config(field_name="assertSigned"))
    signed_by: str = field(metadata=config(field_name="signedBy"))


@dataclass_json
@dataclass
class PGPVerifyOptions:
    signed_by: str = field(metadata=config(field_name="signedBy"))
    signature: bytes = field(metadata=config(field_name="signature"))


@dataclass_json
@dataclass
class KeyInfo:
    fingerprint: str = field(metadata=config(field_name="fingerprint"))
    key: str = field(metadata=config(field_name="key"))
    desc: str = field(metadata=config(field_name="desc"))


@dataclass_json
@dataclass
class PGPQuery:
    secret: bool = field(metadata=config(field_name="secret"))
    query: str = field(metadata=config(field_name="query"))
    exact_match: bool = field(metadata=config(field_name="exactMatch"))


@dataclass_json
@dataclass
class PGPPurgeRes:
    filenames: List[str] = field(metadata=config(field_name="filenames"))


class FileType(Enum):
    UNKNOWN = "unknown"
    DIRECTORY = "directory"
    FILE = "file"


class ProofState(Enum):
    NONE = "none"
    OK = "ok"
    TEMP_FAILURE = "temp_failure"
    PERM_FAILURE = "perm_failure"
    LOOKING = "looking"
    SUPERSEDED = "superseded"
    POSTED = "posted"
    REVOKED = "revoked"
    DELETED = "deleted"
    UNKNOWN_TYPE = "unknown_type"
    SIG_HINT_MISSING = "sig_hint_missing"
    UNCHECKED = "unchecked"


class ProofStatus(Enum):
    """
    3: It's been found in the hunt, but not proven yet
    1xx: Retryable soft errors; note that this will be put in the proof_cache, but won't
    be returned from the proof cache in most cases. Their freshness will always be
    RANCID.
    2xx: Will likely result in a hard error, if repeated enough
    3xx: Hard final errors
    """

    NONE = "none"
    OK = "ok"
    LOCAL = "local"
    FOUND = "found"
    BASE_ERROR = "base_error"
    HOST_UNREACHABLE = "host_unreachable"
    PERMISSION_DENIED = "permission_denied"
    FAILED_PARSE = "failed_parse"
    DNS_ERROR = "dns_error"
    AUTH_FAILED = "auth_failed"
    HTTP_429 = "http_429"
    HTTP_500 = "http_500"
    TIMEOUT = "timeout"
    INTERNAL_ERROR = "internal_error"
    UNCHECKED = "unchecked"
    MISSING_PVL = "missing_pvl"
    BASE_HARD_ERROR = "base_hard_error"
    NOT_FOUND = "not_found"
    CONTENT_FAILURE = "content_failure"
    BAD_USERNAME = "bad_username"
    BAD_REMOTE_ID = "bad_remote_id"
    TEXT_NOT_FOUND = "text_not_found"
    BAD_ARGS = "bad_args"
    CONTENT_MISSING = "content_missing"
    TITLE_NOT_FOUND = "title_not_found"
    SERVICE_ERROR = "service_error"
    TOR_SKIPPED = "tor_skipped"
    TOR_INCOMPATIBLE = "tor_incompatible"
    HTTP_300 = "http_300"
    HTTP_400 = "http_400"
    HTTP_OTHER = "http_other"
    EMPTY_JSON = "empty_json"
    DELETED = "deleted"
    SERVICE_DEAD = "service_dead"
    BAD_SIGNATURE = "bad_signature"
    BAD_API_URL = "bad_api_url"
    UNKNOWN_TYPE = "unknown_type"
    NO_HINT = "no_hint"
    BAD_HINT_TEXT = "bad_hint_text"
    INVALID_PVL = "invalid_pvl"


class ProofType(Enum):
    NONE = "none"
    KEYBASE = "keybase"
    TWITTER = "twitter"
    GITHUB = "github"
    REDDIT = "reddit"
    COINBASE = "coinbase"
    HACKERNEWS = "hackernews"
    FACEBOOK = "facebook"
    GENERIC_SOCIAL = "generic_social"
    GENERIC_WEB_SITE = "generic_web_site"
    DNS = "dns"
    PGP = "pgp"
    ROOTER = "rooter"


@dataclass_json
@dataclass
class SelectorEntry:
    is_index: bool = field(metadata=config(field_name="isIndex"))
    index: int = field(metadata=config(field_name="index"))
    is_key: bool = field(metadata=config(field_name="isKey"))
    key: str = field(metadata=config(field_name="key"))
    is_all: bool = field(metadata=config(field_name="isAll"))
    is_contents: bool = field(metadata=config(field_name="isContents"))


@dataclass_json
@dataclass
class ParamProofUsernameConfig:
    re: str = field(metadata=config(field_name="re"))
    min: int = field(metadata=config(field_name="min"))
    max: int = field(metadata=config(field_name="max"))


@dataclass_json
@dataclass
class ParamProofLogoConfig:
    svg_black: str = field(metadata=config(field_name="svg_black"))
    svg_full: str = field(metadata=config(field_name="svg_full"))


@dataclass_json
@dataclass
class ServiceDisplayConfig:
    creation_disabled: bool = field(metadata=config(field_name="creation_disabled"))
    priority: int = field(metadata=config(field_name="priority"))
    key: str = field(metadata=config(field_name="key"))
    group: Optional[str] = field(metadata=config(field_name="group"))
    new: bool = field(metadata=config(field_name="new"))
    logo_key: str = field(metadata=config(field_name="logo_key"))


class PromptOverwriteType(Enum):
    SOCIAL = "social"
    SITE = "site"


class ProvisionMethod(Enum):
    DEVICE = "device"
    PAPER_KEY = "paper_key"
    PASSPHRASE = "passphrase"
    GPG_IMPORT = "gpg_import"
    GPG_SIGN = "gpg_sign"


class GPGMethod(Enum):
    GPG_NONE = "gpg_none"
    GPG_IMPORT = "gpg_import"
    GPG_SIGN = "gpg_sign"


class ChooseType(Enum):
    EXISTING_DEVICE = "existing_device"
    NEW_DEVICE = "new_device"


@dataclass_json
@dataclass
class SecretResponse:
    secret: bytes = field(metadata=config(field_name="secret"))
    phrase: str = field(metadata=config(field_name="phrase"))


class Reachable(Enum):
    UNKNOWN = "unknown"
    YES = "yes"
    NO = "no"


class Outcome(Enum):
    NONE = "none"
    FIXED = "fixed"
    IGNORED = "ignored"


class RekeyEventType(Enum):
    NONE = "none"
    NOT_LOGGED_IN = "not_logged_in"
    API_ERROR = "api_error"
    NO_PROBLEMS = "no_problems"
    LOAD_ME_ERROR = "load_me_error"
    CURRENT_DEVICE_CAN_REKEY = "current_device_can_rekey"
    DEVICE_LOAD_ERROR = "device_load_error"
    HARASS = "harass"
    NO_GREGOR_MESSAGES = "no_gregor_messages"


SHA512 = bytes


class ResetType(Enum):
    NONE = "none"
    RESET = "reset"
    DELETE = "delete"


class AuthenticityType(Enum):
    SIGNED = "signed"
    REPUDIABLE = "repudiable"
    ANONYMOUS = "anonymous"


@dataclass_json
@dataclass
class SaltpackDecryptOptions:
    interactive: bool = field(metadata=config(field_name="interactive"))
    force_remote_check: bool = field(metadata=config(field_name="forceRemoteCheck"))
    use_paper_key: bool = field(metadata=config(field_name="usePaperKey"))


@dataclass_json
@dataclass
class SaltpackSignOptions:
    detached: bool = field(metadata=config(field_name="detached"))
    binary: bool = field(metadata=config(field_name="binary"))
    saltpack_version: int = field(metadata=config(field_name="saltpackVersion"))


@dataclass_json
@dataclass
class SaltpackVerifyOptions:
    signed_by: str = field(metadata=config(field_name="signedBy"))
    signature: bytes = field(metadata=config(field_name="signature"))


class SaltpackSenderType(Enum):
    NOT_TRACKED = "not_tracked"
    UNKNOWN = "unknown"
    ANONYMOUS = "anonymous"
    TRACKING_BROKE = "tracking_broke"
    TRACKING_OK = "tracking_ok"
    SELF = "self"
    REVOKED = "revoked"
    EXPIRED = "expired"


@dataclass_json
@dataclass
class SecretEntryArg:
    desc: str = field(metadata=config(field_name="desc"))
    prompt: str = field(metadata=config(field_name="prompt"))
    err: str = field(metadata=config(field_name="err"))
    cancel: str = field(metadata=config(field_name="cancel"))
    ok: str = field(metadata=config(field_name="ok"))
    reason: str = field(metadata=config(field_name="reason"))
    show_typing: bool = field(metadata=config(field_name="showTyping"))


@dataclass_json
@dataclass
class SecretEntryRes:
    text: str = field(metadata=config(field_name="text"))
    canceled: bool = field(metadata=config(field_name="canceled"))
    store_secret: bool = field(metadata=config(field_name="storeSecret"))


NaclSigningKeyPublic = Optional[str]
NaclSigningKeyPrivate = Optional[str]
NaclDHKeyPublic = Optional[str]
NaclDHKeyPrivate = Optional[str]


@dataclass_json
@dataclass
class SignupRes:
    passphrase_ok: bool = field(metadata=config(field_name="passphraseOk"))
    post_ok: bool = field(metadata=config(field_name="postOk"))
    write_ok: bool = field(metadata=config(field_name="writeOk"))


@dataclass_json
@dataclass
class SigTypes:
    track: bool = field(metadata=config(field_name="track"))
    proof: bool = field(metadata=config(field_name="proof"))
    cryptocurrency: bool = field(metadata=config(field_name="cryptocurrency"))
    is_self: bool = field(metadata=config(field_name="isSelf"))


OpID = Optional[str]
KBFSRevision = int


class KBFSArchivedType(Enum):
    REVISION = "revision"
    TIME = "time"
    TIME_STRING = "time_string"
    REL_TIME_STRING = "rel_time_string"


class PathType(Enum):
    LOCAL = "local"
    KBFS = "kbfs"
    KBFS_ARCHIVED = "kbfs_archived"


class DirentType(Enum):
    FILE = "file"
    DIR = "dir"
    SYM = "sym"
    EXEC = "exec"


class PrefetchStatus(Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETE = "complete"


class RevisionSpanType(Enum):
    DEFAULT = "default"
    LAST_FIVE = "last_five"


ErrorNum = int


class OpenFlags(Enum):
    READ = "read"
    REPLACE = "replace"
    EXISTING = "existing"
    WRITE = "write"
    APPEND = "append"
    DIRECTORY = "directory"


Progress = int


class AsyncOps(Enum):
    LIST = "list"
    LIST_RECURSIVE = "list_recursive"
    READ = "read"
    WRITE = "write"
    COPY = "copy"
    MOVE = "move"
    REMOVE = "remove"
    LIST_RECURSIVE_TO_DEPTH = "list_recursive_to_depth"
    GET_REVISIONS = "get_revisions"


class ListFilter(Enum):
    NO_FILTER = "no_filter"
    FILTER_ALL_HIDDEN = "filter_all_hidden"
    FILTER_SYSTEM_HIDDEN = "filter_system_hidden"


@dataclass_json
@dataclass
class SimpleFSGetHTTPAddressAndTokenResponse:
    address: str = field(metadata=config(field_name="address"))
    token: str = field(metadata=config(field_name="token"))


@dataclass_json
@dataclass
class SimpleFSQuotaUsage:
    usage_bytes: int = field(metadata=config(field_name="usageBytes"))
    archive_bytes: int = field(metadata=config(field_name="archiveBytes"))
    limit_bytes: int = field(metadata=config(field_name="limitBytes"))
    git_usage_bytes: int = field(metadata=config(field_name="gitUsageBytes"))
    git_archive_bytes: int = field(metadata=config(field_name="gitArchiveBytes"))
    git_limit_bytes: int = field(metadata=config(field_name="gitLimitBytes"))


class FolderSyncMode(Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"
    PARTIAL = "partial"


@dataclass_json
@dataclass
class FSSettings:
    space_available_notification_threshold: int = field(
        metadata=config(field_name="spaceAvailableNotificationThreshold")
    )


class SubscriptionTopic(Enum):
    FAVORITES = "favorites"
    JOURNAL_STATUS = "journal_status"
    ONLINE_STATUS = "online_status"


class PathSubscriptionTopic(Enum):
    CHILDREN = "children"
    STAT = "stat"


TeambotKeyGeneration = int


class TeamRole(Enum):
    NONE = "none"
    READER = "reader"
    WRITER = "writer"
    ADMIN = "admin"
    OWNER = "owner"
    BOT = "bot"
    RESTRICTEDBOT = "restrictedbot"


class TeamApplication(Enum):
    KBFS = "kbfs"
    CHAT = "chat"
    SALTPACK = "saltpack"
    GIT_METADATA = "git_metadata"
    SEITAN_INVITE_TOKEN = "seitan_invite_token"
    STELLAR_RELAY = "stellar_relay"


class TeamStatus(Enum):
    NONE = "none"
    LIVE = "live"
    DELETED = "deleted"
    ABANDONED = "abandoned"


PerTeamKeyGeneration = int


class PTKType(Enum):
    READER = "reader"


class PerTeamSeedCheckVersion(Enum):
    V1 = "v1"


PerTeamSeedCheckValue = bytes
PerTeamSeedCheckValuePostImage = bytes
MaskB64 = bytes
TeamInviteID = str
PerTeamKeySeed = Optional[str]


class TeamMemberStatus(Enum):
    ACTIVE = "active"
    RESET = "reset"
    DELETED = "deleted"


UserVersionPercentForm = str


class RatchetType(Enum):
    MAIN = "main"
    BLINDED = "blinded"
    SELF = "self"


class AuditVersion(Enum):
    V0 = "v0"
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"


class TeamInviteCategory(Enum):
    NONE = "none"
    UNKNOWN = "unknown"
    KEYBASE = "keybase"
    EMAIL = "email"
    SBS = "sbs"
    SEITAN = "seitan"
    PHONE = "phone"


TeamInviteSocialNetwork = str
TeamInviteName = str


@dataclass_json
@dataclass
class TeamEncryptedKBFSKeyset:
    v: int = field(metadata=config(field_name="v"))
    e: bytes = field(metadata=config(field_name="e"))
    n: bytes = field(metadata=config(field_name="n"))


TeamEncryptedKBFSKeysetHash = str
BoxSummaryHash = str
TeamNamePart = str
SeitanAKey = str
SeitanIKey = str
SeitanPubKey = str
SeitanIKeyV2 = str


class SeitanKeyAndLabelVersion(Enum):
    V1 = "v1"
    V2 = "v2"


class SeitanKeyLabelType(Enum):
    SMS = "sms"


@dataclass_json
@dataclass
class SeitanKeyLabelSms:
    f: str = field(metadata=config(field_name="f"))
    n: str = field(metadata=config(field_name="n"))


@dataclass_json
@dataclass
class TeamJoinRequest:
    name: str = field(metadata=config(field_name="name"))
    username: str = field(metadata=config(field_name="username"))


@dataclass_json
@dataclass
class TeamBotSettings:
    cmds: bool = field(metadata=config(field_name="cmds"))
    mentions: bool = field(metadata=config(field_name="mentions"))
    triggers: List[str] = field(metadata=config(field_name="triggers"))
    convs: List[str] = field(metadata=config(field_name="convs"))


@dataclass_json
@dataclass
class TeamRequestAccessResult:
    open: bool = field(metadata=config(field_name="open"))


@dataclass_json
@dataclass
class TeamAcceptOrRequestResult:
    was_token: bool = field(metadata=config(field_name="wasToken"))
    was_seitan: bool = field(metadata=config(field_name="wasSeitan"))
    was_team_name: bool = field(metadata=config(field_name="wasTeamName"))
    was_open_team: bool = field(metadata=config(field_name="wasOpenTeam"))


@dataclass_json
@dataclass
class BulkRes:
    invited: List[str] = field(metadata=config(field_name="invited"))
    already_invited: List[str] = field(metadata=config(field_name="alreadyInvited"))
    malformed: List[str] = field(metadata=config(field_name="malformed"))


ConflictGeneration = int


@dataclass_json
@dataclass
class TeamOperation:
    manage_members: bool = field(metadata=config(field_name="manageMembers"))
    manage_subteams: bool = field(metadata=config(field_name="manageSubteams"))
    create_channel: bool = field(metadata=config(field_name="createChannel"))
    chat: bool = field(metadata=config(field_name="chat"))
    delete_channel: bool = field(metadata=config(field_name="deleteChannel"))
    rename_channel: bool = field(metadata=config(field_name="renameChannel"))
    rename_team: bool = field(metadata=config(field_name="renameTeam"))
    edit_channel_description: bool = field(
        metadata=config(field_name="editChannelDescription")
    )
    edit_team_description: bool = field(
        metadata=config(field_name="editTeamDescription")
    )
    set_team_showcase: bool = field(metadata=config(field_name="setTeamShowcase"))
    set_member_showcase: bool = field(metadata=config(field_name="setMemberShowcase"))
    set_retention_policy: bool = field(metadata=config(field_name="setRetentionPolicy"))
    set_min_writer_role: bool = field(metadata=config(field_name="setMinWriterRole"))
    change_open_team: bool = field(metadata=config(field_name="changeOpenTeam"))
    leave_team: bool = field(metadata=config(field_name="leaveTeam"))
    join_team: bool = field(metadata=config(field_name="joinTeam"))
    set_publicity_any: bool = field(metadata=config(field_name="setPublicityAny"))
    list_first: bool = field(metadata=config(field_name="listFirst"))
    change_tars_disabled: bool = field(metadata=config(field_name="changeTarsDisabled"))
    delete_chat_history: bool = field(metadata=config(field_name="deleteChatHistory"))
    delete_other_messages: bool = field(
        metadata=config(field_name="deleteOtherMessages")
    )
    delete_team: bool = field(metadata=config(field_name="deleteTeam"))
    pin_message: bool = field(metadata=config(field_name="pinMessage"))


@dataclass_json
@dataclass
class ProfileTeamLoadRes:
    load_time_nsec: int = field(metadata=config(field_name="loadTimeNsec"))


class RotationType(Enum):
    VISIBLE = "visible"
    HIDDEN = "hidden"
    CLKR = "clkr"


@dataclass_json
@dataclass
class MemberEmail:
    email: str = field(metadata=config(field_name="email"))
    role: str = field(metadata=config(field_name="role"))


@dataclass_json
@dataclass
class MemberUsername:
    username: str = field(metadata=config(field_name="username"))
    role: str = field(metadata=config(field_name="role"))


@dataclass_json
@dataclass
class Test:
    reply: str = field(metadata=config(field_name="reply"))


class TLFIdentifyBehavior(Enum):
    UNSET = "unset"
    CHAT_CLI = "chat_cli"
    CHAT_GUI = "chat_gui"
    REMOVED_AND_UNUSED = "removed_and_unused"
    KBFS_REKEY = "kbfs_rekey"
    KBFS_QR = "kbfs_qr"
    CHAT_SKIP = "chat_skip"
    SALTPACK = "saltpack"
    CLI = "cli"
    GUI = "gui"
    DEFAULT_KBFS = "default_kbfs"
    KBFS_CHAT = "kbfs_chat"
    RESOLVE_AND_CHECK = "resolve_and_check"
    GUI_PROFILE = "gui_profile"
    KBFS_INIT = "kbfs_init"
    FS_GUI = "fs_gui"


CanonicalTlfName = str


class PromptDefault(Enum):
    NONE = "none"
    YES = "yes"
    NO = "no"


class KeyType(Enum):
    NONE = "none"
    NACL = "nacl"
    PGP = "pgp"


class UPK2MinorVersion(Enum):
    V0 = "v0"
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"
    V4 = "v4"
    V5 = "v5"
    V6 = "v6"


PGPFingerprint = Optional[str]


class UPAKVersion(Enum):
    V1 = "v1"
    V2 = "v2"


class UPKLiteMinorVersion(Enum):
    V0 = "v0"


@dataclass_json
@dataclass
class TrackProof:
    proof_type: str = field(metadata=config(field_name="proofType"))
    proof_name: str = field(metadata=config(field_name="proofName"))
    id_string: str = field(metadata=config(field_name="idString"))


@dataclass_json
@dataclass
class WebProof:
    hostname: str = field(metadata=config(field_name="hostname"))
    protocols: List[str] = field(metadata=config(field_name="protocols"))


EmailAddress = str


@dataclass_json
@dataclass
class CanLogoutRes:
    can_logout: bool = field(metadata=config(field_name="canLogout"))
    reason: str = field(metadata=config(field_name="reason"))
    set_passphrase: bool = field(metadata=config(field_name="setPassphrase"))


APIUserServiceIDWithContact = str


@dataclass_json
@dataclass
class ImpTofuSearchResult:
    assertion: str = field(metadata=config(field_name="assertion"))
    assertion_value: str = field(metadata=config(field_name="assertionValue"))
    assertion_key: str = field(metadata=config(field_name="assertionKey"))
    label: str = field(metadata=config(field_name="label"))
    pretty_name: str = field(metadata=config(field_name="prettyName"))
    keybase_username: str = field(metadata=config(field_name="keybaseUsername"))


class ImpTofuSearchType(Enum):
    PHONE = "phone"
    EMAIL = "email"


@dataclass_json
@dataclass
class LockdownHistory:
    status: bool = field(metadata=config(field_name="status"))
    creation_time: Time = field(metadata=config(field_name="ctime"))
    device_id: DeviceID = field(metadata=config(field_name="device_id"))
    device_name: str = field(metadata=config(field_name="deviceName"))


@dataclass_json
@dataclass
class BoxAuditAttempt:
    ctime: UnixTime = field(metadata=config(field_name="ctime"))
    error: Optional[str] = field(metadata=config(field_name="error"))
    result: BoxAuditAttemptResult = field(metadata=config(field_name="result"))
    generation: Optional[PerTeamKeyGeneration] = field(
        metadata=config(field_name="generation")
    )
    rotated: bool = field(metadata=config(field_name="rotated"))


@dataclass_json
@dataclass
class LoadAvatarsRes:
    picmap: Dict[str, Dict[str, AvatarUrl]] = field(
        metadata=config(field_name="picmap")
    )


@dataclass_json
@dataclass
class AvatarClearCacheMsg:
    name: str = field(metadata=config(field_name="name"))
    formats: List[AvatarFormat] = field(metadata=config(field_name="formats"))
    typ: AvatarUpdateType = field(metadata=config(field_name="typ"))


@dataclass_json
@dataclass
class BlockIdCombo:
    block_hash: str = field(metadata=config(field_name="blockHash"))
    charged_to: UserOrTeamID = field(metadata=config(field_name="chargedTo"))
    block_type: BlockType = field(metadata=config(field_name="blockType"))


@dataclass_json
@dataclass
class GetBlockRes:
    block_key: str = field(metadata=config(field_name="blockKey"))
    buf: bytes = field(metadata=config(field_name="buf"))
    size: int = field(metadata=config(field_name="size"))
    status: BlockStatus = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class Status:
    code: int = field(metadata=config(field_name="code"))
    name: str = field(metadata=config(field_name="name"))
    desc: str = field(metadata=config(field_name="desc"))
    fields: List[StringKVPair] = field(metadata=config(field_name="fields"))


@dataclass_json
@dataclass
class UserVersion:
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))


@dataclass
class CompatibilityTeamID__LEGACY:
    typ: Literal[TeamType.LEGACY]
    LEGACY: Optional[TLFID]


@dataclass
class CompatibilityTeamID__MODERN:
    typ: Literal[TeamType.MODERN]
    MODERN: Optional[TeamID]


CompatibilityTeamID = Union[CompatibilityTeamID__LEGACY, CompatibilityTeamID__MODERN]


@dataclass_json
@dataclass
class TeamIDWithVisibility:
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    visibility: TLFVisibility = field(metadata=config(field_name="visibility"))


@dataclass_json
@dataclass
class PublicKey:
    kid: KID = field(metadata=config(field_name="KID"))
    pgp_fingerprint: str = field(metadata=config(field_name="PGPFingerprint"))
    pgp_identities: List[PGPIdentity] = field(
        metadata=config(field_name="PGPIdentities")
    )
    is_sibkey: bool = field(metadata=config(field_name="isSibkey"))
    is_eldest: bool = field(metadata=config(field_name="isEldest"))
    parent_id: str = field(metadata=config(field_name="parentID"))
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    device_description: str = field(metadata=config(field_name="deviceDescription"))
    device_type: str = field(metadata=config(field_name="deviceType"))
    c_time: Time = field(metadata=config(field_name="cTime"))
    e_time: Time = field(metadata=config(field_name="eTime"))
    is_revoked: bool = field(metadata=config(field_name="isRevoked"))


@dataclass_json
@dataclass
class KeybaseTime:
    unix: Time = field(metadata=config(field_name="unix"))
    chain: Seqno = field(metadata=config(field_name="chain"))


@dataclass_json
@dataclass
class User:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))


@dataclass_json
@dataclass
class Device:
    type: str = field(metadata=config(field_name="type"))
    name: str = field(metadata=config(field_name="name"))
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    c_time: Time = field(metadata=config(field_name="cTime"))
    m_time: Time = field(metadata=config(field_name="mTime"))
    last_used_time: Time = field(metadata=config(field_name="lastUsedTime"))
    encrypt_key: KID = field(metadata=config(field_name="encryptKey"))
    verify_key: KID = field(metadata=config(field_name="verifyKey"))
    status: int = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class UserVersionVector:
    id: int = field(metadata=config(field_name="id"))
    sig_hints: int = field(metadata=config(field_name="sigHints"))
    sig_chain: int = field(metadata=config(field_name="sigChain"))
    cached_at: Time = field(metadata=config(field_name="cachedAt"))


@dataclass_json
@dataclass
class PerUserKey:
    gen: int = field(metadata=config(field_name="gen"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    sig_kid: KID = field(metadata=config(field_name="sigKID"))
    enc_kid: KID = field(metadata=config(field_name="encKID"))
    signed_by_kid: KID = field(metadata=config(field_name="signedByKID"))


@dataclass_json
@dataclass
class UserOrTeamLite:
    id: UserOrTeamID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))


@dataclass_json
@dataclass
class RemoteTrack:
    username: str = field(metadata=config(field_name="username"))
    uid: UID = field(metadata=config(field_name="uid"))
    link_id: LinkID = field(metadata=config(field_name="linkID"))


@dataclass_json
@dataclass
class SocialAssertion:
    user: str = field(metadata=config(field_name="user"))
    service: SocialAssertionService = field(metadata=config(field_name="service"))


@dataclass_json
@dataclass
class FullNamePackage:
    version: FullNamePackageVersion = field(metadata=config(field_name="version"))
    full_name: FullName = field(metadata=config(field_name="fullName"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    status: StatusCode = field(metadata=config(field_name="status"))
    cached_at: Time = field(metadata=config(field_name="cachedAt"))


@dataclass_json
@dataclass
class PhoneLookupResult:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    ctime: UnixTime = field(metadata=config(field_name="ctime"))


@dataclass_json
@dataclass
class UserReacjis:
    top_reacjis: List[str] = field(metadata=config(field_name="topReacjis"))
    skin_tone: ReacjiSkinTone = field(metadata=config(field_name="skinTone"))


@dataclass_json
@dataclass
class ClientDetails:
    pid: int = field(metadata=config(field_name="pid"))
    client_type: ClientType = field(metadata=config(field_name="clientType"))
    argv: List[str] = field(metadata=config(field_name="argv"))
    desc: str = field(metadata=config(field_name="desc"))
    version: str = field(metadata=config(field_name="version"))


@dataclass_json
@dataclass
class Config:
    server_uri: str = field(metadata=config(field_name="serverURI"))
    socket_file: str = field(metadata=config(field_name="socketFile"))
    label: str = field(metadata=config(field_name="label"))
    run_mode: str = field(metadata=config(field_name="runMode"))
    gpg_exists: bool = field(metadata=config(field_name="gpgExists"))
    gpg_path: str = field(metadata=config(field_name="gpgPath"))
    version: str = field(metadata=config(field_name="version"))
    path: str = field(metadata=config(field_name="path"))
    binary_realpath: str = field(metadata=config(field_name="binaryRealpath"))
    config_path: str = field(metadata=config(field_name="configPath"))
    version_short: str = field(metadata=config(field_name="versionShort"))
    version_full: str = field(metadata=config(field_name="versionFull"))
    is_auto_forked: bool = field(metadata=config(field_name="isAutoForked"))
    fork_type: ForkType = field(metadata=config(field_name="forkType"))


@dataclass_json
@dataclass
class UpdateInfo:
    status: UpdateInfoStatus = field(metadata=config(field_name="status"))
    message: str = field(metadata=config(field_name="message"))


@dataclass
class UpdateInfo2__OK:
    status: Literal[UpdateInfoStatus2.OK]
    OK: None


@dataclass
class UpdateInfo2__SUGGESTED:
    status: Literal[UpdateInfoStatus2.SUGGESTED]
    SUGGESTED: Optional[UpdateDetails]


@dataclass
class UpdateInfo2__CRITICAL:
    status: Literal[UpdateInfoStatus2.CRITICAL]
    CRITICAL: Optional[UpdateDetails]


UpdateInfo2 = Union[UpdateInfo2__OK, UpdateInfo2__SUGGESTED, UpdateInfo2__CRITICAL]


@dataclass_json
@dataclass
class ProxyData:
    address_with_port: str = field(metadata=config(field_name="addressWithPort"))
    proxy_type: ProxyType = field(metadata=config(field_name="proxyType"))
    cert_pinning: bool = field(metadata=config(field_name="certPinning"))


@dataclass_json
@dataclass
class ContactComponent:
    label: str = field(metadata=config(field_name="label"))
    phone_number: Optional[RawPhoneNumber] = field(
        metadata=config(field_name="phoneNumber")
    )
    email: Optional[EmailAddress] = field(metadata=config(field_name="email"))


@dataclass_json
@dataclass
class ED25519SignatureInfo:
    sig: ED25519Signature = field(metadata=config(field_name="sig"))
    public_key: ED25519PublicKey = field(metadata=config(field_name="publicKey"))


@dataclass_json
@dataclass
class CiphertextBundle:
    kid: KID = field(metadata=config(field_name="kid"))
    ciphertext: EncryptedBytes32 = field(metadata=config(field_name="ciphertext"))
    nonce: BoxNonce = field(metadata=config(field_name="nonce"))
    public_key: BoxPublicKey = field(metadata=config(field_name="publicKey"))


@dataclass_json
@dataclass
class UnboxAnyRes:
    kid: KID = field(metadata=config(field_name="kid"))
    plaintext: Bytes32 = field(metadata=config(field_name="plaintext"))
    index: int = field(metadata=config(field_name="index"))


@dataclass_json
@dataclass
class DbKey:
    db_type: DbType = field(metadata=config(field_name="dbType"))
    obj_type: int = field(metadata=config(field_name="objType"))
    key: str = field(metadata=config(field_name="key"))


@dataclass_json
@dataclass
class EmailLookupResult:
    email: EmailAddress = field(metadata=config(field_name="email"))
    uid: Optional[UID] = field(metadata=config(field_name="uid"))


@dataclass_json
@dataclass
class EmailAddressVerifiedMsg:
    email: EmailAddress = field(metadata=config(field_name="email"))


@dataclass_json
@dataclass
class EmailAddressChangedMsg:
    email: EmailAddress = field(metadata=config(field_name="email"))


@dataclass_json
@dataclass
class DeviceEkMetadata:
    kid: KID = field(metadata=config(field_name="device_ephemeral_dh_public"))
    hash_meta: HashMeta = field(metadata=config(field_name="hash_meta"))
    generation: EkGeneration = field(metadata=config(field_name="generation"))
    ctime: Time = field(metadata=config(field_name="ctime"))
    device_ctime: Time = field(metadata=config(field_name="deviceCtime"))


@dataclass_json
@dataclass
class UserEkMetadata:
    kid: KID = field(metadata=config(field_name="user_ephemeral_dh_public"))
    hash_meta: HashMeta = field(metadata=config(field_name="hash_meta"))
    generation: EkGeneration = field(metadata=config(field_name="generation"))
    ctime: Time = field(metadata=config(field_name="ctime"))


@dataclass_json
@dataclass
class UserEkBoxMetadata:
    box: str = field(metadata=config(field_name="box"))
    recipient_generation: EkGeneration = field(
        metadata=config(field_name="recipient_generation")
    )
    recipient_device_id: DeviceID = field(
        metadata=config(field_name="recipient_device_id")
    )


@dataclass_json
@dataclass
class TeamEkMetadata:
    kid: KID = field(metadata=config(field_name="team_ephemeral_dh_public"))
    hash_meta: HashMeta = field(metadata=config(field_name="hash_meta"))
    generation: EkGeneration = field(metadata=config(field_name="generation"))
    ctime: Time = field(metadata=config(field_name="ctime"))


@dataclass_json
@dataclass
class TeamEkBoxMetadata:
    box: str = field(metadata=config(field_name="box"))
    recipient_generation: EkGeneration = field(
        metadata=config(field_name="recipient_generation")
    )
    recipient_uid: UID = field(metadata=config(field_name="recipient_uid"))


@dataclass_json
@dataclass
class TeambotEkMetadata:
    kid: KID = field(metadata=config(field_name="teambot_dh_public"))
    generation: EkGeneration = field(metadata=config(field_name="generation"))
    uid: UID = field(metadata=config(field_name="uid"))
    user_ek_generation: EkGeneration = field(
        metadata=config(field_name="user_ek_generation")
    )
    hash_meta: HashMeta = field(metadata=config(field_name="hash_meta"))
    ctime: Time = field(metadata=config(field_name="ctime"))


@dataclass_json
@dataclass
class FolderHandle:
    name: str = field(metadata=config(field_name="name"))
    folder_type: FolderType = field(metadata=config(field_name="folderType"))
    created: bool = field(metadata=config(field_name="created"))


@dataclass_json
@dataclass
class ListResult:
    files: List[File] = field(metadata=config(field_name="files"))


@dataclass_json
@dataclass
class EncryptedGitMetadata:
    v: int = field(metadata=config(field_name="v"))
    e: bytes = field(metadata=config(field_name="e"))
    n: BoxNonce = field(metadata=config(field_name="n"))
    gen: PerTeamKeyGeneration = field(metadata=config(field_name="gen"))


@dataclass_json
@dataclass
class GitLocalMetadataV1:
    repo_name: GitRepoName = field(metadata=config(field_name="repoName"))


@dataclass_json
@dataclass
class GitCommit:
    commit_hash: str = field(metadata=config(field_name="commitHash"))
    message: str = field(metadata=config(field_name="message"))
    author_name: str = field(metadata=config(field_name="authorName"))
    author_email: str = field(metadata=config(field_name="authorEmail"))
    ctime: Time = field(metadata=config(field_name="ctime"))


@dataclass_json
@dataclass
class GitServerMetadata:
    ctime: Time = field(metadata=config(field_name="ctime"))
    mtime: Time = field(metadata=config(field_name="mtime"))
    last_modifying_username: str = field(
        metadata=config(field_name="lastModifyingUsername")
    )
    last_modifying_device_id: DeviceID = field(
        metadata=config(field_name="lastModifyingDeviceID")
    )
    last_modifying_device_name: str = field(
        metadata=config(field_name="lastModifyingDeviceName")
    )


@dataclass_json
@dataclass
class GPGKey:
    algorithm: str = field(metadata=config(field_name="algorithm"))
    key_id: str = field(metadata=config(field_name="keyID"))
    creation: str = field(metadata=config(field_name="creation"))
    expiration: str = field(metadata=config(field_name="expiration"))
    identities: List[PGPIdentity] = field(metadata=config(field_name="identities"))


@dataclass_json
@dataclass
class HomeScreenAnnouncement:
    id: HomeScreenAnnouncementID = field(metadata=config(field_name="id"))
    version: HomeScreenAnnouncementVersion = field(
        metadata=config(field_name="version")
    )
    app_link: AppLinkType = field(metadata=config(field_name="appLink"))
    confirm_label: str = field(metadata=config(field_name="confirmLabel"))
    dismissable: bool = field(metadata=config(field_name="dismissable"))
    icon_url: str = field(metadata=config(field_name="iconUrl"))
    text: str = field(metadata=config(field_name="text"))
    url: str = field(metadata=config(field_name="url"))


@dataclass
class HomeScreenTodo__VERIFY_ALL_PHONE_NUMBER:
    t: Literal[HomeScreenTodoType.VERIFY_ALL_PHONE_NUMBER]
    VERIFY_ALL_PHONE_NUMBER: Optional[PhoneNumber]


@dataclass
class HomeScreenTodo__VERIFY_ALL_EMAIL:
    t: Literal[HomeScreenTodoType.VERIFY_ALL_EMAIL]
    VERIFY_ALL_EMAIL: Optional[EmailAddress]


@dataclass
class HomeScreenTodo__LEGACY_EMAIL_VISIBILITY:
    t: Literal[HomeScreenTodoType.LEGACY_EMAIL_VISIBILITY]
    LEGACY_EMAIL_VISIBILITY: Optional[EmailAddress]


HomeScreenTodo = Union[
    HomeScreenTodo__VERIFY_ALL_PHONE_NUMBER,
    HomeScreenTodo__VERIFY_ALL_EMAIL,
    HomeScreenTodo__LEGACY_EMAIL_VISIBILITY,
]


@dataclass_json
@dataclass
class VerifyAllEmailTodoExt:
    last_verify_email_date: UnixTime = field(
        metadata=config(field_name="lastVerifyEmailDate")
    )


@dataclass_json
@dataclass
class HomeUserSummary:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    bio: str = field(metadata=config(field_name="bio"))
    full_name: str = field(metadata=config(field_name="full_name"))
    pics: Optional[Pics] = field(metadata=config(field_name="pics"))


@dataclass_json
@dataclass
class Identify3RowMeta:
    color: Identify3RowColor = field(metadata=config(field_name="color"))
    label: str = field(metadata=config(field_name="label"))


@dataclass_json
@dataclass
class TrackDiff:
    type: TrackDiffType = field(metadata=config(field_name="type"))
    display_markup: str = field(metadata=config(field_name="displayMarkup"))


@dataclass_json
@dataclass
class TrackSummary:
    username: str = field(metadata=config(field_name="username"))
    time: Time = field(metadata=config(field_name="time"))
    is_remote: bool = field(metadata=config(field_name="isRemote"))


@dataclass_json
@dataclass
class TrackOptions:
    local_only: bool = field(metadata=config(field_name="localOnly"))
    bypass_confirm: bool = field(metadata=config(field_name="bypassConfirm"))
    force_retrack: bool = field(metadata=config(field_name="forceRetrack"))
    expiring_local: bool = field(metadata=config(field_name="expiringLocal"))
    for_pgp_pull: bool = field(metadata=config(field_name="forPGPPull"))
    sig_version: Optional[SigVersion] = field(metadata=config(field_name="sigVersion"))


@dataclass_json
@dataclass
class IdentifyReason:
    type: IdentifyReasonType = field(metadata=config(field_name="type"))
    reason: str = field(metadata=config(field_name="reason"))
    resource: str = field(metadata=config(field_name="resource"))


@dataclass_json
@dataclass
class RemoteProof:
    proof_type: ProofType = field(metadata=config(field_name="proofType"))
    key: str = field(metadata=config(field_name="key"))
    value: str = field(metadata=config(field_name="value"))
    display_markup: str = field(metadata=config(field_name="displayMarkup"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))
    m_time: Time = field(metadata=config(field_name="mTime"))


@dataclass_json
@dataclass
class ProofResult:
    state: ProofState = field(metadata=config(field_name="state"))
    status: ProofStatus = field(metadata=config(field_name="status"))
    desc: str = field(metadata=config(field_name="desc"))


@dataclass_json
@dataclass
class Cryptocurrency:
    row_id: int = field(metadata=config(field_name="rowId"))
    pkhash: bytes = field(metadata=config(field_name="pkhash"))
    address: str = field(metadata=config(field_name="address"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))
    type: str = field(metadata=config(field_name="type"))
    family: str = field(metadata=config(field_name="family"))


@dataclass_json
@dataclass
class StellarAccount:
    account_id: str = field(metadata=config(field_name="accountID"))
    federation_address: str = field(metadata=config(field_name="federationAddress"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))


@dataclass_json
@dataclass
class UserTeamShowcase:
    fq_name: str = field(metadata=config(field_name="fq_name"))
    open: bool = field(metadata=config(field_name="open"))
    team_is_showcased: bool = field(metadata=config(field_name="team_is_showcased"))
    description: str = field(metadata=config(field_name="description"))
    role: TeamRole = field(metadata=config(field_name="role"))
    public_admins: List[str] = field(metadata=config(field_name="public_admins"))
    num_members: int = field(metadata=config(field_name="num_members"))


@dataclass_json
@dataclass
class DismissReason:
    type: DismissReasonType = field(metadata=config(field_name="type"))
    reason: str = field(metadata=config(field_name="reason"))
    resource: str = field(metadata=config(field_name="resource"))


@dataclass_json
@dataclass
class KBFSTeamSettings:
    tlf_id: TLFID = field(metadata=config(field_name="tlfID"))


@dataclass_json
@dataclass
class FSNotification:
    filename: str = field(metadata=config(field_name="filename"))
    status: str = field(metadata=config(field_name="status"))
    status_code: FSStatusCode = field(metadata=config(field_name="statusCode"))
    notification_type: FSNotificationType = field(
        metadata=config(field_name="notificationType")
    )
    error_type: FSErrorType = field(metadata=config(field_name="errorType"))
    params: Dict[str, str] = field(metadata=config(field_name="params"))
    writer_uid: UID = field(metadata=config(field_name="writerUid"))
    local_time: Time = field(metadata=config(field_name="localTime"))
    folder_type: FolderType = field(metadata=config(field_name="folderType"))


@dataclass_json
@dataclass
class FSFolderWriterEdit:
    filename: str = field(metadata=config(field_name="filename"))
    notification_type: FSNotificationType = field(
        metadata=config(field_name="notificationType")
    )
    server_time: Time = field(metadata=config(field_name="serverTime"))


@dataclass_json
@dataclass
class FSPathSyncStatus:
    folder_type: FolderType = field(metadata=config(field_name="folderType"))
    path: str = field(metadata=config(field_name="path"))
    syncing_bytes: int = field(metadata=config(field_name="syncingBytes"))
    syncing_ops: int = field(metadata=config(field_name="syncingOps"))
    synced_bytes: int = field(metadata=config(field_name="syncedBytes"))


@dataclass_json
@dataclass
class FSSyncStatus:
    total_syncing_bytes: int = field(metadata=config(field_name="totalSyncingBytes"))
    syncing_paths: List[str] = field(metadata=config(field_name="syncingPaths"))
    end_estimate: Optional[Time] = field(metadata=config(field_name="endEstimate"))


@dataclass_json
@dataclass
class GcOptions:
    max_loose_refs: int = field(metadata=config(field_name="maxLooseRefs"))
    prune_min_loose_objects: int = field(
        metadata=config(field_name="pruneMinLooseObjects")
    )
    prune_expire_time: Time = field(metadata=config(field_name="pruneExpireTime"))
    max_object_packs: int = field(metadata=config(field_name="maxObjectPacks"))


@dataclass_json
@dataclass
class Hello2Res:
    encryption_key: KID = field(metadata=config(field_name="encryptionKey"))
    sig_payload: HelloRes = field(metadata=config(field_name="sigPayload"))
    device_ek_kid: KID = field(metadata=config(field_name="deviceEkKID"))


@dataclass_json
@dataclass
class PerUserKeyBox:
    generation: PerUserKeyGeneration = field(metadata=config(field_name="generation"))
    box: str = field(metadata=config(field_name="box"))
    receiver_kid: KID = field(metadata=config(field_name="receiver_kid"))


@dataclass_json
@dataclass
class ConfiguredAccount:
    username: str = field(metadata=config(field_name="username"))
    fullname: FullName = field(metadata=config(field_name="fullname"))
    has_stored_secret: bool = field(metadata=config(field_name="hasStoredSecret"))
    is_current: bool = field(metadata=config(field_name="isCurrent"))


@dataclass_json
@dataclass
class KBFSRoot:
    tree_id: MerkleTreeID = field(metadata=config(field_name="treeID"))
    root: KBFSRootHash = field(metadata=config(field_name="root"))


@dataclass_json
@dataclass
class MerkleStoreEntry:
    hash: MerkleStoreKitHash = field(metadata=config(field_name="hash"))
    entry: MerkleStoreEntryString = field(metadata=config(field_name="entry"))


@dataclass_json
@dataclass
class KeyHalf:
    user: UID = field(metadata=config(field_name="user"))
    device_kid: KID = field(metadata=config(field_name="deviceKID"))
    key: bytes = field(metadata=config(field_name="key"))


@dataclass_json
@dataclass
class MDBlock:
    version: int = field(metadata=config(field_name="version"))
    timestamp: Time = field(metadata=config(field_name="timestamp"))
    block: bytes = field(metadata=config(field_name="block"))


@dataclass_json
@dataclass
class PingResponse:
    timestamp: Time = field(metadata=config(field_name="timestamp"))


@dataclass_json
@dataclass
class KeyBundleResponse:
    writer_bundle: KeyBundle = field(metadata=config(field_name="WriterBundle"))
    reader_bundle: KeyBundle = field(metadata=config(field_name="ReaderBundle"))


@dataclass_json
@dataclass
class LockContext:
    require_lock_id: LockID = field(metadata=config(field_name="requireLockID"))
    release_after_success: bool = field(
        metadata=config(field_name="releaseAfterSuccess")
    )


@dataclass_json
@dataclass
class FindNextMDResponse:
    kbfs_root: MerkleRoot = field(metadata=config(field_name="kbfsRoot"))
    merkle_nodes: List[bytes] = field(metadata=config(field_name="merkleNodes"))
    root_seqno: Seqno = field(metadata=config(field_name="rootSeqno"))
    root_hash: HashMeta = field(metadata=config(field_name="rootHash"))


@dataclass_json
@dataclass
class TeamMemberOutReset:
    teamname: str = field(metadata=config(field_name="teamname"))
    username: str = field(metadata=config(field_name="username"))
    uid: UID = field(metadata=config(field_name="uid"))
    id: gregor1.MsgID = field(metadata=config(field_name="id"))


@dataclass_json
@dataclass
class ResetState:
    end_time: Time = field(metadata=config(field_name="end_time"))
    active: bool = field(metadata=config(field_name="active"))


@dataclass_json
@dataclass
class BadgeConversationInfo:
    conv_id: ChatConversationID = field(metadata=config(field_name="convID"))
    badge_counts: Dict[str, int] = field(metadata=config(field_name="badgeCounts"))
    unread_messages: int = field(metadata=config(field_name="unreadMessages"))


@dataclass_json
@dataclass
class DbStats:
    type: DbType = field(metadata=config(field_name="type"))
    mem_comp_active: bool = field(metadata=config(field_name="memCompActive"))
    table_comp_active: bool = field(metadata=config(field_name="tableCompActive"))


@dataclass_json
@dataclass
class ProcessRuntimeStats:
    type: ProcessType = field(metadata=config(field_name="type"))
    cpu: str = field(metadata=config(field_name="cpu"))
    resident: str = field(metadata=config(field_name="resident"))
    virt: str = field(metadata=config(field_name="virt"))
    free: str = field(metadata=config(field_name="free"))
    goheap: str = field(metadata=config(field_name="goheap"))
    goheapsys: str = field(metadata=config(field_name="goheapsys"))
    goreleased: str = field(metadata=config(field_name="goreleased"))
    cpu_severity: StatsSeverityLevel = field(metadata=config(field_name="cpuSeverity"))
    resident_severity: StatsSeverityLevel = field(
        metadata=config(field_name="residentSeverity")
    )


@dataclass_json
@dataclass
class GUIEntryFeatures:
    show_typing: Feature = field(metadata=config(field_name="showTyping"))


@dataclass_json
@dataclass
class PGPSignOptions:
    key_query: str = field(metadata=config(field_name="keyQuery"))
    mode: SignMode = field(metadata=config(field_name="mode"))
    binary_in: bool = field(metadata=config(field_name="binaryIn"))
    binary_out: bool = field(metadata=config(field_name="binaryOut"))


@dataclass_json
@dataclass
class PGPCreateUids:
    use_default: bool = field(metadata=config(field_name="useDefault"))
    ids: List[PGPIdentity] = field(metadata=config(field_name="ids"))


@dataclass_json
@dataclass
class UserPhoneNumber:
    phone_number: PhoneNumber = field(metadata=config(field_name="phone_number"))
    verified: bool = field(metadata=config(field_name="verified"))
    superseded: bool = field(metadata=config(field_name="superseded"))
    visibility: IdentityVisibility = field(metadata=config(field_name="visibility"))
    ctime: UnixTime = field(metadata=config(field_name="ctime"))


@dataclass_json
@dataclass
class PhoneNumberLookupResult:
    phone_number: RawPhoneNumber = field(metadata=config(field_name="phone_number"))
    coerced_phone_number: PhoneNumber = field(
        metadata=config(field_name="coerced_phone_number")
    )
    err: Optional[str] = field(metadata=config(field_name="err"))
    uid: Optional[UID] = field(metadata=config(field_name="uid"))


@dataclass_json
@dataclass
class PhoneNumberChangedMsg:
    phone_number: PhoneNumber = field(metadata=config(field_name="phone"))


@dataclass_json
@dataclass
class FileDescriptor:
    name: str = field(metadata=config(field_name="name"))
    type: FileType = field(metadata=config(field_name="type"))


@dataclass_json
@dataclass
class CheckProofStatus:
    found: bool = field(metadata=config(field_name="found"))
    status: ProofStatus = field(metadata=config(field_name="status"))
    proof_text: str = field(metadata=config(field_name="proofText"))
    state: ProofState = field(metadata=config(field_name="state"))


@dataclass_json
@dataclass
class StartProofResult:
    sig_id: SigID = field(metadata=config(field_name="sigID"))


@dataclass_json
@dataclass
class ParamProofJSON:
    sig_hash: SigID = field(metadata=config(field_name="sig_hash"))
    kb_username: str = field(metadata=config(field_name="kb_username"))


@dataclass_json
@dataclass
class ParamProofServiceConfig:
    version: int = field(metadata=config(field_name="version"))
    domain: str = field(metadata=config(field_name="domain"))
    display_name: str = field(metadata=config(field_name="display_name"))
    logo: Optional[ParamProofLogoConfig] = field(metadata=config(field_name="logo"))
    description: str = field(metadata=config(field_name="description"))
    username_config: ParamProofUsernameConfig = field(
        metadata=config(field_name="username")
    )
    brand_color: str = field(metadata=config(field_name="brand_color"))
    prefill_url: str = field(metadata=config(field_name="prefill_url"))
    profile_url: str = field(metadata=config(field_name="profile_url"))
    check_url: str = field(metadata=config(field_name="check_url"))
    check_path: List[SelectorEntry] = field(metadata=config(field_name="check_path"))
    avatar_path: List[SelectorEntry] = field(metadata=config(field_name="avatar_path"))


@dataclass_json
@dataclass
class ProveParameters:
    logo_full: List[SizedImage] = field(metadata=config(field_name="logoFull"))
    logo_black: List[SizedImage] = field(metadata=config(field_name="logoBlack"))
    title: str = field(metadata=config(field_name="title"))
    subtext: str = field(metadata=config(field_name="subtext"))
    suffix: str = field(metadata=config(field_name="suffix"))
    button_label: str = field(metadata=config(field_name="buttonLabel"))


@dataclass_json
@dataclass
class VerifySessionRes:
    uid: UID = field(metadata=config(field_name="uid"))
    sid: str = field(metadata=config(field_name="sid"))
    generated: int = field(metadata=config(field_name="generated"))
    lifetime: int = field(metadata=config(field_name="lifetime"))


@dataclass_json
@dataclass
class Reachability:
    reachable: Reachable = field(metadata=config(field_name="reachable"))


@dataclass_json
@dataclass
class TLF:
    id: TLFID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))
    writers: List[str] = field(metadata=config(field_name="writers"))
    readers: List[str] = field(metadata=config(field_name="readers"))
    is_private: bool = field(metadata=config(field_name="isPrivate"))


@dataclass_json
@dataclass
class RekeyEvent:
    event_type: RekeyEventType = field(metadata=config(field_name="eventType"))
    interrupt_type: int = field(metadata=config(field_name="interruptType"))


@dataclass_json
@dataclass
class ResetMerkleRoot:
    hash_meta: HashMeta = field(metadata=config(field_name="hash_meta"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))


@dataclass_json
@dataclass
class ResetPrev:
    eldest_kid: Optional[KID] = field(metadata=config(field_name="eldest_kid"))
    last_seqno: Seqno = field(metadata=config(field_name="public_seqno"))
    reset: SHA512 = field(metadata=config(field_name="reset"))


@dataclass_json
@dataclass
class SaltpackEncryptOptions:
    recipients: List[str] = field(metadata=config(field_name="recipients"))
    team_recipients: List[str] = field(metadata=config(field_name="teamRecipients"))
    authenticity_type: AuthenticityType = field(
        metadata=config(field_name="authenticityType")
    )
    use_entity_keys: bool = field(metadata=config(field_name="useEntityKeys"))
    use_device_keys: bool = field(metadata=config(field_name="useDeviceKeys"))
    use_paper_keys: bool = field(metadata=config(field_name="usePaperKeys"))
    no_self_encrypt: bool = field(metadata=config(field_name="noSelfEncrypt"))
    binary: bool = field(metadata=config(field_name="binary"))
    saltpack_version: int = field(metadata=config(field_name="saltpackVersion"))
    use_kbfs_keys_only_for_testing: bool = field(
        metadata=config(field_name="useKBFSKeysOnlyForTesting")
    )


@dataclass_json
@dataclass
class SaltpackSender:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    sender_type: SaltpackSenderType = field(metadata=config(field_name="senderType"))


@dataclass_json
@dataclass
class SecretKeys:
    signing: NaclSigningKeyPrivate = field(metadata=config(field_name="signing"))
    encryption: NaclDHKeyPrivate = field(metadata=config(field_name="encryption"))


@dataclass_json
@dataclass
class Session:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    token: str = field(metadata=config(field_name="token"))
    device_subkey_kid: KID = field(metadata=config(field_name="deviceSubkeyKid"))
    device_sibkey_kid: KID = field(metadata=config(field_name="deviceSibkeyKid"))


@dataclass_json
@dataclass
class Sig:
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))
    sig_id_display: str = field(metadata=config(field_name="sigIDDisplay"))
    type: str = field(metadata=config(field_name="type"))
    c_time: Time = field(metadata=config(field_name="cTime"))
    revoked: bool = field(metadata=config(field_name="revoked"))
    active: bool = field(metadata=config(field_name="active"))
    key: str = field(metadata=config(field_name="key"))
    body: str = field(metadata=config(field_name="body"))


@dataclass_json
@dataclass
class SigListArgs:
    session_id: int = field(metadata=config(field_name="sessionID"))
    username: str = field(metadata=config(field_name="username"))
    all_keys: bool = field(metadata=config(field_name="allKeys"))
    types: Optional[SigTypes] = field(metadata=config(field_name="types"))
    filterx: str = field(metadata=config(field_name="filterx"))
    verbose: bool = field(metadata=config(field_name="verbose"))
    revoked: bool = field(metadata=config(field_name="revoked"))


@dataclass
class KBFSArchivedParam__REVISION:
    KBFSArchivedType: Literal[KBFSArchivedType.REVISION]
    REVISION: Optional[KBFSRevision]


@dataclass
class KBFSArchivedParam__TIME:
    KBFSArchivedType: Literal[KBFSArchivedType.TIME]
    TIME: Optional[Time]


@dataclass
class KBFSArchivedParam__TIME_STRING:
    KBFSArchivedType: Literal[KBFSArchivedType.TIME_STRING]
    TIME_STRING: Optional[str]


@dataclass
class KBFSArchivedParam__REL_TIME_STRING:
    KBFSArchivedType: Literal[KBFSArchivedType.REL_TIME_STRING]
    REL_TIME_STRING: Optional[str]


KBFSArchivedParam = Union[
    KBFSArchivedParam__REVISION,
    KBFSArchivedParam__TIME,
    KBFSArchivedParam__TIME_STRING,
    KBFSArchivedParam__REL_TIME_STRING,
]


@dataclass_json
@dataclass
class KBFSPath:
    path: str = field(metadata=config(field_name="path"))
    identify_behavior: Optional[TLFIdentifyBehavior] = field(
        metadata=config(field_name="identifyBehavior")
    )


@dataclass_json
@dataclass
class PrefetchProgress:
    start: Time = field(metadata=config(field_name="start"))
    end_estimate: Time = field(metadata=config(field_name="endEstimate"))
    bytes_total: int = field(metadata=config(field_name="bytesTotal"))
    bytes_fetched: int = field(metadata=config(field_name="bytesFetched"))


@dataclass_json
@dataclass
class FileContent:
    data: bytes = field(metadata=config(field_name="data"))
    progress: Progress = field(metadata=config(field_name="progress"))


@dataclass_json
@dataclass
class OpProgress:
    start: Time = field(metadata=config(field_name="start"))
    end_estimate: Time = field(metadata=config(field_name="endEstimate"))
    op_type: AsyncOps = field(metadata=config(field_name="opType"))
    bytes_total: int = field(metadata=config(field_name="bytesTotal"))
    bytes_read: int = field(metadata=config(field_name="bytesRead"))
    bytes_written: int = field(metadata=config(field_name="bytesWritten"))
    files_total: int = field(metadata=config(field_name="filesTotal"))
    files_read: int = field(metadata=config(field_name="filesRead"))
    files_written: int = field(metadata=config(field_name="filesWritten"))


@dataclass_json
@dataclass
class FolderSyncConfig:
    mode: FolderSyncMode = field(metadata=config(field_name="mode"))
    paths: List[str] = field(metadata=config(field_name="paths"))


@dataclass_json
@dataclass
class TeambotKeyMetadata:
    kid: KID = field(metadata=config(field_name="teambot_dh_public"))
    generation: TeambotKeyGeneration = field(metadata=config(field_name="generation"))
    uid: UID = field(metadata=config(field_name="uid"))
    puk_generation: PerUserKeyGeneration = field(
        metadata=config(field_name="puk_generation")
    )


@dataclass_json
@dataclass
class PerTeamSeedCheck:
    version: PerTeamSeedCheckVersion = field(metadata=config(field_name="version"))
    value: PerTeamSeedCheckValue = field(metadata=config(field_name="value"))


@dataclass_json
@dataclass
class PerTeamSeedCheckPostImage:
    value: PerTeamSeedCheckValuePostImage = field(metadata=config(field_name="h"))
    version: PerTeamSeedCheckVersion = field(metadata=config(field_name="v"))


@dataclass_json
@dataclass
class TeamApplicationKey:
    application: TeamApplication = field(metadata=config(field_name="application"))
    key_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="keyGeneration")
    )
    key: Bytes32 = field(metadata=config(field_name="key"))


@dataclass_json
@dataclass
class ReaderKeyMask:
    application: TeamApplication = field(metadata=config(field_name="application"))
    generation: PerTeamKeyGeneration = field(metadata=config(field_name="generation"))
    mask: MaskB64 = field(metadata=config(field_name="mask"))


@dataclass_json
@dataclass
class PerTeamKey:
    gen: PerTeamKeyGeneration = field(metadata=config(field_name="gen"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    sig_kid: KID = field(metadata=config(field_name="sigKID"))
    enc_kid: KID = field(metadata=config(field_name="encKID"))


@dataclass_json
@dataclass
class TeamMember:
    uid: UID = field(metadata=config(field_name="uid"))
    role: TeamRole = field(metadata=config(field_name="role"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    status: TeamMemberStatus = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class LinkTriple:
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    seq_type: SeqType = field(metadata=config(field_name="seqType"))
    link_id: LinkID = field(metadata=config(field_name="linkID"))


@dataclass_json
@dataclass
class UpPointer:
    our_seqno: Seqno = field(metadata=config(field_name="ourSeqno"))
    parent_id: TeamID = field(metadata=config(field_name="parentID"))
    parent_seqno: Seqno = field(metadata=config(field_name="parentSeqno"))
    deletion: bool = field(metadata=config(field_name="deletion"))


@dataclass_json
@dataclass
class DownPointer:
    id: TeamID = field(metadata=config(field_name="id"))
    name_component: str = field(metadata=config(field_name="nameComponent"))
    is_deleted: bool = field(metadata=config(field_name="isDeleted"))


@dataclass_json
@dataclass
class Signer:
    e: Seqno = field(metadata=config(field_name="e"))
    k: KID = field(metadata=config(field_name="k"))
    u: UID = field(metadata=config(field_name="u"))


@dataclass_json
@dataclass
class Audit:
    time: Time = field(metadata=config(field_name="time"))
    max_merkle_seqno: Seqno = field(metadata=config(field_name="mms"))
    max_chain_seqno: Seqno = field(metadata=config(field_name="mcs"))
    max_merkle_probe: Seqno = field(metadata=config(field_name="mmp"))


@dataclass_json
@dataclass
class Probe:
    index: int = field(metadata=config(field_name="i"))
    team_seqno: Seqno = field(metadata=config(field_name="t"))


@dataclass
class TeamInviteType__UNKNOWN:
    c: Literal[TeamInviteCategory.UNKNOWN]
    UNKNOWN: Optional[str]


@dataclass
class TeamInviteType__SBS:
    c: Literal[TeamInviteCategory.SBS]
    SBS: Optional[TeamInviteSocialNetwork]


TeamInviteType = Union[TeamInviteType__UNKNOWN, TeamInviteType__SBS]


@dataclass_json
@dataclass
class TeamGetLegacyTLFUpgrade:
    encrypted_keyset: str = field(metadata=config(field_name="encrypted_keyset"))
    team_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="team_generation")
    )
    legacy_generation: int = field(metadata=config(field_name="legacy_generation"))
    app_type: TeamApplication = field(metadata=config(field_name="app_type"))


@dataclass_json
@dataclass
class TeamLegacyTLFUpgradeChainInfo:
    keyset_hash: TeamEncryptedKBFSKeysetHash = field(
        metadata=config(field_name="keysetHash")
    )
    team_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="teamGeneration")
    )
    legacy_generation: int = field(metadata=config(field_name="legacyGeneration"))
    app_type: TeamApplication = field(metadata=config(field_name="appType"))


@dataclass_json
@dataclass
class TeamNameLogPoint:
    last_part: TeamNamePart = field(metadata=config(field_name="lastPart"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))


@dataclass_json
@dataclass
class TeamName:
    parts: List[TeamNamePart] = field(metadata=config(field_name="parts"))


@dataclass_json
@dataclass
class TeamCLKRResetUser:
    uid: UID = field(metadata=config(field_name="uid"))
    user_eldest_seqno: Seqno = field(metadata=config(field_name="user_eldest"))
    member_eldest_seqno: Seqno = field(metadata=config(field_name="member_eldest"))


@dataclass_json
@dataclass
class TeamResetUser:
    username: str = field(metadata=config(field_name="username"))
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldest_seqno"))
    is_delete: bool = field(metadata=config(field_name="is_delete"))


@dataclass_json
@dataclass
class TeamChangeRow:
    id: TeamID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))
    key_rotated: bool = field(metadata=config(field_name="key_rotated"))
    membership_changed: bool = field(metadata=config(field_name="membership_changed"))
    latest_seqno: Seqno = field(metadata=config(field_name="latest_seqno"))
    latest_hidden_seqno: Seqno = field(
        metadata=config(field_name="latest_hidden_seqno")
    )
    implicit_team: bool = field(metadata=config(field_name="implicit_team"))
    misc: bool = field(metadata=config(field_name="misc"))
    removed_reset_users: bool = field(metadata=config(field_name="removed_reset_users"))


@dataclass_json
@dataclass
class TeamExitRow:
    id: TeamID = field(metadata=config(field_name="id"))


@dataclass_json
@dataclass
class TeamNewlyAddedRow:
    id: TeamID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))


@dataclass_json
@dataclass
class TeamInvitee:
    invite_id: TeamInviteID = field(metadata=config(field_name="invite_id"))
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldest_seqno"))
    role: TeamRole = field(metadata=config(field_name="role"))


@dataclass_json
@dataclass
class TeamAccessRequest:
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldest_seqno"))


@dataclass
class SeitanKeyLabel__SMS:
    t: Literal[SeitanKeyLabelType.SMS]
    SMS: Optional[SeitanKeyLabelSms]


SeitanKeyLabel = Union[SeitanKeyLabel__SMS]


@dataclass_json
@dataclass
class TeamSeitanRequest:
    invite_id: TeamInviteID = field(metadata=config(field_name="invite_id"))
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldest_seqno"))
    akey: SeitanAKey = field(metadata=config(field_name="akey"))
    role: TeamRole = field(metadata=config(field_name="role"))
    unix_c_time: int = field(metadata=config(field_name="ctime"))


@dataclass_json
@dataclass
class TeamKBFSKeyRefresher:
    generation: int = field(metadata=config(field_name="generation"))
    app_type: TeamApplication = field(metadata=config(field_name="appType"))


@dataclass_json
@dataclass
class ImplicitRole:
    role: TeamRole = field(metadata=config(field_name="role"))
    ancestor: TeamID = field(metadata=config(field_name="ancestor"))


@dataclass_json
@dataclass
class TeamCreateResult:
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    chat_sent: bool = field(metadata=config(field_name="chatSent"))
    creator_added: bool = field(metadata=config(field_name="creatorAdded"))


@dataclass_json
@dataclass
class TeamSettings:
    open: bool = field(metadata=config(field_name="open"))
    join_as: TeamRole = field(metadata=config(field_name="joinAs"))


@dataclass_json
@dataclass
class TeamShowcase:
    is_showcased: bool = field(metadata=config(field_name="is_showcased"))
    description: Optional[str] = field(metadata=config(field_name="description"))
    set_by_uid: Optional[UID] = field(metadata=config(field_name="set_by_uid"))
    any_member_showcase: bool = field(metadata=config(field_name="any_member_showcase"))


@dataclass_json
@dataclass
class UserRolePair:
    assertion_or_email: str = field(metadata=config(field_name="assertionOrEmail"))
    role: TeamRole = field(metadata=config(field_name="role"))
    bot_settings: Optional[TeamBotSettings] = field(
        metadata=config(field_name="botSettings")
    )


@dataclass_json
@dataclass
class ImplicitTeamConflictInfo:
    generation: ConflictGeneration = field(metadata=config(field_name="generation"))
    time: Time = field(metadata=config(field_name="time"))


@dataclass_json
@dataclass
class CryptKey:
    key_generation: int = field(metadata=config(field_name="KeyGeneration"))
    key: Bytes32 = field(metadata=config(field_name="Key"))


@dataclass_json
@dataclass
class TLFQuery:
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    identify_behavior: TLFIdentifyBehavior = field(
        metadata=config(field_name="identifyBehavior")
    )


@dataclass_json
@dataclass
class MerkleRootV2:
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    hash_meta: HashMeta = field(metadata=config(field_name="hashMeta"))


@dataclass_json
@dataclass
class SigChainLocation:
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    seq_type: SeqType = field(metadata=config(field_name="seqType"))


@dataclass_json
@dataclass
class Email:
    email: EmailAddress = field(metadata=config(field_name="email"))
    is_verified: bool = field(metadata=config(field_name="isVerified"))
    is_primary: bool = field(metadata=config(field_name="isPrimary"))
    visibility: IdentityVisibility = field(metadata=config(field_name="visibility"))
    last_verify_email_date: UnixTime = field(
        metadata=config(field_name="lastVerifyEmailDate")
    )


@dataclass_json
@dataclass
class UserSummary2:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    thumbnail: str = field(metadata=config(field_name="thumbnail"))
    full_name: str = field(metadata=config(field_name="fullName"))
    is_follower: bool = field(metadata=config(field_name="isFollower"))
    is_followee: bool = field(metadata=config(field_name="isFollowee"))


@dataclass_json
@dataclass
class InterestingPerson:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    fullname: str = field(metadata=config(field_name="fullname"))


@dataclass_json
@dataclass
class APIUserKeybaseResult:
    username: str = field(metadata=config(field_name="username"))
    uid: UID = field(metadata=config(field_name="uid"))
    picture_url: Optional[str] = field(metadata=config(field_name="picture_url"))
    full_name: Optional[str] = field(metadata=config(field_name="full_name"))
    raw_score: float = field(metadata=config(field_name="raw_score"))
    stellar: Optional[str] = field(metadata=config(field_name="stellar"))
    is_followee: bool = field(metadata=config(field_name="is_followee"))


@dataclass_json
@dataclass
class APIUserServiceResult:
    service_name: APIUserServiceIDWithContact = field(
        metadata=config(field_name="service_name")
    )
    username: str = field(metadata=config(field_name="username"))
    picture_url: str = field(metadata=config(field_name="picture_url"))
    bio: str = field(metadata=config(field_name="bio"))
    location: str = field(metadata=config(field_name="location"))
    full_name: str = field(metadata=config(field_name="full_name"))
    confirmed: Optional[bool] = field(metadata=config(field_name="confirmed"))


@dataclass_json
@dataclass
class APIUserServiceSummary:
    service_name: APIUserServiceIDWithContact = field(
        metadata=config(field_name="service_name")
    )
    username: str = field(metadata=config(field_name="username"))


@dataclass
class ImpTofuQuery__PHONE:
    t: Literal[ImpTofuSearchType.PHONE]
    PHONE: Optional[PhoneNumber]


@dataclass
class ImpTofuQuery__EMAIL:
    t: Literal[ImpTofuSearchType.EMAIL]
    EMAIL: Optional[EmailAddress]


ImpTofuQuery = Union[ImpTofuQuery__PHONE, ImpTofuQuery__EMAIL]


@dataclass_json
@dataclass
class GetLockdownResponse:
    history: List[LockdownHistory] = field(metadata=config(field_name="history"))
    status: bool = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class BlockReference:
    bid: BlockIdCombo = field(metadata=config(field_name="bid"))
    nonce: BlockRefNonce = field(metadata=config(field_name="nonce"))
    charged_to: UserOrTeamID = field(metadata=config(field_name="chargedTo"))


@dataclass_json
@dataclass
class BlockIdCount:
    id: BlockIdCombo = field(metadata=config(field_name="id"))
    live_count: int = field(metadata=config(field_name="liveCount"))


@dataclass_json
@dataclass
class TeamIDAndName:
    id: TeamID = field(metadata=config(field_name="id"))
    name: TeamName = field(metadata=config(field_name="name"))


@dataclass_json
@dataclass
class RevokedKey:
    key: PublicKey = field(metadata=config(field_name="key"))
    time: KeybaseTime = field(metadata=config(field_name="time"))
    by: KID = field(metadata=config(field_name="by"))


@dataclass_json
@dataclass
class CurrentStatus:
    configured: bool = field(metadata=config(field_name="configured"))
    registered: bool = field(metadata=config(field_name="registered"))
    logged_in: bool = field(metadata=config(field_name="loggedIn"))
    session_is_valid: bool = field(metadata=config(field_name="sessionIsValid"))
    user: Optional[User] = field(metadata=config(field_name="user"))


@dataclass_json
@dataclass
class ClientStatus:
    details: ClientDetails = field(metadata=config(field_name="details"))
    connection_id: int = field(metadata=config(field_name="connectionID"))
    notification_channels: NotificationChannels = field(
        metadata=config(field_name="notificationChannels")
    )


@dataclass_json
@dataclass
class BootstrapStatus:
    registered: bool = field(metadata=config(field_name="registered"))
    logged_in: bool = field(metadata=config(field_name="loggedIn"))
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    device_name: str = field(metadata=config(field_name="deviceName"))
    fullname: FullName = field(metadata=config(field_name="fullname"))
    user_reacjis: UserReacjis = field(metadata=config(field_name="userReacjis"))
    http_srv_info: Optional[HttpSrvInfo] = field(
        metadata=config(field_name="httpSrvInfo")
    )


@dataclass_json
@dataclass
class Contact:
    name: str = field(metadata=config(field_name="name"))
    components: List[ContactComponent] = field(metadata=config(field_name="components"))


@dataclass_json
@dataclass
class ProcessedContact:
    contact_index: int = field(metadata=config(field_name="contactIndex"))
    contact_name: str = field(metadata=config(field_name="contactName"))
    component: ContactComponent = field(metadata=config(field_name="component"))
    resolved: bool = field(metadata=config(field_name="resolved"))
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    full_name: str = field(metadata=config(field_name="fullName"))
    following: bool = field(metadata=config(field_name="following"))
    service_map: Dict[str, str] = field(metadata=config(field_name="serviceMap"))
    assertion: str = field(metadata=config(field_name="assertion"))
    display_name: str = field(metadata=config(field_name="displayName"))
    display_label: str = field(metadata=config(field_name="displayLabel"))


@dataclass_json
@dataclass
class DeviceDetail:
    device: Device = field(metadata=config(field_name="device"))
    eldest: bool = field(metadata=config(field_name="eldest"))
    provisioner: Optional[Device] = field(metadata=config(field_name="provisioner"))
    provisioned_at: Optional[Time] = field(metadata=config(field_name="provisionedAt"))
    revoked_at: Optional[Time] = field(metadata=config(field_name="revokedAt"))
    revoked_by: KID = field(metadata=config(field_name="revokedBy"))
    revoked_by_device: Optional[Device] = field(
        metadata=config(field_name="revokedByDevice")
    )
    current_device: bool = field(metadata=config(field_name="currentDevice"))


@dataclass_json
@dataclass
class DeviceEkStatement:
    current_device_ek_metadata: DeviceEkMetadata = field(
        metadata=config(field_name="current_device_ek_metadata")
    )


@dataclass_json
@dataclass
class DeviceEk:
    seed: Bytes32 = field(metadata=config(field_name="seed"))
    metadata: DeviceEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass_json
@dataclass
class UserEkStatement:
    current_user_ek_metadata: UserEkMetadata = field(
        metadata=config(field_name="current_user_ek_metadata")
    )


@dataclass_json
@dataclass
class UserEkBoxed:
    box: str = field(metadata=config(field_name="box"))
    device_ek_generation: EkGeneration = field(
        metadata=config(field_name="device_ek_generation")
    )
    metadata: UserEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass_json
@dataclass
class UserEk:
    seed: Bytes32 = field(metadata=config(field_name="seed"))
    metadata: UserEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass_json
@dataclass
class UserEkReboxArg:
    user_ek_box_metadata: UserEkBoxMetadata = field(
        metadata=config(field_name="userEkBoxMetadata")
    )
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    device_ek_statement_sig: str = field(
        metadata=config(field_name="deviceEkStatementSig")
    )


@dataclass_json
@dataclass
class TeamEkStatement:
    current_team_ek_metadata: TeamEkMetadata = field(
        metadata=config(field_name="current_team_ek_metadata")
    )


@dataclass_json
@dataclass
class TeamEkBoxed:
    box: str = field(metadata=config(field_name="box"))
    user_ek_generation: EkGeneration = field(
        metadata=config(field_name="user_ek_generation")
    )
    metadata: TeamEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass_json
@dataclass
class TeamEk:
    seed: Bytes32 = field(metadata=config(field_name="seed"))
    metadata: TeamEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass_json
@dataclass
class TeambotEkBoxed:
    box: str = field(metadata=config(field_name="box"))
    metadata: TeambotEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass_json
@dataclass
class TeambotEk:
    seed: Bytes32 = field(metadata=config(field_name="seed"))
    metadata: TeambotEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass
class GitLocalMetadataVersioned__V1:
    version: Literal[GitLocalMetadataVersion.V1]
    V1: Optional[GitLocalMetadataV1]


GitLocalMetadataVersioned = Union[GitLocalMetadataVersioned__V1]


@dataclass_json
@dataclass
class GitRefMetadata:
    ref_name: str = field(metadata=config(field_name="refName"))
    commits: List[GitCommit] = field(metadata=config(field_name="commits"))
    more_commits_available: bool = field(
        metadata=config(field_name="moreCommitsAvailable")
    )
    is_delete: bool = field(metadata=config(field_name="isDelete"))


@dataclass
class HomeScreenTodoExt__VERIFY_ALL_EMAIL:
    t: Literal[HomeScreenTodoType.VERIFY_ALL_EMAIL]
    VERIFY_ALL_EMAIL: Optional[VerifyAllEmailTodoExt]


HomeScreenTodoExt = Union[HomeScreenTodoExt__VERIFY_ALL_EMAIL]


@dataclass_json
@dataclass
class Identify3Row:
    gui_id: Identify3GUIID = field(metadata=config(field_name="guiID"))
    key: str = field(metadata=config(field_name="key"))
    value: str = field(metadata=config(field_name="value"))
    priority: int = field(metadata=config(field_name="priority"))
    site_url: str = field(metadata=config(field_name="siteURL"))
    site_icon: List[SizedImage] = field(metadata=config(field_name="siteIcon"))
    site_icon_full: List[SizedImage] = field(metadata=config(field_name="siteIconFull"))
    proof_url: str = field(metadata=config(field_name="proofURL"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))
    ctime: Time = field(metadata=config(field_name="ctime"))
    state: Identify3RowState = field(metadata=config(field_name="state"))
    metas: List[Identify3RowMeta] = field(metadata=config(field_name="metas"))
    color: Identify3RowColor = field(metadata=config(field_name="color"))
    kid: Optional[KID] = field(metadata=config(field_name="kid"))


@dataclass_json
@dataclass
class IdentifyOutcome:
    username: str = field(metadata=config(field_name="username"))
    status: Optional[Status] = field(metadata=config(field_name="status"))
    warnings: List[str] = field(metadata=config(field_name="warnings"))
    track_used: Optional[TrackSummary] = field(metadata=config(field_name="trackUsed"))
    track_status: TrackStatus = field(metadata=config(field_name="trackStatus"))
    num_track_failures: int = field(metadata=config(field_name="numTrackFailures"))
    num_track_changes: int = field(metadata=config(field_name="numTrackChanges"))
    num_proof_failures: int = field(metadata=config(field_name="numProofFailures"))
    num_revoked: int = field(metadata=config(field_name="numRevoked"))
    num_proof_successes: int = field(metadata=config(field_name="numProofSuccesses"))
    revoked: List[TrackDiff] = field(metadata=config(field_name="revoked"))
    track_options: TrackOptions = field(metadata=config(field_name="trackOptions"))
    for_pgp_pull: bool = field(metadata=config(field_name="forPGPPull"))
    reason: IdentifyReason = field(metadata=config(field_name="reason"))


@dataclass_json
@dataclass
class IdentifyRow:
    row_id: int = field(metadata=config(field_name="rowId"))
    proof: RemoteProof = field(metadata=config(field_name="proof"))
    track_diff: Optional[TrackDiff] = field(metadata=config(field_name="trackDiff"))


@dataclass_json
@dataclass
class IdentifyKey:
    pgp_fingerprint: bytes = field(metadata=config(field_name="pgpFingerprint"))
    kid: KID = field(metadata=config(field_name="KID"))
    track_diff: Optional[TrackDiff] = field(metadata=config(field_name="trackDiff"))
    breaks_tracking: bool = field(metadata=config(field_name="breaksTracking"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))


@dataclass_json
@dataclass
class RevokedProof:
    proof: RemoteProof = field(metadata=config(field_name="proof"))
    diff: TrackDiff = field(metadata=config(field_name="diff"))
    snoozed: bool = field(metadata=config(field_name="snoozed"))


@dataclass_json
@dataclass
class CheckResult:
    proof_result: ProofResult = field(metadata=config(field_name="proofResult"))
    time: Time = field(metadata=config(field_name="time"))
    freshness: CheckResultFreshness = field(metadata=config(field_name="freshness"))


@dataclass_json
@dataclass
class UserCard:
    following: int = field(metadata=config(field_name="following"))
    followers: int = field(metadata=config(field_name="followers"))
    uid: UID = field(metadata=config(field_name="uid"))
    full_name: str = field(metadata=config(field_name="fullName"))
    location: str = field(metadata=config(field_name="location"))
    bio: str = field(metadata=config(field_name="bio"))
    website: str = field(metadata=config(field_name="website"))
    twitter: str = field(metadata=config(field_name="twitter"))
    you_follow_them: bool = field(metadata=config(field_name="youFollowThem"))
    they_follow_you: bool = field(metadata=config(field_name="theyFollowYou"))
    team_showcase: List[UserTeamShowcase] = field(
        metadata=config(field_name="teamShowcase")
    )
    registered_for_airdrop: bool = field(
        metadata=config(field_name="registeredForAirdrop")
    )
    blocked: bool = field(metadata=config(field_name="blocked"))


@dataclass_json
@dataclass
class ServiceStatus:
    version: str = field(metadata=config(field_name="version"))
    label: str = field(metadata=config(field_name="label"))
    pid: str = field(metadata=config(field_name="pid"))
    last_exit_status: str = field(metadata=config(field_name="lastExitStatus"))
    bundle_version: str = field(metadata=config(field_name="bundleVersion"))
    install_status: InstallStatus = field(metadata=config(field_name="installStatus"))
    install_action: InstallAction = field(metadata=config(field_name="installAction"))
    status: Status = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class FuseStatus:
    version: str = field(metadata=config(field_name="version"))
    bundle_version: str = field(metadata=config(field_name="bundleVersion"))
    kext_id: str = field(metadata=config(field_name="kextID"))
    path: str = field(metadata=config(field_name="path"))
    kext_started: bool = field(metadata=config(field_name="kextStarted"))
    install_status: InstallStatus = field(metadata=config(field_name="installStatus"))
    install_action: InstallAction = field(metadata=config(field_name="installAction"))
    mount_infos: List[FuseMountInfo] = field(metadata=config(field_name="mountInfos"))
    status: Status = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class ComponentResult:
    name: str = field(metadata=config(field_name="name"))
    status: Status = field(metadata=config(field_name="status"))
    exit_code: int = field(metadata=config(field_name="exitCode"))


@dataclass_json
@dataclass
class FSFolderWriterEditHistory:
    writer_name: str = field(metadata=config(field_name="writerName"))
    edits: List[FSFolderWriterEdit] = field(metadata=config(field_name="edits"))
    deletes: List[FSFolderWriterEdit] = field(metadata=config(field_name="deletes"))


@dataclass_json
@dataclass
class FolderSyncStatus:
    local_disk_bytes_available: int = field(
        metadata=config(field_name="localDiskBytesAvailable")
    )
    local_disk_bytes_total: int = field(
        metadata=config(field_name="localDiskBytesTotal")
    )
    prefetch_status: PrefetchStatus = field(
        metadata=config(field_name="prefetchStatus")
    )
    prefetch_progress: PrefetchProgress = field(
        metadata=config(field_name="prefetchProgress")
    )
    stored_bytes_total: int = field(metadata=config(field_name="storedBytesTotal"))
    out_of_sync_space: bool = field(metadata=config(field_name="outOfSyncSpace"))


@dataclass_json
@dataclass
class MerkleRootAndTime:
    root: MerkleRootV2 = field(metadata=config(field_name="root"))
    update_time: Time = field(metadata=config(field_name="updateTime"))
    fetch_time: Time = field(metadata=config(field_name="fetchTime"))


@dataclass_json
@dataclass
class MetadataResponse:
    folder_id: str = field(metadata=config(field_name="folderID"))
    md_blocks: List[MDBlock] = field(metadata=config(field_name="mdBlocks"))


@dataclass_json
@dataclass
class BadgeState:
    new_tlfs: int = field(metadata=config(field_name="newTlfs"))
    rekeys_needed: int = field(metadata=config(field_name="rekeysNeeded"))
    new_followers: int = field(metadata=config(field_name="newFollowers"))
    inbox_vers: int = field(metadata=config(field_name="inboxVers"))
    home_todo_items: int = field(metadata=config(field_name="homeTodoItems"))
    unverified_emails: int = field(metadata=config(field_name="unverifiedEmails"))
    unverified_phones: int = field(metadata=config(field_name="unverifiedPhones"))
    new_devices: List[DeviceID] = field(metadata=config(field_name="newDevices"))
    revoked_devices: List[DeviceID] = field(
        metadata=config(field_name="revokedDevices")
    )
    conversations: List[BadgeConversationInfo] = field(
        metadata=config(field_name="conversations")
    )
    new_git_repo_global_unique_i_ds: List[str] = field(
        metadata=config(field_name="newGitRepoGlobalUniqueIDs")
    )
    new_team_names: List[str] = field(metadata=config(field_name="newTeamNames"))
    deleted_teams: List[DeletedTeamInfo] = field(
        metadata=config(field_name="deletedTeams")
    )
    new_team_access_requests: List[str] = field(
        metadata=config(field_name="newTeamAccessRequests")
    )
    teams_with_reset_users: List[TeamMemberOutReset] = field(
        metadata=config(field_name="teamsWithResetUsers")
    )
    unread_wallet_accounts: List[WalletAccountInfo] = field(
        metadata=config(field_name="unreadWalletAccounts")
    )
    reset_state: ResetState = field(metadata=config(field_name="resetState"))


@dataclass_json
@dataclass
class RuntimeStats:
    process_stats: List[ProcessRuntimeStats] = field(
        metadata=config(field_name="processStats")
    )
    db_stats: List[DbStats] = field(metadata=config(field_name="dbStats"))
    conv_loader_active: bool = field(metadata=config(field_name="convLoaderActive"))
    selective_sync_active: bool = field(
        metadata=config(field_name="selectiveSyncActive")
    )


@dataclass_json
@dataclass
class GUIEntryArg:
    window_title: str = field(metadata=config(field_name="windowTitle"))
    prompt: str = field(metadata=config(field_name="prompt"))
    username: str = field(metadata=config(field_name="username"))
    submit_label: str = field(metadata=config(field_name="submitLabel"))
    cancel_label: str = field(metadata=config(field_name="cancelLabel"))
    retry_label: str = field(metadata=config(field_name="retryLabel"))
    type: PassphraseType = field(metadata=config(field_name="type"))
    features: GUIEntryFeatures = field(metadata=config(field_name="features"))


@dataclass_json
@dataclass
class PGPSigVerification:
    is_signed: bool = field(metadata=config(field_name="isSigned"))
    verified: bool = field(metadata=config(field_name="verified"))
    signer: User = field(metadata=config(field_name="signer"))
    sign_key: PublicKey = field(metadata=config(field_name="signKey"))


@dataclass_json
@dataclass
class Process:
    pid: str = field(metadata=config(field_name="pid"))
    command: str = field(metadata=config(field_name="command"))
    file_descriptors: List[FileDescriptor] = field(
        metadata=config(field_name="fileDescriptors")
    )


@dataclass_json
@dataclass
class ExternalServiceConfig:
    schema_version: int = field(metadata=config(field_name="schema_version"))
    display: Optional[ServiceDisplayConfig] = field(
        metadata=config(field_name="display")
    )
    config: Optional[ParamProofServiceConfig] = field(
        metadata=config(field_name="config")
    )


@dataclass_json
@dataclass
class ProblemTLF:
    tlf: TLF = field(metadata=config(field_name="tlf"))
    score: int = field(metadata=config(field_name="score"))
    solution_kids: List[KID] = field(metadata=config(field_name="solution_kids"))


@dataclass_json
@dataclass
class RevokeWarning:
    endangered_tl_fs: List[TLF] = field(metadata=config(field_name="endangeredTLFs"))


@dataclass_json
@dataclass
class ResetLink:
    ctime: UnixTime = field(metadata=config(field_name="ctime"))
    merkle_root: ResetMerkleRoot = field(metadata=config(field_name="merkle_root"))
    prev: ResetPrev = field(metadata=config(field_name="prev"))
    reset_seqno: Seqno = field(metadata=config(field_name="reset_seqno"))
    type: ResetType = field(metadata=config(field_name="type"))
    uid: UID = field(metadata=config(field_name="uid"))


@dataclass_json
@dataclass
class ResetSummary:
    ctime: UnixTime = field(metadata=config(field_name="ctime"))
    merkle_root: ResetMerkleRoot = field(metadata=config(field_name="merkleRoot"))
    reset_seqno: Seqno = field(metadata=config(field_name="resetSeqno"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    type: ResetType = field(metadata=config(field_name="type"))


@dataclass_json
@dataclass
class SaltpackEncryptedMessageInfo:
    devices: List[Device] = field(metadata=config(field_name="devices"))
    num_anon_receivers: int = field(metadata=config(field_name="numAnonReceivers"))
    receiver_is_anon: bool = field(metadata=config(field_name="receiverIsAnon"))
    sender: SaltpackSender = field(metadata=config(field_name="sender"))


@dataclass_json
@dataclass
class KBFSArchivedPath:
    path: str = field(metadata=config(field_name="path"))
    archived_param: KBFSArchivedParam = field(
        metadata=config(field_name="archivedParam")
    )
    identify_behavior: Optional[TLFIdentifyBehavior] = field(
        metadata=config(field_name="identifyBehavior")
    )


@dataclass_json
@dataclass
class Dirent:
    time: Time = field(metadata=config(field_name="time"))
    size: int = field(metadata=config(field_name="size"))
    name: str = field(metadata=config(field_name="name"))
    dirent_type: DirentType = field(metadata=config(field_name="direntType"))
    last_writer_unverified: User = field(
        metadata=config(field_name="lastWriterUnverified")
    )
    writable: bool = field(metadata=config(field_name="writable"))
    prefetch_status: PrefetchStatus = field(
        metadata=config(field_name="prefetchStatus")
    )
    prefetch_progress: PrefetchProgress = field(
        metadata=config(field_name="prefetchProgress")
    )


@dataclass_json
@dataclass
class SimpleFSStats:
    process_stats: ProcessRuntimeStats = field(
        metadata=config(field_name="processStats")
    )
    block_cache_db_stats: List[str] = field(
        metadata=config(field_name="blockCacheDbStats")
    )
    sync_cache_db_stats: List[str] = field(
        metadata=config(field_name="syncCacheDbStats")
    )
    runtime_db_stats: List[DbStats] = field(
        metadata=config(field_name="runtimeDbStats")
    )


@dataclass_json
@dataclass
class TeambotKeyBoxed:
    box: str = field(metadata=config(field_name="box"))
    metadata: TeambotKeyMetadata = field(metadata=config(field_name="metadata"))


@dataclass_json
@dataclass
class TeambotKey:
    seed: Bytes32 = field(metadata=config(field_name="seed"))
    metadata: TeambotKeyMetadata = field(metadata=config(field_name="metadata"))


@dataclass_json
@dataclass
class PerTeamKeyAndCheck:
    ptk: PerTeamKey = field(metadata=config(field_name="ptk"))
    check: PerTeamSeedCheckPostImage = field(metadata=config(field_name="check"))


@dataclass_json
@dataclass
class PerTeamKeySeedItem:
    seed: PerTeamKeySeed = field(metadata=config(field_name="seed"))
    generation: PerTeamKeyGeneration = field(metadata=config(field_name="generation"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    check: Optional[PerTeamSeedCheck] = field(metadata=config(field_name="check"))


@dataclass_json
@dataclass
class TeamMembers:
    owners: List[UserVersion] = field(metadata=config(field_name="owners"))
    admins: List[UserVersion] = field(metadata=config(field_name="admins"))
    writers: List[UserVersion] = field(metadata=config(field_name="writers"))
    readers: List[UserVersion] = field(metadata=config(field_name="readers"))
    bots: List[UserVersion] = field(metadata=config(field_name="bots"))
    restricted_bots: List[UserVersion] = field(
        metadata=config(field_name="restrictedBots")
    )


@dataclass_json
@dataclass
class TeamMemberDetails:
    uv: UserVersion = field(metadata=config(field_name="uv"))
    username: str = field(metadata=config(field_name="username"))
    full_name: FullName = field(metadata=config(field_name="fullName"))
    needs_puk: bool = field(metadata=config(field_name="needsPUK"))
    status: TeamMemberStatus = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class TeamChangeReq:
    owners: List[UserVersion] = field(metadata=config(field_name="owners"))
    admins: List[UserVersion] = field(metadata=config(field_name="admins"))
    writers: List[UserVersion] = field(metadata=config(field_name="writers"))
    readers: List[UserVersion] = field(metadata=config(field_name="readers"))
    bots: List[UserVersion] = field(metadata=config(field_name="bots"))
    restricted_bots: Dict[str, TeamBotSettings] = field(
        metadata=config(field_name="restrictedBots")
    )
    none: List[UserVersion] = field(metadata=config(field_name="none"))
    completed_invites: Dict[str, UserVersionPercentForm] = field(
        metadata=config(field_name="completedInvites")
    )


@dataclass_json
@dataclass
class TeamPlusApplicationKeys:
    id: TeamID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))
    implicit: bool = field(metadata=config(field_name="implicit"))
    public: bool = field(metadata=config(field_name="public"))
    application: TeamApplication = field(metadata=config(field_name="application"))
    writers: List[UserVersion] = field(metadata=config(field_name="writers"))
    only_readers: List[UserVersion] = field(metadata=config(field_name="onlyReaders"))
    only_restricted_bots: List[UserVersion] = field(
        metadata=config(field_name="onlyRestrictedBots")
    )
    application_keys: List[TeamApplicationKey] = field(
        metadata=config(field_name="applicationKeys")
    )


@dataclass_json
@dataclass
class LinkTripleAndTime:
    triple: LinkTriple = field(metadata=config(field_name="triple"))
    time: Time = field(metadata=config(field_name="time"))


@dataclass_json
@dataclass
class FastTeamSigChainState:
    id: TeamID = field(metadata=config(field_name="ID"))
    public: bool = field(metadata=config(field_name="public"))
    root_ancestor: TeamName = field(metadata=config(field_name="rootAncestor"))
    name_depth: int = field(metadata=config(field_name="nameDepth"))
    last: Optional[LinkTriple] = field(metadata=config(field_name="last"))
    per_team_keys: Dict[str, PerTeamKey] = field(
        metadata=config(field_name="perTeamKeys")
    )
    per_team_key_seeds_verified: Dict[str, PerTeamKeySeed] = field(
        metadata=config(field_name="perTeamKeySeedsVerified")
    )
    down_pointers: Dict[str, DownPointer] = field(
        metadata=config(field_name="downPointers")
    )
    last_up_pointer: Optional[UpPointer] = field(
        metadata=config(field_name="lastUpPointer")
    )
    per_team_key_c_time: UnixTime = field(metadata=config(field_name="perTeamKeyCTime"))
    link_i_ds: Dict[str, LinkID] = field(metadata=config(field_name="linkIDs"))
    merkle_info: Dict[str, MerkleRootV2] = field(
        metadata=config(field_name="merkleInfo")
    )


@dataclass_json
@dataclass
class AuditHistory:
    id: TeamID = field(metadata=config(field_name="ID"))
    public: bool = field(metadata=config(field_name="public"))
    prior_merkle_seqno: Seqno = field(metadata=config(field_name="priorMerkleSeqno"))
    version: AuditVersion = field(metadata=config(field_name="version"))
    audits: List[Audit] = field(metadata=config(field_name="audits"))
    pre_probes: Dict[str, Probe] = field(metadata=config(field_name="preProbes"))
    post_probes: Dict[str, Probe] = field(metadata=config(field_name="postProbes"))
    tails: Dict[str, LinkID] = field(metadata=config(field_name="tails"))
    skip_until: Time = field(metadata=config(field_name="skipUntil"))


@dataclass_json
@dataclass
class TeamInvite:
    role: TeamRole = field(metadata=config(field_name="role"))
    id: TeamInviteID = field(metadata=config(field_name="id"))
    type: TeamInviteType = field(metadata=config(field_name="type"))
    name: TeamInviteName = field(metadata=config(field_name="name"))
    inviter: UserVersion = field(metadata=config(field_name="inviter"))


@dataclass_json
@dataclass
class AnnotatedTeamInvite:
    role: TeamRole = field(metadata=config(field_name="role"))
    id: TeamInviteID = field(metadata=config(field_name="id"))
    type: TeamInviteType = field(metadata=config(field_name="type"))
    name: TeamInviteName = field(metadata=config(field_name="name"))
    uv: UserVersion = field(metadata=config(field_name="uv"))
    inviter: UserVersion = field(metadata=config(field_name="inviter"))
    inviter_username: str = field(metadata=config(field_name="inviterUsername"))
    team_name: str = field(metadata=config(field_name="teamName"))
    status: TeamMemberStatus = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class SubteamLogPoint:
    name: TeamName = field(metadata=config(field_name="name"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))


@dataclass_json
@dataclass
class TeamCLKRMsg:
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    generation: PerTeamKeyGeneration = field(metadata=config(field_name="generation"))
    score: int = field(metadata=config(field_name="score"))
    reset_users_untrusted: List[TeamCLKRResetUser] = field(
        metadata=config(field_name="reset_users")
    )


@dataclass_json
@dataclass
class TeamMemberOutFromReset:
    team_name: str = field(metadata=config(field_name="team_name"))
    reset_user: TeamResetUser = field(metadata=config(field_name="reset_user"))


@dataclass_json
@dataclass
class TeamSBSMsg:
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    score: int = field(metadata=config(field_name="score"))
    invitees: List[TeamInvitee] = field(metadata=config(field_name="invitees"))


@dataclass_json
@dataclass
class TeamOpenReqMsg:
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    tars: List[TeamAccessRequest] = field(metadata=config(field_name="tars"))


@dataclass_json
@dataclass
class SeitanKeyAndLabelVersion1:
    i: SeitanIKey = field(metadata=config(field_name="i"))
    l: SeitanKeyLabel = field(metadata=config(field_name="l"))


@dataclass_json
@dataclass
class SeitanKeyAndLabelVersion2:
    k: SeitanPubKey = field(metadata=config(field_name="k"))
    l: SeitanKeyLabel = field(metadata=config(field_name="l"))


@dataclass_json
@dataclass
class TeamSeitanMsg:
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    seitans: List[TeamSeitanRequest] = field(metadata=config(field_name="seitans"))


@dataclass_json
@dataclass
class TeamOpenSweepMsg:
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    reset_users_untrusted: List[TeamCLKRResetUser] = field(
        metadata=config(field_name="reset_users")
    )


@dataclass_json
@dataclass
class TeamRefreshers:
    need_key_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="needKeyGeneration")
    )
    need_applications_at_generations: Dict[str, List[TeamApplication]] = field(
        metadata=config(field_name="needApplicationsAtGenerations")
    )
    need_applications_at_generations_with_kbfs: Dict[
        str, List[TeamApplication]
    ] = field(metadata=config(field_name="needApplicationsAtGenerationsWithKBFS"))
    want_members: List[UserVersion] = field(metadata=config(field_name="wantMembers"))
    want_members_role: TeamRole = field(metadata=config(field_name="wantMembersRole"))
    need_kbfs_key_generation: TeamKBFSKeyRefresher = field(
        metadata=config(field_name="needKBFSKeyGeneration")
    )


@dataclass_json
@dataclass
class FastTeamLoadArg:
    id: TeamID = field(metadata=config(field_name="ID"))
    public: bool = field(metadata=config(field_name="public"))
    assert_team_name: Optional[TeamName] = field(
        metadata=config(field_name="assertTeamName")
    )
    applications: List[TeamApplication] = field(
        metadata=config(field_name="applications")
    )
    key_generations_needed: List[PerTeamKeyGeneration] = field(
        metadata=config(field_name="keyGenerationsNeeded")
    )
    need_latest_key: bool = field(metadata=config(field_name="needLatestKey"))
    force_refresh: bool = field(metadata=config(field_name="forceRefresh"))


@dataclass_json
@dataclass
class FastTeamLoadRes:
    name: TeamName = field(metadata=config(field_name="name"))
    application_keys: List[TeamApplicationKey] = field(
        metadata=config(field_name="applicationKeys")
    )


@dataclass_json
@dataclass
class MemberInfo:
    user_id: UID = field(metadata=config(field_name="uid"))
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    fq_name: str = field(metadata=config(field_name="fq_name"))
    is_implicit_team: bool = field(metadata=config(field_name="is_implicit_team"))
    is_open_team: bool = field(metadata=config(field_name="is_open_team"))
    role: TeamRole = field(metadata=config(field_name="role"))
    implicit: Optional[ImplicitRole] = field(metadata=config(field_name="implicit"))
    member_count: int = field(metadata=config(field_name="member_count"))
    allow_profile_promote: bool = field(
        metadata=config(field_name="allow_profile_promote")
    )
    is_member_showcased: bool = field(metadata=config(field_name="is_member_showcased"))


@dataclass_json
@dataclass
class AnnotatedMemberInfo:
    user_id: UID = field(metadata=config(field_name="uid"))
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    username: str = field(metadata=config(field_name="username"))
    full_name: str = field(metadata=config(field_name="full_name"))
    fq_name: str = field(metadata=config(field_name="fq_name"))
    is_implicit_team: bool = field(metadata=config(field_name="is_implicit_team"))
    imp_team_display_name: str = field(
        metadata=config(field_name="implicit_team_display_name")
    )
    is_open_team: bool = field(metadata=config(field_name="is_open_team"))
    role: TeamRole = field(metadata=config(field_name="role"))
    implicit: Optional[ImplicitRole] = field(metadata=config(field_name="implicit"))
    needs_puk: bool = field(metadata=config(field_name="needsPUK"))
    member_count: int = field(metadata=config(field_name="member_count"))
    eldest_seqno: Seqno = field(metadata=config(field_name="member_eldest_seqno"))
    allow_profile_promote: bool = field(
        metadata=config(field_name="allow_profile_promote")
    )
    is_member_showcased: bool = field(metadata=config(field_name="is_member_showcased"))
    status: TeamMemberStatus = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class TeamAddMemberResult:
    invited: bool = field(metadata=config(field_name="invited"))
    user: Optional[User] = field(metadata=config(field_name="user"))
    email_sent: bool = field(metadata=config(field_name="emailSent"))
    chat_sending: bool = field(metadata=config(field_name="chatSending"))


@dataclass_json
@dataclass
class TeamTreeEntry:
    name: TeamName = field(metadata=config(field_name="name"))
    admin: bool = field(metadata=config(field_name="admin"))


@dataclass_json
@dataclass
class SubteamListEntry:
    name: TeamName = field(metadata=config(field_name="name"))
    member_count: int = field(metadata=config(field_name="memberCount"))


@dataclass_json
@dataclass
class TeamAndMemberShowcase:
    team_showcase: TeamShowcase = field(metadata=config(field_name="teamShowcase"))
    is_member_showcased: bool = field(metadata=config(field_name="isMemberShowcased"))


@dataclass_json
@dataclass
class ImplicitTeamUserSet:
    keybase_users: List[str] = field(metadata=config(field_name="keybaseUsers"))
    unresolved_users: List[SocialAssertion] = field(
        metadata=config(field_name="unresolvedUsers")
    )


@dataclass_json
@dataclass
class TeamProfileAddEntry:
    team_name: TeamName = field(metadata=config(field_name="teamName"))
    open: bool = field(metadata=config(field_name="open"))
    disabled_reason: str = field(metadata=config(field_name="disabledReason"))


@dataclass_json
@dataclass
class MerkleTreeLocation:
    leaf: UserOrTeamID = field(metadata=config(field_name="leaf"))
    loc: SigChainLocation = field(metadata=config(field_name="loc"))


@dataclass_json
@dataclass
class SignatureMetadata:
    signing_kid: KID = field(metadata=config(field_name="signingKID"))
    prev_merkle_root_signed: MerkleRootV2 = field(
        metadata=config(field_name="prevMerkleRootSigned")
    )
    first_appeared_unverified: Seqno = field(
        metadata=config(field_name="firstAppearedUnverified")
    )
    time: Time = field(metadata=config(field_name="time"))
    sig_chain_location: SigChainLocation = field(
        metadata=config(field_name="sigChainLocation")
    )


@dataclass_json
@dataclass
class Proofs:
    social: List[TrackProof] = field(metadata=config(field_name="social"))
    web: List[WebProof] = field(metadata=config(field_name="web"))
    public_keys: List[PublicKey] = field(metadata=config(field_name="publicKeys"))


@dataclass_json
@dataclass
class UserSettings:
    emails: List[Email] = field(metadata=config(field_name="emails"))
    phone_numbers: List[UserPhoneNumber] = field(
        metadata=config(field_name="phoneNumbers")
    )


@dataclass_json
@dataclass
class UserSummary2Set:
    users: List[UserSummary2] = field(metadata=config(field_name="users"))
    time: Time = field(metadata=config(field_name="time"))
    version: int = field(metadata=config(field_name="version"))


@dataclass_json
@dataclass
class ProofSuggestion:
    key: str = field(metadata=config(field_name="key"))
    below_fold: bool = field(metadata=config(field_name="belowFold"))
    profile_text: str = field(metadata=config(field_name="profileText"))
    profile_icon: List[SizedImage] = field(metadata=config(field_name="profileIcon"))
    picker_text: str = field(metadata=config(field_name="pickerText"))
    picker_subtext: str = field(metadata=config(field_name="pickerSubtext"))
    picker_icon: List[SizedImage] = field(metadata=config(field_name="pickerIcon"))
    metas: List[Identify3RowMeta] = field(metadata=config(field_name="metas"))


@dataclass_json
@dataclass
class NextMerkleRootRes:
    res: Optional[MerkleRootV2] = field(metadata=config(field_name="res"))


@dataclass_json
@dataclass
class BlockReferenceCount:
    ref: BlockReference = field(metadata=config(field_name="ref"))
    live_count: int = field(metadata=config(field_name="liveCount"))


@dataclass_json
@dataclass
class ReferenceCountRes:
    counts: List[BlockIdCount] = field(metadata=config(field_name="counts"))


@dataclass_json
@dataclass
class UserPlusKeys:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    status: StatusCode = field(metadata=config(field_name="status"))
    device_keys: List[PublicKey] = field(metadata=config(field_name="deviceKeys"))
    revoked_device_keys: List[RevokedKey] = field(
        metadata=config(field_name="revokedDeviceKeys")
    )
    pgp_key_count: int = field(metadata=config(field_name="pgpKeyCount"))
    uvv: UserVersionVector = field(metadata=config(field_name="uvv"))
    deleted_device_keys: List[PublicKey] = field(
        metadata=config(field_name="deletedDeviceKeys")
    )
    per_user_keys: List[PerUserKey] = field(metadata=config(field_name="perUserKeys"))
    resets: List[ResetSummary] = field(metadata=config(field_name="resets"))


@dataclass_json
@dataclass
class ExtendedStatus:
    standalone: bool = field(metadata=config(field_name="standalone"))
    passphrase_stream_cached: bool = field(
        metadata=config(field_name="passphraseStreamCached")
    )
    tsec_cached: bool = field(metadata=config(field_name="tsecCached"))
    device_sig_key_cached: bool = field(
        metadata=config(field_name="deviceSigKeyCached")
    )
    device_enc_key_cached: bool = field(
        metadata=config(field_name="deviceEncKeyCached")
    )
    paper_sig_key_cached: bool = field(metadata=config(field_name="paperSigKeyCached"))
    paper_enc_key_cached: bool = field(metadata=config(field_name="paperEncKeyCached"))
    stored_secret: bool = field(metadata=config(field_name="storedSecret"))
    secret_prompt_skip: bool = field(metadata=config(field_name="secretPromptSkip"))
    remember_passphrase: bool = field(metadata=config(field_name="rememberPassphrase"))
    device: Optional[Device] = field(metadata=config(field_name="device"))
    device_err: Optional[LoadDeviceErr] = field(metadata=config(field_name="deviceErr"))
    log_dir: str = field(metadata=config(field_name="logDir"))
    session: Optional[SessionStatus] = field(metadata=config(field_name="session"))
    default_username: str = field(metadata=config(field_name="defaultUsername"))
    provisioned_usernames: List[str] = field(
        metadata=config(field_name="provisionedUsernames")
    )
    configured_accounts: List[ConfiguredAccount] = field(
        metadata=config(field_name="configuredAccounts")
    )
    clients: List[ClientStatus] = field(metadata=config(field_name="Clients"))
    device_ek_names: List[str] = field(metadata=config(field_name="deviceEkNames"))
    platform_info: PlatformInfo = field(metadata=config(field_name="platformInfo"))
    default_device_id: DeviceID = field(metadata=config(field_name="defaultDeviceID"))
    local_db_stats: List[str] = field(metadata=config(field_name="localDbStats"))
    local_chat_db_stats: List[str] = field(
        metadata=config(field_name="localChatDbStats")
    )
    local_block_cache_db_stats: List[str] = field(
        metadata=config(field_name="localBlockCacheDbStats")
    )
    local_sync_cache_db_stats: List[str] = field(
        metadata=config(field_name="localSyncCacheDbStats")
    )
    cache_dir_size_info: List[DirSizeInfo] = field(
        metadata=config(field_name="cacheDirSizeInfo")
    )
    ui_router_mapping: Dict[str, int] = field(
        metadata=config(field_name="uiRouterMapping")
    )


@dataclass
class TeamEphemeralKey__TEAM:
    keyType: Literal[TeamEphemeralKeyType.TEAM]
    TEAM: Optional[TeamEk]


@dataclass
class TeamEphemeralKey__TEAMBOT:
    keyType: Literal[TeamEphemeralKeyType.TEAMBOT]
    TEAMBOT: Optional[TeambotEk]


TeamEphemeralKey = Union[TeamEphemeralKey__TEAM, TeamEphemeralKey__TEAMBOT]


@dataclass
class TeamEphemeralKeyBoxed__TEAM:
    keyType: Literal[TeamEphemeralKeyType.TEAM]
    TEAM: Optional[TeamEkBoxed]


@dataclass
class TeamEphemeralKeyBoxed__TEAMBOT:
    keyType: Literal[TeamEphemeralKeyType.TEAMBOT]
    TEAMBOT: Optional[TeambotEkBoxed]


TeamEphemeralKeyBoxed = Union[
    TeamEphemeralKeyBoxed__TEAM, TeamEphemeralKeyBoxed__TEAMBOT
]


@dataclass_json
@dataclass
class GitLocalMetadata:
    repo_name: GitRepoName = field(metadata=config(field_name="repoName"))
    refs: List[GitRefMetadata] = field(metadata=config(field_name="refs"))
    push_type: GitPushType = field(metadata=config(field_name="pushType"))
    previous_repo_name: GitRepoName = field(
        metadata=config(field_name="previousRepoName")
    )


@dataclass
class HomeScreenItemDataExt__TODO:
    t: Literal[HomeScreenItemType.TODO]
    TODO: Optional[HomeScreenTodoExt]


HomeScreenItemDataExt = Union[HomeScreenItemDataExt__TODO]


@dataclass_json
@dataclass
class Identity:
    status: Optional[Status] = field(metadata=config(field_name="status"))
    when_last_tracked: Time = field(metadata=config(field_name="whenLastTracked"))
    proofs: List[IdentifyRow] = field(metadata=config(field_name="proofs"))
    cryptocurrency: List[Cryptocurrency] = field(
        metadata=config(field_name="cryptocurrency")
    )
    revoked: List[TrackDiff] = field(metadata=config(field_name="revoked"))
    revoked_details: List[RevokedProof] = field(
        metadata=config(field_name="revokedDetails")
    )
    breaks_tracking: bool = field(metadata=config(field_name="breaksTracking"))


@dataclass_json
@dataclass
class LinkCheckResult:
    proof_id: int = field(metadata=config(field_name="proofId"))
    proof_result: ProofResult = field(metadata=config(field_name="proofResult"))
    snoozed_result: ProofResult = field(metadata=config(field_name="snoozedResult"))
    tor_warning: bool = field(metadata=config(field_name="torWarning"))
    tmp_track_expire_time: Time = field(
        metadata=config(field_name="tmpTrackExpireTime")
    )
    cached: Optional[CheckResult] = field(metadata=config(field_name="cached"))
    diff: Optional[TrackDiff] = field(metadata=config(field_name="diff"))
    remote_diff: Optional[TrackDiff] = field(metadata=config(field_name="remoteDiff"))
    hint: Optional[SigHint] = field(metadata=config(field_name="hint"))
    breaks_tracking: bool = field(metadata=config(field_name="breaksTracking"))


@dataclass_json
@dataclass
class ServicesStatus:
    service: List[ServiceStatus] = field(metadata=config(field_name="service"))
    kbfs: List[ServiceStatus] = field(metadata=config(field_name="kbfs"))
    updater: List[ServiceStatus] = field(metadata=config(field_name="updater"))


@dataclass_json
@dataclass
class InstallResult:
    component_results: List[ComponentResult] = field(
        metadata=config(field_name="componentResults")
    )
    status: Status = field(metadata=config(field_name="status"))
    fatal: bool = field(metadata=config(field_name="fatal"))


@dataclass_json
@dataclass
class UninstallResult:
    component_results: List[ComponentResult] = field(
        metadata=config(field_name="componentResults")
    )
    status: Status = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class ProblemSet:
    user: User = field(metadata=config(field_name="user"))
    kid: KID = field(metadata=config(field_name="kid"))
    tlfs: List[ProblemTLF] = field(metadata=config(field_name="tlfs"))


@dataclass
class Path__LOCAL:
    PathType: Literal[PathType.LOCAL]
    LOCAL: Optional[str]


@dataclass
class Path__KBFS:
    PathType: Literal[PathType.KBFS]
    KBFS: Optional[KBFSPath]


@dataclass
class Path__KBFS_ARCHIVED:
    PathType: Literal[PathType.KBFS_ARCHIVED]
    KBFS_ARCHIVED: Optional[KBFSArchivedPath]


Path = Union[Path__LOCAL, Path__KBFS, Path__KBFS_ARCHIVED]


@dataclass_json
@dataclass
class DirentWithRevision:
    entry: Dirent = field(metadata=config(field_name="entry"))
    revision: KBFSRevision = field(metadata=config(field_name="revision"))


@dataclass_json
@dataclass
class SimpleFSListResult:
    entries: List[Dirent] = field(metadata=config(field_name="entries"))
    progress: Progress = field(metadata=config(field_name="progress"))


@dataclass_json
@dataclass
class FolderSyncConfigAndStatus:
    config: FolderSyncConfig = field(metadata=config(field_name="config"))
    status: FolderSyncStatus = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class TeamMembersDetails:
    owners: List[TeamMemberDetails] = field(metadata=config(field_name="owners"))
    admins: List[TeamMemberDetails] = field(metadata=config(field_name="admins"))
    writers: List[TeamMemberDetails] = field(metadata=config(field_name="writers"))
    readers: List[TeamMemberDetails] = field(metadata=config(field_name="readers"))
    bots: List[TeamMemberDetails] = field(metadata=config(field_name="bots"))
    restricted_bots: List[TeamMemberDetails] = field(
        metadata=config(field_name="restrictedBots")
    )


@dataclass_json
@dataclass
class FastTeamData:
    frozen: bool = field(metadata=config(field_name="frozen"))
    subversion: int = field(metadata=config(field_name="subversion"))
    tombstoned: bool = field(metadata=config(field_name="tombstoned"))
    name: TeamName = field(metadata=config(field_name="name"))
    chain: FastTeamSigChainState = field(metadata=config(field_name="chain"))
    per_team_key_seeds_unverified: Dict[str, PerTeamKeySeed] = field(
        metadata=config(field_name="perTeamKeySeedsUnverified")
    )
    max_continuous_ptk_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="maxContinuousPTKGeneration")
    )
    seed_checks: Dict[str, PerTeamSeedCheck] = field(
        metadata=config(field_name="seedChecks")
    )
    latest_key_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="latestKeyGeneration")
    )
    reader_key_masks: Dict[str, Dict[str, MaskB64]] = field(
        metadata=config(field_name="readerKeyMasks")
    )
    latest_seqno_hint: Seqno = field(metadata=config(field_name="latestSeqnoHint"))
    cached_at: Time = field(metadata=config(field_name="cachedAt"))
    loaded_latest: bool = field(metadata=config(field_name="loadedLatest"))


@dataclass_json
@dataclass
class HiddenTeamChainRatchetSet:
    ratchets: Dict[str, LinkTripleAndTime] = field(
        metadata=config(field_name="ratchets")
    )


@dataclass_json
@dataclass
class HiddenTeamChainLink:
    merkle_root: MerkleRootV2 = field(metadata=config(field_name="m"))
    parent_chain: LinkTriple = field(metadata=config(field_name="p"))
    signer: Signer = field(metadata=config(field_name="s"))
    ptk: Dict[str, PerTeamKeyAndCheck] = field(metadata=config(field_name="k"))


@dataclass_json
@dataclass
class UserLogPoint:
    role: TeamRole = field(metadata=config(field_name="role"))
    sig_meta: SignatureMetadata = field(metadata=config(field_name="sigMeta"))


@dataclass
class SeitanKeyAndLabel__V1:
    v: Literal[SeitanKeyAndLabelVersion.V1]
    V1: Optional[SeitanKeyAndLabelVersion1]


@dataclass
class SeitanKeyAndLabel__V2:
    v: Literal[SeitanKeyAndLabelVersion.V2]
    V2: Optional[SeitanKeyAndLabelVersion2]


SeitanKeyAndLabel = Union[SeitanKeyAndLabel__V1, SeitanKeyAndLabel__V2]


@dataclass_json
@dataclass
class LoadTeamArg:
    id: TeamID = field(metadata=config(field_name="ID"))
    name: str = field(metadata=config(field_name="name"))
    public: bool = field(metadata=config(field_name="public"))
    need_admin: bool = field(metadata=config(field_name="needAdmin"))
    refresh_uid_mapper: bool = field(metadata=config(field_name="refreshUIDMapper"))
    refreshers: TeamRefreshers = field(metadata=config(field_name="refreshers"))
    force_full_reload: bool = field(metadata=config(field_name="forceFullReload"))
    force_repoll: bool = field(metadata=config(field_name="forceRepoll"))
    stale_ok: bool = field(metadata=config(field_name="staleOK"))
    allow_name_lookup_burst_cache: bool = field(
        metadata=config(field_name="allowNameLookupBurstCache")
    )
    skip_audit: bool = field(metadata=config(field_name="skipAudit"))
    skip_need_hidden_rotate_check: bool = field(
        metadata=config(field_name="skipNeedHiddenRotateCheck")
    )


@dataclass_json
@dataclass
class TeamList:
    teams: List[MemberInfo] = field(metadata=config(field_name="teams"))


@dataclass_json
@dataclass
class AnnotatedTeamList:
    teams: List[AnnotatedMemberInfo] = field(metadata=config(field_name="teams"))
    annotated_active_invites: Dict[str, AnnotatedTeamInvite] = field(
        metadata=config(field_name="annotatedActiveInvites")
    )


@dataclass_json
@dataclass
class TeamTreeResult:
    entries: List[TeamTreeEntry] = field(metadata=config(field_name="entries"))


@dataclass_json
@dataclass
class SubteamListResult:
    entries: List[SubteamListEntry] = field(metadata=config(field_name="entries"))


@dataclass_json
@dataclass
class ImplicitTeamDisplayName:
    is_public: bool = field(metadata=config(field_name="isPublic"))
    writers: ImplicitTeamUserSet = field(metadata=config(field_name="writers"))
    readers: ImplicitTeamUserSet = field(metadata=config(field_name="readers"))
    conflict_info: Optional[ImplicitTeamConflictInfo] = field(
        metadata=config(field_name="conflictInfo")
    )


@dataclass_json
@dataclass
class PublicKeyV2Base:
    kid: KID = field(metadata=config(field_name="kid"))
    is_sibkey: bool = field(metadata=config(field_name="isSibkey"))
    is_eldest: bool = field(metadata=config(field_name="isEldest"))
    c_time: Time = field(metadata=config(field_name="cTime"))
    e_time: Time = field(metadata=config(field_name="eTime"))
    provisioning: SignatureMetadata = field(metadata=config(field_name="provisioning"))
    revocation: Optional[SignatureMetadata] = field(
        metadata=config(field_name="revocation")
    )


@dataclass_json
@dataclass
class UserSummary:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    thumbnail: str = field(metadata=config(field_name="thumbnail"))
    id_version: int = field(metadata=config(field_name="idVersion"))
    full_name: str = field(metadata=config(field_name="fullName"))
    bio: str = field(metadata=config(field_name="bio"))
    proofs: Proofs = field(metadata=config(field_name="proofs"))
    sig_id_display: str = field(metadata=config(field_name="sigIDDisplay"))
    track_time: Time = field(metadata=config(field_name="trackTime"))


@dataclass_json
@dataclass
class ProofSuggestionsRes:
    suggestions: List[ProofSuggestion] = field(
        metadata=config(field_name="suggestions")
    )
    show_more: bool = field(metadata=config(field_name="showMore"))


@dataclass_json
@dataclass
class APIUserSearchResult:
    score: float = field(metadata=config(field_name="score"))
    keybase: Optional[APIUserKeybaseResult] = field(
        metadata=config(field_name="keybase")
    )
    service: Optional[APIUserServiceResult] = field(
        metadata=config(field_name="service")
    )
    contact: Optional[ProcessedContact] = field(metadata=config(field_name="contact"))
    imptofu: Optional[ImpTofuSearchResult] = field(
        metadata=config(field_name="imptofu")
    )
    services_summary: Dict[str, APIUserServiceSummary] = field(
        metadata=config(field_name="services_summary")
    )
    raw_score: float = field(metadata=config(field_name="rawScore"))


@dataclass_json
@dataclass
class NonUserDetails:
    is_non_user: bool = field(metadata=config(field_name="isNonUser"))
    assertion_value: str = field(metadata=config(field_name="assertionValue"))
    assertion_key: str = field(metadata=config(field_name="assertionKey"))
    description: str = field(metadata=config(field_name="description"))
    contact: Optional[ProcessedContact] = field(metadata=config(field_name="contact"))
    service: Optional[APIUserServiceResult] = field(
        metadata=config(field_name="service")
    )
    site_icon: List[SizedImage] = field(metadata=config(field_name="siteIcon"))
    site_icon_full: List[SizedImage] = field(metadata=config(field_name="siteIconFull"))


@dataclass_json
@dataclass
class DowngradeReferenceRes:
    completed: List[BlockReferenceCount] = field(
        metadata=config(field_name="completed")
    )
    failed: BlockReference = field(metadata=config(field_name="failed"))


@dataclass_json
@dataclass
class UserPlusAllKeys:
    base: UserPlusKeys = field(metadata=config(field_name="base"))
    pgp_keys: List[PublicKey] = field(metadata=config(field_name="pgpKeys"))
    remote_tracks: List[RemoteTrack] = field(metadata=config(field_name="remoteTracks"))


@dataclass_json
@dataclass
class FullStatus:
    username: str = field(metadata=config(field_name="username"))
    config_path: str = field(metadata=config(field_name="configPath"))
    cur_status: CurrentStatus = field(metadata=config(field_name="curStatus"))
    ext_status: ExtendedStatus = field(metadata=config(field_name="extStatus"))
    client: KbClientStatus = field(metadata=config(field_name="client"))
    service: KbServiceStatus = field(metadata=config(field_name="service"))
    kbfs: KBFSStatus = field(metadata=config(field_name="kbfs"))
    desktop: DesktopStatus = field(metadata=config(field_name="desktop"))
    updater: UpdaterStatus = field(metadata=config(field_name="updater"))
    start: StartStatus = field(metadata=config(field_name="start"))
    git: GitStatus = field(metadata=config(field_name="git"))


@dataclass_json
@dataclass
class FolderNormalView:
    resolving_conflict: bool = field(metadata=config(field_name="resolvingConflict"))
    stuck_in_conflict: bool = field(metadata=config(field_name="stuckInConflict"))
    local_views: List[Path] = field(metadata=config(field_name="localViews"))


@dataclass_json
@dataclass
class FolderConflictManualResolvingLocalView:
    normal_view: Path = field(metadata=config(field_name="normalView"))


@dataclass_json
@dataclass
class GitRepoInfo:
    folder: FolderHandle = field(metadata=config(field_name="folder"))
    repo_id: RepoID = field(metadata=config(field_name="repoID"))
    local_metadata: GitLocalMetadata = field(
        metadata=config(field_name="localMetadata")
    )
    server_metadata: GitServerMetadata = field(
        metadata=config(field_name="serverMetadata")
    )
    repo_url: str = field(metadata=config(field_name="repoUrl"))
    global_unique_id: str = field(metadata=config(field_name="globalUniqueID"))
    can_delete: bool = field(metadata=config(field_name="canDelete"))
    team_repo_settings: Optional[GitTeamRepoSettings] = field(
        metadata=config(field_name="teamRepoSettings")
    )


@dataclass_json
@dataclass
class HomeScreenPeopleNotificationFollowed:
    follow_time: Time = field(metadata=config(field_name="followTime"))
    followed_back: bool = field(metadata=config(field_name="followedBack"))
    user: UserSummary = field(metadata=config(field_name="user"))


@dataclass_json
@dataclass
class IdentifyProofBreak:
    remote_proof: RemoteProof = field(metadata=config(field_name="remoteProof"))
    lcr: LinkCheckResult = field(metadata=config(field_name="lcr"))


@dataclass_json
@dataclass
class ProblemSetDevices:
    problem_set: ProblemSet = field(metadata=config(field_name="problemSet"))
    devices: List[Device] = field(metadata=config(field_name="devices"))


@dataclass_json
@dataclass
class ListArgs:
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    filter: ListFilter = field(metadata=config(field_name="filter"))


@dataclass_json
@dataclass
class ListToDepthArgs:
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    filter: ListFilter = field(metadata=config(field_name="filter"))
    depth: int = field(metadata=config(field_name="depth"))


@dataclass_json
@dataclass
class RemoveArgs:
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    recursive: bool = field(metadata=config(field_name="recursive"))


@dataclass_json
@dataclass
class ReadArgs:
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    offset: int = field(metadata=config(field_name="offset"))
    size: int = field(metadata=config(field_name="size"))


@dataclass_json
@dataclass
class WriteArgs:
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    offset: int = field(metadata=config(field_name="offset"))


@dataclass_json
@dataclass
class CopyArgs:
    op_id: OpID = field(metadata=config(field_name="opID"))
    src: Path = field(metadata=config(field_name="src"))
    dest: Path = field(metadata=config(field_name="dest"))


@dataclass_json
@dataclass
class MoveArgs:
    op_id: OpID = field(metadata=config(field_name="opID"))
    src: Path = field(metadata=config(field_name="src"))
    dest: Path = field(metadata=config(field_name="dest"))


@dataclass_json
@dataclass
class GetRevisionsArgs:
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    span_type: RevisionSpanType = field(metadata=config(field_name="spanType"))


@dataclass_json
@dataclass
class GetRevisionsResult:
    revisions: List[DirentWithRevision] = field(metadata=config(field_name="revisions"))
    progress: Progress = field(metadata=config(field_name="progress"))


@dataclass_json
@dataclass
class TeamDetails:
    members: TeamMembersDetails = field(metadata=config(field_name="members"))
    key_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="keyGeneration")
    )
    annotated_active_invites: Dict[str, AnnotatedTeamInvite] = field(
        metadata=config(field_name="annotatedActiveInvites")
    )
    settings: TeamSettings = field(metadata=config(field_name="settings"))
    showcase: TeamShowcase = field(metadata=config(field_name="showcase"))


@dataclass_json
@dataclass
class HiddenTeamChain:
    id: TeamID = field(metadata=config(field_name="id"))
    subversion: int = field(metadata=config(field_name="subversion"))
    public: bool = field(metadata=config(field_name="public"))
    frozen: bool = field(metadata=config(field_name="frozen"))
    tombstoned: bool = field(metadata=config(field_name="tombstoned"))
    last: Seqno = field(metadata=config(field_name="last"))
    latest_seqno_hint: Seqno = field(metadata=config(field_name="latestSeqnoHint"))
    last_per_team_keys: Dict[str, Seqno] = field(
        metadata=config(field_name="lastPerTeamKeys")
    )
    outer: Dict[str, LinkID] = field(metadata=config(field_name="outer"))
    inner: Dict[str, HiddenTeamChainLink] = field(metadata=config(field_name="inner"))
    reader_per_team_keys: Dict[str, Seqno] = field(
        metadata=config(field_name="readerPerTeamKeys")
    )
    ratchet_set: HiddenTeamChainRatchetSet = field(
        metadata=config(field_name="ratchetSet")
    )
    cached_at: Time = field(metadata=config(field_name="cachedAt"))
    need_rotate: bool = field(metadata=config(field_name="needRotate"))
    merkle_roots: Dict[str, MerkleRootV2] = field(
        metadata=config(field_name="merkleRoots")
    )


@dataclass_json
@dataclass
class TeamSigChainState:
    reader: UserVersion = field(metadata=config(field_name="reader"))
    id: TeamID = field(metadata=config(field_name="id"))
    implicit: bool = field(metadata=config(field_name="implicit"))
    public: bool = field(metadata=config(field_name="public"))
    root_ancestor: TeamName = field(metadata=config(field_name="rootAncestor"))
    name_depth: int = field(metadata=config(field_name="nameDepth"))
    name_log: List[TeamNameLogPoint] = field(metadata=config(field_name="nameLog"))
    last_seqno: Seqno = field(metadata=config(field_name="lastSeqno"))
    last_link_id: LinkID = field(metadata=config(field_name="lastLinkID"))
    last_high_seqno: Seqno = field(metadata=config(field_name="lastHighSeqno"))
    last_high_link_id: LinkID = field(metadata=config(field_name="lastHighLinkID"))
    parent_id: Optional[TeamID] = field(metadata=config(field_name="parentID"))
    user_log: Dict[str, List[UserLogPoint]] = field(
        metadata=config(field_name="userLog")
    )
    subteam_log: Dict[str, List[SubteamLogPoint]] = field(
        metadata=config(field_name="subteamLog")
    )
    per_team_keys: Dict[str, PerTeamKey] = field(
        metadata=config(field_name="perTeamKeys")
    )
    max_per_team_key_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="maxPerTeamKeyGeneration")
    )
    per_team_key_c_time: UnixTime = field(metadata=config(field_name="perTeamKeyCTime"))
    link_i_ds: Dict[str, LinkID] = field(metadata=config(field_name="linkIDs"))
    stubbed_links: Dict[str, bool] = field(metadata=config(field_name="stubbedLinks"))
    active_invites: Dict[str, TeamInvite] = field(
        metadata=config(field_name="activeInvites")
    )
    obsolete_invites: Dict[str, TeamInvite] = field(
        metadata=config(field_name="obsoleteInvites")
    )
    open: bool = field(metadata=config(field_name="open"))
    open_team_join_as: TeamRole = field(metadata=config(field_name="openTeamJoinAs"))
    bots: Dict[str, TeamBotSettings] = field(metadata=config(field_name="bots"))
    tlf_i_ds: List[TLFID] = field(metadata=config(field_name="tlfIDs"))
    tlf_legacy_upgrade: Dict[str, TeamLegacyTLFUpgradeChainInfo] = field(
        metadata=config(field_name="tlfLegacyUpgrade")
    )
    head_merkle: Optional[MerkleRootV2] = field(
        metadata=config(field_name="headMerkle")
    )
    merkle_roots: Dict[str, MerkleRootV2] = field(
        metadata=config(field_name="merkleRoots")
    )


@dataclass_json
@dataclass
class LookupImplicitTeamRes:
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    name: TeamName = field(metadata=config(field_name="name"))
    display_name: ImplicitTeamDisplayName = field(
        metadata=config(field_name="displayName")
    )
    tlf_id: TLFID = field(metadata=config(field_name="tlfID"))


@dataclass_json
@dataclass
class PublicKeyV2NaCl:
    base: PublicKeyV2Base = field(metadata=config(field_name="base"))
    parent: Optional[KID] = field(metadata=config(field_name="parent"))
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    device_description: str = field(metadata=config(field_name="deviceDescription"))
    device_type: str = field(metadata=config(field_name="deviceType"))


@dataclass_json
@dataclass
class PublicKeyV2PGPSummary:
    base: PublicKeyV2Base = field(metadata=config(field_name="base"))
    fingerprint: PGPFingerprint = field(metadata=config(field_name="fingerprint"))
    identities: List[PGPIdentity] = field(metadata=config(field_name="identities"))


@dataclass
class ConflictState__NormalView:
    conflictStateType: Literal[ConflictStateType.NormalView]
    NormalView: Optional[FolderNormalView]


@dataclass
class ConflictState__ManualResolvingLocalView:
    conflictStateType: Literal[ConflictStateType.ManualResolvingLocalView]
    ManualResolvingLocalView: Optional[FolderConflictManualResolvingLocalView]


ConflictState = Union[
    ConflictState__NormalView, ConflictState__ManualResolvingLocalView
]


@dataclass
class GitRepoResult__ERR:
    state: Literal[GitRepoResultState.ERR]
    ERR: Optional[str]


@dataclass
class GitRepoResult__OK:
    state: Literal[GitRepoResultState.OK]
    OK: Optional[GitRepoInfo]


GitRepoResult = Union[GitRepoResult__ERR, GitRepoResult__OK]


@dataclass_json
@dataclass
class HomeScreenPeopleNotificationFollowedMulti:
    followers: List[HomeScreenPeopleNotificationFollowed] = field(
        metadata=config(field_name="followers")
    )
    num_others: int = field(metadata=config(field_name="numOthers"))


@dataclass_json
@dataclass
class IdentifyTrackBreaks:
    keys: List[IdentifyKey] = field(metadata=config(field_name="keys"))
    proofs: List[IdentifyProofBreak] = field(metadata=config(field_name="proofs"))


@dataclass
class OpDescription__LIST:
    asyncOp: Literal[AsyncOps.LIST]
    LIST: Optional[ListArgs]


@dataclass
class OpDescription__LIST_RECURSIVE:
    asyncOp: Literal[AsyncOps.LIST_RECURSIVE]
    LIST_RECURSIVE: Optional[ListArgs]


@dataclass
class OpDescription__LIST_RECURSIVE_TO_DEPTH:
    asyncOp: Literal[AsyncOps.LIST_RECURSIVE_TO_DEPTH]
    LIST_RECURSIVE_TO_DEPTH: Optional[ListToDepthArgs]


@dataclass
class OpDescription__READ:
    asyncOp: Literal[AsyncOps.READ]
    READ: Optional[ReadArgs]


@dataclass
class OpDescription__WRITE:
    asyncOp: Literal[AsyncOps.WRITE]
    WRITE: Optional[WriteArgs]


@dataclass
class OpDescription__COPY:
    asyncOp: Literal[AsyncOps.COPY]
    COPY: Optional[CopyArgs]


@dataclass
class OpDescription__MOVE:
    asyncOp: Literal[AsyncOps.MOVE]
    MOVE: Optional[MoveArgs]


@dataclass
class OpDescription__REMOVE:
    asyncOp: Literal[AsyncOps.REMOVE]
    REMOVE: Optional[RemoveArgs]


@dataclass
class OpDescription__GET_REVISIONS:
    asyncOp: Literal[AsyncOps.GET_REVISIONS]
    GET_REVISIONS: Optional[GetRevisionsArgs]


OpDescription = Union[
    OpDescription__LIST,
    OpDescription__LIST_RECURSIVE,
    OpDescription__LIST_RECURSIVE_TO_DEPTH,
    OpDescription__READ,
    OpDescription__WRITE,
    OpDescription__COPY,
    OpDescription__MOVE,
    OpDescription__REMOVE,
    OpDescription__GET_REVISIONS,
]


@dataclass_json
@dataclass
class TeamData:
    subversion: int = field(metadata=config(field_name="v"))
    frozen: bool = field(metadata=config(field_name="frozen"))
    tombstoned: bool = field(metadata=config(field_name="tombstoned"))
    secretless: bool = field(metadata=config(field_name="secretless"))
    name: TeamName = field(metadata=config(field_name="name"))
    chain: TeamSigChainState = field(metadata=config(field_name="chain"))
    per_team_key_seeds_unverified: Dict[str, PerTeamKeySeedItem] = field(
        metadata=config(field_name="perTeamKeySeedsUnverified")
    )
    reader_key_masks: Dict[str, Dict[str, MaskB64]] = field(
        metadata=config(field_name="readerKeyMasks")
    )
    latest_seqno_hint: Seqno = field(metadata=config(field_name="latestSeqnoHint"))
    cached_at: Time = field(metadata=config(field_name="cachedAt"))
    tlf_crypt_keys: Dict[str, List[CryptKey]] = field(
        metadata=config(field_name="tlfCryptKeys")
    )


@dataclass_json
@dataclass
class TeamDebugRes:
    chain: TeamSigChainState = field(metadata=config(field_name="chain"))


@dataclass
class PublicKeyV2__NACL:
    keyType: Literal[KeyType.NACL]
    NACL: Optional[PublicKeyV2NaCl]


@dataclass
class PublicKeyV2__PGP:
    keyType: Literal[KeyType.PGP]
    PGP: Optional[PublicKeyV2PGPSummary]


PublicKeyV2 = Union[PublicKeyV2__NACL, PublicKeyV2__PGP]


@dataclass_json
@dataclass
class UserPlusKeysV2:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    status: StatusCode = field(metadata=config(field_name="status"))
    per_user_keys: List[PerUserKey] = field(metadata=config(field_name="perUserKeys"))
    device_keys: Dict[str, PublicKeyV2NaCl] = field(
        metadata=config(field_name="deviceKeys")
    )
    pgp_keys: Dict[str, PublicKeyV2PGPSummary] = field(
        metadata=config(field_name="pgpKeys")
    )
    stellar_account_id: Optional[str] = field(
        metadata=config(field_name="stellarAccountID")
    )
    remote_tracks: Dict[str, RemoteTrack] = field(
        metadata=config(field_name="remoteTracks")
    )
    reset: Optional[ResetSummary] = field(metadata=config(field_name="reset"))
    unstubbed: bool = field(metadata=config(field_name="unstubbed"))


@dataclass_json
@dataclass
class UPKLiteV1:
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    status: StatusCode = field(metadata=config(field_name="status"))
    device_keys: Dict[str, PublicKeyV2NaCl] = field(
        metadata=config(field_name="deviceKeys")
    )
    reset: Optional[ResetSummary] = field(metadata=config(field_name="reset"))


@dataclass_json
@dataclass
class Folder:
    name: str = field(metadata=config(field_name="name"))
    private: bool = field(metadata=config(field_name="private"))
    created: bool = field(metadata=config(field_name="created"))
    folder_type: FolderType = field(metadata=config(field_name="folderType"))
    team_id: Optional[TeamID] = field(metadata=config(field_name="team_id"))
    reset_members: List[User] = field(metadata=config(field_name="reset_members"))
    mtime: Optional[Time] = field(metadata=config(field_name="mtime"))
    conflict_state: Optional[ConflictState] = field(
        metadata=config(field_name="conflictState")
    )
    sync_config: Optional[FolderSyncConfig] = field(
        metadata=config(field_name="syncConfig")
    )


@dataclass
class HomeScreenPeopleNotification__FOLLOWED:
    t: Literal[HomeScreenPeopleNotificationType.FOLLOWED]
    FOLLOWED: Optional[HomeScreenPeopleNotificationFollowed]


@dataclass
class HomeScreenPeopleNotification__FOLLOWED_MULTI:
    t: Literal[HomeScreenPeopleNotificationType.FOLLOWED_MULTI]
    FOLLOWED_MULTI: Optional[HomeScreenPeopleNotificationFollowedMulti]


HomeScreenPeopleNotification = Union[
    HomeScreenPeopleNotification__FOLLOWED, HomeScreenPeopleNotification__FOLLOWED_MULTI
]


@dataclass_json
@dataclass
class Identify2Res:
    upk: UserPlusKeys = field(metadata=config(field_name="upk"))
    identified_at: Time = field(metadata=config(field_name="identifiedAt"))
    track_breaks: Optional[IdentifyTrackBreaks] = field(
        metadata=config(field_name="trackBreaks")
    )


@dataclass_json
@dataclass
class IdentifyLiteRes:
    ul: UserOrTeamLite = field(metadata=config(field_name="ul"))
    track_breaks: Optional[IdentifyTrackBreaks] = field(
        metadata=config(field_name="trackBreaks")
    )


@dataclass_json
@dataclass
class ResolveIdentifyImplicitTeamRes:
    display_name: str = field(metadata=config(field_name="displayName"))
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    writers: List[UserVersion] = field(metadata=config(field_name="writers"))
    track_breaks: Dict[str, IdentifyTrackBreaks] = field(
        metadata=config(field_name="trackBreaks")
    )
    folder_id: TLFID = field(metadata=config(field_name="folderID"))


@dataclass_json
@dataclass
class TLFIdentifyFailure:
    user: User = field(metadata=config(field_name="user"))
    breaks: Optional[IdentifyTrackBreaks] = field(metadata=config(field_name="breaks"))


@dataclass_json
@dataclass
class UserPlusKeysV2AllIncarnations:
    current: UserPlusKeysV2 = field(metadata=config(field_name="current"))
    past_incarnations: List[UserPlusKeysV2] = field(
        metadata=config(field_name="pastIncarnations")
    )
    uvv: UserVersionVector = field(metadata=config(field_name="uvv"))
    seqno_link_i_ds: Dict[str, LinkID] = field(
        metadata=config(field_name="seqnoLinkIDs")
    )
    minor_version: UPK2MinorVersion = field(metadata=config(field_name="minorVersion"))
    stale: bool = field(metadata=config(field_name="stale"))


@dataclass_json
@dataclass
class UPKLiteV1AllIncarnations:
    current: UPKLiteV1 = field(metadata=config(field_name="current"))
    past_incarnations: List[UPKLiteV1] = field(
        metadata=config(field_name="pastIncarnations")
    )
    seqno_link_i_ds: Dict[str, LinkID] = field(
        metadata=config(field_name="seqnoLinkIDs")
    )
    minor_version: UPKLiteMinorVersion = field(
        metadata=config(field_name="minorVersion")
    )


@dataclass_json
@dataclass
class FavoritesResult:
    favorite_folders: List[Folder] = field(
        metadata=config(field_name="favoriteFolders")
    )
    ignored_folders: List[Folder] = field(metadata=config(field_name="ignoredFolders"))
    new_folders: List[Folder] = field(metadata=config(field_name="newFolders"))


@dataclass
class HomeScreenItemData__TODO:
    t: Literal[HomeScreenItemType.TODO]
    TODO: Optional[HomeScreenTodo]


@dataclass
class HomeScreenItemData__PEOPLE:
    t: Literal[HomeScreenItemType.PEOPLE]
    PEOPLE: Optional[HomeScreenPeopleNotification]


@dataclass
class HomeScreenItemData__ANNOUNCEMENT:
    t: Literal[HomeScreenItemType.ANNOUNCEMENT]
    ANNOUNCEMENT: Optional[HomeScreenAnnouncement]


HomeScreenItemData = Union[
    HomeScreenItemData__TODO,
    HomeScreenItemData__PEOPLE,
    HomeScreenItemData__ANNOUNCEMENT,
]


@dataclass_json
@dataclass
class Identify2ResUPK2:
    upk: UserPlusKeysV2AllIncarnations = field(metadata=config(field_name="upk"))
    identified_at: Time = field(metadata=config(field_name="identifiedAt"))
    track_breaks: Optional[IdentifyTrackBreaks] = field(
        metadata=config(field_name="trackBreaks")
    )


@dataclass_json
@dataclass
class FSEditListRequest:
    folder: Folder = field(metadata=config(field_name="folder"))
    request_id: int = field(metadata=config(field_name="requestID"))


@dataclass_json
@dataclass
class FSFolderEditHistory:
    folder: Folder = field(metadata=config(field_name="folder"))
    server_time: Time = field(metadata=config(field_name="serverTime"))
    history: List[FSFolderWriterEditHistory] = field(
        metadata=config(field_name="history")
    )


@dataclass_json
@dataclass
class FolderSyncConfigAndStatusWithFolder:
    folder: Folder = field(metadata=config(field_name="folder"))
    config: FolderSyncConfig = field(metadata=config(field_name="config"))
    status: FolderSyncStatus = field(metadata=config(field_name="status"))


@dataclass_json
@dataclass
class TLFBreak:
    breaks: List[TLFIdentifyFailure] = field(metadata=config(field_name="breaks"))


@dataclass
class UPAKVersioned__V1:
    v: Literal[UPAKVersion.V1]
    V1: Optional[UserPlusAllKeys]


@dataclass
class UPAKVersioned__V2:
    v: Literal[UPAKVersion.V2]
    V2: Optional[UserPlusKeysV2AllIncarnations]


UPAKVersioned = Union[UPAKVersioned__V1, UPAKVersioned__V2]


@dataclass_json
@dataclass
class HomeScreenItem:
    badged: bool = field(metadata=config(field_name="badged"))
    data: HomeScreenItemData = field(metadata=config(field_name="data"))
    data_ext: HomeScreenItemDataExt = field(metadata=config(field_name="dataExt"))


@dataclass_json
@dataclass
class SyncConfigAndStatusRes:
    folders: List[FolderSyncConfigAndStatusWithFolder] = field(
        metadata=config(field_name="folders")
    )
    overall_status: FolderSyncStatus = field(
        metadata=config(field_name="overallStatus")
    )


@dataclass_json
@dataclass
class CanonicalTLFNameAndIDWithBreaks:
    tlf_id: TLFID = field(metadata=config(field_name="tlfID"))
    canonical_name: CanonicalTlfName = field(
        metadata=config(field_name="CanonicalName")
    )
    breaks: TLFBreak = field(metadata=config(field_name="breaks"))


@dataclass_json
@dataclass
class HomeScreen:
    last_viewed: Time = field(metadata=config(field_name="lastViewed"))
    version: int = field(metadata=config(field_name="version"))
    visits: int = field(metadata=config(field_name="visits"))
    items: List[HomeScreenItem] = field(metadata=config(field_name="items"))
    follow_suggestions: List[HomeUserSummary] = field(
        metadata=config(field_name="followSuggestions")
    )
    announcements_version: int = field(
        metadata=config(field_name="announcementsVersion")
    )


@dataclass_json
@dataclass
class GetTLFCryptKeysRes:
    name_id_breaks: CanonicalTLFNameAndIDWithBreaks = field(
        metadata=config(field_name="nameIDBreaks")
    )
    crypt_keys: List[CryptKey] = field(metadata=config(field_name="CryptKeys"))
