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

from mashumaro import DataClassJSONMixin
from typing_extensions import Literal

import gregor1


@dataclass
class HasServerKeysRes(DataClassJSONMixin):
    has_server_keys: bool


@dataclass
class APIRes(DataClassJSONMixin):
    status: str
    body: str
    http_status: int
    app_status: str


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


@dataclass
class ChallengeInfo(DataClassJSONMixin):
    now: int
    challenge: str


class BlockStatus(Enum):
    UNKNOWN = "unknown"
    LIVE = "live"
    ARCHIVED = "archived"


BlockRefNonce = Optional[str]


@dataclass
class BlockPingResponse(DataClassJSONMixin):
    pass


Time = int
UnixTime = int
DurationSec = float


@dataclass
class StringKVPair(DataClassJSONMixin):
    key: str
    value: str


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


@dataclass
class Text(DataClassJSONMixin):
    data: str
    markup: bool


@dataclass
class PGPIdentity(DataClassJSONMixin):
    username: str
    comment: str
    email: str


class DeviceType(Enum):
    DESKTOP = "desktop"
    MOBILE = "mobile"


@dataclass
class Stream(DataClassJSONMixin):
    fd: int


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


@dataclass
class KBFSPathInfo(DataClassJSONMixin):
    standard_path: str
    deeplink_path: str
    platform_after_mount_path: str


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


@dataclass
class ImageCropRect(DataClassJSONMixin):
    x_0: int
    y_0: int
    x_1: int
    y_1: int


class IdentityVisibility(Enum):
    PRIVATE = "private"
    PUBLIC = "public"


@dataclass
class SizedImage(DataClassJSONMixin):
    path: str
    width: int


class OfflineAvailability(Enum):
    NONE = "none"
    BEST_EFFORT = "best_effort"


ReacjiSkinTone = int


@dataclass
class SessionStatus(DataClassJSONMixin):
    session_for: str
    loaded: bool
    cleared: bool
    salt_only: bool
    expired: bool


@dataclass
class PlatformInfo(DataClassJSONMixin):
    os: str
    os_version: str
    arch: str
    go_version: str


@dataclass
class LoadDeviceErr(DataClassJSONMixin):
    where: str
    desc: str


@dataclass
class DirSizeInfo(DataClassJSONMixin):
    num_files: int
    name: str
    human_size: str


@dataclass
class KbClientStatus(DataClassJSONMixin):
    version: str


@dataclass
class KbServiceStatus(DataClassJSONMixin):
    version: str
    running: bool
    pid: str
    log: str
    ek_log: str


@dataclass
class KBFSStatus(DataClassJSONMixin):
    version: str
    installed_version: str
    running: bool
    pid: str
    log: str
    mount: str


@dataclass
class DesktopStatus(DataClassJSONMixin):
    version: str
    running: bool
    log: str


@dataclass
class UpdaterStatus(DataClassJSONMixin):
    log: str


@dataclass
class StartStatus(DataClassJSONMixin):
    log: str


@dataclass
class GitStatus(DataClassJSONMixin):
    log: str


LogSendID = str


@dataclass
class AllProvisionedUsernames(DataClassJSONMixin):
    default_username: str
    provisioned_usernames: List[str]
    has_provisioned_user: bool


class ForkType(Enum):
    NONE = "none"
    AUTO = "auto"
    WATCHDOG = "watchdog"
    LAUNCHD = "launchd"
    SYSTEMD = "systemd"


@dataclass
class ConfigValue(DataClassJSONMixin):
    is_null: bool
    b: Optional[bool]
    i: Optional[int]
    s: Optional[str]
    o: Optional[str]


@dataclass
class OutOfDateInfo(DataClassJSONMixin):
    upgrade_to: str
    upgrade_uri: str
    custom_message: str
    critical_clock_skew: int


class UpdateInfoStatus(Enum):
    UP_TO_DATE = "up_to_date"
    NEED_UPDATE = "need_update"
    CRITICALLY_OUT_OF_DATE = "critically_out_of_date"


class UpdateInfoStatus2(Enum):
    OK = "ok"
    SUGGESTED = "suggested"
    CRITICAL = "critical"


@dataclass
class UpdateDetails(DataClassJSONMixin):
    message: str


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


@dataclass
class RegisterAddressRes(DataClassJSONMixin):
    type: str
    family: str


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


@dataclass
class FirstStepResult(DataClassJSONMixin):
    val_plus_two: int


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


@dataclass
class File(DataClassJSONMixin):
    path: str


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


@dataclass
class GitTeamRepoSettings(DataClassJSONMixin):
    channel_name: Optional[str]
    chat_disabled: bool


@dataclass
class SelectKeyRes(DataClassJSONMixin):
    key_id: str
    do_secret_push: bool


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


@dataclass
class Pics(DataClassJSONMixin):
    square_40: str
    square_200: str
    square_360: str


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


@dataclass
class SigHint(DataClassJSONMixin):
    remote_id: str
    human_url: str
    api_url: str
    check_text: str


class CheckResultFreshness(Enum):
    FRESH = "fresh"
    AGED = "aged"
    RANCID = "rancid"


@dataclass
class ConfirmResult(DataClassJSONMixin):
    identity_confirmed: bool
    remote_confirmed: bool
    expiring_local: bool
    auto_confirmed: bool


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


@dataclass
class FuseMountInfo(DataClassJSONMixin):
    path: str
    fstype: str
    output: str


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


@dataclass
class FSSyncStatusRequest(DataClassJSONMixin):
    request_id: int


@dataclass
class PassphraseStream(DataClassJSONMixin):
    passphrase_stream: bytes
    generation: int


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


@dataclass
class KeyBundle(DataClassJSONMixin):
    version: int
    bundle: bytes


@dataclass
class MerkleRoot(DataClassJSONMixin):
    version: int
    root: bytes


LockID = int
MDPriority = int


@dataclass
class RekeyRequest(DataClassJSONMixin):
    folder_id: str
    revision: int


ChatConversationID = bytes


@dataclass
class DeletedTeamInfo(DataClassJSONMixin):
    team_name: str
    deleted_by: str
    id: gregor1.MsgID


@dataclass
class WalletAccountInfo(DataClassJSONMixin):
    account_id: str
    num_unread: int


@dataclass
class NotificationChannels(DataClassJSONMixin):
    session: bool
    users: bool
    kbfs: bool
    kbfsdesktop: bool
    kbfslegacy: bool
    kbfssubscription: bool
    tracking: bool
    favorites: bool
    paperkeys: bool
    keyfamily: bool
    service: bool
    app: bool
    chat: bool
    pgp: bool
    kbfsrequest: bool
    badges: bool
    reachability: bool
    team: bool
    ephemeral: bool
    teambot: bool
    chatkbfsedits: bool
    chatdev: bool
    deviceclone: bool
    chatattachments: bool
    wallet: bool
    audit: bool
    runtimestats: bool


class StatsSeverityLevel(Enum):
    NORMAL = "normal"
    WARNING = "warning"
    SEVERE = "severe"


class ProcessType(Enum):
    MAIN = "main"
    KBFS = "kbfs"


@dataclass
class HttpSrvInfo(DataClassJSONMixin):
    address: str
    token: str


@dataclass
class TeamChangeSet(DataClassJSONMixin):
    membership_changed: bool
    key_rotated: bool
    renamed: bool
    misc: bool


class AvatarUpdateType(Enum):
    NONE = "none"
    USER = "user"
    TEAM = "team"


class RuntimeGroup(Enum):
    UNKNOWN = "unknown"
    LINUXLIKE = "linuxlike"
    DARWINLIKE = "darwinlike"
    WINDOWSLIKE = "windowslike"


@dataclass
class Feature(DataClassJSONMixin):
    allow: bool
    default_value: bool
    readonly: bool
    label: str


class PassphraseType(Enum):
    NONE = "none"
    PAPER_KEY = "paper_key"
    PASS_PHRASE = "pass_phrase"
    VERIFY_PASS_PHRASE = "verify_pass_phrase"


@dataclass
class GetPassphraseRes(DataClassJSONMixin):
    passphrase: str
    store_secret: bool


class SignMode(Enum):
    ATTACHED = "attached"
    DETACHED = "detached"
    CLEAR = "clear"


@dataclass
class PGPEncryptOptions(DataClassJSONMixin):
    recipients: List[str]
    no_sign: bool
    no_self: bool
    binary_out: bool
    key_query: str


@dataclass
class PGPDecryptOptions(DataClassJSONMixin):
    assert_signed: bool
    signed_by: str


@dataclass
class PGPVerifyOptions(DataClassJSONMixin):
    signed_by: str
    signature: bytes


@dataclass
class KeyInfo(DataClassJSONMixin):
    fingerprint: str
    key: str
    desc: str


@dataclass
class PGPQuery(DataClassJSONMixin):
    secret: bool
    query: str
    exact_match: bool


@dataclass
class PGPPurgeRes(DataClassJSONMixin):
    filenames: List[str]


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


@dataclass
class SelectorEntry(DataClassJSONMixin):
    is_index: bool
    index: int
    is_key: bool
    key: str
    is_all: bool
    is_contents: bool


@dataclass
class ParamProofUsernameConfig(DataClassJSONMixin):
    re: str
    min: int
    max: int


@dataclass
class ParamProofLogoConfig(DataClassJSONMixin):
    svg_black: str
    svg_full: str


@dataclass
class ServiceDisplayConfig(DataClassJSONMixin):
    creation_disabled: bool
    priority: int
    key: str
    group: Optional[str]
    new: bool
    logo_key: str


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


@dataclass
class SecretResponse(DataClassJSONMixin):
    secret: bytes
    phrase: str


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


@dataclass
class SaltpackDecryptOptions(DataClassJSONMixin):
    interactive: bool
    force_remote_check: bool
    use_paper_key: bool


@dataclass
class SaltpackSignOptions(DataClassJSONMixin):
    detached: bool
    binary: bool
    saltpack_version: int


@dataclass
class SaltpackVerifyOptions(DataClassJSONMixin):
    signed_by: str
    signature: bytes


class SaltpackSenderType(Enum):
    NOT_TRACKED = "not_tracked"
    UNKNOWN = "unknown"
    ANONYMOUS = "anonymous"
    TRACKING_BROKE = "tracking_broke"
    TRACKING_OK = "tracking_ok"
    SELF = "self"
    REVOKED = "revoked"
    EXPIRED = "expired"


@dataclass
class SecretEntryArg(DataClassJSONMixin):
    desc: str
    prompt: str
    err: str
    cancel: str
    ok: str
    reason: str
    show_typing: bool


@dataclass
class SecretEntryRes(DataClassJSONMixin):
    text: str
    canceled: bool
    store_secret: bool


NaclSigningKeyPublic = Optional[str]
NaclSigningKeyPrivate = Optional[str]
NaclDHKeyPublic = Optional[str]
NaclDHKeyPrivate = Optional[str]


@dataclass
class SignupRes(DataClassJSONMixin):
    passphrase_ok: bool
    post_ok: bool
    write_ok: bool


@dataclass
class SigTypes(DataClassJSONMixin):
    track: bool
    proof: bool
    cryptocurrency: bool
    is_self: bool


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


@dataclass
class SimpleFSGetHTTPAddressAndTokenResponse(DataClassJSONMixin):
    address: str
    token: str


@dataclass
class SimpleFSQuotaUsage(DataClassJSONMixin):
    usage_bytes: int
    archive_bytes: int
    limit_bytes: int
    git_usage_bytes: int
    git_archive_bytes: int
    git_limit_bytes: int


class FolderSyncMode(Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"
    PARTIAL = "partial"


@dataclass
class FSSettings(DataClassJSONMixin):
    space_available_notification_threshold: int


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


@dataclass
class TeamEncryptedKBFSKeyset(DataClassJSONMixin):
    v: int
    e: bytes
    n: bytes


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


@dataclass
class SeitanKeyLabelSms(DataClassJSONMixin):
    f: str
    n: str


@dataclass
class TeamJoinRequest(DataClassJSONMixin):
    name: str
    username: str


@dataclass
class TeamBotSettings(DataClassJSONMixin):
    cmds: bool
    mentions: bool
    triggers: List[str]
    convs: List[str]


@dataclass
class TeamRequestAccessResult(DataClassJSONMixin):
    open: bool


@dataclass
class TeamAcceptOrRequestResult(DataClassJSONMixin):
    was_token: bool
    was_seitan: bool
    was_team_name: bool
    was_open_team: bool


@dataclass
class BulkRes(DataClassJSONMixin):
    invited: List[str]
    already_invited: List[str]
    malformed: List[str]


ConflictGeneration = int


@dataclass
class TeamOperation(DataClassJSONMixin):
    manage_members: bool
    manage_subteams: bool
    create_channel: bool
    chat: bool
    delete_channel: bool
    rename_channel: bool
    rename_team: bool
    edit_channel_description: bool
    edit_team_description: bool
    set_team_showcase: bool
    set_member_showcase: bool
    set_retention_policy: bool
    set_min_writer_role: bool
    change_open_team: bool
    leave_team: bool
    join_team: bool
    set_publicity_any: bool
    list_first: bool
    change_tars_disabled: bool
    delete_chat_history: bool
    delete_other_messages: bool
    delete_team: bool
    pin_message: bool


@dataclass
class ProfileTeamLoadRes(DataClassJSONMixin):
    load_time_nsec: int


class RotationType(Enum):
    VISIBLE = "visible"
    HIDDEN = "hidden"
    CLKR = "clkr"


@dataclass
class MemberEmail(DataClassJSONMixin):
    email: str
    role: str


@dataclass
class MemberUsername(DataClassJSONMixin):
    username: str
    role: str


@dataclass
class Test(DataClassJSONMixin):
    reply: str


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


@dataclass
class TrackProof(DataClassJSONMixin):
    proof_type: str
    proof_name: str
    id_string: str


@dataclass
class WebProof(DataClassJSONMixin):
    hostname: str
    protocols: List[str]


EmailAddress = str


@dataclass
class CanLogoutRes(DataClassJSONMixin):
    can_logout: bool
    reason: str
    set_passphrase: bool


APIUserServiceIDWithContact = str


@dataclass
class ImpTofuSearchResult(DataClassJSONMixin):
    assertion: str
    assertion_value: str
    assertion_key: str
    label: str
    pretty_name: str
    keybase_username: str


class ImpTofuSearchType(Enum):
    PHONE = "phone"
    EMAIL = "email"


@dataclass
class LockdownHistory(DataClassJSONMixin):
    status: bool
    ctime: Time
    device_id: DeviceID
    device_name: str


@dataclass
class BoxAuditAttempt(DataClassJSONMixin):
    ctime: UnixTime
    error: Optional[str]
    result: BoxAuditAttemptResult
    generation: Optional[PerTeamKeyGeneration]
    rotated: bool


@dataclass
class LoadAvatarsRes(DataClassJSONMixin):
    picmap: Dict[str, Dict[str, AvatarUrl]]


@dataclass
class AvatarClearCacheMsg(DataClassJSONMixin):
    name: str
    formats: List[AvatarFormat]
    typ: AvatarUpdateType


@dataclass
class BlockIdCombo(DataClassJSONMixin):
    block_hash: str
    charged_to: UserOrTeamID
    block_type: BlockType


@dataclass
class GetBlockRes(DataClassJSONMixin):
    block_key: str
    buf: bytes
    size: int
    status: BlockStatus


@dataclass
class Status(DataClassJSONMixin):
    code: int
    name: str
    desc: str
    fields: List[StringKVPair]


@dataclass
class UserVersion(DataClassJSONMixin):
    uid: UID
    eldest_seqno: Seqno


@dataclass
class CompatibilityTeamID__LEGACY:
    typ: Literal[TeamType.LEGACY]
    LEGACY: Optional[TLFID]


@dataclass
class CompatibilityTeamID__MODERN:
    typ: Literal[TeamType.MODERN]
    MODERN: Optional[TeamID]


CompatibilityTeamID = Union[CompatibilityTeamID__LEGACY, CompatibilityTeamID__MODERN]


@dataclass
class TeamIDWithVisibility(DataClassJSONMixin):
    team_id: TeamID
    visibility: TLFVisibility


@dataclass
class PublicKey(DataClassJSONMixin):
    kid: KID
    pgp_fingerprint: str
    pgp_identities: List[PGPIdentity]
    is_sibkey: bool
    is_eldest: bool
    parent_id: str
    device_id: DeviceID
    device_description: str
    device_type: str
    c_time: Time
    e_time: Time
    is_revoked: bool


@dataclass
class KeybaseTime(DataClassJSONMixin):
    unix: Time
    chain: Seqno


@dataclass
class User(DataClassJSONMixin):
    uid: UID
    username: str


@dataclass
class Device(DataClassJSONMixin):
    type: str
    name: str
    device_id: DeviceID
    c_time: Time
    m_time: Time
    last_used_time: Time
    encrypt_key: KID
    verify_key: KID
    status: int


@dataclass
class UserVersionVector(DataClassJSONMixin):
    id: int
    sig_hints: int
    sig_chain: int
    cached_at: Time


@dataclass
class PerUserKey(DataClassJSONMixin):
    gen: int
    seqno: Seqno
    sig_kid: KID
    enc_kid: KID
    signed_by_kid: KID


@dataclass
class UserOrTeamLite(DataClassJSONMixin):
    id: UserOrTeamID
    name: str


@dataclass
class RemoteTrack(DataClassJSONMixin):
    username: str
    uid: UID
    link_id: LinkID


@dataclass
class SocialAssertion(DataClassJSONMixin):
    user: str
    service: SocialAssertionService


@dataclass
class FullNamePackage(DataClassJSONMixin):
    version: FullNamePackageVersion
    full_name: FullName
    eldest_seqno: Seqno
    status: StatusCode
    cached_at: Time


@dataclass
class PhoneLookupResult(DataClassJSONMixin):
    uid: UID
    username: str
    ctime: UnixTime


@dataclass
class UserReacjis(DataClassJSONMixin):
    top_reacjis: List[str]
    skin_tone: ReacjiSkinTone


@dataclass
class ClientDetails(DataClassJSONMixin):
    pid: int
    client_type: ClientType
    argv: List[str]
    desc: str
    version: str


@dataclass
class Config(DataClassJSONMixin):
    server_uri: str
    socket_file: str
    label: str
    run_mode: str
    gpg_exists: bool
    gpg_path: str
    version: str
    path: str
    binary_realpath: str
    config_path: str
    version_short: str
    version_full: str
    is_auto_forked: bool
    fork_type: ForkType


@dataclass
class UpdateInfo(DataClassJSONMixin):
    status: UpdateInfoStatus
    message: str


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


@dataclass
class ProxyData(DataClassJSONMixin):
    address_with_port: str
    proxy_type: ProxyType
    cert_pinning: bool


@dataclass
class ContactComponent(DataClassJSONMixin):
    label: str
    phone_number: Optional[RawPhoneNumber]
    email: Optional[EmailAddress]


@dataclass
class ED25519SignatureInfo(DataClassJSONMixin):
    sig: ED25519Signature
    public_key: ED25519PublicKey


@dataclass
class CiphertextBundle(DataClassJSONMixin):
    kid: KID
    ciphertext: EncryptedBytes32
    nonce: BoxNonce
    public_key: BoxPublicKey


@dataclass
class UnboxAnyRes(DataClassJSONMixin):
    kid: KID
    plaintext: Bytes32
    index: int


@dataclass
class DbKey(DataClassJSONMixin):
    db_type: DbType
    obj_type: int
    key: str


@dataclass
class EmailLookupResult(DataClassJSONMixin):
    email: EmailAddress
    uid: Optional[UID]


@dataclass
class EmailAddressVerifiedMsg(DataClassJSONMixin):
    email: EmailAddress


@dataclass
class EmailAddressChangedMsg(DataClassJSONMixin):
    email: EmailAddress


@dataclass
class DeviceEkMetadata(DataClassJSONMixin):
    device_ephemeral_dh_public: KID
    hash_meta: HashMeta
    generation: EkGeneration
    ctime: Time
    device_ctime: Time


@dataclass
class UserEkMetadata(DataClassJSONMixin):
    user_ephemeral_dh_public: KID
    hash_meta: HashMeta
    generation: EkGeneration
    ctime: Time


@dataclass
class UserEkBoxMetadata(DataClassJSONMixin):
    box: str
    recipient_generation: EkGeneration
    recipient_device_id: DeviceID


@dataclass
class TeamEkMetadata(DataClassJSONMixin):
    team_ephemeral_dh_public: KID
    hash_meta: HashMeta
    generation: EkGeneration
    ctime: Time


@dataclass
class TeamEkBoxMetadata(DataClassJSONMixin):
    box: str
    recipient_generation: EkGeneration
    recipient_uid: UID


@dataclass
class TeambotEkMetadata(DataClassJSONMixin):
    teambot_dh_public: KID
    generation: EkGeneration
    uid: UID
    user_ek_generation: EkGeneration
    hash_meta: HashMeta
    ctime: Time


@dataclass
class FolderHandle(DataClassJSONMixin):
    name: str
    folder_type: FolderType
    created: bool


@dataclass
class ListResult(DataClassJSONMixin):
    files: List[File]


@dataclass
class EncryptedGitMetadata(DataClassJSONMixin):
    v: int
    e: bytes
    n: BoxNonce
    gen: PerTeamKeyGeneration


@dataclass
class GitLocalMetadataV1(DataClassJSONMixin):
    repo_name: GitRepoName


@dataclass
class GitCommit(DataClassJSONMixin):
    commit_hash: str
    message: str
    author_name: str
    author_email: str
    ctime: Time


@dataclass
class GitServerMetadata(DataClassJSONMixin):
    ctime: Time
    mtime: Time
    last_modifying_username: str
    last_modifying_device_id: DeviceID
    last_modifying_device_name: str


@dataclass
class GPGKey(DataClassJSONMixin):
    algorithm: str
    key_id: str
    creation: str
    expiration: str
    identities: List[PGPIdentity]


@dataclass
class HomeScreenAnnouncement(DataClassJSONMixin):
    id: HomeScreenAnnouncementID
    version: HomeScreenAnnouncementVersion
    app_link: AppLinkType
    confirm_label: str
    dismissable: bool
    icon_url: str
    text: str
    url: str


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


@dataclass
class VerifyAllEmailTodoExt(DataClassJSONMixin):
    last_verify_email_date: UnixTime


@dataclass
class HomeUserSummary(DataClassJSONMixin):
    uid: UID
    username: str
    bio: str
    full_name: str
    pics: Optional[Pics]


@dataclass
class Identify3RowMeta(DataClassJSONMixin):
    color: Identify3RowColor
    label: str


@dataclass
class TrackDiff(DataClassJSONMixin):
    type: TrackDiffType
    display_markup: str


@dataclass
class TrackSummary(DataClassJSONMixin):
    username: str
    time: Time
    is_remote: bool


@dataclass
class TrackOptions(DataClassJSONMixin):
    local_only: bool
    bypass_confirm: bool
    force_retrack: bool
    expiring_local: bool
    for_pgp_pull: bool
    sig_version: Optional[SigVersion]


@dataclass
class IdentifyReason(DataClassJSONMixin):
    type: IdentifyReasonType
    reason: str
    resource: str


@dataclass
class RemoteProof(DataClassJSONMixin):
    proof_type: ProofType
    key: str
    value: str
    display_markup: str
    sig_id: SigID
    m_time: Time


@dataclass
class ProofResult(DataClassJSONMixin):
    state: ProofState
    status: ProofStatus
    desc: str


@dataclass
class Cryptocurrency(DataClassJSONMixin):
    row_id: int
    pkhash: bytes
    address: str
    sig_id: SigID
    type: str
    family: str


@dataclass
class StellarAccount(DataClassJSONMixin):
    account_id: str
    federation_address: str
    sig_id: SigID


@dataclass
class UserTeamShowcase(DataClassJSONMixin):
    fq_name: str
    open: bool
    team_is_showcased: bool
    description: str
    role: TeamRole
    public_admins: List[str]
    num_members: int


@dataclass
class DismissReason(DataClassJSONMixin):
    type: DismissReasonType
    reason: str
    resource: str


@dataclass
class KBFSTeamSettings(DataClassJSONMixin):
    tlf_id: TLFID


@dataclass
class FSNotification(DataClassJSONMixin):
    filename: str
    status: str
    status_code: FSStatusCode
    notification_type: FSNotificationType
    error_type: FSErrorType
    params: Dict[str, str]
    writer_uid: UID
    local_time: Time
    folder_type: FolderType


@dataclass
class FSFolderWriterEdit(DataClassJSONMixin):
    filename: str
    notification_type: FSNotificationType
    server_time: Time


@dataclass
class FSPathSyncStatus(DataClassJSONMixin):
    folder_type: FolderType
    path: str
    syncing_bytes: int
    syncing_ops: int
    synced_bytes: int


@dataclass
class FSSyncStatus(DataClassJSONMixin):
    total_syncing_bytes: int
    syncing_paths: List[str]
    end_estimate: Optional[Time]


@dataclass
class GcOptions(DataClassJSONMixin):
    max_loose_refs: int
    prune_min_loose_objects: int
    prune_expire_time: Time
    max_object_packs: int


@dataclass
class Hello2Res(DataClassJSONMixin):
    encryption_key: KID
    sig_payload: HelloRes
    device_ek_kid: KID


@dataclass
class PerUserKeyBox(DataClassJSONMixin):
    generation: PerUserKeyGeneration
    box: str
    receiver_kid: KID


@dataclass
class ConfiguredAccount(DataClassJSONMixin):
    username: str
    fullname: FullName
    has_stored_secret: bool
    is_current: bool


@dataclass
class KBFSRoot(DataClassJSONMixin):
    tree_id: MerkleTreeID
    root: KBFSRootHash


@dataclass
class MerkleStoreEntry(DataClassJSONMixin):
    hash: MerkleStoreKitHash
    entry: MerkleStoreEntryString


@dataclass
class KeyHalf(DataClassJSONMixin):
    user: UID
    device_kid: KID
    key: bytes


@dataclass
class MDBlock(DataClassJSONMixin):
    version: int
    timestamp: Time
    block: bytes


@dataclass
class PingResponse(DataClassJSONMixin):
    timestamp: Time


@dataclass
class KeyBundleResponse(DataClassJSONMixin):
    writer_bundle: KeyBundle
    reader_bundle: KeyBundle


@dataclass
class LockContext(DataClassJSONMixin):
    require_lock_id: LockID
    release_after_success: bool


@dataclass
class FindNextMDResponse(DataClassJSONMixin):
    kbfs_root: MerkleRoot
    merkle_nodes: List[bytes]
    root_seqno: Seqno
    root_hash: HashMeta


@dataclass
class TeamMemberOutReset(DataClassJSONMixin):
    teamname: str
    username: str
    uid: UID
    id: gregor1.MsgID


@dataclass
class ResetState(DataClassJSONMixin):
    end_time: Time
    active: bool


@dataclass
class BadgeConversationInfo(DataClassJSONMixin):
    conv_id: ChatConversationID
    badge_counts: Dict[str, int]
    unread_messages: int


@dataclass
class DbStats(DataClassJSONMixin):
    type: DbType
    mem_comp_active: bool
    table_comp_active: bool


@dataclass
class ProcessRuntimeStats(DataClassJSONMixin):
    type: ProcessType
    cpu: str
    resident: str
    virt: str
    free: str
    goheap: str
    goheapsys: str
    goreleased: str
    cpu_severity: StatsSeverityLevel
    resident_severity: StatsSeverityLevel


@dataclass
class GUIEntryFeatures(DataClassJSONMixin):
    show_typing: Feature


@dataclass
class PGPSignOptions(DataClassJSONMixin):
    key_query: str
    mode: SignMode
    binary_in: bool
    binary_out: bool


@dataclass
class PGPCreateUids(DataClassJSONMixin):
    use_default: bool
    ids: List[PGPIdentity]


@dataclass
class UserPhoneNumber(DataClassJSONMixin):
    phone_number: PhoneNumber
    verified: bool
    superseded: bool
    visibility: IdentityVisibility
    ctime: UnixTime


@dataclass
class PhoneNumberLookupResult(DataClassJSONMixin):
    phone_number: RawPhoneNumber
    coerced_phone_number: PhoneNumber
    err: Optional[str]
    uid: Optional[UID]


@dataclass
class PhoneNumberChangedMsg(DataClassJSONMixin):
    phone: PhoneNumber


@dataclass
class FileDescriptor(DataClassJSONMixin):
    name: str
    type: FileType


@dataclass
class CheckProofStatus(DataClassJSONMixin):
    found: bool
    status: ProofStatus
    proof_text: str
    state: ProofState


@dataclass
class StartProofResult(DataClassJSONMixin):
    sig_id: SigID


@dataclass
class ParamProofJSON(DataClassJSONMixin):
    sig_hash: SigID
    kb_username: str


@dataclass
class ParamProofServiceConfig(DataClassJSONMixin):
    version: int
    domain: str
    display_name: str
    logo: Optional[ParamProofLogoConfig]
    description: str
    username: ParamProofUsernameConfig
    brand_color: str
    prefill_url: str
    profile_url: str
    check_url: str
    check_path: List[SelectorEntry]
    avatar_path: List[SelectorEntry]


@dataclass
class ProveParameters(DataClassJSONMixin):
    logo_full: List[SizedImage]
    logo_black: List[SizedImage]
    title: str
    subtext: str
    suffix: str
    button_label: str


@dataclass
class VerifySessionRes(DataClassJSONMixin):
    uid: UID
    sid: str
    generated: int
    lifetime: int


@dataclass
class Reachability(DataClassJSONMixin):
    reachable: Reachable


@dataclass
class TLF(DataClassJSONMixin):
    id: TLFID
    name: str
    writers: List[str]
    readers: List[str]
    is_private: bool


@dataclass
class RekeyEvent(DataClassJSONMixin):
    event_type: RekeyEventType
    interrupt_type: int


@dataclass
class ResetMerkleRoot(DataClassJSONMixin):
    hash_meta: HashMeta
    seqno: Seqno


@dataclass
class ResetPrev(DataClassJSONMixin):
    eldest_kid: Optional[KID]
    public_seqno: Seqno
    reset: SHA512


@dataclass
class SaltpackEncryptOptions(DataClassJSONMixin):
    recipients: List[str]
    team_recipients: List[str]
    authenticity_type: AuthenticityType
    use_entity_keys: bool
    use_device_keys: bool
    use_paper_keys: bool
    no_self_encrypt: bool
    binary: bool
    saltpack_version: int
    use_kbfs_keys_only_for_testing: bool


@dataclass
class SaltpackSender(DataClassJSONMixin):
    uid: UID
    username: str
    sender_type: SaltpackSenderType


@dataclass
class SecretKeys(DataClassJSONMixin):
    signing: NaclSigningKeyPrivate
    encryption: NaclDHKeyPrivate


@dataclass
class Session(DataClassJSONMixin):
    uid: UID
    username: str
    token: str
    device_subkey_kid: KID
    device_sibkey_kid: KID


@dataclass
class Sig(DataClassJSONMixin):
    seqno: Seqno
    sig_id: SigID
    sig_id_display: str
    type: str
    c_time: Time
    revoked: bool
    active: bool
    key: str
    body: str


@dataclass
class SigListArgs(DataClassJSONMixin):
    session_id: int
    username: str
    all_keys: bool
    types: Optional[SigTypes]
    filterx: str
    verbose: bool
    revoked: bool


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


@dataclass
class KBFSPath(DataClassJSONMixin):
    path: str
    identify_behavior: Optional[TLFIdentifyBehavior]


@dataclass
class PrefetchProgress(DataClassJSONMixin):
    start: Time
    end_estimate: Time
    bytes_total: int
    bytes_fetched: int


@dataclass
class FileContent(DataClassJSONMixin):
    data: bytes
    progress: Progress


@dataclass
class OpProgress(DataClassJSONMixin):
    start: Time
    end_estimate: Time
    op_type: AsyncOps
    bytes_total: int
    bytes_read: int
    bytes_written: int
    files_total: int
    files_read: int
    files_written: int


@dataclass
class FolderSyncConfig(DataClassJSONMixin):
    mode: FolderSyncMode
    paths: List[str]


@dataclass
class TeambotKeyMetadata(DataClassJSONMixin):
    teambot_dh_public: KID
    generation: TeambotKeyGeneration
    uid: UID
    puk_generation: PerUserKeyGeneration


@dataclass
class PerTeamSeedCheck(DataClassJSONMixin):
    version: PerTeamSeedCheckVersion
    value: PerTeamSeedCheckValue


@dataclass
class PerTeamSeedCheckPostImage(DataClassJSONMixin):
    h: PerTeamSeedCheckValuePostImage
    v: PerTeamSeedCheckVersion


@dataclass
class TeamApplicationKey(DataClassJSONMixin):
    application: TeamApplication
    key_generation: PerTeamKeyGeneration
    key: Bytes32


@dataclass
class ReaderKeyMask(DataClassJSONMixin):
    application: TeamApplication
    generation: PerTeamKeyGeneration
    mask: MaskB64


@dataclass
class PerTeamKey(DataClassJSONMixin):
    gen: PerTeamKeyGeneration
    seqno: Seqno
    sig_kid: KID
    enc_kid: KID


@dataclass
class TeamMember(DataClassJSONMixin):
    uid: UID
    role: TeamRole
    eldest_seqno: Seqno
    status: TeamMemberStatus


@dataclass
class LinkTriple(DataClassJSONMixin):
    seqno: Seqno
    seq_type: SeqType
    link_id: LinkID


@dataclass
class UpPointer(DataClassJSONMixin):
    our_seqno: Seqno
    parent_id: TeamID
    parent_seqno: Seqno
    deletion: bool


@dataclass
class DownPointer(DataClassJSONMixin):
    id: TeamID
    name_component: str
    is_deleted: bool


@dataclass
class Signer(DataClassJSONMixin):
    e: Seqno
    k: KID
    u: UID


@dataclass
class Audit(DataClassJSONMixin):
    time: Time
    mms: Seqno
    mcs: Seqno
    mmp: Seqno


@dataclass
class Probe(DataClassJSONMixin):
    i: int
    t: Seqno


@dataclass
class TeamInviteType__UNKNOWN:
    c: Literal[TeamInviteCategory.UNKNOWN]
    UNKNOWN: Optional[str]


@dataclass
class TeamInviteType__SBS:
    c: Literal[TeamInviteCategory.SBS]
    SBS: Optional[TeamInviteSocialNetwork]


TeamInviteType = Union[TeamInviteType__UNKNOWN, TeamInviteType__SBS]


@dataclass
class TeamGetLegacyTLFUpgrade(DataClassJSONMixin):
    encrypted_keyset: str
    team_generation: PerTeamKeyGeneration
    legacy_generation: int
    app_type: TeamApplication


@dataclass
class TeamLegacyTLFUpgradeChainInfo(DataClassJSONMixin):
    keyset_hash: TeamEncryptedKBFSKeysetHash
    team_generation: PerTeamKeyGeneration
    legacy_generation: int
    app_type: TeamApplication


@dataclass
class TeamNameLogPoint(DataClassJSONMixin):
    last_part: TeamNamePart
    seqno: Seqno


@dataclass
class TeamName(DataClassJSONMixin):
    parts: List[TeamNamePart]


@dataclass
class TeamCLKRResetUser(DataClassJSONMixin):
    uid: UID
    user_eldest: Seqno
    member_eldest: Seqno


@dataclass
class TeamResetUser(DataClassJSONMixin):
    username: str
    uid: UID
    eldest_seqno: Seqno
    is_delete: bool


@dataclass
class TeamChangeRow(DataClassJSONMixin):
    id: TeamID
    name: str
    key_rotated: bool
    membership_changed: bool
    latest_seqno: Seqno
    latest_hidden_seqno: Seqno
    implicit_team: bool
    misc: bool
    removed_reset_users: bool


@dataclass
class TeamExitRow(DataClassJSONMixin):
    id: TeamID


@dataclass
class TeamNewlyAddedRow(DataClassJSONMixin):
    id: TeamID
    name: str


@dataclass
class TeamInvitee(DataClassJSONMixin):
    invite_id: TeamInviteID
    uid: UID
    eldest_seqno: Seqno
    role: TeamRole


@dataclass
class TeamAccessRequest(DataClassJSONMixin):
    uid: UID
    eldest_seqno: Seqno


@dataclass
class SeitanKeyLabel__SMS:
    t: Literal[SeitanKeyLabelType.SMS]
    SMS: Optional[SeitanKeyLabelSms]


SeitanKeyLabel = Union[SeitanKeyLabel__SMS]


@dataclass
class TeamSeitanRequest(DataClassJSONMixin):
    invite_id: TeamInviteID
    uid: UID
    eldest_seqno: Seqno
    akey: SeitanAKey
    role: TeamRole
    ctime: int


@dataclass
class TeamKBFSKeyRefresher(DataClassJSONMixin):
    generation: int
    app_type: TeamApplication


@dataclass
class ImplicitRole(DataClassJSONMixin):
    role: TeamRole
    ancestor: TeamID


@dataclass
class TeamCreateResult(DataClassJSONMixin):
    team_id: TeamID
    chat_sent: bool
    creator_added: bool


@dataclass
class TeamSettings(DataClassJSONMixin):
    open: bool
    join_as: TeamRole


@dataclass
class TeamShowcase(DataClassJSONMixin):
    is_showcased: bool
    description: Optional[str]
    set_by_uid: Optional[UID]
    any_member_showcase: bool


@dataclass
class UserRolePair(DataClassJSONMixin):
    assertion_or_email: str
    role: TeamRole
    bot_settings: Optional[TeamBotSettings]


@dataclass
class ImplicitTeamConflictInfo(DataClassJSONMixin):
    generation: ConflictGeneration
    time: Time


@dataclass
class CryptKey(DataClassJSONMixin):
    key_generation: int
    key: Bytes32


@dataclass
class TLFQuery(DataClassJSONMixin):
    tlf_name: str
    identify_behavior: TLFIdentifyBehavior


@dataclass
class MerkleRootV2(DataClassJSONMixin):
    seqno: Seqno
    hash_meta: HashMeta


@dataclass
class SigChainLocation(DataClassJSONMixin):
    seqno: Seqno
    seq_type: SeqType


@dataclass
class Email(DataClassJSONMixin):
    email: EmailAddress
    is_verified: bool
    is_primary: bool
    visibility: IdentityVisibility
    last_verify_email_date: UnixTime


@dataclass
class UserSummary2(DataClassJSONMixin):
    uid: UID
    username: str
    thumbnail: str
    full_name: str
    is_follower: bool
    is_followee: bool


@dataclass
class InterestingPerson(DataClassJSONMixin):
    uid: UID
    username: str
    fullname: str


@dataclass
class APIUserKeybaseResult(DataClassJSONMixin):
    username: str
    uid: UID
    picture_url: Optional[str]
    full_name: Optional[str]
    raw_score: float
    stellar: Optional[str]
    is_followee: bool


@dataclass
class APIUserServiceResult(DataClassJSONMixin):
    service_name: APIUserServiceIDWithContact
    username: str
    picture_url: str
    bio: str
    location: str
    full_name: str
    confirmed: Optional[bool]


@dataclass
class APIUserServiceSummary(DataClassJSONMixin):
    service_name: APIUserServiceIDWithContact
    username: str


@dataclass
class ImpTofuQuery__PHONE:
    t: Literal[ImpTofuSearchType.PHONE]
    PHONE: Optional[PhoneNumber]


@dataclass
class ImpTofuQuery__EMAIL:
    t: Literal[ImpTofuSearchType.EMAIL]
    EMAIL: Optional[EmailAddress]


ImpTofuQuery = Union[ImpTofuQuery__PHONE, ImpTofuQuery__EMAIL]


@dataclass
class GetLockdownResponse(DataClassJSONMixin):
    history: List[LockdownHistory]
    status: bool


@dataclass
class BlockReference(DataClassJSONMixin):
    bid: BlockIdCombo
    nonce: BlockRefNonce
    charged_to: UserOrTeamID


@dataclass
class BlockIdCount(DataClassJSONMixin):
    id: BlockIdCombo
    live_count: int


@dataclass
class TeamIDAndName(DataClassJSONMixin):
    id: TeamID
    name: TeamName


@dataclass
class RevokedKey(DataClassJSONMixin):
    key: PublicKey
    time: KeybaseTime
    by: KID


@dataclass
class CurrentStatus(DataClassJSONMixin):
    configured: bool
    registered: bool
    logged_in: bool
    session_is_valid: bool
    user: Optional[User]


@dataclass
class ClientStatus(DataClassJSONMixin):
    details: ClientDetails
    connection_id: int
    notification_channels: NotificationChannels


@dataclass
class BootstrapStatus(DataClassJSONMixin):
    registered: bool
    logged_in: bool
    uid: UID
    username: str
    device_id: DeviceID
    device_name: str
    fullname: FullName
    user_reacjis: UserReacjis
    http_srv_info: Optional[HttpSrvInfo]


@dataclass
class Contact(DataClassJSONMixin):
    name: str
    components: List[ContactComponent]


@dataclass
class ProcessedContact(DataClassJSONMixin):
    contact_index: int
    contact_name: str
    component: ContactComponent
    resolved: bool
    uid: UID
    username: str
    full_name: str
    following: bool
    service_map: Dict[str, str]
    assertion: str
    display_name: str
    display_label: str


@dataclass
class DeviceDetail(DataClassJSONMixin):
    device: Device
    eldest: bool
    provisioner: Optional[Device]
    provisioned_at: Optional[Time]
    revoked_at: Optional[Time]
    revoked_by: KID
    revoked_by_device: Optional[Device]
    current_device: bool


@dataclass
class DeviceEkStatement(DataClassJSONMixin):
    current_device_ek_metadata: DeviceEkMetadata


@dataclass
class DeviceEk(DataClassJSONMixin):
    seed: Bytes32
    metadata: DeviceEkMetadata


@dataclass
class UserEkStatement(DataClassJSONMixin):
    current_user_ek_metadata: UserEkMetadata


@dataclass
class UserEkBoxed(DataClassJSONMixin):
    box: str
    device_ek_generation: EkGeneration
    metadata: UserEkMetadata


@dataclass
class UserEk(DataClassJSONMixin):
    seed: Bytes32
    metadata: UserEkMetadata


@dataclass
class UserEkReboxArg(DataClassJSONMixin):
    user_ek_box_metadata: UserEkBoxMetadata
    device_id: DeviceID
    device_ek_statement_sig: str


@dataclass
class TeamEkStatement(DataClassJSONMixin):
    current_team_ek_metadata: TeamEkMetadata


@dataclass
class TeamEkBoxed(DataClassJSONMixin):
    box: str
    user_ek_generation: EkGeneration
    metadata: TeamEkMetadata


@dataclass
class TeamEk(DataClassJSONMixin):
    seed: Bytes32
    metadata: TeamEkMetadata


@dataclass
class TeambotEkBoxed(DataClassJSONMixin):
    box: str
    metadata: TeambotEkMetadata


@dataclass
class TeambotEk(DataClassJSONMixin):
    seed: Bytes32
    metadata: TeambotEkMetadata


@dataclass
class GitLocalMetadataVersioned__V1:
    version: Literal[GitLocalMetadataVersion.V1]
    V1: Optional[GitLocalMetadataV1]


GitLocalMetadataVersioned = Union[GitLocalMetadataVersioned__V1]


@dataclass
class GitRefMetadata(DataClassJSONMixin):
    ref_name: str
    commits: List[GitCommit]
    more_commits_available: bool
    is_delete: bool


@dataclass
class HomeScreenTodoExt__VERIFY_ALL_EMAIL:
    t: Literal[HomeScreenTodoType.VERIFY_ALL_EMAIL]
    VERIFY_ALL_EMAIL: Optional[VerifyAllEmailTodoExt]


HomeScreenTodoExt = Union[HomeScreenTodoExt__VERIFY_ALL_EMAIL]


@dataclass
class Identify3Row(DataClassJSONMixin):
    gui_id: Identify3GUIID
    key: str
    value: str
    priority: int
    site_url: str
    site_icon: List[SizedImage]
    site_icon_full: List[SizedImage]
    proof_url: str
    sig_id: SigID
    ctime: Time
    state: Identify3RowState
    metas: List[Identify3RowMeta]
    color: Identify3RowColor
    kid: Optional[KID]


@dataclass
class IdentifyOutcome(DataClassJSONMixin):
    username: str
    status: Optional[Status]
    warnings: List[str]
    track_used: Optional[TrackSummary]
    track_status: TrackStatus
    num_track_failures: int
    num_track_changes: int
    num_proof_failures: int
    num_revoked: int
    num_proof_successes: int
    revoked: List[TrackDiff]
    track_options: TrackOptions
    for_pgp_pull: bool
    reason: IdentifyReason


@dataclass
class IdentifyRow(DataClassJSONMixin):
    row_id: int
    proof: RemoteProof
    track_diff: Optional[TrackDiff]


@dataclass
class IdentifyKey(DataClassJSONMixin):
    pgp_fingerprint: bytes
    kid: KID
    track_diff: Optional[TrackDiff]
    breaks_tracking: bool
    sig_id: SigID


@dataclass
class RevokedProof(DataClassJSONMixin):
    proof: RemoteProof
    diff: TrackDiff
    snoozed: bool


@dataclass
class CheckResult(DataClassJSONMixin):
    proof_result: ProofResult
    time: Time
    freshness: CheckResultFreshness


@dataclass
class UserCard(DataClassJSONMixin):
    following: int
    followers: int
    uid: UID
    full_name: str
    location: str
    bio: str
    website: str
    twitter: str
    you_follow_them: bool
    they_follow_you: bool
    team_showcase: List[UserTeamShowcase]
    registered_for_airdrop: bool
    blocked: bool


@dataclass
class ServiceStatus(DataClassJSONMixin):
    version: str
    label: str
    pid: str
    last_exit_status: str
    bundle_version: str
    install_status: InstallStatus
    install_action: InstallAction
    status: Status


@dataclass
class FuseStatus(DataClassJSONMixin):
    version: str
    bundle_version: str
    kext_id: str
    path: str
    kext_started: bool
    install_status: InstallStatus
    install_action: InstallAction
    mount_infos: List[FuseMountInfo]
    status: Status


@dataclass
class ComponentResult(DataClassJSONMixin):
    name: str
    status: Status
    exit_code: int


@dataclass
class FSFolderWriterEditHistory(DataClassJSONMixin):
    writer_name: str
    edits: List[FSFolderWriterEdit]
    deletes: List[FSFolderWriterEdit]


@dataclass
class FolderSyncStatus(DataClassJSONMixin):
    local_disk_bytes_available: int
    local_disk_bytes_total: int
    prefetch_status: PrefetchStatus
    prefetch_progress: PrefetchProgress
    stored_bytes_total: int
    out_of_sync_space: bool


@dataclass
class MerkleRootAndTime(DataClassJSONMixin):
    root: MerkleRootV2
    update_time: Time
    fetch_time: Time


@dataclass
class MetadataResponse(DataClassJSONMixin):
    folder_id: str
    md_blocks: List[MDBlock]


@dataclass
class BadgeState(DataClassJSONMixin):
    new_tlfs: int
    rekeys_needed: int
    new_followers: int
    inbox_vers: int
    home_todo_items: int
    unverified_emails: int
    unverified_phones: int
    new_devices: List[DeviceID]
    revoked_devices: List[DeviceID]
    conversations: List[BadgeConversationInfo]
    new_git_repo_global_unique_i_ds: List[str]
    new_team_names: List[str]
    deleted_teams: List[DeletedTeamInfo]
    new_team_access_requests: List[str]
    teams_with_reset_users: List[TeamMemberOutReset]
    unread_wallet_accounts: List[WalletAccountInfo]
    reset_state: ResetState


@dataclass
class RuntimeStats(DataClassJSONMixin):
    process_stats: List[ProcessRuntimeStats]
    db_stats: List[DbStats]
    conv_loader_active: bool
    selective_sync_active: bool


@dataclass
class GUIEntryArg(DataClassJSONMixin):
    window_title: str
    prompt: str
    username: str
    submit_label: str
    cancel_label: str
    retry_label: str
    type: PassphraseType
    features: GUIEntryFeatures


@dataclass
class PGPSigVerification(DataClassJSONMixin):
    is_signed: bool
    verified: bool
    signer: User
    sign_key: PublicKey


@dataclass
class Process(DataClassJSONMixin):
    pid: str
    command: str
    file_descriptors: List[FileDescriptor]


@dataclass
class ExternalServiceConfig(DataClassJSONMixin):
    schema_version: int
    display: Optional[ServiceDisplayConfig]
    config: Optional[ParamProofServiceConfig]


@dataclass
class ProblemTLF(DataClassJSONMixin):
    tlf: TLF
    score: int
    solution_kids: List[KID]


@dataclass
class RevokeWarning(DataClassJSONMixin):
    endangered_tl_fs: List[TLF]


@dataclass
class ResetLink(DataClassJSONMixin):
    ctime: UnixTime
    merkle_root: ResetMerkleRoot
    prev: ResetPrev
    reset_seqno: Seqno
    type: ResetType
    uid: UID


@dataclass
class ResetSummary(DataClassJSONMixin):
    ctime: UnixTime
    merkle_root: ResetMerkleRoot
    reset_seqno: Seqno
    eldest_seqno: Seqno
    type: ResetType


@dataclass
class SaltpackEncryptedMessageInfo(DataClassJSONMixin):
    devices: List[Device]
    num_anon_receivers: int
    receiver_is_anon: bool
    sender: SaltpackSender


@dataclass
class KBFSArchivedPath(DataClassJSONMixin):
    path: str
    archived_param: KBFSArchivedParam
    identify_behavior: Optional[TLFIdentifyBehavior]


@dataclass
class Dirent(DataClassJSONMixin):
    time: Time
    size: int
    name: str
    dirent_type: DirentType
    last_writer_unverified: User
    writable: bool
    prefetch_status: PrefetchStatus
    prefetch_progress: PrefetchProgress


@dataclass
class SimpleFSStats(DataClassJSONMixin):
    process_stats: ProcessRuntimeStats
    block_cache_db_stats: List[str]
    sync_cache_db_stats: List[str]
    runtime_db_stats: List[DbStats]


@dataclass
class TeambotKeyBoxed(DataClassJSONMixin):
    box: str
    metadata: TeambotKeyMetadata


@dataclass
class TeambotKey(DataClassJSONMixin):
    seed: Bytes32
    metadata: TeambotKeyMetadata


@dataclass
class PerTeamKeyAndCheck(DataClassJSONMixin):
    ptk: PerTeamKey
    check: PerTeamSeedCheckPostImage


@dataclass
class PerTeamKeySeedItem(DataClassJSONMixin):
    seed: PerTeamKeySeed
    generation: PerTeamKeyGeneration
    seqno: Seqno
    check: Optional[PerTeamSeedCheck]


@dataclass
class TeamMembers(DataClassJSONMixin):
    owners: List[UserVersion]
    admins: List[UserVersion]
    writers: List[UserVersion]
    readers: List[UserVersion]
    bots: List[UserVersion]
    restricted_bots: List[UserVersion]


@dataclass
class TeamMemberDetails(DataClassJSONMixin):
    uv: UserVersion
    username: str
    full_name: FullName
    needs_puk: bool
    status: TeamMemberStatus


@dataclass
class TeamChangeReq(DataClassJSONMixin):
    owners: List[UserVersion]
    admins: List[UserVersion]
    writers: List[UserVersion]
    readers: List[UserVersion]
    bots: List[UserVersion]
    restricted_bots: Dict[str, TeamBotSettings]
    none: List[UserVersion]
    completed_invites: Dict[str, UserVersionPercentForm]


@dataclass
class TeamPlusApplicationKeys(DataClassJSONMixin):
    id: TeamID
    name: str
    implicit: bool
    public: bool
    application: TeamApplication
    writers: List[UserVersion]
    only_readers: List[UserVersion]
    only_restricted_bots: List[UserVersion]
    application_keys: List[TeamApplicationKey]


@dataclass
class LinkTripleAndTime(DataClassJSONMixin):
    triple: LinkTriple
    time: Time


@dataclass
class FastTeamSigChainState(DataClassJSONMixin):
    id: TeamID
    public: bool
    root_ancestor: TeamName
    name_depth: int
    last: Optional[LinkTriple]
    per_team_keys: Dict[str, PerTeamKey]
    per_team_key_seeds_verified: Dict[str, PerTeamKeySeed]
    down_pointers: Dict[str, DownPointer]
    last_up_pointer: Optional[UpPointer]
    per_team_key_c_time: UnixTime
    link_i_ds: Dict[str, LinkID]
    merkle_info: Dict[str, MerkleRootV2]


@dataclass
class AuditHistory(DataClassJSONMixin):
    id: TeamID
    public: bool
    prior_merkle_seqno: Seqno
    version: AuditVersion
    audits: List[Audit]
    pre_probes: Dict[str, Probe]
    post_probes: Dict[str, Probe]
    tails: Dict[str, LinkID]
    skip_until: Time


@dataclass
class TeamInvite(DataClassJSONMixin):
    role: TeamRole
    id: TeamInviteID
    type: TeamInviteType
    name: TeamInviteName
    inviter: UserVersion


@dataclass
class AnnotatedTeamInvite(DataClassJSONMixin):
    role: TeamRole
    id: TeamInviteID
    type: TeamInviteType
    name: TeamInviteName
    uv: UserVersion
    inviter: UserVersion
    inviter_username: str
    team_name: str
    status: TeamMemberStatus


@dataclass
class SubteamLogPoint(DataClassJSONMixin):
    name: TeamName
    seqno: Seqno


@dataclass
class TeamCLKRMsg(DataClassJSONMixin):
    team_id: TeamID
    generation: PerTeamKeyGeneration
    score: int
    reset_users: List[TeamCLKRResetUser]


@dataclass
class TeamMemberOutFromReset(DataClassJSONMixin):
    team_name: str
    reset_user: TeamResetUser


@dataclass
class TeamSBSMsg(DataClassJSONMixin):
    team_id: TeamID
    score: int
    invitees: List[TeamInvitee]


@dataclass
class TeamOpenReqMsg(DataClassJSONMixin):
    team_id: TeamID
    tars: List[TeamAccessRequest]


@dataclass
class SeitanKeyAndLabelVersion1(DataClassJSONMixin):
    i: SeitanIKey
    l: SeitanKeyLabel


@dataclass
class SeitanKeyAndLabelVersion2(DataClassJSONMixin):
    k: SeitanPubKey
    l: SeitanKeyLabel


@dataclass
class TeamSeitanMsg(DataClassJSONMixin):
    team_id: TeamID
    seitans: List[TeamSeitanRequest]


@dataclass
class TeamOpenSweepMsg(DataClassJSONMixin):
    team_id: TeamID
    reset_users: List[TeamCLKRResetUser]


@dataclass
class TeamRefreshers(DataClassJSONMixin):
    need_key_generation: PerTeamKeyGeneration
    need_applications_at_generations: Dict[str, List[TeamApplication]]
    need_applications_at_generations_with_kbfs: Dict[str, List[TeamApplication]]
    want_members: List[UserVersion]
    want_members_role: TeamRole
    need_kbfs_key_generation: TeamKBFSKeyRefresher


@dataclass
class FastTeamLoadArg(DataClassJSONMixin):
    id: TeamID
    public: bool
    assert_team_name: Optional[TeamName]
    applications: List[TeamApplication]
    key_generations_needed: List[PerTeamKeyGeneration]
    need_latest_key: bool
    force_refresh: bool


@dataclass
class FastTeamLoadRes(DataClassJSONMixin):
    name: TeamName
    application_keys: List[TeamApplicationKey]


@dataclass
class MemberInfo(DataClassJSONMixin):
    uid: UID
    team_id: TeamID
    fq_name: str
    is_implicit_team: bool
    is_open_team: bool
    role: TeamRole
    implicit: Optional[ImplicitRole]
    member_count: int
    allow_profile_promote: bool
    is_member_showcased: bool


@dataclass
class AnnotatedMemberInfo(DataClassJSONMixin):
    uid: UID
    team_id: TeamID
    username: str
    full_name: str
    fq_name: str
    is_implicit_team: bool
    implicit_team_display_name: str
    is_open_team: bool
    role: TeamRole
    implicit: Optional[ImplicitRole]
    needs_puk: bool
    member_count: int
    member_eldest_seqno: Seqno
    allow_profile_promote: bool
    is_member_showcased: bool
    status: TeamMemberStatus


@dataclass
class TeamAddMemberResult(DataClassJSONMixin):
    invited: bool
    user: Optional[User]
    email_sent: bool
    chat_sending: bool


@dataclass
class TeamTreeEntry(DataClassJSONMixin):
    name: TeamName
    admin: bool


@dataclass
class SubteamListEntry(DataClassJSONMixin):
    name: TeamName
    member_count: int


@dataclass
class TeamAndMemberShowcase(DataClassJSONMixin):
    team_showcase: TeamShowcase
    is_member_showcased: bool


@dataclass
class ImplicitTeamUserSet(DataClassJSONMixin):
    keybase_users: List[str]
    unresolved_users: List[SocialAssertion]


@dataclass
class TeamProfileAddEntry(DataClassJSONMixin):
    team_name: TeamName
    open: bool
    disabled_reason: str


@dataclass
class MerkleTreeLocation(DataClassJSONMixin):
    leaf: UserOrTeamID
    loc: SigChainLocation


@dataclass
class SignatureMetadata(DataClassJSONMixin):
    signing_kid: KID
    prev_merkle_root_signed: MerkleRootV2
    first_appeared_unverified: Seqno
    time: Time
    sig_chain_location: SigChainLocation


@dataclass
class Proofs(DataClassJSONMixin):
    social: List[TrackProof]
    web: List[WebProof]
    public_keys: List[PublicKey]


@dataclass
class UserSettings(DataClassJSONMixin):
    emails: List[Email]
    phone_numbers: List[UserPhoneNumber]


@dataclass
class UserSummary2Set(DataClassJSONMixin):
    users: List[UserSummary2]
    time: Time
    version: int


@dataclass
class ProofSuggestion(DataClassJSONMixin):
    key: str
    below_fold: bool
    profile_text: str
    profile_icon: List[SizedImage]
    picker_text: str
    picker_subtext: str
    picker_icon: List[SizedImage]
    metas: List[Identify3RowMeta]


@dataclass
class NextMerkleRootRes(DataClassJSONMixin):
    res: Optional[MerkleRootV2]


@dataclass
class BlockReferenceCount(DataClassJSONMixin):
    ref: BlockReference
    live_count: int


@dataclass
class ReferenceCountRes(DataClassJSONMixin):
    counts: List[BlockIdCount]


@dataclass
class UserPlusKeys(DataClassJSONMixin):
    uid: UID
    username: str
    eldest_seqno: Seqno
    status: StatusCode
    device_keys: List[PublicKey]
    revoked_device_keys: List[RevokedKey]
    pgp_key_count: int
    uvv: UserVersionVector
    deleted_device_keys: List[PublicKey]
    per_user_keys: List[PerUserKey]
    resets: List[ResetSummary]


@dataclass
class ExtendedStatus(DataClassJSONMixin):
    standalone: bool
    passphrase_stream_cached: bool
    tsec_cached: bool
    device_sig_key_cached: bool
    device_enc_key_cached: bool
    paper_sig_key_cached: bool
    paper_enc_key_cached: bool
    stored_secret: bool
    secret_prompt_skip: bool
    remember_passphrase: bool
    device: Optional[Device]
    device_err: Optional[LoadDeviceErr]
    log_dir: str
    session: Optional[SessionStatus]
    default_username: str
    provisioned_usernames: List[str]
    configured_accounts: List[ConfiguredAccount]
    clients: List[ClientStatus]
    device_ek_names: List[str]
    platform_info: PlatformInfo
    default_device_id: DeviceID
    local_db_stats: List[str]
    local_chat_db_stats: List[str]
    local_block_cache_db_stats: List[str]
    local_sync_cache_db_stats: List[str]
    cache_dir_size_info: List[DirSizeInfo]
    ui_router_mapping: Dict[str, int]


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


@dataclass
class GitLocalMetadata(DataClassJSONMixin):
    repo_name: GitRepoName
    refs: List[GitRefMetadata]
    push_type: GitPushType
    previous_repo_name: GitRepoName


@dataclass
class HomeScreenItemDataExt__TODO:
    t: Literal[HomeScreenItemType.TODO]
    TODO: Optional[HomeScreenTodoExt]


HomeScreenItemDataExt = Union[HomeScreenItemDataExt__TODO]


@dataclass
class Identity(DataClassJSONMixin):
    status: Optional[Status]
    when_last_tracked: Time
    proofs: List[IdentifyRow]
    cryptocurrency: List[Cryptocurrency]
    revoked: List[TrackDiff]
    revoked_details: List[RevokedProof]
    breaks_tracking: bool


@dataclass
class LinkCheckResult(DataClassJSONMixin):
    proof_id: int
    proof_result: ProofResult
    snoozed_result: ProofResult
    tor_warning: bool
    tmp_track_expire_time: Time
    cached: Optional[CheckResult]
    diff: Optional[TrackDiff]
    remote_diff: Optional[TrackDiff]
    hint: Optional[SigHint]
    breaks_tracking: bool


@dataclass
class ServicesStatus(DataClassJSONMixin):
    service: List[ServiceStatus]
    kbfs: List[ServiceStatus]
    updater: List[ServiceStatus]


@dataclass
class InstallResult(DataClassJSONMixin):
    component_results: List[ComponentResult]
    status: Status
    fatal: bool


@dataclass
class UninstallResult(DataClassJSONMixin):
    component_results: List[ComponentResult]
    status: Status


@dataclass
class ProblemSet(DataClassJSONMixin):
    user: User
    kid: KID
    tlfs: List[ProblemTLF]


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


@dataclass
class DirentWithRevision(DataClassJSONMixin):
    entry: Dirent
    revision: KBFSRevision


@dataclass
class SimpleFSListResult(DataClassJSONMixin):
    entries: List[Dirent]
    progress: Progress


@dataclass
class FolderSyncConfigAndStatus(DataClassJSONMixin):
    config: FolderSyncConfig
    status: FolderSyncStatus


@dataclass
class TeamMembersDetails(DataClassJSONMixin):
    owners: List[TeamMemberDetails]
    admins: List[TeamMemberDetails]
    writers: List[TeamMemberDetails]
    readers: List[TeamMemberDetails]
    bots: List[TeamMemberDetails]
    restricted_bots: List[TeamMemberDetails]


@dataclass
class FastTeamData(DataClassJSONMixin):
    frozen: bool
    subversion: int
    tombstoned: bool
    name: TeamName
    chain: FastTeamSigChainState
    per_team_key_seeds_unverified: Dict[str, PerTeamKeySeed]
    max_continuous_ptk_generation: PerTeamKeyGeneration
    seed_checks: Dict[str, PerTeamSeedCheck]
    latest_key_generation: PerTeamKeyGeneration
    reader_key_masks: Dict[str, Dict[str, MaskB64]]
    latest_seqno_hint: Seqno
    cached_at: Time
    loaded_latest: bool


@dataclass
class HiddenTeamChainRatchetSet(DataClassJSONMixin):
    ratchets: Dict[str, LinkTripleAndTime]


@dataclass
class HiddenTeamChainLink(DataClassJSONMixin):
    m: MerkleRootV2
    p: LinkTriple
    s: Signer
    k: Dict[str, PerTeamKeyAndCheck]


@dataclass
class UserLogPoint(DataClassJSONMixin):
    role: TeamRole
    sig_meta: SignatureMetadata


@dataclass
class SeitanKeyAndLabel__V1:
    v: Literal[SeitanKeyAndLabelVersion.V1]
    V1: Optional[SeitanKeyAndLabelVersion1]


@dataclass
class SeitanKeyAndLabel__V2:
    v: Literal[SeitanKeyAndLabelVersion.V2]
    V2: Optional[SeitanKeyAndLabelVersion2]


SeitanKeyAndLabel = Union[SeitanKeyAndLabel__V1, SeitanKeyAndLabel__V2]


@dataclass
class LoadTeamArg(DataClassJSONMixin):
    id: TeamID
    name: str
    public: bool
    need_admin: bool
    refresh_uid_mapper: bool
    refreshers: TeamRefreshers
    force_full_reload: bool
    force_repoll: bool
    stale_ok: bool
    allow_name_lookup_burst_cache: bool
    skip_audit: bool
    skip_need_hidden_rotate_check: bool


@dataclass
class TeamList(DataClassJSONMixin):
    teams: List[MemberInfo]


@dataclass
class AnnotatedTeamList(DataClassJSONMixin):
    teams: List[AnnotatedMemberInfo]
    annotated_active_invites: Dict[str, AnnotatedTeamInvite]


@dataclass
class TeamTreeResult(DataClassJSONMixin):
    entries: List[TeamTreeEntry]


@dataclass
class SubteamListResult(DataClassJSONMixin):
    entries: List[SubteamListEntry]


@dataclass
class ImplicitTeamDisplayName(DataClassJSONMixin):
    is_public: bool
    writers: ImplicitTeamUserSet
    readers: ImplicitTeamUserSet
    conflict_info: Optional[ImplicitTeamConflictInfo]


@dataclass
class PublicKeyV2Base(DataClassJSONMixin):
    kid: KID
    is_sibkey: bool
    is_eldest: bool
    c_time: Time
    e_time: Time
    provisioning: SignatureMetadata
    revocation: Optional[SignatureMetadata]


@dataclass
class UserSummary(DataClassJSONMixin):
    uid: UID
    username: str
    thumbnail: str
    id_version: int
    full_name: str
    bio: str
    proofs: Proofs
    sig_id_display: str
    track_time: Time


@dataclass
class ProofSuggestionsRes(DataClassJSONMixin):
    suggestions: List[ProofSuggestion]
    show_more: bool


@dataclass
class APIUserSearchResult(DataClassJSONMixin):
    score: float
    keybase: Optional[APIUserKeybaseResult]
    service: Optional[APIUserServiceResult]
    contact: Optional[ProcessedContact]
    imptofu: Optional[ImpTofuSearchResult]
    services_summary: Dict[str, APIUserServiceSummary]
    raw_score: float


@dataclass
class NonUserDetails(DataClassJSONMixin):
    is_non_user: bool
    assertion_value: str
    assertion_key: str
    description: str
    contact: Optional[ProcessedContact]
    service: Optional[APIUserServiceResult]
    site_icon: List[SizedImage]
    site_icon_full: List[SizedImage]


@dataclass
class DowngradeReferenceRes(DataClassJSONMixin):
    completed: List[BlockReferenceCount]
    failed: BlockReference


@dataclass
class UserPlusAllKeys(DataClassJSONMixin):
    base: UserPlusKeys
    pgp_keys: List[PublicKey]
    remote_tracks: List[RemoteTrack]


@dataclass
class FullStatus(DataClassJSONMixin):
    username: str
    config_path: str
    cur_status: CurrentStatus
    ext_status: ExtendedStatus
    client: KbClientStatus
    service: KbServiceStatus
    kbfs: KBFSStatus
    desktop: DesktopStatus
    updater: UpdaterStatus
    start: StartStatus
    git: GitStatus


@dataclass
class FolderNormalView(DataClassJSONMixin):
    resolving_conflict: bool
    stuck_in_conflict: bool
    local_views: List[Path]


@dataclass
class FolderConflictManualResolvingLocalView(DataClassJSONMixin):
    normal_view: Path


@dataclass
class GitRepoInfo(DataClassJSONMixin):
    folder: FolderHandle
    repo_id: RepoID
    local_metadata: GitLocalMetadata
    server_metadata: GitServerMetadata
    repo_url: str
    global_unique_id: str
    can_delete: bool
    team_repo_settings: Optional[GitTeamRepoSettings]


@dataclass
class HomeScreenPeopleNotificationFollowed(DataClassJSONMixin):
    follow_time: Time
    followed_back: bool
    user: UserSummary


@dataclass
class IdentifyProofBreak(DataClassJSONMixin):
    remote_proof: RemoteProof
    lcr: LinkCheckResult


@dataclass
class ProblemSetDevices(DataClassJSONMixin):
    problem_set: ProblemSet
    devices: List[Device]


@dataclass
class ListArgs(DataClassJSONMixin):
    op_id: OpID
    path: Path
    filter: ListFilter


@dataclass
class ListToDepthArgs(DataClassJSONMixin):
    op_id: OpID
    path: Path
    filter: ListFilter
    depth: int


@dataclass
class RemoveArgs(DataClassJSONMixin):
    op_id: OpID
    path: Path
    recursive: bool


@dataclass
class ReadArgs(DataClassJSONMixin):
    op_id: OpID
    path: Path
    offset: int
    size: int


@dataclass
class WriteArgs(DataClassJSONMixin):
    op_id: OpID
    path: Path
    offset: int


@dataclass
class CopyArgs(DataClassJSONMixin):
    op_id: OpID
    src: Path
    dest: Path


@dataclass
class MoveArgs(DataClassJSONMixin):
    op_id: OpID
    src: Path
    dest: Path


@dataclass
class GetRevisionsArgs(DataClassJSONMixin):
    op_id: OpID
    path: Path
    span_type: RevisionSpanType


@dataclass
class GetRevisionsResult(DataClassJSONMixin):
    revisions: List[DirentWithRevision]
    progress: Progress


@dataclass
class TeamDetails(DataClassJSONMixin):
    members: TeamMembersDetails
    key_generation: PerTeamKeyGeneration
    annotated_active_invites: Dict[str, AnnotatedTeamInvite]
    settings: TeamSettings
    showcase: TeamShowcase


@dataclass
class HiddenTeamChain(DataClassJSONMixin):
    id: TeamID
    subversion: int
    public: bool
    frozen: bool
    tombstoned: bool
    last: Seqno
    latest_seqno_hint: Seqno
    last_per_team_keys: Dict[str, Seqno]
    outer: Dict[str, LinkID]
    inner: Dict[str, HiddenTeamChainLink]
    reader_per_team_keys: Dict[str, Seqno]
    ratchet_set: HiddenTeamChainRatchetSet
    cached_at: Time
    need_rotate: bool
    merkle_roots: Dict[str, MerkleRootV2]


@dataclass
class TeamSigChainState(DataClassJSONMixin):
    reader: UserVersion
    id: TeamID
    implicit: bool
    public: bool
    root_ancestor: TeamName
    name_depth: int
    name_log: List[TeamNameLogPoint]
    last_seqno: Seqno
    last_link_id: LinkID
    last_high_seqno: Seqno
    last_high_link_id: LinkID
    parent_id: Optional[TeamID]
    user_log: Dict[str, List[UserLogPoint]]
    subteam_log: Dict[str, List[SubteamLogPoint]]
    per_team_keys: Dict[str, PerTeamKey]
    max_per_team_key_generation: PerTeamKeyGeneration
    per_team_key_c_time: UnixTime
    link_i_ds: Dict[str, LinkID]
    stubbed_links: Dict[str, bool]
    active_invites: Dict[str, TeamInvite]
    obsolete_invites: Dict[str, TeamInvite]
    open: bool
    open_team_join_as: TeamRole
    bots: Dict[str, TeamBotSettings]
    tlf_i_ds: List[TLFID]
    tlf_legacy_upgrade: Dict[str, TeamLegacyTLFUpgradeChainInfo]
    head_merkle: Optional[MerkleRootV2]
    merkle_roots: Dict[str, MerkleRootV2]


@dataclass
class LookupImplicitTeamRes(DataClassJSONMixin):
    team_id: TeamID
    name: TeamName
    display_name: ImplicitTeamDisplayName
    tlf_id: TLFID


@dataclass
class PublicKeyV2NaCl(DataClassJSONMixin):
    base: PublicKeyV2Base
    parent: Optional[KID]
    device_id: DeviceID
    device_description: str
    device_type: str


@dataclass
class PublicKeyV2PGPSummary(DataClassJSONMixin):
    base: PublicKeyV2Base
    fingerprint: PGPFingerprint
    identities: List[PGPIdentity]


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


@dataclass
class HomeScreenPeopleNotificationFollowedMulti(DataClassJSONMixin):
    followers: List[HomeScreenPeopleNotificationFollowed]
    num_others: int


@dataclass
class IdentifyTrackBreaks(DataClassJSONMixin):
    keys: List[IdentifyKey]
    proofs: List[IdentifyProofBreak]


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


@dataclass
class TeamData(DataClassJSONMixin):
    v: int
    frozen: bool
    tombstoned: bool
    secretless: bool
    name: TeamName
    chain: TeamSigChainState
    per_team_key_seeds_unverified: Dict[str, PerTeamKeySeedItem]
    reader_key_masks: Dict[str, Dict[str, MaskB64]]
    latest_seqno_hint: Seqno
    cached_at: Time
    tlf_crypt_keys: Dict[str, List[CryptKey]]


@dataclass
class TeamDebugRes(DataClassJSONMixin):
    chain: TeamSigChainState


@dataclass
class PublicKeyV2__NACL:
    keyType: Literal[KeyType.NACL]
    NACL: Optional[PublicKeyV2NaCl]


@dataclass
class PublicKeyV2__PGP:
    keyType: Literal[KeyType.PGP]
    PGP: Optional[PublicKeyV2PGPSummary]


PublicKeyV2 = Union[PublicKeyV2__NACL, PublicKeyV2__PGP]


@dataclass
class UserPlusKeysV2(DataClassJSONMixin):
    uid: UID
    username: str
    eldest_seqno: Seqno
    status: StatusCode
    per_user_keys: List[PerUserKey]
    device_keys: Dict[str, PublicKeyV2NaCl]
    pgp_keys: Dict[str, PublicKeyV2PGPSummary]
    stellar_account_id: Optional[str]
    remote_tracks: Dict[str, RemoteTrack]
    reset: Optional[ResetSummary]
    unstubbed: bool


@dataclass
class UPKLiteV1(DataClassJSONMixin):
    uid: UID
    username: str
    eldest_seqno: Seqno
    status: StatusCode
    device_keys: Dict[str, PublicKeyV2NaCl]
    reset: Optional[ResetSummary]


@dataclass
class Folder(DataClassJSONMixin):
    name: str
    private: bool
    created: bool
    folder_type: FolderType
    team_id: Optional[TeamID]
    reset_members: List[User]
    mtime: Optional[Time]
    conflict_state: Optional[ConflictState]
    sync_config: Optional[FolderSyncConfig]


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


@dataclass
class Identify2Res(DataClassJSONMixin):
    upk: UserPlusKeys
    identified_at: Time
    track_breaks: Optional[IdentifyTrackBreaks]


@dataclass
class IdentifyLiteRes(DataClassJSONMixin):
    ul: UserOrTeamLite
    track_breaks: Optional[IdentifyTrackBreaks]


@dataclass
class ResolveIdentifyImplicitTeamRes(DataClassJSONMixin):
    display_name: str
    team_id: TeamID
    writers: List[UserVersion]
    track_breaks: Dict[str, IdentifyTrackBreaks]
    folder_id: TLFID


@dataclass
class TLFIdentifyFailure(DataClassJSONMixin):
    user: User
    breaks: Optional[IdentifyTrackBreaks]


@dataclass
class UserPlusKeysV2AllIncarnations(DataClassJSONMixin):
    current: UserPlusKeysV2
    past_incarnations: List[UserPlusKeysV2]
    uvv: UserVersionVector
    seqno_link_i_ds: Dict[str, LinkID]
    minor_version: UPK2MinorVersion
    stale: bool


@dataclass
class UPKLiteV1AllIncarnations(DataClassJSONMixin):
    current: UPKLiteV1
    past_incarnations: List[UPKLiteV1]
    seqno_link_i_ds: Dict[str, LinkID]
    minor_version: UPKLiteMinorVersion


@dataclass
class FavoritesResult(DataClassJSONMixin):
    favorite_folders: List[Folder]
    ignored_folders: List[Folder]
    new_folders: List[Folder]


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


@dataclass
class Identify2ResUPK2(DataClassJSONMixin):
    upk: UserPlusKeysV2AllIncarnations
    identified_at: Time
    track_breaks: Optional[IdentifyTrackBreaks]


@dataclass
class FSEditListRequest(DataClassJSONMixin):
    folder: Folder
    request_id: int


@dataclass
class FSFolderEditHistory(DataClassJSONMixin):
    folder: Folder
    server_time: Time
    history: List[FSFolderWriterEditHistory]


@dataclass
class FolderSyncConfigAndStatusWithFolder(DataClassJSONMixin):
    folder: Folder
    config: FolderSyncConfig
    status: FolderSyncStatus


@dataclass
class TLFBreak(DataClassJSONMixin):
    breaks: List[TLFIdentifyFailure]


@dataclass
class UPAKVersioned__V1:
    v: Literal[UPAKVersion.V1]
    V1: Optional[UserPlusAllKeys]


@dataclass
class UPAKVersioned__V2:
    v: Literal[UPAKVersion.V2]
    V2: Optional[UserPlusKeysV2AllIncarnations]


UPAKVersioned = Union[UPAKVersioned__V1, UPAKVersioned__V2]


@dataclass
class HomeScreenItem(DataClassJSONMixin):
    badged: bool
    data: HomeScreenItemData
    data_ext: HomeScreenItemDataExt


@dataclass
class SyncConfigAndStatusRes(DataClassJSONMixin):
    folders: List[FolderSyncConfigAndStatusWithFolder]
    overall_status: FolderSyncStatus


@dataclass
class CanonicalTLFNameAndIDWithBreaks(DataClassJSONMixin):
    tlf_id: TLFID
    canonical_name: CanonicalTlfName
    breaks: TLFBreak


@dataclass
class HomeScreen(DataClassJSONMixin):
    last_viewed: Time
    version: int
    visits: int
    items: List[HomeScreenItem]
    follow_suggestions: List[HomeUserSummary]
    announcements_version: int


@dataclass
class GetTLFCryptKeysRes(DataClassJSONMixin):
    name_id_breaks: CanonicalTLFNameAndIDWithBreaks
    crypt_keys: List[CryptKey]
