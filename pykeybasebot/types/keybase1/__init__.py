"""keybase.1

Auto-generated to Python types by avdl-compiler v1.4.8 (https://github.com/keybase/node-avdl-compiler)
Input files:
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/account.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/airdrop.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/apiserver.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/appstate.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/audit.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/avatars.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/backend_common.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/badger.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/block.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/bot.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/btc.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/common.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/config.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/constants.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/contacts.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/crypto.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/cryptocurrency.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/ctl.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/debugging.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/delegate_ui_ctl.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/device.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/emails.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/ephemeral.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/favorite.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/featured_bot.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/fs.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/git.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/gpg_common.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/gpg_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/gregor.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/gregor_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/home.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/home_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/identify.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/identify3.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/identify3_common.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/identify3_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/identify_common.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/identify_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/implicit_team_migration.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/incoming-share.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/install.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/invite_friends.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/kbfs.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/kbfs_common.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/kbfs_git.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/kbfsmount.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/kex2provisionee.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/kex2provisionee2.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/kex2provisioner.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/kvstore.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/log.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/log_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/login.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/login_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/logsend.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/merkle.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/merkle_store.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/metadata.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/metadata_update.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/network_stats.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_app.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_audit.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_badges.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_can_user_perform.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_ctl.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_device_clone.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_email.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_ephemeral.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_favorites.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_featuredbots.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_fs.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_fs_request.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_invite_friends.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_keyfamily.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_paperkey.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_pgp.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_phone.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_runtimestats.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_saltpack.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_service.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_session.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_team.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_teambot.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_tracking.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/notify_users.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/os.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/paperprovision.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/passphrase_common.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/pgp.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/pgp_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/phone_numbers.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/pprof.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/process.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/prove.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/prove_common.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/prove_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/provision_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/quota.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/reachability.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/rekey.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/rekey_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/reset.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/revoke.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/saltpack.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/saltpack_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/scanproofs.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/secret_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/secretkeys.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/selfprovision.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/session.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/signup.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/sigs.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/simple_fs.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/stream_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/teambot.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/teams.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/teams_ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/teamsearch.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/test.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/tlf.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/tlf_keys.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/track.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/ui.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/upk.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/user.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/usersearch.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/keybase1/wot.avdl
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Union

from dataclasses_json import DataClassJsonMixin, config
from typing_extensions import Literal

import pykeybasebot.types.gregor1 as gregor1


@dataclass
class HasServerKeysRes(DataClassJsonMixin):
    has_server_keys: bool = field(metadata=config(field_name="hasServerKeys"))


@dataclass
class APIRes(DataClassJsonMixin):
    status: str = field(metadata=config(field_name="status"))
    body: str = field(metadata=config(field_name="body"))
    http_status: int = field(metadata=config(field_name="httpStatus"))
    app_status: str = field(metadata=config(field_name="appStatus"))


class MobileAppState(Enum):
    FOREGROUND = 0
    BACKGROUND = 1
    INACTIVE = 2
    BACKGROUNDACTIVE = 3


class MobileAppStateStrings(Enum):
    FOREGROUND = "foreground"
    BACKGROUND = "background"
    INACTIVE = "inactive"
    BACKGROUNDACTIVE = "backgroundactive"


class MobileNetworkState(Enum):
    NONE = 0
    WIFI = 1
    CELLULAR = 2
    UNKNOWN = 3
    NOTAVAILABLE = 4


class MobileNetworkStateStrings(Enum):
    NONE = "none"
    WIFI = "wifi"
    CELLULAR = "cellular"
    UNKNOWN = "unknown"
    NOTAVAILABLE = "notavailable"


class BoxAuditAttemptResult(Enum):
    FAILURE_RETRYABLE = 0
    FAILURE_MALICIOUS_SERVER = 1
    OK_VERIFIED = 2
    OK_NOT_ATTEMPTED_ROLE = 3
    OK_NOT_ATTEMPTED_OPENTEAM = 4
    OK_NOT_ATTEMPTED_SUBTEAM = 5


class BoxAuditAttemptResultStrings(Enum):
    FAILURE_RETRYABLE = "failure_retryable"
    FAILURE_MALICIOUS_SERVER = "failure_malicious_server"
    OK_VERIFIED = "ok_verified"
    OK_NOT_ATTEMPTED_ROLE = "ok_not_attempted_role"
    OK_NOT_ATTEMPTED_OPENTEAM = "ok_not_attempted_openteam"
    OK_NOT_ATTEMPTED_SUBTEAM = "ok_not_attempted_subteam"


AvatarUrl = str
AvatarFormat = str


class BlockType(Enum):
    DATA = 0
    MD = 1
    GIT = 2


class BlockTypeStrings(Enum):
    DATA = "data"
    MD = "md"
    GIT = "git"


@dataclass
class ChallengeInfo(DataClassJsonMixin):
    now: int = field(metadata=config(field_name="now"))
    challenge: str = field(metadata=config(field_name="challenge"))


class BlockStatus(Enum):
    UNKNOWN = 0
    LIVE = 1
    ARCHIVED = 2


class BlockStatusStrings(Enum):
    UNKNOWN = "unknown"
    LIVE = "live"
    ARCHIVED = "archived"


BlockRefNonce = Optional[str]


@dataclass
class BlockPingResponse(DataClassJsonMixin):
    pass


@dataclass
class UsageStatRecord(DataClassJsonMixin):
    write: int = field(metadata=config(field_name="write"))
    archive: int = field(metadata=config(field_name="archive"))
    read: int = field(metadata=config(field_name="read"))
    md_write: int = field(metadata=config(field_name="mdWrite"))
    git_write: int = field(metadata=config(field_name="gitWrite"))
    git_archive: int = field(metadata=config(field_name="gitArchive"))


BotToken = str
Time = int
UnixTime = int
DurationSec = float
DurationMsec = float


@dataclass
class StringKVPair(DataClassJsonMixin):
    key: str = field(metadata=config(field_name="key"))
    value: str = field(metadata=config(field_name="value"))


UID = str
VID = str
DeviceID = str
SigID = str
LeaseID = str
KID = str
PhoneNumber = str
RawPhoneNumber = str
LinkID = str
BinaryLinkID = str
BinaryKID = str
TLFID = str
TeamID = str
UserOrTeamID = str
GitRepoName = str
HashMeta = str


class TeamType(Enum):
    NONE = 0
    LEGACY = 1
    MODERN = 2


class TeamTypeStrings(Enum):
    NONE = "none"
    LEGACY = "legacy"
    MODERN = "modern"


class TLFVisibility(Enum):
    ANY = 0
    PUBLIC = 1
    PRIVATE = 2


class TLFVisibilityStrings(Enum):
    ANY = "any"
    PUBLIC = "public"
    PRIVATE = "private"


Seqno = int


class SeqType(Enum):
    NONE = 0
    PUBLIC = 1
    PRIVATE = 2
    SEMIPRIVATE = 3
    USER_PRIVATE_HIDDEN = 16
    TEAM_PRIVATE_HIDDEN = 17


class SeqTypeStrings(Enum):
    NONE = "none"
    PUBLIC = "public"
    PRIVATE = "private"
    SEMIPRIVATE = "semiprivate"
    USER_PRIVATE_HIDDEN = "user_private_hidden"
    TEAM_PRIVATE_HIDDEN = "team_private_hidden"


Bytes32 = Optional[str]


@dataclass
class Text(DataClassJsonMixin):
    data: str = field(metadata=config(field_name="data"))
    markup: bool = field(metadata=config(field_name="markup"))


@dataclass
class PGPIdentity(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    comment: str = field(metadata=config(field_name="comment"))
    email: str = field(metadata=config(field_name="email"))


class DeviceType(Enum):
    DESKTOP = 0
    MOBILE = 1


class DeviceTypeStrings(Enum):
    DESKTOP = "desktop"
    MOBILE = "mobile"


DeviceTypeV2 = str


@dataclass
class Stream(DataClassJsonMixin):
    fd: int = field(metadata=config(field_name="fd"))


class LogLevel(Enum):
    NONE = 0
    DEBUG = 1
    INFO = 2
    NOTICE = 3
    WARN = 4
    ERROR = 5
    CRITICAL = 6
    FATAL = 7


class LogLevelStrings(Enum):
    NONE = "none"
    DEBUG = "debug"
    INFO = "info"
    NOTICE = "notice"
    WARN = "warn"
    ERROR = "error"
    CRITICAL = "critical"
    FATAL = "fatal"


class ClientType(Enum):
    NONE = 0
    CLI = 1
    GUI_MAIN = 2
    KBFS = 3
    GUI_HELPER = 4


class ClientTypeStrings(Enum):
    NONE = "none"
    CLI = "cli"
    GUI_MAIN = "gui_main"
    KBFS = "kbfs"
    GUI_HELPER = "gui_helper"


@dataclass
class KBFSPathInfo(DataClassJsonMixin):
    standard_path: str = field(metadata=config(field_name="standardPath"))
    deeplink_path: str = field(metadata=config(field_name="deeplinkPath"))
    platform_after_mount_path: str = field(
        metadata=config(field_name="platformAfterMountPath")
    )


PerUserKeyGeneration = int


class UserOrTeamResult(Enum):
    USER = 1
    TEAM = 2


class UserOrTeamResultStrings(Enum):
    USER = "user"
    TEAM = "team"


class MerkleTreeID(Enum):
    MASTER = 0
    KBFS_PUBLIC = 1
    KBFS_PRIVATE = 2
    KBFS_PRIVATETEAM = 3


class MerkleTreeIDStrings(Enum):
    MASTER = "master"
    KBFS_PUBLIC = "kbfs_public"
    KBFS_PRIVATE = "kbfs_private"
    KBFS_PRIVATETEAM = "kbfs_privateteam"


SocialAssertionService = str
FullName = str


class FullNamePackageVersion(Enum):
    V0 = 0
    V1 = 1
    V2 = 2


class FullNamePackageVersionStrings(Enum):
    V0 = "v0"
    V1 = "v1"
    V2 = "v2"


@dataclass
class ImageCropRect(DataClassJsonMixin):
    x_0: int = field(metadata=config(field_name="x0"))
    y_0: int = field(metadata=config(field_name="y0"))
    x_1: int = field(metadata=config(field_name="x1"))
    y_1: int = field(metadata=config(field_name="y1"))


class IdentityVisibility(Enum):
    PRIVATE = 0
    PUBLIC = 1


class IdentityVisibilityStrings(Enum):
    PRIVATE = "private"
    PUBLIC = "public"


@dataclass
class SizedImage(DataClassJsonMixin):
    path: str = field(metadata=config(field_name="path"))
    width: int = field(metadata=config(field_name="width"))


class OfflineAvailability(Enum):
    NONE = 0
    BEST_EFFORT = 1


class OfflineAvailabilityStrings(Enum):
    NONE = "none"
    BEST_EFFORT = "best_effort"


@dataclass
class UserReacji(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    custom_addr: Optional[str] = field(
        default=None, metadata=config(field_name="customAddr")
    )
    custom_addr_no_anim: Optional[str] = field(
        default=None, metadata=config(field_name="customAddrNoAnim")
    )


class ReacjiSkinTone(Enum):
    NONE = 0
    SKINTONE1 = 1
    SKINTONE2 = 2
    SKINTONE3 = 3
    SKINTONE4 = 4
    SKINTONE5 = 5


class ReacjiSkinToneStrings(Enum):
    NONE = "none"
    SKINTONE1 = "skintone1"
    SKINTONE2 = "skintone2"
    SKINTONE3 = "skintone3"
    SKINTONE4 = "skintone4"
    SKINTONE5 = "skintone5"


class WotStatusType(Enum):
    NONE = 0
    PROPOSED = 1
    ACCEPTED = 2
    REJECTED = 3
    REVOKED = 4


class WotStatusTypeStrings(Enum):
    NONE = "none"
    PROPOSED = "proposed"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    REVOKED = "revoked"


@dataclass
class SessionStatus(DataClassJsonMixin):
    session_for: str = field(metadata=config(field_name="SessionFor"))
    loaded: bool = field(metadata=config(field_name="Loaded"))
    cleared: bool = field(metadata=config(field_name="Cleared"))
    salt_only: bool = field(metadata=config(field_name="SaltOnly"))
    expired: bool = field(metadata=config(field_name="Expired"))


@dataclass
class PlatformInfo(DataClassJsonMixin):
    os: str = field(metadata=config(field_name="os"))
    os_version: str = field(metadata=config(field_name="osVersion"))
    arch: str = field(metadata=config(field_name="arch"))
    go_version: str = field(metadata=config(field_name="goVersion"))


@dataclass
class LoadDeviceErr(DataClassJsonMixin):
    where: str = field(metadata=config(field_name="where"))
    desc: str = field(metadata=config(field_name="desc"))


@dataclass
class DirSizeInfo(DataClassJsonMixin):
    num_files: int = field(metadata=config(field_name="numFiles"))
    name: str = field(metadata=config(field_name="name"))
    human_size: str = field(metadata=config(field_name="humanSize"))


@dataclass
class KbClientStatus(DataClassJsonMixin):
    version: str = field(metadata=config(field_name="version"))


@dataclass
class KbServiceStatus(DataClassJsonMixin):
    version: str = field(metadata=config(field_name="version"))
    running: bool = field(metadata=config(field_name="running"))
    pid: str = field(metadata=config(field_name="pid"))
    log: str = field(metadata=config(field_name="log"))
    ek_log: str = field(metadata=config(field_name="ekLog"))
    perf_log: str = field(metadata=config(field_name="perfLog"))


@dataclass
class KBFSStatus(DataClassJsonMixin):
    version: str = field(metadata=config(field_name="version"))
    installed_version: str = field(metadata=config(field_name="installedVersion"))
    running: bool = field(metadata=config(field_name="running"))
    pid: str = field(metadata=config(field_name="pid"))
    log: str = field(metadata=config(field_name="log"))
    perf_log: str = field(metadata=config(field_name="perfLog"))
    mount: str = field(metadata=config(field_name="mount"))


@dataclass
class DesktopStatus(DataClassJsonMixin):
    version: str = field(metadata=config(field_name="version"))
    running: bool = field(metadata=config(field_name="running"))
    log: str = field(metadata=config(field_name="log"))


@dataclass
class UpdaterStatus(DataClassJsonMixin):
    log: str = field(metadata=config(field_name="log"))


@dataclass
class StartStatus(DataClassJsonMixin):
    log: str = field(metadata=config(field_name="log"))


@dataclass
class GitStatus(DataClassJsonMixin):
    log: str = field(metadata=config(field_name="log"))
    perf_log: str = field(metadata=config(field_name="perfLog"))


LogSendID = str


@dataclass
class AllProvisionedUsernames(DataClassJsonMixin):
    default_username: str = field(metadata=config(field_name="defaultUsername"))
    has_provisioned_user: bool = field(metadata=config(field_name="hasProvisionedUser"))
    provisioned_usernames: Optional[List[str]] = field(
        default=None, metadata=config(field_name="provisionedUsernames")
    )


class ForkType(Enum):
    NONE = 0
    AUTO = 1
    WATCHDOG = 2
    LAUNCHD = 3
    SYSTEMD = 4


class ForkTypeStrings(Enum):
    NONE = "none"
    AUTO = "auto"
    WATCHDOG = "watchdog"
    LAUNCHD = "launchd"
    SYSTEMD = "systemd"


@dataclass
class ConfigValue(DataClassJsonMixin):
    is_null: bool = field(metadata=config(field_name="isNull"))
    b: Optional[bool] = field(default=None, metadata=config(field_name="b"))
    i: Optional[int] = field(default=None, metadata=config(field_name="i"))
    f: Optional[float] = field(default=None, metadata=config(field_name="f"))
    s: Optional[str] = field(default=None, metadata=config(field_name="s"))
    o: Optional[str] = field(default=None, metadata=config(field_name="o"))


@dataclass
class OutOfDateInfo(DataClassJsonMixin):
    upgrade_to: str = field(metadata=config(field_name="upgradeTo"))
    upgrade_uri: str = field(metadata=config(field_name="upgradeURI"))
    custom_message: str = field(metadata=config(field_name="customMessage"))
    critical_clock_skew: int = field(metadata=config(field_name="criticalClockSkew"))


class UpdateInfoStatus(Enum):
    UP_TO_DATE = 0
    NEED_UPDATE = 1
    CRITICALLY_OUT_OF_DATE = 2


class UpdateInfoStatusStrings(Enum):
    UP_TO_DATE = "up_to_date"
    NEED_UPDATE = "need_update"
    CRITICALLY_OUT_OF_DATE = "critically_out_of_date"


class UpdateInfoStatus2(Enum):
    OK = 0
    SUGGESTED = 1
    CRITICAL = 2


class UpdateInfoStatus2Strings(Enum):
    OK = "ok"
    SUGGESTED = "suggested"
    CRITICAL = "critical"


@dataclass
class UpdateDetails(DataClassJsonMixin):
    message: str = field(metadata=config(field_name="message"))


class ProxyType(Enum):
    No_Proxy = 0
    HTTP_Connect = 1
    Socks = 2


class ProxyTypeStrings(Enum):
    No_Proxy = "no_proxy"
    HTTP_Connect = "http_connect"
    Socks = "socks"


class StatusCode(Enum):
    SCOk = 0
    SCInputError = 100
    SCAssertionParseError = 101
    SCLoginRequired = 201
    SCBadSession = 202
    SCBadLoginUserNotFound = 203
    SCBadLoginPassword = 204
    SCNotFound = 205
    SCThrottleControl = 210
    SCDeleted = 216
    SCGeneric = 218
    SCAlreadyLoggedIn = 235
    SCExists = 230
    SCCanceled = 237
    SCInputCanceled = 239
    SCBadUsername = 243
    SCOffline = 267
    SCReloginRequired = 274
    SCResolutionFailed = 275
    SCProfileNotPublic = 276
    SCIdentifyFailed = 277
    SCTrackingBroke = 278
    SCWrongCryptoFormat = 279
    SCDecryptionError = 280
    SCInvalidAddress = 281
    SCWrongCryptoMsgType = 282
    SCNoSession = 283
    SCAccountReset = 290
    SCIdentifiesFailed = 295
    SCNoSpaceOnDevice = 297
    SCMerkleClientError = 299
    SCMerkleUpdateRoot = 300
    SCBadEmail = 472
    SCRateLimit = 602
    SCBadSignupUsernameTaken = 701
    SCDuplicate = 706
    SCBadInvitationCode = 707
    SCBadSignupUsernameReserved = 710
    SCBadSignupTeamName = 711
    SCFeatureFlag = 712
    SCEmailTaken = 713
    SCEmailAlreadyAdded = 714
    SCEmailLimitExceeded = 715
    SCEmailCannotDeletePrimary = 716
    SCEmailUnknown = 717
    SCBotSignupTokenNotFound = 719
    SCNoUpdate = 723
    SCMissingResult = 801
    SCKeyNotFound = 901
    SCKeyCorrupted = 905
    SCKeyInUse = 907
    SCKeyBadGen = 913
    SCKeyNoSecret = 914
    SCKeyBadUIDs = 915
    SCKeyNoActive = 916
    SCKeyNoSig = 917
    SCKeyBadSig = 918
    SCKeyBadEldest = 919
    SCKeyNoEldest = 920
    SCKeyDuplicateUpdate = 921
    SCSibkeyAlreadyExists = 922
    SCDecryptionKeyNotFound = 924
    SCVerificationKeyNotFound = 925
    SCKeyNoPGPEncryption = 927
    SCKeyNoNaClEncryption = 928
    SCKeySyncedPGPNotFound = 929
    SCKeyNoMatchingGPG = 930
    SCKeyRevoked = 931
    SCSigCannotVerify = 1002
    SCSigWrongKey = 1008
    SCSigOldSeqno = 1010
    SCSigCreationDisallowed = 1016
    SCSigMissingRatchet = 1021
    SCSigBadTotalOrder = 1022
    SCBadTrackSession = 1301
    SCDeviceBadName = 1404
    SCDeviceBadStatus = 1405
    SCDeviceNameInUse = 1408
    SCDeviceNotFound = 1409
    SCDeviceMismatch = 1410
    SCDeviceRequired = 1411
    SCDevicePrevProvisioned = 1413
    SCDeviceNoProvision = 1414
    SCDeviceProvisionViaDevice = 1415
    SCRevokeCurrentDevice = 1416
    SCRevokeLastDevice = 1417
    SCDeviceProvisionOffline = 1418
    SCRevokeLastDevicePGP = 1419
    SCStreamExists = 1501
    SCStreamNotFound = 1502
    SCStreamWrongKind = 1503
    SCStreamEOF = 1504
    SCStreamUnknown = 1505
    SCGenericAPIError = 1600
    SCAPINetworkError = 1601
    SCTimeout = 1602
    SCKBFSClientTimeout = 1603
    SCProofError = 1701
    SCIdentificationExpired = 1702
    SCSelfNotFound = 1703
    SCBadKexPhrase = 1704
    SCNoUIDelegation = 1705
    SCNoUI = 1706
    SCGPGUnavailable = 1707
    SCInvalidVersionError = 1800
    SCOldVersionError = 1801
    SCInvalidLocationError = 1802
    SCServiceStatusError = 1803
    SCInstallError = 1804
    SCLoadKextError = 1810
    SCLoadKextPermError = 1811
    SCGitInternal = 2300
    SCGitRepoAlreadyExists = 2301
    SCGitInvalidRepoName = 2302
    SCGitCannotDelete = 2303
    SCGitRepoDoesntExist = 2304
    SCLoginStateTimeout = 2400
    SCChatInternal = 2500
    SCChatRateLimit = 2501
    SCChatConvExists = 2502
    SCChatUnknownTLFID = 2503
    SCChatNotInConv = 2504
    SCChatBadMsg = 2505
    SCChatBroadcast = 2506
    SCChatAlreadySuperseded = 2507
    SCChatAlreadyDeleted = 2508
    SCChatTLFFinalized = 2509
    SCChatCollision = 2510
    SCIdentifySummaryError = 2511
    SCNeedSelfRekey = 2512
    SCNeedOtherRekey = 2513
    SCChatMessageCollision = 2514
    SCChatDuplicateMessage = 2515
    SCChatClientError = 2516
    SCChatNotInTeam = 2517
    SCChatStalePreviousState = 2518
    SCChatEphemeralRetentionPolicyViolatedError = 2519
    SCChatUsersAlreadyInConversationError = 2520
    SCChatBadConversationError = 2521
    SCTeamBadMembership = 2604
    SCTeamSelfNotOwner = 2607
    SCTeamNotFound = 2614
    SCTeamExists = 2619
    SCTeamReadError = 2623
    SCTeamWritePermDenied = 2625
    SCTeamBadGeneration = 2634
    SCNoOp = 2638
    SCTeamInviteBadCancel = 2645
    SCTeamInviteBadToken = 2646
    SCTeamBadNameReservedDB = 2650
    SCTeamTarDuplicate = 2663
    SCTeamTarNotFound = 2664
    SCTeamMemberExists = 2665
    SCTeamNotReleased = 2666
    SCTeamPermanentlyLeft = 2667
    SCTeamNeedRootId = 2668
    SCTeamHasLiveChildren = 2669
    SCTeamDeleteError = 2670
    SCTeamBadRootTeam = 2671
    SCTeamNameConflictsWithUser = 2672
    SCTeamDeleteNoUpPointer = 2673
    SCTeamNeedOwner = 2674
    SCTeamNoOwnerAllowed = 2675
    SCTeamImplicitNoNonSbs = 2676
    SCTeamImplicitBadHash = 2677
    SCTeamImplicitBadName = 2678
    SCTeamImplicitClash = 2679
    SCTeamImplicitDuplicate = 2680
    SCTeamImplicitBadOp = 2681
    SCTeamImplicitBadRole = 2682
    SCTeamImplicitNotFound = 2683
    SCTeamBadAdminSeqnoType = 2684
    SCTeamImplicitBadAdd = 2685
    SCTeamImplicitBadRemove = 2686
    SCTeamInviteTokenReused = 2696
    SCTeamKeyMaskNotFound = 2697
    SCTeamBanned = 2702
    SCTeamInvalidBan = 2703
    SCTeamShowcasePermDenied = 2711
    SCTeamProvisionalCanKey = 2721
    SCTeamProvisionalCannotKey = 2722
    SCTeamFTLOutdated = 2736
    SCTeamStorageWrongRevision = 2760
    SCTeamStorageBadGeneration = 2761
    SCTeamStorageNotFound = 2762
    SCTeamContactSettingsBlock = 2763
    SCEphemeralKeyBadGeneration = 2900
    SCEphemeralKeyUnexpectedBox = 2901
    SCEphemeralKeyMissingBox = 2902
    SCEphemeralKeyWrongNumberOfKeys = 2903
    SCEphemeralKeyMismatchedKey = 2904
    SCEphemeralPairwiseMACsMissingUIDs = 2905
    SCEphemeralDeviceAfterEK = 2906
    SCEphemeralMemberAfterEK = 2907
    SCEphemeralDeviceStale = 2908
    SCEphemeralUserStale = 2909
    SCStellarError = 3100
    SCStellarBadInput = 3101
    SCStellarWrongRevision = 3102
    SCStellarMissingBundle = 3103
    SCStellarBadPuk = 3104
    SCStellarMissingAccount = 3105
    SCStellarBadPrev = 3106
    SCStellarWrongPrimary = 3107
    SCStellarUnsupportedCurrency = 3108
    SCStellarNeedDisclaimer = 3109
    SCStellarDeviceNotMobile = 3110
    SCStellarMobileOnlyPurgatory = 3111
    SCStellarIncompatibleVersion = 3112
    SCNISTWrongSize = 3201
    SCNISTBadMode = 3202
    SCNISTHashWrongSize = 3203
    SCNISTSigWrongSize = 3204
    SCNISTSigBadInput = 3205
    SCNISTSigBadUID = 3206
    SCNISTSigBadDeviceID = 3207
    SCNISTSigBadNonce = 3208
    SCNISTNoSigOrHash = 3209
    SCNISTExpired = 3210
    SCNISTSigRevoked = 3211
    SCNISTKeyRevoked = 3212
    SCNISTUserDeleted = 3213
    SCNISTNoDevice = 3214
    SCNISTSigCannot_verify = 3215
    SCNISTReplay = 3216
    SCNISTSigBadLifetime = 3217
    SCNISTNotFound = 3218
    SCNISTBadClock = 3219
    SCNISTSigBadCtime = 3220
    SCBadSignupUsernameDeleted = 3221
    SCPhoneNumberUnknown = 3400
    SCPhoneNumberAlreadyVerified = 3401
    SCPhoneNumberVerificationCodeExpired = 3402
    SCPhoneNumberWrongVerificationCode = 3403
    SCPhoneNumberLimitExceeded = 3404
    SCNoPaperKeys = 3605
    SCTeambotKeyGenerationExists = 3800
    SCTeambotKeyOldBoxedGeneration = 3801
    SCTeambotKeyBadGeneration = 3802
    SCAirdropRegisterFailedMisc = 4207
    SCSimpleFSNameExists = 5101
    SCSimpleFSDirNotEmpty = 5102
    SCSimpleFSNotExist = 5103
    SCSimpleFSNoAccess = 5104


class StatusCodeStrings(Enum):
    SCOk = "scok"
    SCInputError = "scinputerror"
    SCAssertionParseError = "scassertionparseerror"
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
    SCWrongCryptoMsgType = "scwrongcryptomsgtype"
    SCNoSession = "scnosession"
    SCAccountReset = "scaccountreset"
    SCIdentifiesFailed = "scidentifiesfailed"
    SCNoSpaceOnDevice = "scnospaceondevice"
    SCMerkleClientError = "scmerkleclienterror"
    SCMerkleUpdateRoot = "scmerkleupdateroot"
    SCBadEmail = "scbademail"
    SCRateLimit = "scratelimit"
    SCBadSignupUsernameTaken = "scbadsignupusernametaken"
    SCDuplicate = "scduplicate"
    SCBadInvitationCode = "scbadinvitationcode"
    SCBadSignupUsernameReserved = "scbadsignupusernamereserved"
    SCBadSignupTeamName = "scbadsignupteamname"
    SCFeatureFlag = "scfeatureflag"
    SCEmailTaken = "scemailtaken"
    SCEmailAlreadyAdded = "scemailalreadyadded"
    SCEmailLimitExceeded = "scemaillimitexceeded"
    SCEmailCannotDeletePrimary = "scemailcannotdeleteprimary"
    SCEmailUnknown = "scemailunknown"
    SCBotSignupTokenNotFound = "scbotsignuptokennotfound"
    SCNoUpdate = "scnoupdate"
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
    SCVerificationKeyNotFound = "scverificationkeynotfound"
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
    SCDeviceBadStatus = "scdevicebadstatus"
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
    SCStreamUnknown = "scstreamunknown"
    SCGenericAPIError = "scgenericapierror"
    SCAPINetworkError = "scapinetworkerror"
    SCTimeout = "sctimeout"
    SCKBFSClientTimeout = "sckbfsclienttimeout"
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
    SCChatUsersAlreadyInConversationError = "scchatusersalreadyinconversationerror"
    SCChatBadConversationError = "scchatbadconversationerror"
    SCTeamBadMembership = "scteambadmembership"
    SCTeamSelfNotOwner = "scteamselfnotowner"
    SCTeamNotFound = "scteamnotfound"
    SCTeamExists = "scteamexists"
    SCTeamReadError = "scteamreaderror"
    SCTeamWritePermDenied = "scteamwritepermdenied"
    SCTeamBadGeneration = "scteambadgeneration"
    SCNoOp = "scnoop"
    SCTeamInviteBadCancel = "scteaminvitebadcancel"
    SCTeamInviteBadToken = "scteaminvitebadtoken"
    SCTeamBadNameReservedDB = "scteambadnamereserveddb"
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
    SCTeamStorageWrongRevision = "scteamstoragewrongrevision"
    SCTeamStorageBadGeneration = "scteamstoragebadgeneration"
    SCTeamStorageNotFound = "scteamstoragenotfound"
    SCTeamContactSettingsBlock = "scteamcontactsettingsblock"
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
    SCAirdropRegisterFailedMisc = "scairdropregisterfailedmisc"
    SCSimpleFSNameExists = "scsimplefsnameexists"
    SCSimpleFSDirNotEmpty = "scsimplefsdirnotempty"
    SCSimpleFSNotExist = "scsimplefsnotexist"
    SCSimpleFSNoAccess = "scsimplefsnoaccess"


ED25519PublicKey = Optional[str]
ED25519Signature = Optional[str]
EncryptedBytes32 = Optional[str]
BoxNonce = Optional[str]
BoxPublicKey = Optional[str]


@dataclass
class RegisterAddressRes(DataClassJsonMixin):
    type: str = field(metadata=config(field_name="type"))
    family: str = field(metadata=config(field_name="family"))


class ExitCode(Enum):
    OK = 0
    NOTOK = 2
    RESTART = 4


class ExitCodeStrings(Enum):
    OK = "ok"
    NOTOK = "notok"
    RESTART = "restart"


class DbType(Enum):
    MAIN = 0
    CHAT = 1
    FS_BLOCK_CACHE = 2
    FS_BLOCK_CACHE_META = 3
    FS_SYNC_BLOCK_CACHE = 4
    FS_SYNC_BLOCK_CACHE_META = 5


class DbTypeStrings(Enum):
    MAIN = "main"
    CHAT = "chat"
    FS_BLOCK_CACHE = "fs_block_cache"
    FS_BLOCK_CACHE_META = "fs_block_cache_meta"
    FS_SYNC_BLOCK_CACHE = "fs_sync_block_cache"
    FS_SYNC_BLOCK_CACHE_META = "fs_sync_block_cache_meta"


DbValue = str


class OnLoginStartupStatus(Enum):
    UNKNOWN = 0
    DISABLED = 1
    ENABLED = 2


class OnLoginStartupStatusStrings(Enum):
    UNKNOWN = "unknown"
    DISABLED = "disabled"
    ENABLED = "enabled"


@dataclass
class FirstStepResult(DataClassJsonMixin):
    val_plus_two: int = field(metadata=config(field_name="valPlusTwo"))


EkGeneration = int


class TeamEphemeralKeyType(Enum):
    TEAM = 0
    TEAMBOT = 1


class TeamEphemeralKeyTypeStrings(Enum):
    TEAM = "team"
    TEAMBOT = "teambot"


class FolderType(Enum):
    UNKNOWN = 0
    PRIVATE = 1
    PUBLIC = 2
    TEAM = 3


class FolderTypeStrings(Enum):
    UNKNOWN = "unknown"
    PRIVATE = "private"
    PUBLIC = "public"
    TEAM = "team"


class FolderConflictType(Enum):
    NONE = 0
    IN_CONFLICT = 1
    IN_CONFLICT_AND_STUCK = 2
    CLEARED_CONFLICT = 3


class FolderConflictTypeStrings(Enum):
    NONE = "none"
    IN_CONFLICT = "in_conflict"
    IN_CONFLICT_AND_STUCK = "in_conflict_and_stuck"
    CLEARED_CONFLICT = "cleared_conflict"


class ConflictStateType(Enum):
    NormalView = 1
    ManualResolvingLocalView = 2


class ConflictStateTypeStrings(Enum):
    NormalView = "normalview"
    ManualResolvingLocalView = "manualresolvinglocalview"


@dataclass
class FeaturedBot(DataClassJsonMixin):
    bot_alias: str = field(metadata=config(field_name="botAlias"))
    description: str = field(metadata=config(field_name="description"))
    extended_description: str = field(metadata=config(field_name="extendedDescription"))
    extended_description_raw: str = field(
        metadata=config(field_name="extendedDescriptionRaw")
    )
    bot_username: str = field(metadata=config(field_name="botUsername"))
    rank: int = field(metadata=config(field_name="rank"))
    is_promoted: bool = field(metadata=config(field_name="isPromoted"))
    owner_team: Optional[str] = field(
        default=None, metadata=config(field_name="ownerTeam")
    )
    owner_user: Optional[str] = field(
        default=None, metadata=config(field_name="ownerUser")
    )


@dataclass
class File(DataClassJsonMixin):
    path: str = field(metadata=config(field_name="path"))


RepoID = str


class GitLocalMetadataVersion(Enum):
    V1 = 1


class GitLocalMetadataVersionStrings(Enum):
    V1 = "v1"


class GitPushType(Enum):
    DEFAULT = 0
    CREATEREPO = 1
    RENAMEREPO = 3


class GitPushTypeStrings(Enum):
    DEFAULT = "default"
    CREATEREPO = "createrepo"
    RENAMEREPO = "renamerepo"


class GitRepoResultState(Enum):
    ERR = 0
    OK = 1


class GitRepoResultStateStrings(Enum):
    ERR = "err"
    OK = "ok"


@dataclass
class GitTeamRepoSettings(DataClassJsonMixin):
    chat_disabled: bool = field(metadata=config(field_name="chatDisabled"))
    channel_name: Optional[str] = field(
        default=None, metadata=config(field_name="channelName")
    )


@dataclass
class SelectKeyRes(DataClassJsonMixin):
    key_id: str = field(metadata=config(field_name="keyID"))
    do_secret_push: bool = field(metadata=config(field_name="doSecretPush"))


class PushReason(Enum):
    NONE = 0
    RECONNECTED = 1
    NEW_DATA = 2


class PushReasonStrings(Enum):
    NONE = "none"
    RECONNECTED = "reconnected"
    NEW_DATA = "new_data"


HomeScreenItemID = str


class HomeScreenItemType(Enum):
    TODO = 1
    PEOPLE = 2
    ANNOUNCEMENT = 3


class HomeScreenItemTypeStrings(Enum):
    TODO = "todo"
    PEOPLE = "people"
    ANNOUNCEMENT = "announcement"


class AppLinkType(Enum):
    NONE = 0
    PEOPLE = 1
    CHAT = 2
    FILES = 3
    WALLET = 4
    GIT = 5
    DEVICES = 6
    SETTINGS = 7
    TEAMS = 8


class AppLinkTypeStrings(Enum):
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
    NONE = 0
    BIO = 1
    PROOF = 2
    DEVICE = 3
    FOLLOW = 4
    CHAT = 5
    PAPERKEY = 6
    TEAM = 7
    FOLDER = 8
    GIT_REPO = 9
    TEAM_SHOWCASE = 10
    AVATAR_USER = 11
    AVATAR_TEAM = 12
    ADD_PHONE_NUMBER = 18
    VERIFY_ALL_PHONE_NUMBER = 19
    VERIFY_ALL_EMAIL = 20
    LEGACY_EMAIL_VISIBILITY = 21
    ADD_EMAIL = 22
    ANNONCEMENT_PLACEHOLDER = 10000


class HomeScreenTodoTypeStrings(Enum):
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
    FOLLOWED = 1
    FOLLOWED_MULTI = 2
    CONTACT = 3
    CONTACT_MULTI = 4


class HomeScreenPeopleNotificationTypeStrings(Enum):
    FOLLOWED = "followed"
    FOLLOWED_MULTI = "followed_multi"
    CONTACT = "contact"
    CONTACT_MULTI = "contact_multi"


@dataclass
class Pics(DataClassJsonMixin):
    square_40: str = field(metadata=config(field_name="square_40"))
    square_200: str = field(metadata=config(field_name="square_200"))
    square_360: str = field(metadata=config(field_name="square_360"))


Identify3Assertion = str
Identify3GUIID = str


class Identify3RowState(Enum):
    CHECKING = 1
    VALID = 2
    ERROR = 3
    WARNING = 4
    REVOKED = 5


class Identify3RowStateStrings(Enum):
    CHECKING = "checking"
    VALID = "valid"
    ERROR = "error"
    WARNING = "warning"
    REVOKED = "revoked"


class Identify3RowColor(Enum):
    BLUE = 1
    RED = 2
    BLACK = 3
    GREEN = 4
    GRAY = 5
    YELLOW = 6
    ORANGE = 7


class Identify3RowColorStrings(Enum):
    BLUE = "blue"
    RED = "red"
    BLACK = "black"
    GREEN = "green"
    GRAY = "gray"
    YELLOW = "yellow"
    ORANGE = "orange"


class Identify3ResultType(Enum):
    OK = 0
    BROKEN = 1
    NEEDS_UPGRADE = 2
    CANCELED = 3


class Identify3ResultTypeStrings(Enum):
    OK = "ok"
    BROKEN = "broken"
    NEEDS_UPGRADE = "needs_upgrade"
    CANCELED = "canceled"


TrackToken = str
SigVersion = int


class TrackDiffType(Enum):
    NONE = 0
    ERROR = 1
    CLASH = 2
    REVOKED = 3
    UPGRADED = 4
    NEW = 5
    REMOTE_FAIL = 6
    REMOTE_WORKING = 7
    REMOTE_CHANGED = 8
    NEW_ELDEST = 9
    NONE_VIA_TEMPORARY = 10


class TrackDiffTypeStrings(Enum):
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

    NEW_OK = 1
    NEW_ZERO_PROOFS = 2
    NEW_FAIL_PROOFS = 3
    UPDATE_BROKEN_FAILED_PROOFS = 4
    UPDATE_NEW_PROOFS = 5
    UPDATE_OK = 6
    UPDATE_BROKEN_REVOKED = 7


class TrackStatusStrings(Enum):
    NEW_OK = "new_ok"
    NEW_ZERO_PROOFS = "new_zero_proofs"
    NEW_FAIL_PROOFS = "new_fail_proofs"
    UPDATE_BROKEN_FAILED_PROOFS = "update_broken_failed_proofs"
    UPDATE_NEW_PROOFS = "update_new_proofs"
    UPDATE_OK = "update_ok"
    UPDATE_BROKEN_REVOKED = "update_broken_revoked"


class IdentifyReasonType(Enum):
    NONE = 0
    ID = 1
    TRACK = 2
    ENCRYPT = 3
    DECRYPT = 4
    VERIFY = 5
    RESOURCE = 6
    BACKGROUND = 7


class IdentifyReasonTypeStrings(Enum):
    NONE = "none"
    ID = "id"
    TRACK = "track"
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    VERIFY = "verify"
    RESOURCE = "resource"
    BACKGROUND = "background"


@dataclass
class SigHint(DataClassJsonMixin):
    remote_id: str = field(metadata=config(field_name="remoteId"))
    human_url: str = field(metadata=config(field_name="humanUrl"))
    api_url: str = field(metadata=config(field_name="apiUrl"))
    check_text: str = field(metadata=config(field_name="checkText"))


class CheckResultFreshness(Enum):
    FRESH = 0
    AGED = 1
    RANCID = 2


class CheckResultFreshnessStrings(Enum):
    FRESH = "fresh"
    AGED = "aged"
    RANCID = "rancid"


@dataclass
class ConfirmResult(DataClassJsonMixin):
    identity_confirmed: bool = field(metadata=config(field_name="identityConfirmed"))
    remote_confirmed: bool = field(metadata=config(field_name="remoteConfirmed"))
    expiring_local: bool = field(metadata=config(field_name="expiringLocal"))
    auto_confirmed: bool = field(metadata=config(field_name="autoConfirmed"))


class DismissReasonType(Enum):
    NONE = 0
    HANDLED_ELSEWHERE = 1


class DismissReasonTypeStrings(Enum):
    NONE = "none"
    HANDLED_ELSEWHERE = "handled_elsewhere"


class IncomingShareType(Enum):
    FILE = 0
    TEXT = 1
    IMAGE = 2
    VIDEO = 3


class IncomingShareTypeStrings(Enum):
    FILE = "file"
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"


class InstallStatus(Enum):
    """
    Install status describes state of install for a component or service.
    """

    UNKNOWN = 0
    ERROR = 1
    NOT_INSTALLED = 2
    INSTALLED = 4


class InstallStatusStrings(Enum):
    UNKNOWN = "unknown"
    ERROR = "error"
    NOT_INSTALLED = "not_installed"
    INSTALLED = "installed"


class InstallAction(Enum):
    UNKNOWN = 0
    NONE = 1
    UPGRADE = 2
    REINSTALL = 3
    INSTALL = 4


class InstallActionStrings(Enum):
    UNKNOWN = "unknown"
    NONE = "none"
    UPGRADE = "upgrade"
    REINSTALL = "reinstall"
    INSTALL = "install"


@dataclass
class FuseMountInfo(DataClassJsonMixin):
    path: str = field(metadata=config(field_name="path"))
    fstype: str = field(metadata=config(field_name="fstype"))
    output: str = field(metadata=config(field_name="output"))


@dataclass
class InviteCounts(DataClassJsonMixin):
    invite_count: int = field(metadata=config(field_name="inviteCount"))
    percentage_change: float = field(metadata=config(field_name="percentageChange"))
    show_num_invites: bool = field(metadata=config(field_name="showNumInvites"))
    show_fire: bool = field(metadata=config(field_name="showFire"))
    tooltip_markdown: str = field(metadata=config(field_name="tooltipMarkdown"))


class FSStatusCode(Enum):
    START = 0
    FINISH = 1
    ERROR = 2


class FSStatusCodeStrings(Enum):
    START = "start"
    FINISH = "finish"
    ERROR = "error"


class FSNotificationType(Enum):
    ENCRYPTING = 0
    DECRYPTING = 1
    SIGNING = 2
    VERIFYING = 3
    REKEYING = 4
    CONNECTION = 5
    MD_READ_SUCCESS = 6
    FILE_CREATED = 7
    FILE_MODIFIED = 8
    FILE_DELETED = 9
    FILE_RENAMED = 10
    INITIALIZED = 11
    SYNC_CONFIG_CHANGED = 12


class FSNotificationTypeStrings(Enum):
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
    ACCESS_DENIED = 0
    USER_NOT_FOUND = 1
    REVOKED_DATA_DETECTED = 2
    NOT_LOGGED_IN = 3
    TIMEOUT = 4
    REKEY_NEEDED = 5
    BAD_FOLDER = 6
    NOT_IMPLEMENTED = 7
    OLD_VERSION = 8
    OVER_QUOTA = 9
    NO_SIG_CHAIN = 10
    TOO_MANY_FOLDERS = 11
    EXDEV_NOT_SUPPORTED = 12
    DISK_LIMIT_REACHED = 13
    DISK_CACHE_ERROR_LOG_SEND = 14
    OFFLINE_ARCHIVED = 15
    OFFLINE_UNSYNCED = 16


class FSErrorTypeStrings(Enum):
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
class FSSyncStatusRequest(DataClassJsonMixin):
    request_id: int = field(metadata=config(field_name="requestID"))


@dataclass
class PassphraseStream(DataClassJsonMixin):
    passphrase_stream: str = field(metadata=config(field_name="passphraseStream"))
    generation: int = field(metadata=config(field_name="generation"))


SessionToken = str
CsrfToken = str
HelloRes = str


@dataclass
class KVGetResult(DataClassJsonMixin):
    team_name: str = field(metadata=config(field_name="teamName"))
    namespace: str = field(metadata=config(field_name="namespace"))
    entry_key: str = field(metadata=config(field_name="entryKey"))
    revision: int = field(metadata=config(field_name="revision"))
    entry_value: Optional[str] = field(
        default=None, metadata=config(field_name="entryValue")
    )


@dataclass
class KVPutResult(DataClassJsonMixin):
    team_name: str = field(metadata=config(field_name="teamName"))
    namespace: str = field(metadata=config(field_name="namespace"))
    entry_key: str = field(metadata=config(field_name="entryKey"))
    revision: int = field(metadata=config(field_name="revision"))


@dataclass
class EncryptedKVEntry(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    e: str = field(metadata=config(field_name="e"))
    n: str = field(metadata=config(field_name="n"))


@dataclass
class KVListNamespaceResult(DataClassJsonMixin):
    team_name: str = field(metadata=config(field_name="teamName"))
    namespaces: Optional[List[str]] = field(
        default=None, metadata=config(field_name="namespaces")
    )


@dataclass
class KVListEntryKey(DataClassJsonMixin):
    entry_key: str = field(metadata=config(field_name="entryKey"))
    revision: int = field(metadata=config(field_name="revision"))


@dataclass
class KVDeleteEntryResult(DataClassJsonMixin):
    team_name: str = field(metadata=config(field_name="teamName"))
    namespace: str = field(metadata=config(field_name="namespace"))
    entry_key: str = field(metadata=config(field_name="entryKey"))
    revision: int = field(metadata=config(field_name="revision"))


class ResetPromptType(Enum):
    COMPLETE = 0
    ENTER_NO_DEVICES = 1
    ENTER_FORGOT_PW = 2
    ENTER_RESET_PW = 3


class ResetPromptTypeStrings(Enum):
    COMPLETE = "complete"
    ENTER_NO_DEVICES = "enter_no_devices"
    ENTER_FORGOT_PW = "enter_forgot_pw"
    ENTER_RESET_PW = "enter_reset_pw"


@dataclass
class ResetPromptInfo(DataClassJsonMixin):
    has_wallet: bool = field(metadata=config(field_name="hasWallet"))


class ResetPromptResponse(Enum):
    NOTHING = 0
    CANCEL_RESET = 1
    CONFIRM_RESET = 2


class ResetPromptResponseStrings(Enum):
    NOTHING = "nothing"
    CANCEL_RESET = "cancel_reset"
    CONFIRM_RESET = "confirm_reset"


class PassphraseRecoveryPromptType(Enum):
    ENCRYPTED_PGP_KEYS = 0


class PassphraseRecoveryPromptTypeStrings(Enum):
    ENCRYPTED_PGP_KEYS = "encrypted_pgp_keys"


class ResetMessage(Enum):
    ENTERED_VERIFIED = 0
    ENTERED_PASSWORDLESS = 1
    REQUEST_VERIFIED = 2
    NOT_COMPLETED = 3
    CANCELED = 4
    COMPLETED = 5
    RESET_LINK_SENT = 6


class ResetMessageStrings(Enum):
    ENTERED_VERIFIED = "entered_verified"
    ENTERED_PASSWORDLESS = "entered_passwordless"
    REQUEST_VERIFIED = "request_verified"
    NOT_COMPLETED = "not_completed"
    CANCELED = "canceled"
    COMPLETED = "completed"
    RESET_LINK_SENT = "reset_link_sent"


KBFSRootHash = str
MerkleStoreSupportedVersion = int
MerkleStoreKitHash = str
MerkleStoreKit = str
MerkleStoreEntryString = str


@dataclass
class KeyBundle(DataClassJsonMixin):
    version: int = field(metadata=config(field_name="version"))
    bundle: str = field(metadata=config(field_name="bundle"))


@dataclass
class MerkleRoot(DataClassJsonMixin):
    version: int = field(metadata=config(field_name="version"))
    root: str = field(metadata=config(field_name="root"))


LockID = int
MDPriority = int


@dataclass
class RekeyRequest(DataClassJsonMixin):
    folder_id: str = field(metadata=config(field_name="folderID"))
    revision: int = field(metadata=config(field_name="revision"))


class NetworkSource(Enum):
    LOCAL = 0
    REMOTE = 1


class NetworkSourceStrings(Enum):
    LOCAL = "local"
    REMOTE = "remote"


ChatConversationID = str


@dataclass
class DeletedTeamInfo(DataClassJsonMixin):
    team_name: str = field(metadata=config(field_name="teamName"))
    deleted_by: str = field(metadata=config(field_name="deletedBy"))
    id: gregor1.MsgID = field(metadata=config(field_name="id"))


@dataclass
class WalletAccountInfo(DataClassJsonMixin):
    account_id: str = field(metadata=config(field_name="accountID"))
    num_unread: int = field(metadata=config(field_name="numUnread"))


@dataclass
class NotificationChannels(DataClassJsonMixin):
    badges: bool = field(metadata=config(field_name="badges"))
    session: bool = field(metadata=config(field_name="session"))
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
    users: bool = field(metadata=config(field_name="users"))
    reachability: bool = field(metadata=config(field_name="reachability"))
    team: bool = field(metadata=config(field_name="team"))
    ephemeral: bool = field(metadata=config(field_name="ephemeral"))
    teambot: bool = field(metadata=config(field_name="teambot"))
    chatkbfsedits: bool = field(metadata=config(field_name="chatkbfsedits"))
    chatdev: bool = field(metadata=config(field_name="chatdev"))
    chatemoji: bool = field(metadata=config(field_name="chatemoji"))
    chatemojicross: bool = field(metadata=config(field_name="chatemojicross"))
    deviceclone: bool = field(metadata=config(field_name="deviceclone"))
    chatattachments: bool = field(metadata=config(field_name="chatattachments"))
    wallet: bool = field(metadata=config(field_name="wallet"))
    audit: bool = field(metadata=config(field_name="audit"))
    runtimestats: bool = field(metadata=config(field_name="runtimestats"))
    featured_bots: bool = field(metadata=config(field_name="featuredBots"))
    saltpack: bool = field(metadata=config(field_name="saltpack"))


class StatsSeverityLevel(Enum):
    NORMAL = 0
    WARNING = 1
    SEVERE = 2


class StatsSeverityLevelStrings(Enum):
    NORMAL = "normal"
    WARNING = "warning"
    SEVERE = "severe"


class ProcessType(Enum):
    MAIN = 0
    KBFS = 1


class ProcessTypeStrings(Enum):
    MAIN = "main"
    KBFS = "kbfs"


class PerfEventType(Enum):
    NETWORK = 0
    TEAMBOXAUDIT = 1
    TEAMAUDIT = 2
    USERCHAIN = 3
    TEAMCHAIN = 4
    CLEARCONV = 5
    CLEARINBOX = 6
    TEAMTREELOAD = 7


class PerfEventTypeStrings(Enum):
    NETWORK = "network"
    TEAMBOXAUDIT = "teamboxaudit"
    TEAMAUDIT = "teamaudit"
    USERCHAIN = "userchain"
    TEAMCHAIN = "teamchain"
    CLEARCONV = "clearconv"
    CLEARINBOX = "clearinbox"
    TEAMTREELOAD = "teamtreeload"


class SaltpackOperationType(Enum):
    ENCRYPT = 0
    DECRYPT = 1
    SIGN = 2
    VERIFY = 3


class SaltpackOperationTypeStrings(Enum):
    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    SIGN = "sign"
    VERIFY = "verify"


@dataclass
class HttpSrvInfo(DataClassJsonMixin):
    address: str = field(metadata=config(field_name="address"))
    token: str = field(metadata=config(field_name="token"))


@dataclass
class TeamChangeSet(DataClassJsonMixin):
    membership_changed: bool = field(metadata=config(field_name="membershipChanged"))
    key_rotated: bool = field(metadata=config(field_name="keyRotated"))
    renamed: bool = field(metadata=config(field_name="renamed"))
    misc: bool = field(metadata=config(field_name="misc"))


class AvatarUpdateType(Enum):
    NONE = 0
    USER = 1
    TEAM = 2


class AvatarUpdateTypeStrings(Enum):
    NONE = "none"
    USER = "user"
    TEAM = "team"


class RuntimeGroup(Enum):
    UNKNOWN = 0
    LINUXLIKE = 1
    DARWINLIKE = 2
    WINDOWSLIKE = 3


class RuntimeGroupStrings(Enum):
    UNKNOWN = "unknown"
    LINUXLIKE = "linuxlike"
    DARWINLIKE = "darwinlike"
    WINDOWSLIKE = "windowslike"


@dataclass
class Feature(DataClassJsonMixin):
    allow: bool = field(metadata=config(field_name="allow"))
    default_value: bool = field(metadata=config(field_name="defaultValue"))
    readonly: bool = field(metadata=config(field_name="readonly"))
    label: str = field(metadata=config(field_name="label"))


class PassphraseType(Enum):
    NONE = 0
    PAPER_KEY = 1
    PASS_PHRASE = 2
    VERIFY_PASS_PHRASE = 3


class PassphraseTypeStrings(Enum):
    NONE = "none"
    PAPER_KEY = "paper_key"
    PASS_PHRASE = "pass_phrase"
    VERIFY_PASS_PHRASE = "verify_pass_phrase"


@dataclass
class GetPassphraseRes(DataClassJsonMixin):
    passphrase: str = field(metadata=config(field_name="passphrase"))
    store_secret: bool = field(metadata=config(field_name="storeSecret"))


class SignMode(Enum):
    ATTACHED = 0
    DETACHED = 1
    CLEAR = 2


class SignModeStrings(Enum):
    ATTACHED = "attached"
    DETACHED = "detached"
    CLEAR = "clear"


@dataclass
class PGPEncryptOptions(DataClassJsonMixin):
    no_sign: bool = field(metadata=config(field_name="noSign"))
    no_self: bool = field(metadata=config(field_name="noSelf"))
    binary_out: bool = field(metadata=config(field_name="binaryOut"))
    key_query: str = field(metadata=config(field_name="keyQuery"))
    recipients: Optional[List[str]] = field(
        default=None, metadata=config(field_name="recipients")
    )


@dataclass
class PGPDecryptOptions(DataClassJsonMixin):
    assert_signed: bool = field(metadata=config(field_name="assertSigned"))
    signed_by: str = field(metadata=config(field_name="signedBy"))


@dataclass
class PGPVerifyOptions(DataClassJsonMixin):
    signed_by: str = field(metadata=config(field_name="signedBy"))
    signature: str = field(metadata=config(field_name="signature"))


@dataclass
class KeyInfo(DataClassJsonMixin):
    fingerprint: str = field(metadata=config(field_name="fingerprint"))
    key: str = field(metadata=config(field_name="key"))
    desc: str = field(metadata=config(field_name="desc"))


@dataclass
class PGPQuery(DataClassJsonMixin):
    secret: bool = field(metadata=config(field_name="secret"))
    query: str = field(metadata=config(field_name="query"))
    exact_match: bool = field(metadata=config(field_name="exactMatch"))


@dataclass
class PGPPurgeRes(DataClassJsonMixin):
    filenames: Optional[List[str]] = field(
        default=None, metadata=config(field_name="filenames")
    )


class FileType(Enum):
    UNKNOWN = 0
    DIRECTORY = 1
    FILE = 2


class FileTypeStrings(Enum):
    UNKNOWN = "unknown"
    DIRECTORY = "directory"
    FILE = "file"


class ProofState(Enum):
    NONE = 0
    OK = 1
    TEMP_FAILURE = 2
    PERM_FAILURE = 3
    LOOKING = 4
    SUPERSEDED = 5
    POSTED = 6
    REVOKED = 7
    DELETED = 8
    UNKNOWN_TYPE = 9
    SIG_HINT_MISSING = 10
    UNCHECKED = 11


class ProofStateStrings(Enum):
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

    NONE = 0
    OK = 1
    LOCAL = 2
    FOUND = 3
    BASE_ERROR = 100
    HOST_UNREACHABLE = 101
    PERMISSION_DENIED = 103
    FAILED_PARSE = 106
    DNS_ERROR = 107
    AUTH_FAILED = 108
    HTTP_429 = 129
    HTTP_500 = 150
    TIMEOUT = 160
    INTERNAL_ERROR = 170
    UNCHECKED = 171
    MISSING_PVL = 172
    BASE_HARD_ERROR = 200
    NOT_FOUND = 201
    CONTENT_FAILURE = 202
    BAD_USERNAME = 203
    BAD_REMOTE_ID = 204
    TEXT_NOT_FOUND = 205
    BAD_ARGS = 206
    CONTENT_MISSING = 207
    TITLE_NOT_FOUND = 208
    SERVICE_ERROR = 209
    TOR_SKIPPED = 210
    TOR_INCOMPATIBLE = 211
    HTTP_300 = 230
    HTTP_400 = 240
    HTTP_OTHER = 260
    EMPTY_JSON = 270
    DELETED = 301
    SERVICE_DEAD = 302
    BAD_SIGNATURE = 303
    BAD_API_URL = 304
    UNKNOWN_TYPE = 305
    NO_HINT = 306
    BAD_HINT_TEXT = 307
    INVALID_PVL = 308


class ProofStatusStrings(Enum):
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
    NONE = 0
    KEYBASE = 1
    TWITTER = 2
    GITHUB = 3
    REDDIT = 4
    COINBASE = 5
    HACKERNEWS = 6
    FACEBOOK = 8
    GENERIC_SOCIAL = 9
    GENERIC_WEB_SITE = 1000
    DNS = 1001
    PGP = 1002
    ROOTER = 100001


class ProofTypeStrings(Enum):
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
class SelectorEntry(DataClassJsonMixin):
    is_index: bool = field(metadata=config(field_name="isIndex"))
    index: int = field(metadata=config(field_name="index"))
    is_key: bool = field(metadata=config(field_name="isKey"))
    key: str = field(metadata=config(field_name="key"))
    is_all: bool = field(metadata=config(field_name="isAll"))
    is_contents: bool = field(metadata=config(field_name="isContents"))


@dataclass
class ParamProofUsernameConfig(DataClassJsonMixin):
    re: str = field(metadata=config(field_name="re"))
    min: int = field(metadata=config(field_name="min"))
    max: int = field(metadata=config(field_name="max"))


@dataclass
class ServiceDisplayConfig(DataClassJsonMixin):
    creation_disabled: bool = field(metadata=config(field_name="creation_disabled"))
    priority: int = field(metadata=config(field_name="priority"))
    key: str = field(metadata=config(field_name="key"))
    new: bool = field(metadata=config(field_name="new"))
    logo_key: str = field(metadata=config(field_name="logo_key"))
    group: Optional[str] = field(default=None, metadata=config(field_name="group"))


class PromptOverwriteType(Enum):
    SOCIAL = 0
    SITE = 1


class PromptOverwriteTypeStrings(Enum):
    SOCIAL = "social"
    SITE = "site"


class ProvisionMethod(Enum):
    DEVICE = 0
    PAPER_KEY = 1
    PASSPHRASE = 2
    GPG_IMPORT = 3
    GPG_SIGN = 4


class ProvisionMethodStrings(Enum):
    DEVICE = "device"
    PAPER_KEY = "paper_key"
    PASSPHRASE = "passphrase"
    GPG_IMPORT = "gpg_import"
    GPG_SIGN = "gpg_sign"


class GPGMethod(Enum):
    GPG_NONE = 0
    GPG_IMPORT = 1
    GPG_SIGN = 2


class GPGMethodStrings(Enum):
    GPG_NONE = "gpg_none"
    GPG_IMPORT = "gpg_import"
    GPG_SIGN = "gpg_sign"


class ChooseType(Enum):
    EXISTING_DEVICE = 0
    NEW_DEVICE = 1


class ChooseTypeStrings(Enum):
    EXISTING_DEVICE = "existing_device"
    NEW_DEVICE = "new_device"


@dataclass
class SecretResponse(DataClassJsonMixin):
    secret: str = field(metadata=config(field_name="secret"))
    phrase: str = field(metadata=config(field_name="phrase"))


class Reachable(Enum):
    UNKNOWN = 0
    YES = 1
    NO = 2


class ReachableStrings(Enum):
    UNKNOWN = "unknown"
    YES = "yes"
    NO = "no"


class Outcome(Enum):
    NONE = 0
    FIXED = 1
    IGNORED = 2


class OutcomeStrings(Enum):
    NONE = "none"
    FIXED = "fixed"
    IGNORED = "ignored"


class RekeyEventType(Enum):
    NONE = 0
    NOT_LOGGED_IN = 1
    API_ERROR = 2
    NO_PROBLEMS = 3
    LOAD_ME_ERROR = 4
    CURRENT_DEVICE_CAN_REKEY = 5
    DEVICE_LOAD_ERROR = 6
    HARASS = 7
    NO_GREGOR_MESSAGES = 8


class RekeyEventTypeStrings(Enum):
    NONE = "none"
    NOT_LOGGED_IN = "not_logged_in"
    API_ERROR = "api_error"
    NO_PROBLEMS = "no_problems"
    LOAD_ME_ERROR = "load_me_error"
    CURRENT_DEVICE_CAN_REKEY = "current_device_can_rekey"
    DEVICE_LOAD_ERROR = "device_load_error"
    HARASS = "harass"
    NO_GREGOR_MESSAGES = "no_gregor_messages"


SHA512 = str


class ResetType(Enum):
    NONE = 0
    RESET = 1
    DELETE = 2


class ResetTypeStrings(Enum):
    NONE = "none"
    RESET = "reset"
    DELETE = "delete"


class AuthenticityType(Enum):
    SIGNED = 0
    REPUDIABLE = 1
    ANONYMOUS = 2


class AuthenticityTypeStrings(Enum):
    SIGNED = "signed"
    REPUDIABLE = "repudiable"
    ANONYMOUS = "anonymous"


@dataclass
class SaltpackDecryptOptions(DataClassJsonMixin):
    interactive: bool = field(metadata=config(field_name="interactive"))
    force_remote_check: bool = field(metadata=config(field_name="forceRemoteCheck"))
    use_paper_key: bool = field(metadata=config(field_name="usePaperKey"))


@dataclass
class SaltpackSignOptions(DataClassJsonMixin):
    detached: bool = field(metadata=config(field_name="detached"))
    binary: bool = field(metadata=config(field_name="binary"))
    saltpack_version: int = field(metadata=config(field_name="saltpackVersion"))


@dataclass
class SaltpackVerifyOptions(DataClassJsonMixin):
    signed_by: str = field(metadata=config(field_name="signedBy"))
    signature: str = field(metadata=config(field_name="signature"))


@dataclass
class SaltpackEncryptResult(DataClassJsonMixin):
    used_unresolved_sbs: bool = field(metadata=config(field_name="usedUnresolvedSBS"))
    unresolved_sbs_assertion: str = field(
        metadata=config(field_name="unresolvedSBSAssertion")
    )


@dataclass
class SaltpackFrontendEncryptOptions(DataClassJsonMixin):
    signed: bool = field(metadata=config(field_name="signed"))
    include_self: bool = field(metadata=config(field_name="includeSelf"))
    recipients: Optional[List[str]] = field(
        default=None, metadata=config(field_name="recipients")
    )


@dataclass
class SaltpackEncryptStringResult(DataClassJsonMixin):
    used_unresolved_sbs: bool = field(metadata=config(field_name="usedUnresolvedSBS"))
    unresolved_sbs_assertion: str = field(
        metadata=config(field_name="unresolvedSBSAssertion")
    )
    ciphertext: str = field(metadata=config(field_name="ciphertext"))


@dataclass
class SaltpackEncryptFileResult(DataClassJsonMixin):
    used_unresolved_sbs: bool = field(metadata=config(field_name="usedUnresolvedSBS"))
    unresolved_sbs_assertion: str = field(
        metadata=config(field_name="unresolvedSBSAssertion")
    )
    filename: str = field(metadata=config(field_name="filename"))


class SaltpackSenderType(Enum):
    NOT_TRACKED = 0
    UNKNOWN = 1
    ANONYMOUS = 2
    TRACKING_BROKE = 3
    TRACKING_OK = 4
    SELF = 5
    REVOKED = 6
    EXPIRED = 7


class SaltpackSenderTypeStrings(Enum):
    NOT_TRACKED = "not_tracked"
    UNKNOWN = "unknown"
    ANONYMOUS = "anonymous"
    TRACKING_BROKE = "tracking_broke"
    TRACKING_OK = "tracking_ok"
    SELF = "self"
    REVOKED = "revoked"
    EXPIRED = "expired"


@dataclass
class SecretEntryArg(DataClassJsonMixin):
    desc: str = field(metadata=config(field_name="desc"))
    prompt: str = field(metadata=config(field_name="prompt"))
    err: str = field(metadata=config(field_name="err"))
    cancel: str = field(metadata=config(field_name="cancel"))
    ok: str = field(metadata=config(field_name="ok"))
    reason: str = field(metadata=config(field_name="reason"))
    show_typing: bool = field(metadata=config(field_name="showTyping"))


@dataclass
class SecretEntryRes(DataClassJsonMixin):
    text: str = field(metadata=config(field_name="text"))
    canceled: bool = field(metadata=config(field_name="canceled"))
    store_secret: bool = field(metadata=config(field_name="storeSecret"))


NaclSigningKeyPublic = Optional[str]
NaclSigningKeyPrivate = Optional[str]
NaclDHKeyPublic = Optional[str]
NaclDHKeyPrivate = Optional[str]


@dataclass
class SignupRes(DataClassJsonMixin):
    passphrase_ok: bool = field(metadata=config(field_name="passphraseOk"))
    post_ok: bool = field(metadata=config(field_name="postOk"))
    write_ok: bool = field(metadata=config(field_name="writeOk"))
    paper_key: str = field(metadata=config(field_name="paperKey"))


@dataclass
class SigTypes(DataClassJsonMixin):
    track: bool = field(metadata=config(field_name="track"))
    proof: bool = field(metadata=config(field_name="proof"))
    cryptocurrency: bool = field(metadata=config(field_name="cryptocurrency"))
    is_self: bool = field(metadata=config(field_name="isSelf"))


OpID = Optional[str]
KBFSRevision = int


class KBFSArchivedType(Enum):
    REVISION = 0
    TIME = 1
    TIME_STRING = 2
    REL_TIME_STRING = 3


class KBFSArchivedTypeStrings(Enum):
    REVISION = "revision"
    TIME = "time"
    TIME_STRING = "time_string"
    REL_TIME_STRING = "rel_time_string"


class PathType(Enum):
    LOCAL = 0
    KBFS = 1
    KBFS_ARCHIVED = 2


class PathTypeStrings(Enum):
    LOCAL = "local"
    KBFS = "kbfs"
    KBFS_ARCHIVED = "kbfs_archived"


class DirentType(Enum):
    FILE = 0
    DIR = 1
    SYM = 2
    EXEC = 3


class DirentTypeStrings(Enum):
    FILE = "file"
    DIR = "dir"
    SYM = "sym"
    EXEC = "exec"


class PrefetchStatus(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETE = 2


class PrefetchStatusStrings(Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETE = "complete"


class RevisionSpanType(Enum):
    DEFAULT = 0
    LAST_FIVE = 1


class RevisionSpanTypeStrings(Enum):
    DEFAULT = "default"
    LAST_FIVE = "last_five"


ErrorNum = int


class OpenFlags(Enum):
    READ = 0
    REPLACE = 1
    EXISTING = 2
    WRITE = 4
    APPEND = 8
    DIRECTORY = 16


class OpenFlagsStrings(Enum):
    READ = "read"
    REPLACE = "replace"
    EXISTING = "existing"
    WRITE = "write"
    APPEND = "append"
    DIRECTORY = "directory"


Progress = int


class AsyncOps(Enum):
    LIST = 0
    LIST_RECURSIVE = 1
    READ = 2
    WRITE = 3
    COPY = 4
    MOVE = 5
    REMOVE = 6
    LIST_RECURSIVE_TO_DEPTH = 7
    GET_REVISIONS = 8


class AsyncOpsStrings(Enum):
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
    NO_FILTER = 0
    FILTER_ALL_HIDDEN = 1
    FILTER_SYSTEM_HIDDEN = 2


class ListFilterStrings(Enum):
    NO_FILTER = "no_filter"
    FILTER_ALL_HIDDEN = "filter_all_hidden"
    FILTER_SYSTEM_HIDDEN = "filter_system_hidden"


@dataclass
class SimpleFSQuotaUsage(DataClassJsonMixin):
    usage_bytes: int = field(metadata=config(field_name="usageBytes"))
    archive_bytes: int = field(metadata=config(field_name="archiveBytes"))
    limit_bytes: int = field(metadata=config(field_name="limitBytes"))
    git_usage_bytes: int = field(metadata=config(field_name="gitUsageBytes"))
    git_archive_bytes: int = field(metadata=config(field_name="gitArchiveBytes"))
    git_limit_bytes: int = field(metadata=config(field_name="gitLimitBytes"))


class FolderSyncMode(Enum):
    DISABLED = 0
    ENABLED = 1
    PARTIAL = 2


class FolderSyncModeStrings(Enum):
    DISABLED = "disabled"
    ENABLED = "enabled"
    PARTIAL = "partial"


class KbfsOnlineStatus(Enum):
    OFFLINE = 0
    TRYING = 1
    ONLINE = 2


class KbfsOnlineStatusStrings(Enum):
    OFFLINE = "offline"
    TRYING = "trying"
    ONLINE = "online"


@dataclass
class FSSettings(DataClassJsonMixin):
    space_available_notification_threshold: int = field(
        metadata=config(field_name="spaceAvailableNotificationThreshold")
    )
    sfmi_banner_dismissed: bool = field(
        metadata=config(field_name="sfmiBannerDismissed")
    )
    sync_on_cellular: bool = field(metadata=config(field_name="syncOnCellular"))


class SubscriptionTopic(Enum):
    FAVORITES = 0
    JOURNAL_STATUS = 1
    ONLINE_STATUS = 2
    DOWNLOAD_STATUS = 3
    FILES_TAB_BADGE = 4
    OVERALL_SYNC_STATUS = 5
    SETTINGS = 6
    UPLOAD_STATUS = 7


class SubscriptionTopicStrings(Enum):
    FAVORITES = "favorites"
    JOURNAL_STATUS = "journal_status"
    ONLINE_STATUS = "online_status"
    DOWNLOAD_STATUS = "download_status"
    FILES_TAB_BADGE = "files_tab_badge"
    OVERALL_SYNC_STATUS = "overall_sync_status"
    SETTINGS = "settings"
    UPLOAD_STATUS = "upload_status"


class PathSubscriptionTopic(Enum):
    CHILDREN = 0
    STAT = 1


class PathSubscriptionTopicStrings(Enum):
    CHILDREN = "children"
    STAT = "stat"


class FilesTabBadge(Enum):
    NONE = 0
    UPLOADING_STUCK = 1
    AWAITING_UPLOAD = 2
    UPLOADING = 3


class FilesTabBadgeStrings(Enum):
    NONE = "none"
    UPLOADING_STUCK = "uploading_stuck"
    AWAITING_UPLOAD = "awaiting_upload"
    UPLOADING = "uploading"


class GUIViewType(Enum):
    DEFAULT = 0
    TEXT = 1
    IMAGE = 2
    AUDIO = 3
    VIDEO = 4
    PDF = 5


class GUIViewTypeStrings(Enum):
    DEFAULT = "default"
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    PDF = "pdf"


@dataclass
class SimpleFSSearchHit(DataClassJsonMixin):
    path: str = field(metadata=config(field_name="path"))


TeambotKeyGeneration = int


class TeamRole(Enum):
    NONE = 0
    READER = 1
    WRITER = 2
    ADMIN = 3
    OWNER = 4
    BOT = 5
    RESTRICTEDBOT = 6


class TeamRoleStrings(Enum):
    NONE = "none"
    READER = "reader"
    WRITER = "writer"
    ADMIN = "admin"
    OWNER = "owner"
    BOT = "bot"
    RESTRICTEDBOT = "restrictedbot"


class TeamApplication(Enum):
    KBFS = 1
    CHAT = 2
    SALTPACK = 3
    GIT_METADATA = 4
    SEITAN_INVITE_TOKEN = 5
    STELLAR_RELAY = 6
    KVSTORE = 7


class TeamApplicationStrings(Enum):
    KBFS = "kbfs"
    CHAT = "chat"
    SALTPACK = "saltpack"
    GIT_METADATA = "git_metadata"
    SEITAN_INVITE_TOKEN = "seitan_invite_token"
    STELLAR_RELAY = "stellar_relay"
    KVSTORE = "kvstore"


class TeamStatus(Enum):
    NONE = 0
    LIVE = 1
    DELETED = 2
    ABANDONED = 3


class TeamStatusStrings(Enum):
    NONE = "none"
    LIVE = "live"
    DELETED = "deleted"
    ABANDONED = "abandoned"


class AuditMode(Enum):
    STANDARD = 0
    JUST_CREATED = 1
    SKIP = 2
    STANDARD_NO_HIDDEN = 3


class AuditModeStrings(Enum):
    STANDARD = "standard"
    JUST_CREATED = "just_created"
    SKIP = "skip"
    STANDARD_NO_HIDDEN = "standard_no_hidden"


PerTeamKeyGeneration = int


class PTKType(Enum):
    READER = 0


class PTKTypeStrings(Enum):
    READER = "reader"


class PerTeamSeedCheckVersion(Enum):
    V1 = 1


class PerTeamSeedCheckVersionStrings(Enum):
    V1 = "v1"


PerTeamSeedCheckValue = str
PerTeamSeedCheckValuePostImage = str
MaskB64 = str
TeamInviteID = str
TeamInviteMaxUses = int
PerTeamKeySeed = Optional[str]


class TeamMemberStatus(Enum):
    ACTIVE = 0
    RESET = 1
    DELETED = 2


class TeamMemberStatusStrings(Enum):
    ACTIVE = "active"
    RESET = "reset"
    DELETED = "deleted"


UserVersionPercentForm = str


class RatchetType(Enum):
    MAIN = 0
    BLINDED = 1
    SELF = 2
    UNCOMMITTED = 3


class RatchetTypeStrings(Enum):
    MAIN = "main"
    BLINDED = "blinded"
    SELF = "self"
    UNCOMMITTED = "uncommitted"


class AuditVersion(Enum):
    V0 = 0
    V1 = 1
    V2 = 2
    V3 = 3
    V4 = 4


class AuditVersionStrings(Enum):
    V0 = "v0"
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"
    V4 = "v4"


class TeamInviteCategory(Enum):
    NONE = 0
    UNKNOWN = 1
    KEYBASE = 2
    EMAIL = 3
    SBS = 4
    SEITAN = 5
    PHONE = 6
    INVITELINK = 7


class TeamInviteCategoryStrings(Enum):
    NONE = "none"
    UNKNOWN = "unknown"
    KEYBASE = "keybase"
    EMAIL = "email"
    SBS = "sbs"
    SEITAN = "seitan"
    PHONE = "phone"
    INVITELINK = "invitelink"


TeamInviteSocialNetwork = str
TeamInviteName = str
TeamInviteDisplayName = str


@dataclass
class TeamEncryptedKBFSKeyset(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    e: str = field(metadata=config(field_name="e"))
    n: str = field(metadata=config(field_name="n"))


TeamEncryptedKBFSKeysetHash = str
BoxSummaryHash = str
TeamNamePart = str
SeitanAKey = str
SeitanIKey = str
SeitanIKeyInvitelink = str
SeitanPubKey = str
SeitanIKeyV2 = str


class SeitanKeyAndLabelVersion(Enum):
    V1 = 1
    V2 = 2
    Invitelink = 3


class SeitanKeyAndLabelVersionStrings(Enum):
    V1 = "v1"
    V2 = "v2"
    Invitelink = "invitelink"


class SeitanKeyLabelType(Enum):
    SMS = 1
    GENERIC = 2


class SeitanKeyLabelTypeStrings(Enum):
    SMS = "sms"
    GENERIC = "generic"


@dataclass
class SeitanKeyLabelSms(DataClassJsonMixin):
    f: str = field(metadata=config(field_name="f"))
    n: str = field(metadata=config(field_name="n"))


@dataclass
class SeitanKeyLabelGeneric(DataClassJsonMixin):
    l: str = field(metadata=config(field_name="l"))


@dataclass
class TeamBotSettings(DataClassJsonMixin):
    cmds: bool = field(metadata=config(field_name="cmds"))
    mentions: bool = field(metadata=config(field_name="mentions"))
    triggers: Optional[List[str]] = field(
        default=None, metadata=config(field_name="triggers")
    )
    convs: Optional[List[str]] = field(
        default=None, metadata=config(field_name="convs")
    )


@dataclass
class TeamRequestAccessResult(DataClassJsonMixin):
    open: bool = field(metadata=config(field_name="open"))


@dataclass
class TeamAcceptOrRequestResult(DataClassJsonMixin):
    was_token: bool = field(metadata=config(field_name="wasToken"))
    was_seitan: bool = field(metadata=config(field_name="wasSeitan"))
    was_team_name: bool = field(metadata=config(field_name="wasTeamName"))
    was_open_team: bool = field(metadata=config(field_name="wasOpenTeam"))


@dataclass
class BulkRes(DataClassJsonMixin):
    malformed: Optional[List[str]] = field(
        default=None, metadata=config(field_name="malformed")
    )


ConflictGeneration = int


@dataclass
class TeamOperation(DataClassJsonMixin):
    change_open_team: bool = field(metadata=config(field_name="changeOpenTeam"))
    manage_members: bool = field(metadata=config(field_name="manageMembers"))
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
    manage_subteams: bool = field(metadata=config(field_name="manageSubteams"))
    leave_team: bool = field(metadata=config(field_name="leaveTeam"))
    join_team: bool = field(metadata=config(field_name="joinTeam"))
    set_publicity_any: bool = field(metadata=config(field_name="setPublicityAny"))
    list_first: bool = field(metadata=config(field_name="listFirst"))
    change_tars_disabled: bool = field(metadata=config(field_name="changeTarsDisabled"))
    delete_chat_history: bool = field(metadata=config(field_name="deleteChatHistory"))
    delete_other_emojis: bool = field(metadata=config(field_name="deleteOtherEmojis"))
    delete_other_messages: bool = field(
        metadata=config(field_name="deleteOtherMessages")
    )
    delete_team: bool = field(metadata=config(field_name="deleteTeam"))
    pin_message: bool = field(metadata=config(field_name="pinMessage"))
    manage_bots: bool = field(metadata=config(field_name="manageBots"))
    manage_emojis: bool = field(metadata=config(field_name="manageEmojis"))


@dataclass
class ProfileTeamLoadRes(DataClassJsonMixin):
    load_time_nsec: int = field(metadata=config(field_name="loadTimeNsec"))


class RotationType(Enum):
    VISIBLE = 0
    HIDDEN = 1
    CLKR = 2


class RotationTypeStrings(Enum):
    VISIBLE = "visible"
    HIDDEN = "hidden"
    CLKR = "clkr"


@dataclass
class MemberEmail(DataClassJsonMixin):
    email: str = field(metadata=config(field_name="email"))
    role: str = field(metadata=config(field_name="role"))


@dataclass
class MemberUsername(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    role: str = field(metadata=config(field_name="role"))


UserTeamVersion = int


class TeamTreeMembershipStatus(Enum):
    OK = 0
    ERROR = 1
    HIDDEN = 2


class TeamTreeMembershipStatusStrings(Enum):
    OK = "ok"
    ERROR = "error"
    HIDDEN = "hidden"


@dataclass
class TeamTreeError(DataClassJsonMixin):
    message: str = field(metadata=config(field_name="message"))
    will_skip_subtree: bool = field(metadata=config(field_name="willSkipSubtree"))
    will_skip_ancestors: bool = field(metadata=config(field_name="willSkipAncestors"))


@dataclass
class TeamTreeInitial(DataClassJsonMixin):
    guid: int = field(metadata=config(field_name="guid"))


@dataclass
class Test(DataClassJsonMixin):
    reply: str = field(metadata=config(field_name="reply"))


class TLFIdentifyBehavior(Enum):
    UNSET = 0
    CHAT_CLI = 1
    CHAT_GUI = 2
    REMOVED_AND_UNUSED = 3
    KBFS_REKEY = 4
    KBFS_QR = 5
    CHAT_SKIP = 6
    SALTPACK = 7
    CLI = 8
    GUI = 9
    DEFAULT_KBFS = 10
    KBFS_CHAT = 11
    RESOLVE_AND_CHECK = 12
    GUI_PROFILE = 13
    KBFS_INIT = 14
    FS_GUI = 15


class TLFIdentifyBehaviorStrings(Enum):
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
    NONE = 0
    YES = 1
    NO = 2


class PromptDefaultStrings(Enum):
    NONE = "none"
    YES = "yes"
    NO = "no"


class KeyType(Enum):
    NONE = 0
    NACL = 1
    PGP = 2


class KeyTypeStrings(Enum):
    NONE = "none"
    NACL = "nacl"
    PGP = "pgp"


class UPK2MinorVersion(Enum):
    V0 = 0
    V1 = 1
    V2 = 2
    V3 = 3
    V4 = 4
    V5 = 5
    V6 = 6


class UPK2MinorVersionStrings(Enum):
    V0 = "v0"
    V1 = "v1"
    V2 = "v2"
    V3 = "v3"
    V4 = "v4"
    V5 = "v5"
    V6 = "v6"


PGPFingerprint = Optional[str]


class UPAKVersion(Enum):
    V1 = 1
    V2 = 2


class UPAKVersionStrings(Enum):
    V1 = "v1"
    V2 = "v2"


class UPKLiteMinorVersion(Enum):
    V0 = 0


class UPKLiteMinorVersionStrings(Enum):
    V0 = "v0"


@dataclass
class TrackProof(DataClassJsonMixin):
    proof_type: str = field(metadata=config(field_name="proofType"))
    proof_name: str = field(metadata=config(field_name="proofName"))
    id_string: str = field(metadata=config(field_name="idString"))


@dataclass
class WebProof(DataClassJsonMixin):
    hostname: str = field(metadata=config(field_name="hostname"))
    protocols: Optional[List[str]] = field(
        default=None, metadata=config(field_name="protocols")
    )


EmailAddress = str


class PassphraseState(Enum):
    """
    PassphraseState values are used in .config.json, so should not be changed without a migration strategy
    """

    KNOWN = 0
    RANDOM = 1


class PassphraseStateStrings(Enum):
    KNOWN = "known"
    RANDOM = "random"


class UserBlockType(Enum):
    CHAT = 0
    FOLLOW = 1


class UserBlockTypeStrings(Enum):
    CHAT = "chat"
    FOLLOW = "follow"


@dataclass
class UserBlockArg(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    set_chat_block: Optional[bool] = field(
        default=None, metadata=config(field_name="setChatBlock")
    )
    set_follow_block: Optional[bool] = field(
        default=None, metadata=config(field_name="setFollowBlock")
    )


APIUserServiceID = str


@dataclass
class ImpTofuSearchResult(DataClassJsonMixin):
    assertion: str = field(metadata=config(field_name="assertion"))
    assertion_value: str = field(metadata=config(field_name="assertionValue"))
    assertion_key: str = field(metadata=config(field_name="assertionKey"))
    label: str = field(metadata=config(field_name="label"))
    pretty_name: str = field(metadata=config(field_name="prettyName"))
    keybase_username: str = field(metadata=config(field_name="keybaseUsername"))


@dataclass
class EmailOrPhoneNumberSearchResult(DataClassJsonMixin):
    input: str = field(metadata=config(field_name="input"))
    assertion: str = field(metadata=config(field_name="assertion"))
    assertion_value: str = field(metadata=config(field_name="assertionValue"))
    assertion_key: str = field(metadata=config(field_name="assertionKey"))
    found_user: bool = field(metadata=config(field_name="foundUser"))
    username: str = field(metadata=config(field_name="username"))
    full_name: str = field(metadata=config(field_name="fullName"))


UsernameVerificationType = str


class WotReactionType(Enum):
    ACCEPT = 0
    REJECT = 1


class WotReactionTypeStrings(Enum):
    ACCEPT = "accept"
    REJECT = "reject"


@dataclass
class LockdownHistory(DataClassJsonMixin):
    status: bool = field(metadata=config(field_name="status"))
    creation_time: Time = field(metadata=config(field_name="ctime"))
    device_id: DeviceID = field(metadata=config(field_name="device_id"))
    device_name: str = field(metadata=config(field_name="deviceName"))


@dataclass
class TeamContactSettings(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    enabled: bool = field(metadata=config(field_name="enabled"))


@dataclass
class AirdropDetails(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    kid: BinaryKID = field(metadata=config(field_name="kid"))
    vid: VID = field(metadata=config(field_name="vid"))
    vers: str = field(metadata=config(field_name="vers"))
    time: Time = field(metadata=config(field_name="time"))


@dataclass
class BoxAuditAttempt(DataClassJsonMixin):
    ctime: UnixTime = field(metadata=config(field_name="ctime"))
    result: BoxAuditAttemptResult = field(metadata=config(field_name="result"))
    rotated: bool = field(metadata=config(field_name="rotated"))
    error: Optional[str] = field(default=None, metadata=config(field_name="error"))
    generation: Optional[PerTeamKeyGeneration] = field(
        default=None, metadata=config(field_name="generation")
    )


@dataclass
class LoadAvatarsRes(DataClassJsonMixin):
    picmap: Dict[str, Dict[str, AvatarUrl]] = field(
        metadata=config(field_name="picmap")
    )


@dataclass
class AvatarClearCacheMsg(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    typ: AvatarUpdateType = field(metadata=config(field_name="typ"))
    formats: Optional[List[AvatarFormat]] = field(
        default=None, metadata=config(field_name="formats")
    )


@dataclass
class BlockIdCombo(DataClassJsonMixin):
    block_hash: str = field(metadata=config(field_name="blockHash"))
    charged_to: UserOrTeamID = field(metadata=config(field_name="chargedTo"))
    block_type: BlockType = field(metadata=config(field_name="blockType"))


@dataclass
class GetBlockRes(DataClassJsonMixin):
    block_key: str = field(metadata=config(field_name="blockKey"))
    buf: str = field(metadata=config(field_name="buf"))
    size: int = field(metadata=config(field_name="size"))
    status: BlockStatus = field(metadata=config(field_name="status"))


@dataclass
class GetBlockSizesRes(DataClassJsonMixin):
    sizes: Optional[List[int]] = field(
        default=None, metadata=config(field_name="sizes")
    )
    statuses: Optional[List[BlockStatus]] = field(
        default=None, metadata=config(field_name="statuses")
    )


@dataclass
class UsageStat(DataClassJsonMixin):
    bytes: UsageStatRecord = field(metadata=config(field_name="bytes"))
    blocks: UsageStatRecord = field(metadata=config(field_name="blocks"))
    mtime: Time = field(metadata=config(field_name="mtime"))


@dataclass
class BotTokenInfo(DataClassJsonMixin):
    token: BotToken = field(metadata=config(field_name="bot_token"))
    ctime: Time = field(metadata=config(field_name="ctime"))


@dataclass
class Status(DataClassJsonMixin):
    code: int = field(metadata=config(field_name="code"))
    name: str = field(metadata=config(field_name="name"))
    desc: str = field(metadata=config(field_name="desc"))
    fields: Optional[List[StringKVPair]] = field(
        default=None, metadata=config(field_name="fields")
    )


@dataclass
class UserVersion(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))


@dataclass
class CompatibilityTeamID__LEGACY(DataClassJsonMixin):
    typ: Literal[TeamTypeStrings.LEGACY]
    LEGACY: Optional[TLFID]


@dataclass
class CompatibilityTeamID__MODERN(DataClassJsonMixin):
    typ: Literal[TeamTypeStrings.MODERN]
    MODERN: Optional[TeamID]


CompatibilityTeamID = Union[CompatibilityTeamID__LEGACY, CompatibilityTeamID__MODERN]


@dataclass
class TeamIDWithVisibility(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    visibility: TLFVisibility = field(metadata=config(field_name="visibility"))


@dataclass
class PublicKey(DataClassJsonMixin):
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    kid: KID = field(metadata=config(field_name="KID"))
    e_time: Time = field(metadata=config(field_name="eTime"))
    is_sibkey: bool = field(metadata=config(field_name="isSibkey"))
    is_eldest: bool = field(metadata=config(field_name="isEldest"))
    parent_id: str = field(metadata=config(field_name="parentID"))
    pgp_fingerprint: str = field(metadata=config(field_name="PGPFingerprint"))
    device_description: str = field(metadata=config(field_name="deviceDescription"))
    device_type: DeviceTypeV2 = field(metadata=config(field_name="deviceType"))
    c_time: Time = field(metadata=config(field_name="cTime"))
    is_revoked: bool = field(metadata=config(field_name="isRevoked"))
    pgp_identities: Optional[List[PGPIdentity]] = field(
        default=None, metadata=config(field_name="PGPIdentities")
    )


@dataclass
class KeybaseTime(DataClassJsonMixin):
    unix: Time = field(metadata=config(field_name="unix"))
    chain: Seqno = field(metadata=config(field_name="chain"))


@dataclass
class User(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))


@dataclass
class Device(DataClassJsonMixin):
    type: DeviceTypeV2 = field(metadata=config(field_name="type"))
    name: str = field(metadata=config(field_name="name"))
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    device_number_of_type: int = field(metadata=config(field_name="deviceNumberOfType"))
    c_time: Time = field(metadata=config(field_name="cTime"))
    m_time: Time = field(metadata=config(field_name="mTime"))
    last_used_time: Time = field(metadata=config(field_name="lastUsedTime"))
    encrypt_key: KID = field(metadata=config(field_name="encryptKey"))
    verify_key: KID = field(metadata=config(field_name="verifyKey"))
    status: int = field(metadata=config(field_name="status"))


@dataclass
class UserVersionVector(DataClassJsonMixin):
    id: int = field(metadata=config(field_name="id"))
    sig_hints: int = field(metadata=config(field_name="sigHints"))
    sig_chain: int = field(metadata=config(field_name="sigChain"))
    cached_at: Time = field(metadata=config(field_name="cachedAt"))


@dataclass
class PerUserKey(DataClassJsonMixin):
    gen: int = field(metadata=config(field_name="gen"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    sig_kid: KID = field(metadata=config(field_name="sigKID"))
    enc_kid: KID = field(metadata=config(field_name="encKID"))
    signed_by_kid: KID = field(metadata=config(field_name="signedByKID"))


@dataclass
class UserOrTeamLite(DataClassJsonMixin):
    id: UserOrTeamID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))


@dataclass
class RemoteTrack(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    uid: UID = field(metadata=config(field_name="uid"))
    link_id: LinkID = field(metadata=config(field_name="linkID"))


@dataclass
class SocialAssertion(DataClassJsonMixin):
    user: str = field(metadata=config(field_name="user"))
    service: SocialAssertionService = field(metadata=config(field_name="service"))


@dataclass
class FullNamePackage(DataClassJsonMixin):
    version: FullNamePackageVersion = field(metadata=config(field_name="version"))
    full_name: FullName = field(metadata=config(field_name="fullName"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    status: StatusCode = field(metadata=config(field_name="status"))
    cached_at: Time = field(metadata=config(field_name="cachedAt"))


@dataclass
class PhoneLookupResult(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    ctime: UnixTime = field(metadata=config(field_name="ctime"))


@dataclass
class UserReacjis(DataClassJsonMixin):
    skin_tone: ReacjiSkinTone = field(metadata=config(field_name="skinTone"))
    top_reacjis: Optional[List[UserReacji]] = field(
        default=None, metadata=config(field_name="topReacjis")
    )


@dataclass
class ClientDetails(DataClassJsonMixin):
    pid: int = field(metadata=config(field_name="pid"))
    client_type: ClientType = field(metadata=config(field_name="clientType"))
    desc: str = field(metadata=config(field_name="desc"))
    version: str = field(metadata=config(field_name="version"))
    argv: Optional[List[str]] = field(default=None, metadata=config(field_name="argv"))


@dataclass
class Config(DataClassJsonMixin):
    path: str = field(metadata=config(field_name="path"))
    server_uri: str = field(metadata=config(field_name="serverURI"))
    label: str = field(metadata=config(field_name="label"))
    run_mode: str = field(metadata=config(field_name="runMode"))
    gpg_exists: bool = field(metadata=config(field_name="gpgExists"))
    gpg_path: str = field(metadata=config(field_name="gpgPath"))
    version: str = field(metadata=config(field_name="version"))
    socket_file: str = field(metadata=config(field_name="socketFile"))
    binary_realpath: str = field(metadata=config(field_name="binaryRealpath"))
    config_path: str = field(metadata=config(field_name="configPath"))
    version_short: str = field(metadata=config(field_name="versionShort"))
    version_full: str = field(metadata=config(field_name="versionFull"))
    is_auto_forked: bool = field(metadata=config(field_name="isAutoForked"))
    fork_type: ForkType = field(metadata=config(field_name="forkType"))


@dataclass
class UpdateInfo(DataClassJsonMixin):
    status: UpdateInfoStatus = field(metadata=config(field_name="status"))
    message: str = field(metadata=config(field_name="message"))


@dataclass
class UpdateInfo2__OK(DataClassJsonMixin):
    status: Literal[UpdateInfoStatus2Strings.OK]
    OK: None


@dataclass
class UpdateInfo2__SUGGESTED(DataClassJsonMixin):
    status: Literal[UpdateInfoStatus2Strings.SUGGESTED]
    SUGGESTED: Optional[UpdateDetails]


@dataclass
class UpdateInfo2__CRITICAL(DataClassJsonMixin):
    status: Literal[UpdateInfoStatus2Strings.CRITICAL]
    CRITICAL: Optional[UpdateDetails]


UpdateInfo2 = Union[UpdateInfo2__OK, UpdateInfo2__SUGGESTED, UpdateInfo2__CRITICAL]


@dataclass
class ProxyData(DataClassJsonMixin):
    address_with_port: str = field(metadata=config(field_name="addressWithPort"))
    proxy_type: ProxyType = field(metadata=config(field_name="proxyType"))
    cert_pinning: bool = field(metadata=config(field_name="certPinning"))


@dataclass
class ContactComponent(DataClassJsonMixin):
    label: str = field(metadata=config(field_name="label"))
    phone_number: Optional[RawPhoneNumber] = field(
        default=None, metadata=config(field_name="phoneNumber")
    )
    email: Optional[EmailAddress] = field(
        default=None, metadata=config(field_name="email")
    )


@dataclass
class ED25519SignatureInfo(DataClassJsonMixin):
    sig: ED25519Signature = field(metadata=config(field_name="sig"))
    public_key: ED25519PublicKey = field(metadata=config(field_name="publicKey"))


@dataclass
class CiphertextBundle(DataClassJsonMixin):
    kid: KID = field(metadata=config(field_name="kid"))
    ciphertext: EncryptedBytes32 = field(metadata=config(field_name="ciphertext"))
    nonce: BoxNonce = field(metadata=config(field_name="nonce"))
    public_key: BoxPublicKey = field(metadata=config(field_name="publicKey"))


@dataclass
class UnboxAnyRes(DataClassJsonMixin):
    kid: KID = field(metadata=config(field_name="kid"))
    plaintext: Bytes32 = field(metadata=config(field_name="plaintext"))
    index: int = field(metadata=config(field_name="index"))


@dataclass
class DbKey(DataClassJsonMixin):
    db_type: DbType = field(metadata=config(field_name="dbType"))
    obj_type: int = field(metadata=config(field_name="objType"))
    key: str = field(metadata=config(field_name="key"))


@dataclass
class EmailLookupResult(DataClassJsonMixin):
    email: EmailAddress = field(metadata=config(field_name="email"))
    uid: Optional[UID] = field(default=None, metadata=config(field_name="uid"))


@dataclass
class EmailAddressVerifiedMsg(DataClassJsonMixin):
    email: EmailAddress = field(metadata=config(field_name="email"))


@dataclass
class EmailAddressChangedMsg(DataClassJsonMixin):
    email: EmailAddress = field(metadata=config(field_name="email"))


@dataclass
class DeviceEkMetadata(DataClassJsonMixin):
    kid: KID = field(metadata=config(field_name="device_ephemeral_dh_public"))
    hash_meta: HashMeta = field(metadata=config(field_name="hash_meta"))
    generation: EkGeneration = field(metadata=config(field_name="generation"))
    ctime: Time = field(metadata=config(field_name="ctime"))
    device_ctime: Time = field(metadata=config(field_name="deviceCtime"))


@dataclass
class UserEkMetadata(DataClassJsonMixin):
    kid: KID = field(metadata=config(field_name="user_ephemeral_dh_public"))
    hash_meta: HashMeta = field(metadata=config(field_name="hash_meta"))
    generation: EkGeneration = field(metadata=config(field_name="generation"))
    ctime: Time = field(metadata=config(field_name="ctime"))


@dataclass
class UserEkBoxMetadata(DataClassJsonMixin):
    box: str = field(metadata=config(field_name="box"))
    recipient_generation: EkGeneration = field(
        metadata=config(field_name="recipient_generation")
    )
    recipient_device_id: DeviceID = field(
        metadata=config(field_name="recipient_device_id")
    )


@dataclass
class TeamEkMetadata(DataClassJsonMixin):
    kid: KID = field(metadata=config(field_name="team_ephemeral_dh_public"))
    hash_meta: HashMeta = field(metadata=config(field_name="hash_meta"))
    generation: EkGeneration = field(metadata=config(field_name="generation"))
    ctime: Time = field(metadata=config(field_name="ctime"))


@dataclass
class TeamEkBoxMetadata(DataClassJsonMixin):
    box: str = field(metadata=config(field_name="box"))
    recipient_generation: EkGeneration = field(
        metadata=config(field_name="recipient_generation")
    )
    recipient_uid: UID = field(metadata=config(field_name="recipient_uid"))


@dataclass
class TeambotEkMetadata(DataClassJsonMixin):
    kid: KID = field(metadata=config(field_name="teambot_dh_public"))
    generation: EkGeneration = field(metadata=config(field_name="generation"))
    uid: UID = field(metadata=config(field_name="uid"))
    user_ek_generation: EkGeneration = field(
        metadata=config(field_name="user_ek_generation")
    )
    hash_meta: HashMeta = field(metadata=config(field_name="hash_meta"))
    ctime: Time = field(metadata=config(field_name="ctime"))


@dataclass
class FolderHandle(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    folder_type: FolderType = field(metadata=config(field_name="folderType"))
    created: bool = field(metadata=config(field_name="created"))


@dataclass
class FeaturedBotsRes(DataClassJsonMixin):
    is_last_page: bool = field(metadata=config(field_name="isLastPage"))
    bots: Optional[List[FeaturedBot]] = field(
        default=None, metadata=config(field_name="bots")
    )


@dataclass
class SearchRes(DataClassJsonMixin):
    is_last_page: bool = field(metadata=config(field_name="isLastPage"))
    bots: Optional[List[FeaturedBot]] = field(
        default=None, metadata=config(field_name="bots")
    )


@dataclass
class ListResult(DataClassJsonMixin):
    files: Optional[List[File]] = field(
        default=None, metadata=config(field_name="files")
    )


@dataclass
class EncryptedGitMetadata(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    e: str = field(metadata=config(field_name="e"))
    n: BoxNonce = field(metadata=config(field_name="n"))
    gen: PerTeamKeyGeneration = field(metadata=config(field_name="gen"))


@dataclass
class GitLocalMetadataV1(DataClassJsonMixin):
    repo_name: GitRepoName = field(metadata=config(field_name="repoName"))


@dataclass
class GitCommit(DataClassJsonMixin):
    commit_hash: str = field(metadata=config(field_name="commitHash"))
    message: str = field(metadata=config(field_name="message"))
    author_name: str = field(metadata=config(field_name="authorName"))
    author_email: str = field(metadata=config(field_name="authorEmail"))
    ctime: Time = field(metadata=config(field_name="ctime"))


@dataclass
class GitServerMetadata(DataClassJsonMixin):
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


@dataclass
class GPGKey(DataClassJsonMixin):
    algorithm: str = field(metadata=config(field_name="algorithm"))
    key_id: str = field(metadata=config(field_name="keyID"))
    creation: str = field(metadata=config(field_name="creation"))
    expiration: str = field(metadata=config(field_name="expiration"))
    identities: Optional[List[PGPIdentity]] = field(
        default=None, metadata=config(field_name="identities")
    )


@dataclass
class HomeScreenAnnouncement(DataClassJsonMixin):
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
class HomeScreenTodo__VERIFY_ALL_PHONE_NUMBER(DataClassJsonMixin):
    t: Literal[HomeScreenTodoTypeStrings.VERIFY_ALL_PHONE_NUMBER]
    VERIFY_ALL_PHONE_NUMBER: Optional[PhoneNumber]


@dataclass
class HomeScreenTodo__VERIFY_ALL_EMAIL(DataClassJsonMixin):
    t: Literal[HomeScreenTodoTypeStrings.VERIFY_ALL_EMAIL]
    VERIFY_ALL_EMAIL: Optional[EmailAddress]


@dataclass
class HomeScreenTodo__LEGACY_EMAIL_VISIBILITY(DataClassJsonMixin):
    t: Literal[HomeScreenTodoTypeStrings.LEGACY_EMAIL_VISIBILITY]
    LEGACY_EMAIL_VISIBILITY: Optional[EmailAddress]


HomeScreenTodo = Union[
    HomeScreenTodo__VERIFY_ALL_PHONE_NUMBER,
    HomeScreenTodo__VERIFY_ALL_EMAIL,
    HomeScreenTodo__LEGACY_EMAIL_VISIBILITY,
]


@dataclass
class VerifyAllEmailTodoExt(DataClassJsonMixin):
    last_verify_email_date: UnixTime = field(
        metadata=config(field_name="lastVerifyEmailDate")
    )


@dataclass
class HomeScreenPeopleNotificationContact(DataClassJsonMixin):
    resolve_time: Time = field(metadata=config(field_name="resolveTime"))
    username: str = field(metadata=config(field_name="username"))
    description: str = field(metadata=config(field_name="description"))
    resolved_contact_blob: str = field(
        metadata=config(field_name="resolvedContactBlob")
    )


@dataclass
class HomeUserSummary(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    bio: str = field(metadata=config(field_name="bio"))
    full_name: str = field(metadata=config(field_name="full_name"))
    pics: Optional[Pics] = field(default=None, metadata=config(field_name="pics"))


@dataclass
class Identify3RowMeta(DataClassJsonMixin):
    color: Identify3RowColor = field(metadata=config(field_name="color"))
    label: str = field(metadata=config(field_name="label"))


@dataclass
class Identify3Summary(DataClassJsonMixin):
    gui_id: Identify3GUIID = field(metadata=config(field_name="guiID"))
    num_proofs_to_check: int = field(metadata=config(field_name="numProofsToCheck"))


@dataclass
class TrackDiff(DataClassJsonMixin):
    type: TrackDiffType = field(metadata=config(field_name="type"))
    display_markup: str = field(metadata=config(field_name="displayMarkup"))


@dataclass
class TrackSummary(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    time: Time = field(metadata=config(field_name="time"))
    is_remote: bool = field(metadata=config(field_name="isRemote"))


@dataclass
class TrackOptions(DataClassJsonMixin):
    local_only: bool = field(metadata=config(field_name="localOnly"))
    bypass_confirm: bool = field(metadata=config(field_name="bypassConfirm"))
    force_retrack: bool = field(metadata=config(field_name="forceRetrack"))
    expiring_local: bool = field(metadata=config(field_name="expiringLocal"))
    for_pgp_pull: bool = field(metadata=config(field_name="forPGPPull"))
    sig_version: Optional[SigVersion] = field(
        default=None, metadata=config(field_name="sigVersion")
    )


@dataclass
class IdentifyReason(DataClassJsonMixin):
    type: IdentifyReasonType = field(metadata=config(field_name="type"))
    reason: str = field(metadata=config(field_name="reason"))
    resource: str = field(metadata=config(field_name="resource"))


@dataclass
class RemoteProof(DataClassJsonMixin):
    proof_type: ProofType = field(metadata=config(field_name="proofType"))
    key: str = field(metadata=config(field_name="key"))
    value: str = field(metadata=config(field_name="value"))
    display_markup: str = field(metadata=config(field_name="displayMarkup"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))
    m_time: Time = field(metadata=config(field_name="mTime"))


@dataclass
class ProofResult(DataClassJsonMixin):
    state: ProofState = field(metadata=config(field_name="state"))
    status: ProofStatus = field(metadata=config(field_name="status"))
    desc: str = field(metadata=config(field_name="desc"))


@dataclass
class Cryptocurrency(DataClassJsonMixin):
    row_id: int = field(metadata=config(field_name="rowId"))
    pkhash: str = field(metadata=config(field_name="pkhash"))
    address: str = field(metadata=config(field_name="address"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))
    type: str = field(metadata=config(field_name="type"))
    family: str = field(metadata=config(field_name="family"))


@dataclass
class StellarAccount(DataClassJsonMixin):
    account_id: str = field(metadata=config(field_name="accountID"))
    federation_address: str = field(metadata=config(field_name="federationAddress"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))
    hidden: bool = field(metadata=config(field_name="hidden"))


@dataclass
class UserTeamShowcase(DataClassJsonMixin):
    fq_name: str = field(metadata=config(field_name="fq_name"))
    open: bool = field(metadata=config(field_name="open"))
    team_is_showcased: bool = field(metadata=config(field_name="team_is_showcased"))
    description: str = field(metadata=config(field_name="description"))
    role: TeamRole = field(metadata=config(field_name="role"))
    num_members: int = field(metadata=config(field_name="num_members"))
    public_admins: Optional[List[str]] = field(
        default=None, metadata=config(field_name="public_admins")
    )


@dataclass
class DismissReason(DataClassJsonMixin):
    type: DismissReasonType = field(metadata=config(field_name="type"))
    reason: str = field(metadata=config(field_name="reason"))
    resource: str = field(metadata=config(field_name="resource"))


@dataclass
class IncomingShareItem(DataClassJsonMixin):
    type: IncomingShareType = field(metadata=config(field_name="type"))
    original_path: str = field(metadata=config(field_name="originalPath"))
    original_size: int = field(metadata=config(field_name="originalSize"))
    scaled_path: Optional[str] = field(
        default=None, metadata=config(field_name="scaledPath")
    )
    scaled_size: Optional[int] = field(
        default=None, metadata=config(field_name="scaledSize")
    )
    thumbnail_path: Optional[str] = field(
        default=None, metadata=config(field_name="thumbnailPath")
    )
    content: Optional[str] = field(default=None, metadata=config(field_name="content"))


@dataclass
class KBFSTeamSettings(DataClassJsonMixin):
    tlf_id: TLFID = field(metadata=config(field_name="tlfID"))


@dataclass
class FSNotification(DataClassJsonMixin):
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


@dataclass
class FSFolderWriterEdit(DataClassJsonMixin):
    filename: str = field(metadata=config(field_name="filename"))
    notification_type: FSNotificationType = field(
        metadata=config(field_name="notificationType")
    )
    server_time: Time = field(metadata=config(field_name="serverTime"))


@dataclass
class FSPathSyncStatus(DataClassJsonMixin):
    folder_type: FolderType = field(metadata=config(field_name="folderType"))
    path: str = field(metadata=config(field_name="path"))
    syncing_bytes: int = field(metadata=config(field_name="syncingBytes"))
    syncing_ops: int = field(metadata=config(field_name="syncingOps"))
    synced_bytes: int = field(metadata=config(field_name="syncedBytes"))


@dataclass
class FSSyncStatus(DataClassJsonMixin):
    total_syncing_bytes: int = field(metadata=config(field_name="totalSyncingBytes"))
    syncing_paths: Optional[List[str]] = field(
        default=None, metadata=config(field_name="syncingPaths")
    )
    end_estimate: Optional[Time] = field(
        default=None, metadata=config(field_name="endEstimate")
    )


@dataclass
class GcOptions(DataClassJsonMixin):
    max_loose_refs: int = field(metadata=config(field_name="maxLooseRefs"))
    prune_min_loose_objects: int = field(
        metadata=config(field_name="pruneMinLooseObjects")
    )
    prune_expire_time: Time = field(metadata=config(field_name="pruneExpireTime"))
    max_object_packs: int = field(metadata=config(field_name="maxObjectPacks"))


@dataclass
class Hello2Res(DataClassJsonMixin):
    encryption_key: KID = field(metadata=config(field_name="encryptionKey"))
    sig_payload: HelloRes = field(metadata=config(field_name="sigPayload"))
    device_ek_kid: KID = field(metadata=config(field_name="deviceEkKID"))


@dataclass
class PerUserKeyBox(DataClassJsonMixin):
    generation: PerUserKeyGeneration = field(metadata=config(field_name="generation"))
    box: str = field(metadata=config(field_name="box"))
    receiver_kid: KID = field(metadata=config(field_name="receiver_kid"))


@dataclass
class KVEntryID(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    namespace: str = field(metadata=config(field_name="namespace"))
    entry_key: str = field(metadata=config(field_name="entryKey"))


@dataclass
class KVListEntryResult(DataClassJsonMixin):
    team_name: str = field(metadata=config(field_name="teamName"))
    namespace: str = field(metadata=config(field_name="namespace"))
    entry_keys: Optional[List[KVListEntryKey]] = field(
        default=None, metadata=config(field_name="entryKeys")
    )


@dataclass
class ConfiguredAccount(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    fullname: FullName = field(metadata=config(field_name="fullname"))
    has_stored_secret: bool = field(metadata=config(field_name="hasStoredSecret"))
    is_current: bool = field(metadata=config(field_name="isCurrent"))


@dataclass
class ResetPrompt__COMPLETE(DataClassJsonMixin):
    t: Literal[ResetPromptTypeStrings.COMPLETE]
    COMPLETE: Optional[ResetPromptInfo]


ResetPrompt = Union[ResetPrompt__COMPLETE]


@dataclass
class KBFSRoot(DataClassJsonMixin):
    tree_id: MerkleTreeID = field(metadata=config(field_name="treeID"))
    root: KBFSRootHash = field(metadata=config(field_name="root"))


@dataclass
class MerkleStoreEntry(DataClassJsonMixin):
    hash: MerkleStoreKitHash = field(metadata=config(field_name="hash"))
    entry: MerkleStoreEntryString = field(metadata=config(field_name="entry"))


@dataclass
class KeyHalf(DataClassJsonMixin):
    user: UID = field(metadata=config(field_name="user"))
    device_kid: KID = field(metadata=config(field_name="deviceKID"))
    key: str = field(metadata=config(field_name="key"))


@dataclass
class MDBlock(DataClassJsonMixin):
    version: int = field(metadata=config(field_name="version"))
    timestamp: Time = field(metadata=config(field_name="timestamp"))
    block: str = field(metadata=config(field_name="block"))


@dataclass
class PingResponse(DataClassJsonMixin):
    timestamp: Time = field(metadata=config(field_name="timestamp"))


@dataclass
class KeyBundleResponse(DataClassJsonMixin):
    writer_bundle: KeyBundle = field(metadata=config(field_name="WriterBundle"))
    reader_bundle: KeyBundle = field(metadata=config(field_name="ReaderBundle"))


@dataclass
class LockContext(DataClassJsonMixin):
    require_lock_id: LockID = field(metadata=config(field_name="requireLockID"))
    release_after_success: bool = field(
        metadata=config(field_name="releaseAfterSuccess")
    )


@dataclass
class FindNextMDResponse(DataClassJsonMixin):
    kbfs_root: MerkleRoot = field(metadata=config(field_name="kbfsRoot"))
    root_seqno: Seqno = field(metadata=config(field_name="rootSeqno"))
    root_hash: HashMeta = field(metadata=config(field_name="rootHash"))
    merkle_nodes: Optional[List[str]] = field(
        default=None, metadata=config(field_name="merkleNodes")
    )


@dataclass
class InstrumentationStat(DataClassJsonMixin):
    min_dur: DurationMsec = field(metadata=config(field_name="minDur"))
    tag: str = field(metadata=config(field_name="tag"))
    ctime: Time = field(metadata=config(field_name="ctime"))
    mtime: Time = field(metadata=config(field_name="mtime"))
    avg_dur: DurationMsec = field(metadata=config(field_name="avgDur"))
    max_dur: DurationMsec = field(metadata=config(field_name="maxDur"))
    num_calls: int = field(metadata=config(field_name="numCalls"))
    total_dur: DurationMsec = field(metadata=config(field_name="totalDur"))
    avg_size: int = field(metadata=config(field_name="avgSize"))
    max_size: int = field(metadata=config(field_name="maxSize"))
    min_size: int = field(metadata=config(field_name="minSize"))
    total_size: int = field(metadata=config(field_name="totalSize"))


@dataclass
class TeamMemberOutReset(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    teamname: str = field(metadata=config(field_name="teamname"))
    username: str = field(metadata=config(field_name="username"))
    uid: UID = field(metadata=config(field_name="uid"))
    id: gregor1.MsgID = field(metadata=config(field_name="id"))


@dataclass
class ResetState(DataClassJsonMixin):
    end_time: Time = field(metadata=config(field_name="end_time"))
    active: bool = field(metadata=config(field_name="active"))


@dataclass
class WotUpdate(DataClassJsonMixin):
    voucher: str = field(metadata=config(field_name="voucher"))
    vouchee: str = field(metadata=config(field_name="vouchee"))
    status: WotStatusType = field(metadata=config(field_name="status"))


@dataclass
class BadgeConversationInfo(DataClassJsonMixin):
    conv_id: ChatConversationID = field(metadata=config(field_name="convID"))
    badge_count: int = field(metadata=config(field_name="badgeCount"))
    unread_messages: int = field(metadata=config(field_name="unreadMessages"))


@dataclass
class DbStats(DataClassJsonMixin):
    type: DbType = field(metadata=config(field_name="type"))
    mem_comp_active: bool = field(metadata=config(field_name="memCompActive"))
    table_comp_active: bool = field(metadata=config(field_name="tableCompActive"))


@dataclass
class ProcessRuntimeStats(DataClassJsonMixin):
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


@dataclass
class PerfEvent(DataClassJsonMixin):
    message: str = field(metadata=config(field_name="message"))
    ctime: Time = field(metadata=config(field_name="ctime"))
    event_type: PerfEventType = field(metadata=config(field_name="eventType"))


@dataclass
class GUIEntryFeatures(DataClassJsonMixin):
    show_typing: Feature = field(metadata=config(field_name="showTyping"))


@dataclass
class PGPSignOptions(DataClassJsonMixin):
    key_query: str = field(metadata=config(field_name="keyQuery"))
    mode: SignMode = field(metadata=config(field_name="mode"))
    binary_in: bool = field(metadata=config(field_name="binaryIn"))
    binary_out: bool = field(metadata=config(field_name="binaryOut"))


@dataclass
class PGPCreateUids(DataClassJsonMixin):
    use_default: bool = field(metadata=config(field_name="useDefault"))
    ids: Optional[List[PGPIdentity]] = field(
        default=None, metadata=config(field_name="ids")
    )


@dataclass
class UserPhoneNumber(DataClassJsonMixin):
    phone_number: PhoneNumber = field(metadata=config(field_name="phone_number"))
    verified: bool = field(metadata=config(field_name="verified"))
    superseded: bool = field(metadata=config(field_name="superseded"))
    visibility: IdentityVisibility = field(metadata=config(field_name="visibility"))
    ctime: UnixTime = field(metadata=config(field_name="ctime"))


@dataclass
class PhoneNumberLookupResult(DataClassJsonMixin):
    phone_number: RawPhoneNumber = field(metadata=config(field_name="phone_number"))
    coerced_phone_number: PhoneNumber = field(
        metadata=config(field_name="coerced_phone_number")
    )
    err: Optional[str] = field(default=None, metadata=config(field_name="err"))
    uid: Optional[UID] = field(default=None, metadata=config(field_name="uid"))


@dataclass
class PhoneNumberChangedMsg(DataClassJsonMixin):
    phone_number: PhoneNumber = field(metadata=config(field_name="phone"))


@dataclass
class FileDescriptor(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    type: FileType = field(metadata=config(field_name="type"))


@dataclass
class CheckProofStatus(DataClassJsonMixin):
    found: bool = field(metadata=config(field_name="found"))
    status: ProofStatus = field(metadata=config(field_name="status"))
    proof_text: str = field(metadata=config(field_name="proofText"))
    state: ProofState = field(metadata=config(field_name="state"))


@dataclass
class StartProofResult(DataClassJsonMixin):
    sig_id: SigID = field(metadata=config(field_name="sigID"))


@dataclass
class ParamProofJSON(DataClassJsonMixin):
    sig_hash: SigID = field(metadata=config(field_name="sig_hash"))
    kb_username: str = field(metadata=config(field_name="kb_username"))


@dataclass
class ParamProofServiceConfig(DataClassJsonMixin):
    brand_color: str = field(metadata=config(field_name="brand_color"))
    version: int = field(metadata=config(field_name="version"))
    display_name: str = field(metadata=config(field_name="display_name"))
    description: str = field(metadata=config(field_name="description"))
    username_config: ParamProofUsernameConfig = field(
        metadata=config(field_name="username")
    )
    domain: str = field(metadata=config(field_name="domain"))
    prefill_url: str = field(metadata=config(field_name="prefill_url"))
    profile_url: str = field(metadata=config(field_name="profile_url"))
    check_url: str = field(metadata=config(field_name="check_url"))
    check_path: Optional[List[SelectorEntry]] = field(
        default=None, metadata=config(field_name="check_path")
    )
    avatar_path: Optional[List[SelectorEntry]] = field(
        default=None, metadata=config(field_name="avatar_path")
    )


@dataclass
class ProveParameters(DataClassJsonMixin):
    title: str = field(metadata=config(field_name="title"))
    subtext: str = field(metadata=config(field_name="subtext"))
    suffix: str = field(metadata=config(field_name="suffix"))
    button_label: str = field(metadata=config(field_name="buttonLabel"))
    logo_full: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="logoFull")
    )
    logo_black: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="logoBlack")
    )
    logo_white: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="logoWhite")
    )


@dataclass
class VerifySessionRes(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    sid: str = field(metadata=config(field_name="sid"))
    generated: int = field(metadata=config(field_name="generated"))
    lifetime: int = field(metadata=config(field_name="lifetime"))


@dataclass
class Reachability(DataClassJsonMixin):
    reachable: Reachable = field(metadata=config(field_name="reachable"))


@dataclass
class TLF(DataClassJsonMixin):
    id: TLFID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))
    is_private: bool = field(metadata=config(field_name="isPrivate"))
    writers: Optional[List[str]] = field(
        default=None, metadata=config(field_name="writers")
    )
    readers: Optional[List[str]] = field(
        default=None, metadata=config(field_name="readers")
    )


@dataclass
class RekeyEvent(DataClassJsonMixin):
    event_type: RekeyEventType = field(metadata=config(field_name="eventType"))
    interrupt_type: int = field(metadata=config(field_name="interruptType"))


@dataclass
class ResetMerkleRoot(DataClassJsonMixin):
    hash_meta: HashMeta = field(metadata=config(field_name="hash_meta"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))


@dataclass
class ResetPrev(DataClassJsonMixin):
    last_seqno: Seqno = field(metadata=config(field_name="public_seqno"))
    reset: SHA512 = field(metadata=config(field_name="reset"))
    eldest_kid: Optional[KID] = field(
        default=None, metadata=config(field_name="eldest_kid")
    )


@dataclass
class SaltpackEncryptOptions(DataClassJsonMixin):
    use_paper_keys: bool = field(metadata=config(field_name="usePaperKeys"))
    use_kbfs_keys_only_for_testing: bool = field(
        metadata=config(field_name="useKBFSKeysOnlyForTesting")
    )
    authenticity_type: AuthenticityType = field(
        metadata=config(field_name="authenticityType")
    )
    use_entity_keys: bool = field(metadata=config(field_name="useEntityKeys"))
    use_device_keys: bool = field(metadata=config(field_name="useDeviceKeys"))
    no_force_poll: bool = field(metadata=config(field_name="noForcePoll"))
    no_self_encrypt: bool = field(metadata=config(field_name="noSelfEncrypt"))
    binary: bool = field(metadata=config(field_name="binary"))
    saltpack_version: int = field(metadata=config(field_name="saltpackVersion"))
    team_recipients: Optional[List[str]] = field(
        default=None, metadata=config(field_name="teamRecipients")
    )
    recipients: Optional[List[str]] = field(
        default=None, metadata=config(field_name="recipients")
    )


@dataclass
class SaltpackSender(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    fullname: str = field(metadata=config(field_name="fullname"))
    sender_type: SaltpackSenderType = field(metadata=config(field_name="senderType"))


@dataclass
class SecretKeys(DataClassJsonMixin):
    signing: NaclSigningKeyPrivate = field(metadata=config(field_name="signing"))
    encryption: NaclDHKeyPrivate = field(metadata=config(field_name="encryption"))


@dataclass
class Session(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    token: str = field(metadata=config(field_name="token"))
    device_subkey_kid: KID = field(metadata=config(field_name="deviceSubkeyKid"))
    device_sibkey_kid: KID = field(metadata=config(field_name="deviceSibkeyKid"))


@dataclass
class Sig(DataClassJsonMixin):
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))
    sig_id_display: str = field(metadata=config(field_name="sigIDDisplay"))
    type: str = field(metadata=config(field_name="type"))
    c_time: Time = field(metadata=config(field_name="cTime"))
    revoked: bool = field(metadata=config(field_name="revoked"))
    active: bool = field(metadata=config(field_name="active"))
    key: str = field(metadata=config(field_name="key"))
    body: str = field(metadata=config(field_name="body"))


@dataclass
class SigListArgs(DataClassJsonMixin):
    session_id: int = field(metadata=config(field_name="sessionID"))
    username: str = field(metadata=config(field_name="username"))
    all_keys: bool = field(metadata=config(field_name="allKeys"))
    filterx: str = field(metadata=config(field_name="filterx"))
    verbose: bool = field(metadata=config(field_name="verbose"))
    revoked: bool = field(metadata=config(field_name="revoked"))
    types: Optional[SigTypes] = field(default=None, metadata=config(field_name="types"))


@dataclass
class KBFSArchivedParam__REVISION(DataClassJsonMixin):
    KBFSArchivedType: Literal[KBFSArchivedTypeStrings.REVISION]
    REVISION: Optional[KBFSRevision]


@dataclass
class KBFSArchivedParam__TIME(DataClassJsonMixin):
    KBFSArchivedType: Literal[KBFSArchivedTypeStrings.TIME]
    TIME: Optional[Time]


@dataclass
class KBFSArchivedParam__TIME_STRING(DataClassJsonMixin):
    KBFSArchivedType: Literal[KBFSArchivedTypeStrings.TIME_STRING]
    TIME_STRING: Optional[str]


@dataclass
class KBFSArchivedParam__REL_TIME_STRING(DataClassJsonMixin):
    KBFSArchivedType: Literal[KBFSArchivedTypeStrings.REL_TIME_STRING]
    REL_TIME_STRING: Optional[str]


KBFSArchivedParam = Union[
    KBFSArchivedParam__REVISION,
    KBFSArchivedParam__TIME,
    KBFSArchivedParam__TIME_STRING,
    KBFSArchivedParam__REL_TIME_STRING,
]


@dataclass
class KBFSPath(DataClassJsonMixin):
    path: str = field(metadata=config(field_name="path"))
    identify_behavior: Optional[TLFIdentifyBehavior] = field(
        default=None, metadata=config(field_name="identifyBehavior")
    )


@dataclass
class PrefetchProgress(DataClassJsonMixin):
    start: Time = field(metadata=config(field_name="start"))
    end_estimate: Time = field(metadata=config(field_name="endEstimate"))
    bytes_total: int = field(metadata=config(field_name="bytesTotal"))
    bytes_fetched: int = field(metadata=config(field_name="bytesFetched"))


@dataclass
class FileContent(DataClassJsonMixin):
    data: str = field(metadata=config(field_name="data"))
    progress: Progress = field(metadata=config(field_name="progress"))


@dataclass
class OpProgress(DataClassJsonMixin):
    start: Time = field(metadata=config(field_name="start"))
    end_estimate: Time = field(metadata=config(field_name="endEstimate"))
    op_type: AsyncOps = field(metadata=config(field_name="opType"))
    bytes_total: int = field(metadata=config(field_name="bytesTotal"))
    bytes_read: int = field(metadata=config(field_name="bytesRead"))
    bytes_written: int = field(metadata=config(field_name="bytesWritten"))
    files_total: int = field(metadata=config(field_name="filesTotal"))
    files_read: int = field(metadata=config(field_name="filesRead"))
    files_written: int = field(metadata=config(field_name="filesWritten"))


@dataclass
class FolderSyncConfig(DataClassJsonMixin):
    mode: FolderSyncMode = field(metadata=config(field_name="mode"))
    paths: Optional[List[str]] = field(
        default=None, metadata=config(field_name="paths")
    )


@dataclass
class DownloadState(DataClassJsonMixin):
    download_id: str = field(metadata=config(field_name="downloadID"))
    progress: float = field(metadata=config(field_name="progress"))
    end_estimate: Time = field(metadata=config(field_name="endEstimate"))
    local_path: str = field(metadata=config(field_name="localPath"))
    error: str = field(metadata=config(field_name="error"))
    done: bool = field(metadata=config(field_name="done"))
    canceled: bool = field(metadata=config(field_name="canceled"))


@dataclass
class GUIFileContext(DataClassJsonMixin):
    view_type: GUIViewType = field(metadata=config(field_name="viewType"))
    content_type: str = field(metadata=config(field_name="contentType"))
    url: str = field(metadata=config(field_name="url"))


@dataclass
class SimpleFSSearchResults(DataClassJsonMixin):
    next_result: int = field(metadata=config(field_name="nextResult"))
    hits: Optional[List[SimpleFSSearchHit]] = field(
        default=None, metadata=config(field_name="hits")
    )


@dataclass
class IndexProgressRecord(DataClassJsonMixin):
    end_estimate: Time = field(metadata=config(field_name="endEstimate"))
    bytes_total: int = field(metadata=config(field_name="bytesTotal"))
    bytes_so_far: int = field(metadata=config(field_name="bytesSoFar"))


@dataclass
class TeambotKeyMetadata(DataClassJsonMixin):
    kid: KID = field(metadata=config(field_name="teambot_dh_public"))
    generation: TeambotKeyGeneration = field(metadata=config(field_name="generation"))
    uid: UID = field(metadata=config(field_name="uid"))
    puk_generation: PerUserKeyGeneration = field(
        metadata=config(field_name="puk_generation")
    )
    application: TeamApplication = field(metadata=config(field_name="application"))


@dataclass
class PerTeamSeedCheck(DataClassJsonMixin):
    version: PerTeamSeedCheckVersion = field(metadata=config(field_name="version"))
    value: PerTeamSeedCheckValue = field(metadata=config(field_name="value"))


@dataclass
class PerTeamSeedCheckPostImage(DataClassJsonMixin):
    value: PerTeamSeedCheckValuePostImage = field(metadata=config(field_name="h"))
    version: PerTeamSeedCheckVersion = field(metadata=config(field_name="v"))


@dataclass
class TeamApplicationKey(DataClassJsonMixin):
    application: TeamApplication = field(metadata=config(field_name="application"))
    key_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="keyGeneration")
    )
    key: Bytes32 = field(metadata=config(field_name="key"))


@dataclass
class ReaderKeyMask(DataClassJsonMixin):
    application: TeamApplication = field(metadata=config(field_name="application"))
    generation: PerTeamKeyGeneration = field(metadata=config(field_name="generation"))
    mask: MaskB64 = field(metadata=config(field_name="mask"))


@dataclass
class PerTeamKey(DataClassJsonMixin):
    gen: PerTeamKeyGeneration = field(metadata=config(field_name="gen"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    sig_kid: KID = field(metadata=config(field_name="sigKID"))
    enc_kid: KID = field(metadata=config(field_name="encKID"))


@dataclass
class TeamMember(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    role: TeamRole = field(metadata=config(field_name="role"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    status: TeamMemberStatus = field(metadata=config(field_name="status"))
    bot_settings: Optional[TeamBotSettings] = field(
        default=None, metadata=config(field_name="botSettings")
    )


@dataclass
class TeamMemberRole(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    full_name: FullName = field(metadata=config(field_name="fullName"))
    role: TeamRole = field(metadata=config(field_name="role"))


@dataclass
class TeamUsedInvite(DataClassJsonMixin):
    invite_id: TeamInviteID = field(metadata=config(field_name="inviteID"))
    uv: UserVersionPercentForm = field(metadata=config(field_name="uv"))


@dataclass
class LinkTriple(DataClassJsonMixin):
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    seq_type: SeqType = field(metadata=config(field_name="seqType"))
    link_id: LinkID = field(metadata=config(field_name="linkID"))


@dataclass
class UpPointer(DataClassJsonMixin):
    our_seqno: Seqno = field(metadata=config(field_name="ourSeqno"))
    parent_id: TeamID = field(metadata=config(field_name="parentID"))
    parent_seqno: Seqno = field(metadata=config(field_name="parentSeqno"))
    deletion: bool = field(metadata=config(field_name="deletion"))


@dataclass
class DownPointer(DataClassJsonMixin):
    id: TeamID = field(metadata=config(field_name="id"))
    name_component: str = field(metadata=config(field_name="nameComponent"))
    is_deleted: bool = field(metadata=config(field_name="isDeleted"))


@dataclass
class Signer(DataClassJsonMixin):
    e: Seqno = field(metadata=config(field_name="e"))
    k: KID = field(metadata=config(field_name="k"))
    u: UID = field(metadata=config(field_name="u"))


@dataclass
class Audit(DataClassJsonMixin):
    time: Time = field(metadata=config(field_name="time"))
    max_merkle_seqno: Seqno = field(metadata=config(field_name="mms"))
    max_chain_seqno: Seqno = field(metadata=config(field_name="mcs"))
    max_hidden_seqno: Seqno = field(metadata=config(field_name="mhs"))
    max_merkle_probe: Seqno = field(metadata=config(field_name="mmp"))


@dataclass
class Probe(DataClassJsonMixin):
    index: int = field(metadata=config(field_name="i"))
    team_seqno: Seqno = field(metadata=config(field_name="t"))
    team_hidden_seqno: Seqno = field(metadata=config(field_name="h"))


@dataclass
class TeamInviteType__UNKNOWN(DataClassJsonMixin):
    c: Literal[TeamInviteCategoryStrings.UNKNOWN]
    UNKNOWN: Optional[str]


@dataclass
class TeamInviteType__SBS(DataClassJsonMixin):
    c: Literal[TeamInviteCategoryStrings.SBS]
    SBS: Optional[TeamInviteSocialNetwork]


TeamInviteType = Union[TeamInviteType__UNKNOWN, TeamInviteType__SBS]


@dataclass
class TeamGetLegacyTLFUpgrade(DataClassJsonMixin):
    encrypted_keyset: str = field(metadata=config(field_name="encrypted_keyset"))
    team_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="team_generation")
    )
    legacy_generation: int = field(metadata=config(field_name="legacy_generation"))
    app_type: TeamApplication = field(metadata=config(field_name="app_type"))


@dataclass
class TeamLegacyTLFUpgradeChainInfo(DataClassJsonMixin):
    keyset_hash: TeamEncryptedKBFSKeysetHash = field(
        metadata=config(field_name="keysetHash")
    )
    team_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="teamGeneration")
    )
    legacy_generation: int = field(metadata=config(field_name="legacyGeneration"))
    app_type: TeamApplication = field(metadata=config(field_name="appType"))


@dataclass
class TeamNameLogPoint(DataClassJsonMixin):
    last_part: TeamNamePart = field(metadata=config(field_name="lastPart"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))


@dataclass
class TeamName(DataClassJsonMixin):
    parts: Optional[List[TeamNamePart]] = field(
        default=None, metadata=config(field_name="parts")
    )


@dataclass
class TeamCLKRResetUser(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    user_eldest_seqno: Seqno = field(metadata=config(field_name="user_eldest"))
    member_eldest_seqno: Seqno = field(metadata=config(field_name="member_eldest"))


@dataclass
class TeamResetUser(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldest_seqno"))
    is_delete: bool = field(metadata=config(field_name="is_delete"))


@dataclass
class TeamChangeRow(DataClassJsonMixin):
    id: TeamID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))
    key_rotated: bool = field(metadata=config(field_name="key_rotated"))
    membership_changed: bool = field(metadata=config(field_name="membership_changed"))
    latest_seqno: Seqno = field(metadata=config(field_name="latest_seqno"))
    latest_hidden_seqno: Seqno = field(
        metadata=config(field_name="latest_hidden_seqno")
    )
    latest_offchain_seqno: Seqno = field(
        metadata=config(field_name="latest_offchain_version")
    )
    implicit_team: bool = field(metadata=config(field_name="implicit_team"))
    misc: bool = field(metadata=config(field_name="misc"))
    removed_reset_users: bool = field(metadata=config(field_name="removed_reset_users"))


@dataclass
class TeamExitRow(DataClassJsonMixin):
    id: TeamID = field(metadata=config(field_name="id"))


@dataclass
class TeamNewlyAddedRow(DataClassJsonMixin):
    id: TeamID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))


@dataclass
class TeamInvitee(DataClassJsonMixin):
    invite_id: TeamInviteID = field(metadata=config(field_name="invite_id"))
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldest_seqno"))
    role: TeamRole = field(metadata=config(field_name="role"))


@dataclass
class TeamAccessRequest(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldest_seqno"))


@dataclass
class SeitanKeyLabel__SMS(DataClassJsonMixin):
    t: Literal[SeitanKeyLabelTypeStrings.SMS]
    SMS: Optional[SeitanKeyLabelSms]


@dataclass
class SeitanKeyLabel__GENERIC(DataClassJsonMixin):
    t: Literal[SeitanKeyLabelTypeStrings.GENERIC]
    GENERIC: Optional[SeitanKeyLabelGeneric]


SeitanKeyLabel = Union[SeitanKeyLabel__SMS, SeitanKeyLabel__GENERIC]


@dataclass
class TeamSeitanRequest(DataClassJsonMixin):
    invite_id: TeamInviteID = field(metadata=config(field_name="invite_id"))
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldest_seqno"))
    akey: SeitanAKey = field(metadata=config(field_name="akey"))
    role: TeamRole = field(metadata=config(field_name="role"))
    unix_c_time: int = field(metadata=config(field_name="ctime"))


@dataclass
class TeamKBFSKeyRefresher(DataClassJsonMixin):
    generation: int = field(metadata=config(field_name="generation"))
    app_type: TeamApplication = field(metadata=config(field_name="appType"))


@dataclass
class ImplicitRole(DataClassJsonMixin):
    role: TeamRole = field(metadata=config(field_name="role"))
    ancestor: TeamID = field(metadata=config(field_name="ancestor"))


@dataclass
class TeamJoinRequest(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    username: str = field(metadata=config(field_name="username"))
    full_name: FullName = field(metadata=config(field_name="fullName"))
    ctime: UnixTime = field(metadata=config(field_name="ctime"))


@dataclass
class TeamCreateResult(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    chat_sent: bool = field(metadata=config(field_name="chatSent"))
    creator_added: bool = field(metadata=config(field_name="creatorAdded"))


@dataclass
class TeamSettings(DataClassJsonMixin):
    open: bool = field(metadata=config(field_name="open"))
    join_as: TeamRole = field(metadata=config(field_name="joinAs"))


@dataclass
class TeamShowcase(DataClassJsonMixin):
    is_showcased: bool = field(metadata=config(field_name="is_showcased"))
    any_member_showcase: bool = field(metadata=config(field_name="any_member_showcase"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )
    set_by_uid: Optional[UID] = field(
        default=None, metadata=config(field_name="set_by_uid")
    )


@dataclass
class UserRolePair(DataClassJsonMixin):
    assertion: str = field(metadata=config(field_name="assertion"))
    role: TeamRole = field(metadata=config(field_name="role"))
    bot_settings: Optional[TeamBotSettings] = field(
        default=None, metadata=config(field_name="botSettings")
    )


@dataclass
class TeamMemberToRemove(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    email: str = field(metadata=config(field_name="email"))
    invite_id: TeamInviteID = field(metadata=config(field_name="inviteID"))
    allow_inaction: bool = field(metadata=config(field_name="allowInaction"))


@dataclass
class UntrustedTeamExistsResult(DataClassJsonMixin):
    exists: bool = field(metadata=config(field_name="exists"))
    status: StatusCode = field(metadata=config(field_name="status"))


@dataclass
class Invitelink(DataClassJsonMixin):
    ikey: SeitanIKeyInvitelink = field(metadata=config(field_name="ikey"))
    url: str = field(metadata=config(field_name="url"))


@dataclass
class ImplicitTeamConflictInfo(DataClassJsonMixin):
    generation: ConflictGeneration = field(metadata=config(field_name="generation"))
    time: Time = field(metadata=config(field_name="time"))


@dataclass
class TeamRolePair(DataClassJsonMixin):
    role: TeamRole = field(metadata=config(field_name="role"))
    implicit_role: TeamRole = field(metadata=config(field_name="implicit_role"))


@dataclass
class UserTeamVersionUpdate(DataClassJsonMixin):
    version: UserTeamVersion = field(metadata=config(field_name="version"))


@dataclass
class TeamTreeMembershipValue(DataClassJsonMixin):
    role: TeamRole = field(metadata=config(field_name="role"))
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    join_time: Optional[Time] = field(
        default=None, metadata=config(field_name="joinTime")
    )


@dataclass
class TeamTreeMembershipsDoneResult(DataClassJsonMixin):
    expected_count: int = field(metadata=config(field_name="expectedCount"))
    target_team_id: TeamID = field(metadata=config(field_name="targetTeamID"))
    target_username: str = field(metadata=config(field_name="targetUsername"))
    guid: int = field(metadata=config(field_name="guid"))


@dataclass
class TeamSearchItem(DataClassJsonMixin):
    id: TeamID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))
    member_count: int = field(metadata=config(field_name="memberCount"))
    last_active: Time = field(metadata=config(field_name="lastActive"))
    is_demoted: bool = field(metadata=config(field_name="isDemoted"))
    in_team: bool = field(metadata=config(field_name="inTeam"))
    description: Optional[str] = field(
        default=None, metadata=config(field_name="description")
    )


@dataclass
class CryptKey(DataClassJsonMixin):
    key_generation: int = field(metadata=config(field_name="KeyGeneration"))
    key: Bytes32 = field(metadata=config(field_name="Key"))


@dataclass
class TLFQuery(DataClassJsonMixin):
    tlf_name: str = field(metadata=config(field_name="tlfName"))
    identify_behavior: TLFIdentifyBehavior = field(
        metadata=config(field_name="identifyBehavior")
    )


@dataclass
class MerkleRootV2(DataClassJsonMixin):
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    hash_meta: HashMeta = field(metadata=config(field_name="hashMeta"))


@dataclass
class SigChainLocation(DataClassJsonMixin):
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    seq_type: SeqType = field(metadata=config(field_name="seqType"))


@dataclass
class UserSummary(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    full_name: str = field(metadata=config(field_name="fullName"))
    link_id: Optional[LinkID] = field(
        default=None, metadata=config(field_name="linkID")
    )


@dataclass
class Email(DataClassJsonMixin):
    email: EmailAddress = field(metadata=config(field_name="email"))
    is_verified: bool = field(metadata=config(field_name="isVerified"))
    is_primary: bool = field(metadata=config(field_name="isPrimary"))
    visibility: IdentityVisibility = field(metadata=config(field_name="visibility"))
    last_verify_email_date: UnixTime = field(
        metadata=config(field_name="lastVerifyEmailDate")
    )


@dataclass
class InterestingPerson(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    fullname: str = field(metadata=config(field_name="fullname"))
    service_map: Dict[str, str] = field(metadata=config(field_name="serviceMap"))


@dataclass
class CanLogoutRes(DataClassJsonMixin):
    can_logout: bool = field(metadata=config(field_name="canLogout"))
    reason: str = field(metadata=config(field_name="reason"))
    passphrase_state: PassphraseState = field(
        metadata=config(field_name="passphraseState")
    )


@dataclass
class UserPassphraseStateMsg(DataClassJsonMixin):
    passphrase_state: PassphraseState = field(metadata=config(field_name="state"))


@dataclass
class UserBlockedRow(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="block_uid"))
    username: str = field(metadata=config(field_name="block_username"))
    chat: Optional[bool] = field(default=None, metadata=config(field_name="chat"))
    follow: Optional[bool] = field(default=None, metadata=config(field_name="follow"))


@dataclass
class UserBlockState(DataClassJsonMixin):
    block_type: UserBlockType = field(metadata=config(field_name="blockType"))
    blocked: bool = field(metadata=config(field_name="blocked"))


@dataclass
class UserBlock(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    chat_blocked: bool = field(metadata=config(field_name="chatBlocked"))
    follow_blocked: bool = field(metadata=config(field_name="followBlocked"))
    create_time: Optional[Time] = field(
        default=None, metadata=config(field_name="createTime")
    )
    modify_time: Optional[Time] = field(
        default=None, metadata=config(field_name="modifyTime")
    )


@dataclass
class TeamBlock(DataClassJsonMixin):
    team_name: str = field(metadata=config(field_name="fq_name"))
    create_time: Time = field(metadata=config(field_name="ctime"))


@dataclass
class APIUserKeybaseResult(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    uid: UID = field(metadata=config(field_name="uid"))
    raw_score: float = field(metadata=config(field_name="raw_score"))
    is_followee: bool = field(metadata=config(field_name="is_followee"))
    picture_url: Optional[str] = field(
        default=None, metadata=config(field_name="picture_url")
    )
    full_name: Optional[str] = field(
        default=None, metadata=config(field_name="full_name")
    )
    stellar: Optional[str] = field(default=None, metadata=config(field_name="stellar"))


@dataclass
class APIUserServiceResult(DataClassJsonMixin):
    service_name: APIUserServiceID = field(metadata=config(field_name="service_name"))
    username: str = field(metadata=config(field_name="username"))
    picture_url: str = field(metadata=config(field_name="picture_url"))
    bio: str = field(metadata=config(field_name="bio"))
    location: str = field(metadata=config(field_name="location"))
    full_name: str = field(metadata=config(field_name="full_name"))
    confirmed: Optional[bool] = field(
        default=None, metadata=config(field_name="confirmed")
    )


@dataclass
class APIUserServiceSummary(DataClassJsonMixin):
    service_name: APIUserServiceID = field(metadata=config(field_name="service_name"))
    username: str = field(metadata=config(field_name="username"))


@dataclass
class WotProof(DataClassJsonMixin):
    proof_type: ProofType = field(metadata=config(field_name="proof_type"))
    name: str = field(metadata=config(field_name="name,omitempty"))
    username: str = field(metadata=config(field_name="username,omitempty"))
    protocol: str = field(metadata=config(field_name="protocol,omitempty"))
    hostname: str = field(metadata=config(field_name="hostname,omitempty"))
    domain: str = field(metadata=config(field_name="domain,omitempty"))


@dataclass
class GetLockdownResponse(DataClassJsonMixin):
    status: bool = field(metadata=config(field_name="status"))
    history: Optional[List[LockdownHistory]] = field(
        default=None, metadata=config(field_name="history")
    )


@dataclass
class ContactSettings(DataClassJsonMixin):
    allow_followee_degrees: int = field(
        metadata=config(field_name="allow_followee_degrees")
    )
    allow_good_teams: bool = field(metadata=config(field_name="allow_good_teams"))
    enabled: bool = field(metadata=config(field_name="enabled"))
    version: Optional[int] = field(default=None, metadata=config(field_name="version"))
    teams: Optional[List[TeamContactSettings]] = field(
        default=None, metadata=config(field_name="teams")
    )


@dataclass
class BlockReference(DataClassJsonMixin):
    bid: BlockIdCombo = field(metadata=config(field_name="bid"))
    nonce: BlockRefNonce = field(metadata=config(field_name="nonce"))
    charged_to: UserOrTeamID = field(metadata=config(field_name="chargedTo"))


@dataclass
class BlockIdCount(DataClassJsonMixin):
    id: BlockIdCombo = field(metadata=config(field_name="id"))
    live_count: int = field(metadata=config(field_name="liveCount"))


@dataclass
class FolderUsageStat(DataClassJsonMixin):
    folder_id: str = field(metadata=config(field_name="folderID"))
    stats: UsageStat = field(metadata=config(field_name="stats"))


@dataclass
class TeamIDAndName(DataClassJsonMixin):
    id: TeamID = field(metadata=config(field_name="id"))
    name: TeamName = field(metadata=config(field_name="name"))


@dataclass
class RevokedKey(DataClassJsonMixin):
    key: PublicKey = field(metadata=config(field_name="key"))
    time: KeybaseTime = field(metadata=config(field_name="time"))
    by: KID = field(metadata=config(field_name="by"))


@dataclass
class CurrentStatus(DataClassJsonMixin):
    configured: bool = field(metadata=config(field_name="configured"))
    registered: bool = field(metadata=config(field_name="registered"))
    logged_in: bool = field(metadata=config(field_name="loggedIn"))
    session_is_valid: bool = field(metadata=config(field_name="sessionIsValid"))
    device_name: str = field(metadata=config(field_name="deviceName"))
    user: Optional[User] = field(default=None, metadata=config(field_name="user"))


@dataclass
class ClientStatus(DataClassJsonMixin):
    details: ClientDetails = field(metadata=config(field_name="details"))
    connection_id: int = field(metadata=config(field_name="connectionID"))
    notification_channels: NotificationChannels = field(
        metadata=config(field_name="notificationChannels")
    )


@dataclass
class BootstrapStatus(DataClassJsonMixin):
    registered: bool = field(metadata=config(field_name="registered"))
    logged_in: bool = field(metadata=config(field_name="loggedIn"))
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    device_name: str = field(metadata=config(field_name="deviceName"))
    fullname: FullName = field(metadata=config(field_name="fullname"))
    user_reacjis: UserReacjis = field(metadata=config(field_name="userReacjis"))
    http_srv_info: Optional[HttpSrvInfo] = field(
        default=None, metadata=config(field_name="httpSrvInfo")
    )


@dataclass
class Contact(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    components: Optional[List[ContactComponent]] = field(
        default=None, metadata=config(field_name="components")
    )


@dataclass
class ProcessedContact(DataClassJsonMixin):
    full_name: str = field(metadata=config(field_name="fullName"))
    contact_index: int = field(metadata=config(field_name="contactIndex"))
    component: ContactComponent = field(metadata=config(field_name="component"))
    resolved: bool = field(metadata=config(field_name="resolved"))
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    contact_name: str = field(metadata=config(field_name="contactName"))
    following: bool = field(metadata=config(field_name="following"))
    service_map: Dict[str, str] = field(metadata=config(field_name="serviceMap"))
    assertion: str = field(metadata=config(field_name="assertion"))
    display_name: str = field(metadata=config(field_name="displayName"))
    display_label: str = field(metadata=config(field_name="displayLabel"))


@dataclass
class DeviceDetail(DataClassJsonMixin):
    device: Device = field(metadata=config(field_name="device"))
    eldest: bool = field(metadata=config(field_name="eldest"))
    revoked_by: KID = field(metadata=config(field_name="revokedBy"))
    current_device: bool = field(metadata=config(field_name="currentDevice"))
    provisioner: Optional[Device] = field(
        default=None, metadata=config(field_name="provisioner")
    )
    provisioned_at: Optional[Time] = field(
        default=None, metadata=config(field_name="provisionedAt")
    )
    revoked_at: Optional[Time] = field(
        default=None, metadata=config(field_name="revokedAt")
    )
    revoked_by_device: Optional[Device] = field(
        default=None, metadata=config(field_name="revokedByDevice")
    )


@dataclass
class DeviceEkStatement(DataClassJsonMixin):
    current_device_ek_metadata: DeviceEkMetadata = field(
        metadata=config(field_name="current_device_ek_metadata")
    )


@dataclass
class DeviceEk(DataClassJsonMixin):
    seed: Bytes32 = field(metadata=config(field_name="seed"))
    metadata: DeviceEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass
class UserEkStatement(DataClassJsonMixin):
    current_user_ek_metadata: UserEkMetadata = field(
        metadata=config(field_name="current_user_ek_metadata")
    )


@dataclass
class UserEkBoxed(DataClassJsonMixin):
    box: str = field(metadata=config(field_name="box"))
    device_ek_generation: EkGeneration = field(
        metadata=config(field_name="device_ek_generation")
    )
    metadata: UserEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass
class UserEk(DataClassJsonMixin):
    seed: Bytes32 = field(metadata=config(field_name="seed"))
    metadata: UserEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass
class UserEkReboxArg(DataClassJsonMixin):
    user_ek_box_metadata: UserEkBoxMetadata = field(
        metadata=config(field_name="userEkBoxMetadata")
    )
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    device_ek_statement_sig: str = field(
        metadata=config(field_name="deviceEkStatementSig")
    )


@dataclass
class TeamEkStatement(DataClassJsonMixin):
    current_team_ek_metadata: TeamEkMetadata = field(
        metadata=config(field_name="current_team_ek_metadata")
    )


@dataclass
class TeamEkBoxed(DataClassJsonMixin):
    box: str = field(metadata=config(field_name="box"))
    user_ek_generation: EkGeneration = field(
        metadata=config(field_name="user_ek_generation")
    )
    metadata: TeamEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass
class TeamEk(DataClassJsonMixin):
    seed: Bytes32 = field(metadata=config(field_name="seed"))
    metadata: TeamEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass
class TeambotEkBoxed(DataClassJsonMixin):
    box: str = field(metadata=config(field_name="box"))
    metadata: TeambotEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass
class TeambotEk(DataClassJsonMixin):
    seed: Bytes32 = field(metadata=config(field_name="seed"))
    metadata: TeambotEkMetadata = field(metadata=config(field_name="metadata"))


@dataclass
class GitLocalMetadataVersioned__V1(DataClassJsonMixin):
    version: Literal[GitLocalMetadataVersionStrings.V1]
    V1: Optional[GitLocalMetadataV1]


GitLocalMetadataVersioned = Union[GitLocalMetadataVersioned__V1]


@dataclass
class GitRefMetadata(DataClassJsonMixin):
    ref_name: str = field(metadata=config(field_name="refName"))
    more_commits_available: bool = field(
        metadata=config(field_name="moreCommitsAvailable")
    )
    is_delete: bool = field(metadata=config(field_name="isDelete"))
    commits: Optional[List[GitCommit]] = field(
        default=None, metadata=config(field_name="commits")
    )


@dataclass
class HomeScreenTodoExt__VERIFY_ALL_EMAIL(DataClassJsonMixin):
    t: Literal[HomeScreenTodoTypeStrings.VERIFY_ALL_EMAIL]
    VERIFY_ALL_EMAIL: Optional[VerifyAllEmailTodoExt]


HomeScreenTodoExt = Union[HomeScreenTodoExt__VERIFY_ALL_EMAIL]


@dataclass
class HomeScreenPeopleNotificationFollowed(DataClassJsonMixin):
    follow_time: Time = field(metadata=config(field_name="followTime"))
    followed_back: bool = field(metadata=config(field_name="followedBack"))
    user: UserSummary = field(metadata=config(field_name="user"))


@dataclass
class HomeScreenPeopleNotificationContactMulti(DataClassJsonMixin):
    num_others: int = field(metadata=config(field_name="numOthers"))
    contacts: Optional[List[HomeScreenPeopleNotificationContact]] = field(
        default=None, metadata=config(field_name="contacts")
    )


@dataclass
class Identify3Row(DataClassJsonMixin):
    gui_id: Identify3GUIID = field(metadata=config(field_name="guiID"))
    value: str = field(metadata=config(field_name="value"))
    priority: int = field(metadata=config(field_name="priority"))
    site_url: str = field(metadata=config(field_name="siteURL"))
    key: str = field(metadata=config(field_name="key"))
    proof_url: str = field(metadata=config(field_name="proofURL"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))
    ctime: Time = field(metadata=config(field_name="ctime"))
    state: Identify3RowState = field(metadata=config(field_name="state"))
    color: Identify3RowColor = field(metadata=config(field_name="color"))
    site_icon_darkmode: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="siteIconDarkmode")
    )
    site_icon_full: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="siteIconFull")
    )
    kid: Optional[KID] = field(default=None, metadata=config(field_name="kid"))
    metas: Optional[List[Identify3RowMeta]] = field(
        default=None, metadata=config(field_name="metas")
    )
    site_icon: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="siteIcon")
    )
    site_icon_full_darkmode: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="siteIconFullDarkmode")
    )


@dataclass
class IdentifyOutcome(DataClassJsonMixin):
    num_proof_failures: int = field(metadata=config(field_name="numProofFailures"))
    username: str = field(metadata=config(field_name="username"))
    for_pgp_pull: bool = field(metadata=config(field_name="forPGPPull"))
    track_options: TrackOptions = field(metadata=config(field_name="trackOptions"))
    track_status: TrackStatus = field(metadata=config(field_name="trackStatus"))
    num_track_failures: int = field(metadata=config(field_name="numTrackFailures"))
    num_track_changes: int = field(metadata=config(field_name="numTrackChanges"))
    num_proof_successes: int = field(metadata=config(field_name="numProofSuccesses"))
    num_revoked: int = field(metadata=config(field_name="numRevoked"))
    reason: IdentifyReason = field(metadata=config(field_name="reason"))
    status: Optional[Status] = field(default=None, metadata=config(field_name="status"))
    revoked: Optional[List[TrackDiff]] = field(
        default=None, metadata=config(field_name="revoked")
    )
    track_used: Optional[TrackSummary] = field(
        default=None, metadata=config(field_name="trackUsed")
    )
    warnings: Optional[List[str]] = field(
        default=None, metadata=config(field_name="warnings")
    )


@dataclass
class IdentifyRow(DataClassJsonMixin):
    row_id: int = field(metadata=config(field_name="rowId"))
    proof: RemoteProof = field(metadata=config(field_name="proof"))
    track_diff: Optional[TrackDiff] = field(
        default=None, metadata=config(field_name="trackDiff")
    )


@dataclass
class IdentifyKey(DataClassJsonMixin):
    pgp_fingerprint: str = field(metadata=config(field_name="pgpFingerprint"))
    kid: KID = field(metadata=config(field_name="KID"))
    breaks_tracking: bool = field(metadata=config(field_name="breaksTracking"))
    sig_id: SigID = field(metadata=config(field_name="sigID"))
    track_diff: Optional[TrackDiff] = field(
        default=None, metadata=config(field_name="trackDiff")
    )


@dataclass
class RevokedProof(DataClassJsonMixin):
    proof: RemoteProof = field(metadata=config(field_name="proof"))
    diff: TrackDiff = field(metadata=config(field_name="diff"))
    snoozed: bool = field(metadata=config(field_name="snoozed"))


@dataclass
class CheckResult(DataClassJsonMixin):
    proof_result: ProofResult = field(metadata=config(field_name="proofResult"))
    time: Time = field(metadata=config(field_name="time"))
    freshness: CheckResultFreshness = field(metadata=config(field_name="freshness"))


@dataclass
class UserCard(DataClassJsonMixin):
    website: str = field(metadata=config(field_name="website"))
    unverified_num_following: int = field(
        metadata=config(field_name="unverifiedNumFollowing")
    )
    uid: UID = field(metadata=config(field_name="uid"))
    full_name: str = field(metadata=config(field_name="fullName"))
    location: str = field(metadata=config(field_name="location"))
    bio: str = field(metadata=config(field_name="bio"))
    bio_decorated: str = field(metadata=config(field_name="bioDecorated"))
    unverified_num_followers: int = field(
        metadata=config(field_name="unverifiedNumFollowers")
    )
    twitter: str = field(metadata=config(field_name="twitter"))
    blocked: bool = field(metadata=config(field_name="blocked"))
    registered_for_airdrop: bool = field(
        metadata=config(field_name="registeredForAirdrop")
    )
    stellar_hidden: bool = field(metadata=config(field_name="stellarHidden"))
    hid_from_followers: bool = field(metadata=config(field_name="hidFromFollowers"))
    team_showcase: Optional[List[UserTeamShowcase]] = field(
        default=None, metadata=config(field_name="teamShowcase")
    )


@dataclass
class ServiceStatus(DataClassJsonMixin):
    version: str = field(metadata=config(field_name="version"))
    label: str = field(metadata=config(field_name="label"))
    pid: str = field(metadata=config(field_name="pid"))
    last_exit_status: str = field(metadata=config(field_name="lastExitStatus"))
    bundle_version: str = field(metadata=config(field_name="bundleVersion"))
    install_status: InstallStatus = field(metadata=config(field_name="installStatus"))
    install_action: InstallAction = field(metadata=config(field_name="installAction"))
    status: Status = field(metadata=config(field_name="status"))


@dataclass
class FuseStatus(DataClassJsonMixin):
    version: str = field(metadata=config(field_name="version"))
    bundle_version: str = field(metadata=config(field_name="bundleVersion"))
    kext_id: str = field(metadata=config(field_name="kextID"))
    path: str = field(metadata=config(field_name="path"))
    kext_started: bool = field(metadata=config(field_name="kextStarted"))
    install_status: InstallStatus = field(metadata=config(field_name="installStatus"))
    install_action: InstallAction = field(metadata=config(field_name="installAction"))
    status: Status = field(metadata=config(field_name="status"))
    mount_infos: Optional[List[FuseMountInfo]] = field(
        default=None, metadata=config(field_name="mountInfos")
    )


@dataclass
class ComponentResult(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    status: Status = field(metadata=config(field_name="status"))
    exit_code: int = field(metadata=config(field_name="exitCode"))


@dataclass
class FSFolderWriterEditHistory(DataClassJsonMixin):
    writer_name: str = field(metadata=config(field_name="writerName"))
    edits: Optional[List[FSFolderWriterEdit]] = field(
        default=None, metadata=config(field_name="edits")
    )
    deletes: Optional[List[FSFolderWriterEdit]] = field(
        default=None, metadata=config(field_name="deletes")
    )


@dataclass
class FolderSyncStatus(DataClassJsonMixin):
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


@dataclass
class MerkleRootAndTime(DataClassJsonMixin):
    root: MerkleRootV2 = field(metadata=config(field_name="root"))
    update_time: Time = field(metadata=config(field_name="updateTime"))
    fetch_time: Time = field(metadata=config(field_name="fetchTime"))


@dataclass
class MetadataResponse(DataClassJsonMixin):
    folder_id: str = field(metadata=config(field_name="folderID"))
    md_blocks: Optional[List[MDBlock]] = field(
        default=None, metadata=config(field_name="mdBlocks")
    )


@dataclass
class BadgeState(DataClassJsonMixin):
    new_tlfs: int = field(metadata=config(field_name="newTlfs"))
    reset_state: ResetState = field(metadata=config(field_name="resetState"))
    new_followers: int = field(metadata=config(field_name="newFollowers"))
    inbox_vers: int = field(metadata=config(field_name="inboxVers"))
    home_todo_items: int = field(metadata=config(field_name="homeTodoItems"))
    unverified_emails: int = field(metadata=config(field_name="unverifiedEmails"))
    unverified_phones: int = field(metadata=config(field_name="unverifiedPhones"))
    small_team_badge_count: int = field(
        metadata=config(field_name="smallTeamBadgeCount")
    )
    big_team_badge_count: int = field(metadata=config(field_name="bigTeamBadgeCount"))
    new_team_access_request_count: int = field(
        metadata=config(field_name="newTeamAccessRequestCount")
    )
    rekeys_needed: int = field(metadata=config(field_name="rekeysNeeded"))
    wot_updates: Dict[str, WotUpdate] = field(metadata=config(field_name="wotUpdates"))
    conversations: Optional[List[BadgeConversationInfo]] = field(
        default=None, metadata=config(field_name="conversations")
    )
    new_git_repo_global_unique_i_ds: Optional[List[str]] = field(
        default=None, metadata=config(field_name="newGitRepoGlobalUniqueIDs")
    )
    new_teams: Optional[List[TeamID]] = field(
        default=None, metadata=config(field_name="newTeams")
    )
    deleted_teams: Optional[List[DeletedTeamInfo]] = field(
        default=None, metadata=config(field_name="deletedTeams")
    )
    teams_with_reset_users: Optional[List[TeamMemberOutReset]] = field(
        default=None, metadata=config(field_name="teamsWithResetUsers")
    )
    unread_wallet_accounts: Optional[List[WalletAccountInfo]] = field(
        default=None, metadata=config(field_name="unreadWalletAccounts")
    )
    revoked_devices: Optional[List[DeviceID]] = field(
        default=None, metadata=config(field_name="revokedDevices")
    )
    new_devices: Optional[List[DeviceID]] = field(
        default=None, metadata=config(field_name="newDevices")
    )


@dataclass
class RuntimeStats(DataClassJsonMixin):
    conv_loader_active: bool = field(metadata=config(field_name="convLoaderActive"))
    selective_sync_active: bool = field(
        metadata=config(field_name="selectiveSyncActive")
    )
    process_stats: Optional[List[ProcessRuntimeStats]] = field(
        default=None, metadata=config(field_name="processStats")
    )
    db_stats: Optional[List[DbStats]] = field(
        default=None, metadata=config(field_name="dbStats")
    )
    perf_events: Optional[List[PerfEvent]] = field(
        default=None, metadata=config(field_name="perfEvents")
    )


@dataclass
class GUIEntryArg(DataClassJsonMixin):
    window_title: str = field(metadata=config(field_name="windowTitle"))
    prompt: str = field(metadata=config(field_name="prompt"))
    username: str = field(metadata=config(field_name="username"))
    submit_label: str = field(metadata=config(field_name="submitLabel"))
    cancel_label: str = field(metadata=config(field_name="cancelLabel"))
    retry_label: str = field(metadata=config(field_name="retryLabel"))
    type: PassphraseType = field(metadata=config(field_name="type"))
    features: GUIEntryFeatures = field(metadata=config(field_name="features"))


@dataclass
class PGPSigVerification(DataClassJsonMixin):
    is_signed: bool = field(metadata=config(field_name="isSigned"))
    verified: bool = field(metadata=config(field_name="verified"))
    signer: User = field(metadata=config(field_name="signer"))
    sign_key: PublicKey = field(metadata=config(field_name="signKey"))
    warnings: Optional[List[str]] = field(
        default=None, metadata=config(field_name="warnings")
    )


@dataclass
class Process(DataClassJsonMixin):
    pid: str = field(metadata=config(field_name="pid"))
    command: str = field(metadata=config(field_name="command"))
    file_descriptors: Optional[List[FileDescriptor]] = field(
        default=None, metadata=config(field_name="fileDescriptors")
    )


@dataclass
class ExternalServiceConfig(DataClassJsonMixin):
    schema_version: int = field(metadata=config(field_name="schema_version"))
    display: Optional[ServiceDisplayConfig] = field(
        default=None, metadata=config(field_name="display")
    )
    config_: Optional[ParamProofServiceConfig] = field(
        default=None, metadata=config(field_name="config")
    )


@dataclass
class ProblemTLF(DataClassJsonMixin):
    tlf: TLF = field(metadata=config(field_name="tlf"))
    score: int = field(metadata=config(field_name="score"))
    solution_kids: Optional[List[KID]] = field(
        default=None, metadata=config(field_name="solution_kids")
    )


@dataclass
class RevokeWarning(DataClassJsonMixin):
    endangered_tl_fs: Optional[List[TLF]] = field(
        default=None, metadata=config(field_name="endangeredTLFs")
    )


@dataclass
class ResetLink(DataClassJsonMixin):
    ctime: UnixTime = field(metadata=config(field_name="ctime"))
    merkle_root: ResetMerkleRoot = field(metadata=config(field_name="merkle_root"))
    prev: ResetPrev = field(metadata=config(field_name="prev"))
    reset_seqno: Seqno = field(metadata=config(field_name="reset_seqno"))
    type: ResetType = field(metadata=config(field_name="type"))
    uid: UID = field(metadata=config(field_name="uid"))


@dataclass
class ResetSummary(DataClassJsonMixin):
    ctime: UnixTime = field(metadata=config(field_name="ctime"))
    merkle_root: ResetMerkleRoot = field(metadata=config(field_name="merkleRoot"))
    reset_seqno: Seqno = field(metadata=config(field_name="resetSeqno"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    type: ResetType = field(metadata=config(field_name="type"))


@dataclass
class SaltpackEncryptedMessageInfo(DataClassJsonMixin):
    num_anon_receivers: int = field(metadata=config(field_name="numAnonReceivers"))
    receiver_is_anon: bool = field(metadata=config(field_name="receiverIsAnon"))
    sender: SaltpackSender = field(metadata=config(field_name="sender"))
    devices: Optional[List[Device]] = field(
        default=None, metadata=config(field_name="devices")
    )


@dataclass
class SaltpackVerifyResult(DataClassJsonMixin):
    signing_kid: KID = field(metadata=config(field_name="signingKID"))
    sender: SaltpackSender = field(metadata=config(field_name="sender"))
    plaintext: str = field(metadata=config(field_name="plaintext"))
    verified: bool = field(metadata=config(field_name="verified"))


@dataclass
class SaltpackVerifyFileResult(DataClassJsonMixin):
    signing_kid: KID = field(metadata=config(field_name="signingKID"))
    sender: SaltpackSender = field(metadata=config(field_name="sender"))
    verified_filename: str = field(metadata=config(field_name="verifiedFilename"))
    verified: bool = field(metadata=config(field_name="verified"))


@dataclass
class KBFSArchivedPath(DataClassJsonMixin):
    path: str = field(metadata=config(field_name="path"))
    archived_param: KBFSArchivedParam = field(
        metadata=config(field_name="archivedParam")
    )
    identify_behavior: Optional[TLFIdentifyBehavior] = field(
        default=None, metadata=config(field_name="identifyBehavior")
    )


@dataclass
class Dirent(DataClassJsonMixin):
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
    symlink_target: str = field(metadata=config(field_name="symlinkTarget"))


@dataclass
class SimpleFSStats(DataClassJsonMixin):
    process_stats: ProcessRuntimeStats = field(
        metadata=config(field_name="processStats")
    )
    block_cache_db_stats: Optional[List[str]] = field(
        default=None, metadata=config(field_name="blockCacheDbStats")
    )
    sync_cache_db_stats: Optional[List[str]] = field(
        default=None, metadata=config(field_name="syncCacheDbStats")
    )
    runtime_db_stats: Optional[List[DbStats]] = field(
        default=None, metadata=config(field_name="runtimeDbStats")
    )


@dataclass
class DownloadInfo(DataClassJsonMixin):
    download_id: str = field(metadata=config(field_name="downloadID"))
    path: KBFSPath = field(metadata=config(field_name="path"))
    filename: str = field(metadata=config(field_name="filename"))
    start_time: Time = field(metadata=config(field_name="startTime"))
    is_regular_download: bool = field(metadata=config(field_name="isRegularDownload"))


@dataclass
class DownloadStatus(DataClassJsonMixin):
    regular_download_i_ds: Optional[List[str]] = field(
        default=None, metadata=config(field_name="regularDownloadIDs")
    )
    states: Optional[List[DownloadState]] = field(
        default=None, metadata=config(field_name="states")
    )


@dataclass
class UploadState(DataClassJsonMixin):
    upload_id: str = field(metadata=config(field_name="uploadID"))
    target_path: KBFSPath = field(metadata=config(field_name="targetPath"))
    canceled: bool = field(metadata=config(field_name="canceled"))
    error: Optional[str] = field(default=None, metadata=config(field_name="error"))


@dataclass
class TeambotKeyBoxed(DataClassJsonMixin):
    box: str = field(metadata=config(field_name="box"))
    metadata: TeambotKeyMetadata = field(metadata=config(field_name="metadata"))


@dataclass
class TeambotKey(DataClassJsonMixin):
    seed: Bytes32 = field(metadata=config(field_name="seed"))
    metadata: TeambotKeyMetadata = field(metadata=config(field_name="metadata"))


@dataclass
class PerTeamKeyAndCheck(DataClassJsonMixin):
    ptk: PerTeamKey = field(metadata=config(field_name="ptk"))
    check: PerTeamSeedCheckPostImage = field(metadata=config(field_name="check"))


@dataclass
class PerTeamKeySeedItem(DataClassJsonMixin):
    seed: PerTeamKeySeed = field(metadata=config(field_name="seed"))
    generation: PerTeamKeyGeneration = field(metadata=config(field_name="generation"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))
    check: Optional[PerTeamSeedCheck] = field(
        default=None, metadata=config(field_name="check")
    )


@dataclass
class TeamMembers(DataClassJsonMixin):
    owners: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="owners")
    )
    admins: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="admins")
    )
    writers: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="writers")
    )
    readers: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="readers")
    )
    bots: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="bots")
    )
    restricted_bots: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="restrictedBots")
    )


@dataclass
class TeamMemberDetails(DataClassJsonMixin):
    uv: UserVersion = field(metadata=config(field_name="uv"))
    username: str = field(metadata=config(field_name="username"))
    full_name: FullName = field(metadata=config(field_name="fullName"))
    needs_puk: bool = field(metadata=config(field_name="needsPUK"))
    status: TeamMemberStatus = field(metadata=config(field_name="status"))
    join_time: Optional[Time] = field(
        default=None, metadata=config(field_name="joinTime")
    )


@dataclass
class UntrustedTeamInfo(DataClassJsonMixin):
    name: TeamName = field(metadata=config(field_name="name"))
    in_team: bool = field(metadata=config(field_name="inTeam"))
    open: bool = field(metadata=config(field_name="open"))
    description: str = field(metadata=config(field_name="description"))
    num_members: int = field(metadata=config(field_name="numMembers"))
    public_admins: Optional[List[str]] = field(
        default=None, metadata=config(field_name="publicAdmins")
    )
    public_members: Optional[List[TeamMemberRole]] = field(
        default=None, metadata=config(field_name="publicMembers")
    )


@dataclass
class TeamChangeReq(DataClassJsonMixin):
    restricted_bots: Dict[str, TeamBotSettings] = field(
        metadata=config(field_name="restrictedBots")
    )
    completed_invites: Dict[str, UserVersionPercentForm] = field(
        metadata=config(field_name="completedInvites")
    )
    owners: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="owners")
    )
    admins: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="admins")
    )
    writers: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="writers")
    )
    readers: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="readers")
    )
    bots: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="bots")
    )
    none: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="none")
    )
    used_invites: Optional[List[TeamUsedInvite]] = field(
        default=None, metadata=config(field_name="usedInvites")
    )


@dataclass
class TeamPlusApplicationKeys(DataClassJsonMixin):
    id: TeamID = field(metadata=config(field_name="id"))
    name: str = field(metadata=config(field_name="name"))
    implicit: bool = field(metadata=config(field_name="implicit"))
    public: bool = field(metadata=config(field_name="public"))
    application: TeamApplication = field(metadata=config(field_name="application"))
    writers: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="writers")
    )
    only_readers: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="onlyReaders")
    )
    only_restricted_bots: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="onlyRestrictedBots")
    )
    application_keys: Optional[List[TeamApplicationKey]] = field(
        default=None, metadata=config(field_name="applicationKeys")
    )


@dataclass
class LinkTripleAndTime(DataClassJsonMixin):
    triple: LinkTriple = field(metadata=config(field_name="triple"))
    time: Time = field(metadata=config(field_name="time"))


@dataclass
class FastTeamSigChainState(DataClassJsonMixin):
    per_team_key_seeds_verified: Dict[str, PerTeamKeySeed] = field(
        metadata=config(field_name="perTeamKeySeedsVerified")
    )
    id: TeamID = field(metadata=config(field_name="ID"))
    root_ancestor: TeamName = field(metadata=config(field_name="rootAncestor"))
    name_depth: int = field(metadata=config(field_name="nameDepth"))
    link_i_ds: Dict[str, LinkID] = field(metadata=config(field_name="linkIDs"))
    per_team_keys: Dict[str, PerTeamKey] = field(
        metadata=config(field_name="perTeamKeys")
    )
    public: bool = field(metadata=config(field_name="public"))
    down_pointers: Dict[str, DownPointer] = field(
        metadata=config(field_name="downPointers")
    )
    per_team_key_c_time: UnixTime = field(metadata=config(field_name="perTeamKeyCTime"))
    merkle_info: Dict[str, MerkleRootV2] = field(
        metadata=config(field_name="merkleInfo")
    )
    last_up_pointer: Optional[UpPointer] = field(
        default=None, metadata=config(field_name="lastUpPointer")
    )
    last: Optional[LinkTriple] = field(default=None, metadata=config(field_name="last"))


@dataclass
class AuditHistory(DataClassJsonMixin):
    post_probes: Dict[str, Probe] = field(metadata=config(field_name="postProbes"))
    id: TeamID = field(metadata=config(field_name="ID"))
    prior_merkle_seqno: Seqno = field(metadata=config(field_name="priorMerkleSeqno"))
    version: AuditVersion = field(metadata=config(field_name="version"))
    hidden_tails: Dict[str, LinkID] = field(metadata=config(field_name="hiddenTails"))
    pre_probes: Dict[str, Probe] = field(metadata=config(field_name="preProbes"))
    public: bool = field(metadata=config(field_name="public"))
    tails: Dict[str, LinkID] = field(metadata=config(field_name="tails"))
    skip_until: Time = field(metadata=config(field_name="skipUntil"))
    audits: Optional[List[Audit]] = field(
        default=None, metadata=config(field_name="audits")
    )
    pre_probes_to_retry: Optional[List[Seqno]] = field(
        default=None, metadata=config(field_name="preProbesToRetry")
    )
    post_probes_to_retry: Optional[List[Seqno]] = field(
        default=None, metadata=config(field_name="postProbesToRetry")
    )


@dataclass
class TeamInvite(DataClassJsonMixin):
    role: TeamRole = field(metadata=config(field_name="role"))
    id: TeamInviteID = field(metadata=config(field_name="id"))
    type: TeamInviteType = field(metadata=config(field_name="type"))
    name: TeamInviteName = field(metadata=config(field_name="name"))
    inviter: UserVersion = field(metadata=config(field_name="inviter"))
    max_uses: Optional[TeamInviteMaxUses] = field(
        default=None, metadata=config(field_name="maxUses")
    )
    etime: Optional[UnixTime] = field(default=None, metadata=config(field_name="etime"))


@dataclass
class TeamUsedInviteLogPoint(DataClassJsonMixin):
    uv: UserVersion = field(metadata=config(field_name="uv"))
    log_point: int = field(metadata=config(field_name="logPoint"))


@dataclass
class SubteamLogPoint(DataClassJsonMixin):
    name: TeamName = field(metadata=config(field_name="name"))
    seqno: Seqno = field(metadata=config(field_name="seqno"))


@dataclass
class TeamCLKRMsg(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    generation: PerTeamKeyGeneration = field(metadata=config(field_name="generation"))
    score: int = field(metadata=config(field_name="score"))
    reset_users_untrusted: Optional[List[TeamCLKRResetUser]] = field(
        default=None, metadata=config(field_name="reset_users")
    )


@dataclass
class TeamMemberOutFromReset(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    team_name: str = field(metadata=config(field_name="team_name"))
    reset_user: TeamResetUser = field(metadata=config(field_name="reset_user"))


@dataclass
class TeamSBSMsg(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    score: int = field(metadata=config(field_name="score"))
    invitees: Optional[List[TeamInvitee]] = field(
        default=None, metadata=config(field_name="invitees")
    )


@dataclass
class TeamOpenReqMsg(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    tars: Optional[List[TeamAccessRequest]] = field(
        default=None, metadata=config(field_name="tars")
    )


@dataclass
class SeitanKeyAndLabelVersion1(DataClassJsonMixin):
    i: SeitanIKey = field(metadata=config(field_name="i"))
    l: SeitanKeyLabel = field(metadata=config(field_name="l"))


@dataclass
class SeitanKeyAndLabelVersion2(DataClassJsonMixin):
    k: SeitanPubKey = field(metadata=config(field_name="k"))
    l: SeitanKeyLabel = field(metadata=config(field_name="l"))


@dataclass
class SeitanKeyAndLabelInvitelink(DataClassJsonMixin):
    i: SeitanIKeyInvitelink = field(metadata=config(field_name="i"))
    l: SeitanKeyLabel = field(metadata=config(field_name="l"))


@dataclass
class TeamSeitanMsg(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    seitans: Optional[List[TeamSeitanRequest]] = field(
        default=None, metadata=config(field_name="seitans")
    )


@dataclass
class TeamOpenSweepMsg(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    reset_users_untrusted: Optional[List[TeamCLKRResetUser]] = field(
        default=None, metadata=config(field_name="reset_users")
    )


@dataclass
class TeamRefreshers(DataClassJsonMixin):
    need_key_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="needKeyGeneration")
    )
    need_applications_at_generations: Dict[
        str, Optional[List[TeamApplication]]
    ] = field(metadata=config(field_name="needApplicationsAtGenerations"))
    need_applications_at_generations_with_kbfs: Dict[
        str, Optional[List[TeamApplication]]
    ] = field(metadata=config(field_name="needApplicationsAtGenerationsWithKBFS"))
    want_members_role: TeamRole = field(metadata=config(field_name="wantMembersRole"))
    need_kbfs_key_generation: TeamKBFSKeyRefresher = field(
        metadata=config(field_name="needKBFSKeyGeneration")
    )
    want_members: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="wantMembers")
    )


@dataclass
class FastTeamLoadArg(DataClassJsonMixin):
    id: TeamID = field(metadata=config(field_name="ID"))
    public: bool = field(metadata=config(field_name="public"))
    need_latest_key: bool = field(metadata=config(field_name="needLatestKey"))
    force_refresh: bool = field(metadata=config(field_name="forceRefresh"))
    hidden_chain_is_optional: bool = field(
        metadata=config(field_name="hiddenChainIsOptional")
    )
    assert_team_name: Optional[TeamName] = field(
        default=None, metadata=config(field_name="assertTeamName")
    )
    applications: Optional[List[TeamApplication]] = field(
        default=None, metadata=config(field_name="applications")
    )
    key_generations_needed: Optional[List[PerTeamKeyGeneration]] = field(
        default=None, metadata=config(field_name="keyGenerationsNeeded")
    )


@dataclass
class FastTeamLoadRes(DataClassJsonMixin):
    name: TeamName = field(metadata=config(field_name="name"))
    application_keys: Optional[List[TeamApplicationKey]] = field(
        default=None, metadata=config(field_name="applicationKeys")
    )


@dataclass
class MemberInfo(DataClassJsonMixin):
    user_id: UID = field(metadata=config(field_name="uid"))
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    fq_name: str = field(metadata=config(field_name="fq_name"))
    is_implicit_team: bool = field(metadata=config(field_name="is_implicit_team"))
    is_open_team: bool = field(metadata=config(field_name="is_open_team"))
    role: TeamRole = field(metadata=config(field_name="role"))
    member_count: int = field(metadata=config(field_name="member_count"))
    allow_profile_promote: bool = field(
        metadata=config(field_name="allow_profile_promote")
    )
    is_member_showcased: bool = field(metadata=config(field_name="is_member_showcased"))
    implicit: Optional[ImplicitRole] = field(
        default=None, metadata=config(field_name="implicit")
    )


@dataclass
class AnnotatedMemberInfo(DataClassJsonMixin):
    role: TeamRole = field(metadata=config(field_name="role"))
    user_id: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    full_name: str = field(metadata=config(field_name="full_name"))
    fq_name: str = field(metadata=config(field_name="fq_name"))
    is_implicit_team: bool = field(metadata=config(field_name="is_implicit_team"))
    imp_team_display_name: str = field(
        metadata=config(field_name="implicit_team_display_name")
    )
    is_open_team: bool = field(metadata=config(field_name="is_open_team"))
    team_id: TeamID = field(metadata=config(field_name="team_id"))
    is_member_showcased: bool = field(metadata=config(field_name="is_member_showcased"))
    needs_puk: bool = field(metadata=config(field_name="needsPUK"))
    member_count: int = field(metadata=config(field_name="member_count"))
    eldest_seqno: Seqno = field(metadata=config(field_name="member_eldest_seqno"))
    allow_profile_promote: bool = field(
        metadata=config(field_name="allow_profile_promote")
    )
    status: TeamMemberStatus = field(metadata=config(field_name="status"))
    implicit: Optional[ImplicitRole] = field(
        default=None, metadata=config(field_name="implicit")
    )


@dataclass
class TeamAddMemberResult(DataClassJsonMixin):
    invited: bool = field(metadata=config(field_name="invited"))
    chat_sending: bool = field(metadata=config(field_name="chatSending"))
    user: Optional[User] = field(default=None, metadata=config(field_name="user"))


@dataclass
class TeamAddMembersResult(DataClassJsonMixin):
    not_added: Optional[List[User]] = field(
        default=None, metadata=config(field_name="notAdded")
    )


@dataclass
class TeamTreeEntry(DataClassJsonMixin):
    name: TeamName = field(metadata=config(field_name="name"))
    admin: bool = field(metadata=config(field_name="admin"))


@dataclass
class SubteamListEntry(DataClassJsonMixin):
    name: TeamName = field(metadata=config(field_name="name"))
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    member_count: int = field(metadata=config(field_name="memberCount"))


@dataclass
class TeamAndMemberShowcase(DataClassJsonMixin):
    team_showcase: TeamShowcase = field(metadata=config(field_name="teamShowcase"))
    is_member_showcased: bool = field(metadata=config(field_name="isMemberShowcased"))


@dataclass
class TeamRemoveMembersResult(DataClassJsonMixin):
    failures: Optional[List[TeamMemberToRemove]] = field(
        default=None, metadata=config(field_name="failures")
    )


@dataclass
class TeamEditMembersResult(DataClassJsonMixin):
    failures: Optional[List[UserRolePair]] = field(
        default=None, metadata=config(field_name="failures")
    )


@dataclass
class InviteLinkDetails(DataClassJsonMixin):
    invite_id: TeamInviteID = field(metadata=config(field_name="inviteID"))
    inviter_uid: UID = field(metadata=config(field_name="inviterUID"))
    inviter_username: str = field(metadata=config(field_name="inviterUsername"))
    inviter_reset_or_del: bool = field(metadata=config(field_name="inviterResetOrDel"))
    team_is_open: bool = field(metadata=config(field_name="teamIsOpen"))
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    team_desc: str = field(metadata=config(field_name="teamDesc"))
    team_name: TeamName = field(metadata=config(field_name="teamName"))
    team_num_members: int = field(metadata=config(field_name="teamNumMembers"))
    team_avatars: Dict[str, AvatarUrl] = field(
        metadata=config(field_name="teamAvatars")
    )


@dataclass
class ImplicitTeamUserSet(DataClassJsonMixin):
    keybase_users: Optional[List[str]] = field(
        default=None, metadata=config(field_name="keybaseUsers")
    )
    unresolved_users: Optional[List[SocialAssertion]] = field(
        default=None, metadata=config(field_name="unresolvedUsers")
    )


@dataclass
class TeamProfileAddEntry(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    team_name: TeamName = field(metadata=config(field_name="teamName"))
    open: bool = field(metadata=config(field_name="open"))
    disabled_reason: str = field(metadata=config(field_name="disabledReason"))


@dataclass
class TeamRoleMapAndVersion(DataClassJsonMixin):
    teams: Dict[str, TeamRolePair] = field(metadata=config(field_name="teams"))
    version: UserTeamVersion = field(metadata=config(field_name="user_team_version"))


@dataclass
class TeamTreeMembershipResult__OK(DataClassJsonMixin):
    s: Literal[TeamTreeMembershipStatusStrings.OK]
    OK: Optional[TeamTreeMembershipValue]


@dataclass
class TeamTreeMembershipResult__ERROR(DataClassJsonMixin):
    s: Literal[TeamTreeMembershipStatusStrings.ERROR]
    ERROR: Optional[TeamTreeError]


@dataclass
class TeamTreeMembershipResult__HIDDEN(DataClassJsonMixin):
    s: Literal[TeamTreeMembershipStatusStrings.HIDDEN]
    HIDDEN: None


TeamTreeMembershipResult = Union[
    TeamTreeMembershipResult__OK,
    TeamTreeMembershipResult__ERROR,
    TeamTreeMembershipResult__HIDDEN,
]


@dataclass
class TeamSearchExport(DataClassJsonMixin):
    items: Dict[str, TeamSearchItem] = field(metadata=config(field_name="items"))
    suggested: Optional[List[TeamID]] = field(
        default=None, metadata=config(field_name="suggested")
    )


@dataclass
class TeamSearchRes(DataClassJsonMixin):
    results: Optional[List[TeamSearchItem]] = field(
        default=None, metadata=config(field_name="results")
    )


@dataclass
class MerkleTreeLocation(DataClassJsonMixin):
    leaf: UserOrTeamID = field(metadata=config(field_name="leaf"))
    loc: SigChainLocation = field(metadata=config(field_name="loc"))


@dataclass
class SignatureMetadata(DataClassJsonMixin):
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


@dataclass
class Proofs(DataClassJsonMixin):
    social: Optional[List[TrackProof]] = field(
        default=None, metadata=config(field_name="social")
    )
    web: Optional[List[WebProof]] = field(
        default=None, metadata=config(field_name="web")
    )
    public_keys: Optional[List[PublicKey]] = field(
        default=None, metadata=config(field_name="publicKeys")
    )


@dataclass
class UserSummarySet(DataClassJsonMixin):
    time: Time = field(metadata=config(field_name="time"))
    version: int = field(metadata=config(field_name="version"))
    users: Optional[List[UserSummary]] = field(
        default=None, metadata=config(field_name="users")
    )


@dataclass
class UserSettings(DataClassJsonMixin):
    emails: Optional[List[Email]] = field(
        default=None, metadata=config(field_name="emails")
    )
    phone_numbers: Optional[List[UserPhoneNumber]] = field(
        default=None, metadata=config(field_name="phoneNumbers")
    )


@dataclass
class ProofSuggestion(DataClassJsonMixin):
    key: str = field(metadata=config(field_name="key"))
    below_fold: bool = field(metadata=config(field_name="belowFold"))
    profile_text: str = field(metadata=config(field_name="profileText"))
    picker_text: str = field(metadata=config(field_name="pickerText"))
    picker_subtext: str = field(metadata=config(field_name="pickerSubtext"))
    profile_icon: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="profileIcon")
    )
    profile_icon_darkmode: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="profileIconDarkmode")
    )
    picker_icon: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="pickerIcon")
    )
    picker_icon_darkmode: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="pickerIconDarkmode")
    )
    metas: Optional[List[Identify3RowMeta]] = field(
        default=None, metadata=config(field_name="metas")
    )


@dataclass
class NextMerkleRootRes(DataClassJsonMixin):
    res: Optional[MerkleRootV2] = field(default=None, metadata=config(field_name="res"))


@dataclass
class UserBlockedBody(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="blocker_uid"))
    username: str = field(metadata=config(field_name="blocker_username"))
    blocks: Optional[List[UserBlockedRow]] = field(
        default=None, metadata=config(field_name="blocks")
    )


@dataclass
class UserBlockedSummary(DataClassJsonMixin):
    blocker: str = field(metadata=config(field_name="blocker"))
    blocks: Dict[str, Optional[List[UserBlockState]]] = field(
        metadata=config(field_name="blocks")
    )


@dataclass
class Confidence(DataClassJsonMixin):
    username_verified_via: UsernameVerificationType = field(
        metadata=config(field_name="username_verified_via,omitempty")
    )
    other: str = field(metadata=config(field_name="other,omitempty"))
    proofs: Optional[List[WotProof]] = field(
        default=None, metadata=config(field_name="proofs,omitempty")
    )


@dataclass
class BlockReferenceCount(DataClassJsonMixin):
    ref: BlockReference = field(metadata=config(field_name="ref"))
    live_count: int = field(metadata=config(field_name="liveCount"))


@dataclass
class ReferenceCountRes(DataClassJsonMixin):
    counts: Optional[List[BlockIdCount]] = field(
        default=None, metadata=config(field_name="counts")
    )


@dataclass
class BlockQuotaInfo(DataClassJsonMixin):
    total: UsageStat = field(metadata=config(field_name="total"))
    limit: int = field(metadata=config(field_name="limit"))
    git_limit: int = field(metadata=config(field_name="gitLimit"))
    folders: Optional[List[FolderUsageStat]] = field(
        default=None, metadata=config(field_name="folders")
    )


@dataclass
class UserPlusKeys(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    status: StatusCode = field(metadata=config(field_name="status"))
    username: str = field(metadata=config(field_name="username"))
    pgp_key_count: int = field(metadata=config(field_name="pgpKeyCount"))
    uvv: UserVersionVector = field(metadata=config(field_name="uvv"))
    device_keys: Optional[List[PublicKey]] = field(
        default=None, metadata=config(field_name="deviceKeys")
    )
    resets: Optional[List[ResetSummary]] = field(
        default=None, metadata=config(field_name="resets")
    )
    deleted_device_keys: Optional[List[PublicKey]] = field(
        default=None, metadata=config(field_name="deletedDeviceKeys")
    )
    per_user_keys: Optional[List[PerUserKey]] = field(
        default=None, metadata=config(field_name="perUserKeys")
    )
    revoked_device_keys: Optional[List[RevokedKey]] = field(
        default=None, metadata=config(field_name="revokedDeviceKeys")
    )


@dataclass
class ExtendedStatus(DataClassJsonMixin):
    standalone: bool = field(metadata=config(field_name="standalone"))
    ui_router_mapping: Dict[str, int] = field(
        metadata=config(field_name="uiRouterMapping")
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
    default_device_id: DeviceID = field(metadata=config(field_name="defaultDeviceID"))
    platform_info: PlatformInfo = field(metadata=config(field_name="platformInfo"))
    log_dir: str = field(metadata=config(field_name="logDir"))
    passphrase_stream_cached: bool = field(
        metadata=config(field_name="passphraseStreamCached")
    )
    default_username: str = field(metadata=config(field_name="defaultUsername"))
    local_db_stats: Optional[List[str]] = field(
        default=None, metadata=config(field_name="localDbStats")
    )
    provisioned_usernames: Optional[List[str]] = field(
        default=None, metadata=config(field_name="provisionedUsernames")
    )
    clients: Optional[List[ClientStatus]] = field(
        default=None, metadata=config(field_name="Clients")
    )
    device_ek_names: Optional[List[str]] = field(
        default=None, metadata=config(field_name="deviceEkNames")
    )
    device_err: Optional[LoadDeviceErr] = field(
        default=None, metadata=config(field_name="deviceErr")
    )
    device: Optional[Device] = field(default=None, metadata=config(field_name="device"))
    configured_accounts: Optional[List[ConfiguredAccount]] = field(
        default=None, metadata=config(field_name="configuredAccounts")
    )
    local_chat_db_stats: Optional[List[str]] = field(
        default=None, metadata=config(field_name="localChatDbStats")
    )
    local_block_cache_db_stats: Optional[List[str]] = field(
        default=None, metadata=config(field_name="localBlockCacheDbStats")
    )
    local_sync_cache_db_stats: Optional[List[str]] = field(
        default=None, metadata=config(field_name="localSyncCacheDbStats")
    )
    cache_dir_size_info: Optional[List[DirSizeInfo]] = field(
        default=None, metadata=config(field_name="cacheDirSizeInfo")
    )
    session: Optional[SessionStatus] = field(
        default=None, metadata=config(field_name="session")
    )


@dataclass
class ContactListResolutionResult(DataClassJsonMixin):
    newly_resolved: Optional[List[ProcessedContact]] = field(
        default=None, metadata=config(field_name="newlyResolved")
    )
    resolved: Optional[List[ProcessedContact]] = field(
        default=None, metadata=config(field_name="resolved")
    )


@dataclass
class TeamEphemeralKey__TEAM(DataClassJsonMixin):
    keyType: Literal[TeamEphemeralKeyTypeStrings.TEAM]
    TEAM: Optional[TeamEk]


@dataclass
class TeamEphemeralKey__TEAMBOT(DataClassJsonMixin):
    keyType: Literal[TeamEphemeralKeyTypeStrings.TEAMBOT]
    TEAMBOT: Optional[TeambotEk]


TeamEphemeralKey = Union[TeamEphemeralKey__TEAM, TeamEphemeralKey__TEAMBOT]


@dataclass
class TeamEphemeralKeyBoxed__TEAM(DataClassJsonMixin):
    keyType: Literal[TeamEphemeralKeyTypeStrings.TEAM]
    TEAM: Optional[TeamEkBoxed]


@dataclass
class TeamEphemeralKeyBoxed__TEAMBOT(DataClassJsonMixin):
    keyType: Literal[TeamEphemeralKeyTypeStrings.TEAMBOT]
    TEAMBOT: Optional[TeambotEkBoxed]


TeamEphemeralKeyBoxed = Union[
    TeamEphemeralKeyBoxed__TEAM, TeamEphemeralKeyBoxed__TEAMBOT
]


@dataclass
class GitLocalMetadata(DataClassJsonMixin):
    repo_name: GitRepoName = field(metadata=config(field_name="repoName"))
    push_type: GitPushType = field(metadata=config(field_name="pushType"))
    previous_repo_name: GitRepoName = field(
        metadata=config(field_name="previousRepoName")
    )
    refs: Optional[List[GitRefMetadata]] = field(
        default=None, metadata=config(field_name="refs")
    )


@dataclass
class HomeScreenItemDataExt__TODO(DataClassJsonMixin):
    t: Literal[HomeScreenItemTypeStrings.TODO]
    TODO: Optional[HomeScreenTodoExt]


HomeScreenItemDataExt = Union[HomeScreenItemDataExt__TODO]


@dataclass
class HomeScreenPeopleNotificationFollowedMulti(DataClassJsonMixin):
    num_others: int = field(metadata=config(field_name="numOthers"))
    followers: Optional[List[HomeScreenPeopleNotificationFollowed]] = field(
        default=None, metadata=config(field_name="followers")
    )


@dataclass
class Identity(DataClassJsonMixin):
    when_last_tracked: Time = field(metadata=config(field_name="whenLastTracked"))
    breaks_tracking: bool = field(metadata=config(field_name="breaksTracking"))
    status: Optional[Status] = field(default=None, metadata=config(field_name="status"))
    proofs: Optional[List[IdentifyRow]] = field(
        default=None, metadata=config(field_name="proofs")
    )
    cryptocurrency: Optional[List[Cryptocurrency]] = field(
        default=None, metadata=config(field_name="cryptocurrency")
    )
    revoked: Optional[List[TrackDiff]] = field(
        default=None, metadata=config(field_name="revoked")
    )
    revoked_details: Optional[List[RevokedProof]] = field(
        default=None, metadata=config(field_name="revokedDetails")
    )


@dataclass
class LinkCheckResult(DataClassJsonMixin):
    proof_id: int = field(metadata=config(field_name="proofId"))
    proof_result: ProofResult = field(metadata=config(field_name="proofResult"))
    snoozed_result: ProofResult = field(metadata=config(field_name="snoozedResult"))
    tor_warning: bool = field(metadata=config(field_name="torWarning"))
    tmp_track_expire_time: Time = field(
        metadata=config(field_name="tmpTrackExpireTime")
    )
    breaks_tracking: bool = field(metadata=config(field_name="breaksTracking"))
    cached: Optional[CheckResult] = field(
        default=None, metadata=config(field_name="cached")
    )
    diff: Optional[TrackDiff] = field(default=None, metadata=config(field_name="diff"))
    remote_diff: Optional[TrackDiff] = field(
        default=None, metadata=config(field_name="remoteDiff")
    )
    hint: Optional[SigHint] = field(default=None, metadata=config(field_name="hint"))


@dataclass
class ServicesStatus(DataClassJsonMixin):
    service: Optional[List[ServiceStatus]] = field(
        default=None, metadata=config(field_name="service")
    )
    kbfs: Optional[List[ServiceStatus]] = field(
        default=None, metadata=config(field_name="kbfs")
    )
    updater: Optional[List[ServiceStatus]] = field(
        default=None, metadata=config(field_name="updater")
    )


@dataclass
class InstallResult(DataClassJsonMixin):
    status: Status = field(metadata=config(field_name="status"))
    fatal: bool = field(metadata=config(field_name="fatal"))
    component_results: Optional[List[ComponentResult]] = field(
        default=None, metadata=config(field_name="componentResults")
    )


@dataclass
class UninstallResult(DataClassJsonMixin):
    status: Status = field(metadata=config(field_name="status"))
    component_results: Optional[List[ComponentResult]] = field(
        default=None, metadata=config(field_name="componentResults")
    )


@dataclass
class ProblemSet(DataClassJsonMixin):
    user: User = field(metadata=config(field_name="user"))
    kid: KID = field(metadata=config(field_name="kid"))
    tlfs: Optional[List[ProblemTLF]] = field(
        default=None, metadata=config(field_name="tlfs")
    )


@dataclass
class SaltpackPlaintextResult(DataClassJsonMixin):
    info: SaltpackEncryptedMessageInfo = field(metadata=config(field_name="info"))
    plaintext: str = field(metadata=config(field_name="plaintext"))
    signed: bool = field(metadata=config(field_name="signed"))


@dataclass
class SaltpackFileResult(DataClassJsonMixin):
    info: SaltpackEncryptedMessageInfo = field(metadata=config(field_name="info"))
    decrypted_filename: str = field(metadata=config(field_name="decryptedFilename"))
    signed: bool = field(metadata=config(field_name="signed"))


@dataclass
class Path__LOCAL(DataClassJsonMixin):
    PathType: Literal[PathTypeStrings.LOCAL]
    LOCAL: Optional[str]


@dataclass
class Path__KBFS(DataClassJsonMixin):
    PathType: Literal[PathTypeStrings.KBFS]
    KBFS: Optional[KBFSPath]


@dataclass
class Path__KBFS_ARCHIVED(DataClassJsonMixin):
    PathType: Literal[PathTypeStrings.KBFS_ARCHIVED]
    KBFS_ARCHIVED: Optional[KBFSArchivedPath]


Path = Union[Path__LOCAL, Path__KBFS, Path__KBFS_ARCHIVED]


@dataclass
class DirentWithRevision(DataClassJsonMixin):
    entry: Dirent = field(metadata=config(field_name="entry"))
    revision: KBFSRevision = field(metadata=config(field_name="revision"))


@dataclass
class SimpleFSListResult(DataClassJsonMixin):
    progress: Progress = field(metadata=config(field_name="progress"))
    entries: Optional[List[Dirent]] = field(
        default=None, metadata=config(field_name="entries")
    )


@dataclass
class FolderSyncConfigAndStatus(DataClassJsonMixin):
    config_: FolderSyncConfig = field(metadata=config(field_name="config"))
    status: FolderSyncStatus = field(metadata=config(field_name="status"))


@dataclass
class TeamMembersDetails(DataClassJsonMixin):
    owners: Optional[List[TeamMemberDetails]] = field(
        default=None, metadata=config(field_name="owners")
    )
    admins: Optional[List[TeamMemberDetails]] = field(
        default=None, metadata=config(field_name="admins")
    )
    writers: Optional[List[TeamMemberDetails]] = field(
        default=None, metadata=config(field_name="writers")
    )
    readers: Optional[List[TeamMemberDetails]] = field(
        default=None, metadata=config(field_name="readers")
    )
    bots: Optional[List[TeamMemberDetails]] = field(
        default=None, metadata=config(field_name="bots")
    )
    restricted_bots: Optional[List[TeamMemberDetails]] = field(
        default=None, metadata=config(field_name="restrictedBots")
    )


@dataclass
class FastTeamData(DataClassJsonMixin):
    max_continuous_ptk_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="maxContinuousPTKGeneration")
    )
    frozen: bool = field(metadata=config(field_name="frozen"))
    tombstoned: bool = field(metadata=config(field_name="tombstoned"))
    name: TeamName = field(metadata=config(field_name="name"))
    chain: FastTeamSigChainState = field(metadata=config(field_name="chain"))
    per_team_key_seeds_unverified: Dict[str, PerTeamKeySeed] = field(
        metadata=config(field_name="perTeamKeySeedsUnverified")
    )
    subversion: int = field(metadata=config(field_name="subversion"))
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


@dataclass
class HiddenTeamChainRatchetSet(DataClassJsonMixin):
    ratchets: Dict[str, LinkTripleAndTime] = field(
        metadata=config(field_name="ratchets")
    )


@dataclass
class HiddenTeamChainLink(DataClassJsonMixin):
    merkle_root: MerkleRootV2 = field(metadata=config(field_name="m"))
    parent_chain: LinkTriple = field(metadata=config(field_name="p"))
    signer: Signer = field(metadata=config(field_name="s"))
    ptk: Dict[str, PerTeamKeyAndCheck] = field(metadata=config(field_name="k"))


@dataclass
class UserLogPoint(DataClassJsonMixin):
    role: TeamRole = field(metadata=config(field_name="role"))
    sig_meta: SignatureMetadata = field(metadata=config(field_name="sigMeta"))


@dataclass
class AnnotatedTeamUsedInviteLogPoint(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    team_used_invite_log_point: TeamUsedInviteLogPoint = field(
        metadata=config(field_name="teamUsedInviteLogPoint")
    )


@dataclass
class SeitanKeyAndLabel__V1(DataClassJsonMixin):
    v: Literal[SeitanKeyAndLabelVersionStrings.V1]
    V1: Optional[SeitanKeyAndLabelVersion1]


@dataclass
class SeitanKeyAndLabel__V2(DataClassJsonMixin):
    v: Literal[SeitanKeyAndLabelVersionStrings.V2]
    V2: Optional[SeitanKeyAndLabelVersion2]


@dataclass
class SeitanKeyAndLabel__Invitelink(DataClassJsonMixin):
    v: Literal[SeitanKeyAndLabelVersionStrings.Invitelink]
    Invitelink: Optional[SeitanKeyAndLabelInvitelink]


SeitanKeyAndLabel = Union[
    SeitanKeyAndLabel__V1, SeitanKeyAndLabel__V2, SeitanKeyAndLabel__Invitelink
]


@dataclass
class LoadTeamArg(DataClassJsonMixin):
    force_full_reload: bool = field(metadata=config(field_name="forceFullReload"))
    id: TeamID = field(metadata=config(field_name="ID"))
    public: bool = field(metadata=config(field_name="public"))
    need_admin: bool = field(metadata=config(field_name="needAdmin"))
    refresh_uid_mapper: bool = field(metadata=config(field_name="refreshUIDMapper"))
    refreshers: TeamRefreshers = field(metadata=config(field_name="refreshers"))
    name: str = field(metadata=config(field_name="name"))
    force_repoll: bool = field(metadata=config(field_name="forceRepoll"))
    stale_ok: bool = field(metadata=config(field_name="staleOK"))
    allow_name_lookup_burst_cache: bool = field(
        metadata=config(field_name="allowNameLookupBurstCache")
    )
    skip_need_hidden_rotate_check: bool = field(
        metadata=config(field_name="skipNeedHiddenRotateCheck")
    )
    audit_mode: AuditMode = field(metadata=config(field_name="auditMode"))


@dataclass
class TeamList(DataClassJsonMixin):
    teams: Optional[List[MemberInfo]] = field(
        default=None, metadata=config(field_name="teams")
    )


@dataclass
class TeamTreeResult(DataClassJsonMixin):
    entries: Optional[List[TeamTreeEntry]] = field(
        default=None, metadata=config(field_name="entries")
    )


@dataclass
class SubteamListResult(DataClassJsonMixin):
    entries: Optional[List[SubteamListEntry]] = field(
        default=None, metadata=config(field_name="entries")
    )


@dataclass
class ImplicitTeamDisplayName(DataClassJsonMixin):
    is_public: bool = field(metadata=config(field_name="isPublic"))
    writers: ImplicitTeamUserSet = field(metadata=config(field_name="writers"))
    readers: ImplicitTeamUserSet = field(metadata=config(field_name="readers"))
    conflict_info: Optional[ImplicitTeamConflictInfo] = field(
        default=None, metadata=config(field_name="conflictInfo")
    )


@dataclass
class TeamRoleMapStored(DataClassJsonMixin):
    data: TeamRoleMapAndVersion = field(metadata=config(field_name="data"))
    cached_at: Time = field(metadata=config(field_name="cachedAt"))


@dataclass
class AnnotatedTeamMemberDetails(DataClassJsonMixin):
    details: TeamMemberDetails = field(metadata=config(field_name="details"))
    role: TeamRole = field(metadata=config(field_name="role"))


@dataclass
class TeamTreeMembership(DataClassJsonMixin):
    team_name: str = field(metadata=config(field_name="teamName"))
    result: TeamTreeMembershipResult = field(metadata=config(field_name="result"))
    target_team_id: TeamID = field(metadata=config(field_name="targetTeamID"))
    target_username: str = field(metadata=config(field_name="targetUsername"))
    guid: int = field(metadata=config(field_name="guid"))


@dataclass
class PublicKeyV2Base(DataClassJsonMixin):
    kid: KID = field(metadata=config(field_name="kid"))
    is_sibkey: bool = field(metadata=config(field_name="isSibkey"))
    is_eldest: bool = field(metadata=config(field_name="isEldest"))
    c_time: Time = field(metadata=config(field_name="cTime"))
    e_time: Time = field(metadata=config(field_name="eTime"))
    provisioning: SignatureMetadata = field(metadata=config(field_name="provisioning"))
    revocation: Optional[SignatureMetadata] = field(
        default=None, metadata=config(field_name="revocation")
    )


@dataclass
class ProofSuggestionsRes(DataClassJsonMixin):
    show_more: bool = field(metadata=config(field_name="showMore"))
    suggestions: Optional[List[ProofSuggestion]] = field(
        default=None, metadata=config(field_name="suggestions")
    )


@dataclass
class APIUserSearchResult(DataClassJsonMixin):
    score: float = field(metadata=config(field_name="score"))
    services_summary: Dict[str, APIUserServiceSummary] = field(
        metadata=config(field_name="services_summary")
    )
    raw_score: float = field(metadata=config(field_name="rawScore"))
    keybase: Optional[APIUserKeybaseResult] = field(
        default=None, metadata=config(field_name="keybase")
    )
    service: Optional[APIUserServiceResult] = field(
        default=None, metadata=config(field_name="service")
    )
    contact: Optional[ProcessedContact] = field(
        default=None, metadata=config(field_name="contact")
    )
    imptofu: Optional[ImpTofuSearchResult] = field(
        default=None, metadata=config(field_name="imptofu")
    )


@dataclass
class NonUserDetails(DataClassJsonMixin):
    is_non_user: bool = field(metadata=config(field_name="isNonUser"))
    assertion_value: str = field(metadata=config(field_name="assertionValue"))
    assertion_key: str = field(metadata=config(field_name="assertionKey"))
    description: str = field(metadata=config(field_name="description"))
    contact: Optional[ProcessedContact] = field(
        default=None, metadata=config(field_name="contact")
    )
    service: Optional[APIUserServiceResult] = field(
        default=None, metadata=config(field_name="service")
    )
    site_icon: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="siteIcon")
    )
    site_icon_darkmode: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="siteIconDarkmode")
    )
    site_icon_full: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="siteIconFull")
    )
    site_icon_full_darkmode: Optional[List[SizedImage]] = field(
        default=None, metadata=config(field_name="siteIconFullDarkmode")
    )


@dataclass
class WotVouch(DataClassJsonMixin):
    status: WotStatusType = field(metadata=config(field_name="status"))
    vouch_proof: SigID = field(metadata=config(field_name="vouchProof"))
    vouchee: UserVersion = field(metadata=config(field_name="vouchee"))
    vouchee_username: str = field(metadata=config(field_name="voucheeUsername"))
    voucher: UserVersion = field(metadata=config(field_name="voucher"))
    voucher_username: str = field(metadata=config(field_name="voucherUsername"))
    vouched_at: Time = field(metadata=config(field_name="vouchedAt"))
    vouch_texts: Optional[List[str]] = field(
        default=None, metadata=config(field_name="vouchTexts")
    )
    confidence: Optional[Confidence] = field(
        default=None, metadata=config(field_name="confidence")
    )


@dataclass
class DowngradeReferenceRes(DataClassJsonMixin):
    failed: BlockReference = field(metadata=config(field_name="failed"))
    completed: Optional[List[BlockReferenceCount]] = field(
        default=None, metadata=config(field_name="completed")
    )


@dataclass
class UserPlusAllKeys(DataClassJsonMixin):
    base: UserPlusKeys = field(metadata=config(field_name="base"))
    pgp_keys: Optional[List[PublicKey]] = field(
        default=None, metadata=config(field_name="pgpKeys")
    )
    remote_tracks: Optional[List[RemoteTrack]] = field(
        default=None, metadata=config(field_name="remoteTracks")
    )


@dataclass
class FullStatus(DataClassJsonMixin):
    service: KbServiceStatus = field(metadata=config(field_name="service"))
    username: str = field(metadata=config(field_name="username"))
    cur_status: CurrentStatus = field(metadata=config(field_name="curStatus"))
    ext_status: ExtendedStatus = field(metadata=config(field_name="extStatus"))
    client: KbClientStatus = field(metadata=config(field_name="client"))
    config_path: str = field(metadata=config(field_name="configPath"))
    kbfs: KBFSStatus = field(metadata=config(field_name="kbfs"))
    desktop: DesktopStatus = field(metadata=config(field_name="desktop"))
    updater: UpdaterStatus = field(metadata=config(field_name="updater"))
    start: StartStatus = field(metadata=config(field_name="start"))
    git: GitStatus = field(metadata=config(field_name="git"))


@dataclass
class FolderNormalView(DataClassJsonMixin):
    resolving_conflict: bool = field(metadata=config(field_name="resolvingConflict"))
    stuck_in_conflict: bool = field(metadata=config(field_name="stuckInConflict"))
    local_views: Optional[List[Path]] = field(
        default=None, metadata=config(field_name="localViews")
    )


@dataclass
class FolderConflictManualResolvingLocalView(DataClassJsonMixin):
    normal_view: Path = field(metadata=config(field_name="normalView"))


@dataclass
class GitRepoInfo(DataClassJsonMixin):
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
        default=None, metadata=config(field_name="teamRepoSettings")
    )


@dataclass
class HomeScreenPeopleNotification__FOLLOWED(DataClassJsonMixin):
    t: Literal[HomeScreenPeopleNotificationTypeStrings.FOLLOWED]
    FOLLOWED: Optional[HomeScreenPeopleNotificationFollowed]


@dataclass
class HomeScreenPeopleNotification__FOLLOWED_MULTI(DataClassJsonMixin):
    t: Literal[HomeScreenPeopleNotificationTypeStrings.FOLLOWED_MULTI]
    FOLLOWED_MULTI: Optional[HomeScreenPeopleNotificationFollowedMulti]


@dataclass
class HomeScreenPeopleNotification__CONTACT(DataClassJsonMixin):
    t: Literal[HomeScreenPeopleNotificationTypeStrings.CONTACT]
    CONTACT: Optional[HomeScreenPeopleNotificationContact]


@dataclass
class HomeScreenPeopleNotification__CONTACT_MULTI(DataClassJsonMixin):
    t: Literal[HomeScreenPeopleNotificationTypeStrings.CONTACT_MULTI]
    CONTACT_MULTI: Optional[HomeScreenPeopleNotificationContactMulti]


HomeScreenPeopleNotification = Union[
    HomeScreenPeopleNotification__FOLLOWED,
    HomeScreenPeopleNotification__FOLLOWED_MULTI,
    HomeScreenPeopleNotification__CONTACT,
    HomeScreenPeopleNotification__CONTACT_MULTI,
]


@dataclass
class IdentifyProofBreak(DataClassJsonMixin):
    remote_proof: RemoteProof = field(metadata=config(field_name="remoteProof"))
    lcr: LinkCheckResult = field(metadata=config(field_name="lcr"))


@dataclass
class ProblemSetDevices(DataClassJsonMixin):
    problem_set: ProblemSet = field(metadata=config(field_name="problemSet"))
    devices: Optional[List[Device]] = field(
        default=None, metadata=config(field_name="devices")
    )


@dataclass
class ListArgs(DataClassJsonMixin):
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    filter: ListFilter = field(metadata=config(field_name="filter"))


@dataclass
class ListToDepthArgs(DataClassJsonMixin):
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    filter: ListFilter = field(metadata=config(field_name="filter"))
    depth: int = field(metadata=config(field_name="depth"))


@dataclass
class RemoveArgs(DataClassJsonMixin):
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    recursive: bool = field(metadata=config(field_name="recursive"))


@dataclass
class ReadArgs(DataClassJsonMixin):
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    offset: int = field(metadata=config(field_name="offset"))
    size: int = field(metadata=config(field_name="size"))


@dataclass
class WriteArgs(DataClassJsonMixin):
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    offset: int = field(metadata=config(field_name="offset"))


@dataclass
class CopyArgs(DataClassJsonMixin):
    op_id: OpID = field(metadata=config(field_name="opID"))
    src: Path = field(metadata=config(field_name="src"))
    dest: Path = field(metadata=config(field_name="dest"))
    overwrite_existing_files: bool = field(
        metadata=config(field_name="overwriteExistingFiles")
    )


@dataclass
class MoveArgs(DataClassJsonMixin):
    op_id: OpID = field(metadata=config(field_name="opID"))
    src: Path = field(metadata=config(field_name="src"))
    dest: Path = field(metadata=config(field_name="dest"))
    overwrite_existing_files: bool = field(
        metadata=config(field_name="overwriteExistingFiles")
    )


@dataclass
class GetRevisionsArgs(DataClassJsonMixin):
    op_id: OpID = field(metadata=config(field_name="opID"))
    path: Path = field(metadata=config(field_name="path"))
    span_type: RevisionSpanType = field(metadata=config(field_name="spanType"))


@dataclass
class GetRevisionsResult(DataClassJsonMixin):
    progress: Progress = field(metadata=config(field_name="progress"))
    revisions: Optional[List[DirentWithRevision]] = field(
        default=None, metadata=config(field_name="revisions")
    )


@dataclass
class HiddenTeamChain(DataClassJsonMixin):
    link_receipt_times: Dict[str, Time] = field(
        metadata=config(field_name="linkReceiptTimes")
    )
    id: TeamID = field(metadata=config(field_name="id"))
    public: bool = field(metadata=config(field_name="public"))
    frozen: bool = field(metadata=config(field_name="frozen"))
    tombstoned: bool = field(metadata=config(field_name="tombstoned"))
    last: Seqno = field(metadata=config(field_name="last"))
    last_full: Seqno = field(metadata=config(field_name="lastFull"))
    latest_seqno_hint: Seqno = field(metadata=config(field_name="latestSeqnoHint"))
    last_committed_seqno: Seqno = field(
        metadata=config(field_name="lastCommittedSeqno")
    )
    subversion: int = field(metadata=config(field_name="subversion"))
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


@dataclass
class AnnotatedTeamInvite(DataClassJsonMixin):
    invite: TeamInvite = field(metadata=config(field_name="invite"))
    display_name: TeamInviteDisplayName = field(
        metadata=config(field_name="displayName")
    )
    inviter_username: str = field(metadata=config(field_name="inviterUsername"))
    invitee_uv: UserVersion = field(metadata=config(field_name="inviteeUv"))
    team_name: str = field(metadata=config(field_name="teamName"))
    status: Optional[TeamMemberStatus] = field(
        default=None, metadata=config(field_name="status")
    )
    used_invites: Optional[List[AnnotatedTeamUsedInviteLogPoint]] = field(
        default=None, metadata=config(field_name="usedInvites")
    )


@dataclass
class TeamSigChainState(DataClassJsonMixin):
    per_team_keys: Dict[str, PerTeamKey] = field(
        metadata=config(field_name="perTeamKeys")
    )
    reader: UserVersion = field(metadata=config(field_name="reader"))
    implicit: bool = field(metadata=config(field_name="implicit"))
    public: bool = field(metadata=config(field_name="public"))
    root_ancestor: TeamName = field(metadata=config(field_name="rootAncestor"))
    name_depth: int = field(metadata=config(field_name="nameDepth"))
    tlf_legacy_upgrade: Dict[str, TeamLegacyTLFUpgradeChainInfo] = field(
        metadata=config(field_name="tlfLegacyUpgrade")
    )
    last_seqno: Seqno = field(metadata=config(field_name="lastSeqno"))
    last_link_id: LinkID = field(metadata=config(field_name="lastLinkID"))
    last_high_seqno: Seqno = field(metadata=config(field_name="lastHighSeqno"))
    last_high_link_id: LinkID = field(metadata=config(field_name="lastHighLinkID"))
    bots: Dict[str, TeamBotSettings] = field(metadata=config(field_name="bots"))
    user_log: Dict[str, Optional[List[UserLogPoint]]] = field(
        metadata=config(field_name="userLog")
    )
    subteam_log: Dict[str, Optional[List[SubteamLogPoint]]] = field(
        metadata=config(field_name="subteamLog")
    )
    id: TeamID = field(metadata=config(field_name="id"))
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
    used_invites: Dict[str, Optional[List[TeamUsedInviteLogPoint]]] = field(
        metadata=config(field_name="usedInvites")
    )
    open: bool = field(metadata=config(field_name="open"))
    open_team_join_as: TeamRole = field(metadata=config(field_name="openTeamJoinAs"))
    merkle_roots: Dict[str, MerkleRootV2] = field(
        metadata=config(field_name="merkleRoots")
    )
    parent_id: Optional[TeamID] = field(
        default=None, metadata=config(field_name="parentID")
    )
    tlf_i_ds: Optional[List[TLFID]] = field(
        default=None, metadata=config(field_name="tlfIDs")
    )
    name_log: Optional[List[TeamNameLogPoint]] = field(
        default=None, metadata=config(field_name="nameLog")
    )
    head_merkle: Optional[MerkleRootV2] = field(
        default=None, metadata=config(field_name="headMerkle")
    )


@dataclass
class LookupImplicitTeamRes(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    name: TeamName = field(metadata=config(field_name="name"))
    display_name: ImplicitTeamDisplayName = field(
        metadata=config(field_name="displayName")
    )
    tlf_id: TLFID = field(metadata=config(field_name="tlfID"))


@dataclass
class PublicKeyV2NaCl(DataClassJsonMixin):
    base: PublicKeyV2Base = field(metadata=config(field_name="base"))
    device_id: DeviceID = field(metadata=config(field_name="deviceID"))
    device_description: str = field(metadata=config(field_name="deviceDescription"))
    device_type: DeviceTypeV2 = field(metadata=config(field_name="deviceType"))
    parent: Optional[KID] = field(default=None, metadata=config(field_name="parent"))


@dataclass
class PublicKeyV2PGPSummary(DataClassJsonMixin):
    base: PublicKeyV2Base = field(metadata=config(field_name="base"))
    fingerprint: PGPFingerprint = field(metadata=config(field_name="fingerprint"))
    identities: Optional[List[PGPIdentity]] = field(
        default=None, metadata=config(field_name="identities")
    )


@dataclass
class ConflictState__NormalView(DataClassJsonMixin):
    conflictStateType: Literal[ConflictStateTypeStrings.NormalView]
    NormalView: Optional[FolderNormalView]


@dataclass
class ConflictState__ManualResolvingLocalView(DataClassJsonMixin):
    conflictStateType: Literal[ConflictStateTypeStrings.ManualResolvingLocalView]
    ManualResolvingLocalView: Optional[FolderConflictManualResolvingLocalView]


ConflictState = Union[
    ConflictState__NormalView, ConflictState__ManualResolvingLocalView
]


@dataclass
class GitRepoResult__ERR(DataClassJsonMixin):
    state: Literal[GitRepoResultStateStrings.ERR]
    ERR: Optional[str]


@dataclass
class GitRepoResult__OK(DataClassJsonMixin):
    state: Literal[GitRepoResultStateStrings.OK]
    OK: Optional[GitRepoInfo]


GitRepoResult = Union[GitRepoResult__ERR, GitRepoResult__OK]


@dataclass
class HomeScreenItemData__TODO(DataClassJsonMixin):
    t: Literal[HomeScreenItemTypeStrings.TODO]
    TODO: Optional[HomeScreenTodo]


@dataclass
class HomeScreenItemData__PEOPLE(DataClassJsonMixin):
    t: Literal[HomeScreenItemTypeStrings.PEOPLE]
    PEOPLE: Optional[HomeScreenPeopleNotification]


@dataclass
class HomeScreenItemData__ANNOUNCEMENT(DataClassJsonMixin):
    t: Literal[HomeScreenItemTypeStrings.ANNOUNCEMENT]
    ANNOUNCEMENT: Optional[HomeScreenAnnouncement]


HomeScreenItemData = Union[
    HomeScreenItemData__TODO,
    HomeScreenItemData__PEOPLE,
    HomeScreenItemData__ANNOUNCEMENT,
]


@dataclass
class IdentifyTrackBreaks(DataClassJsonMixin):
    keys: Optional[List[IdentifyKey]] = field(
        default=None, metadata=config(field_name="keys")
    )
    proofs: Optional[List[IdentifyProofBreak]] = field(
        default=None, metadata=config(field_name="proofs")
    )


@dataclass
class OpDescription__LIST(DataClassJsonMixin):
    asyncOp: Literal[AsyncOpsStrings.LIST]
    LIST: Optional[ListArgs]


@dataclass
class OpDescription__LIST_RECURSIVE(DataClassJsonMixin):
    asyncOp: Literal[AsyncOpsStrings.LIST_RECURSIVE]
    LIST_RECURSIVE: Optional[ListArgs]


@dataclass
class OpDescription__LIST_RECURSIVE_TO_DEPTH(DataClassJsonMixin):
    asyncOp: Literal[AsyncOpsStrings.LIST_RECURSIVE_TO_DEPTH]
    LIST_RECURSIVE_TO_DEPTH: Optional[ListToDepthArgs]


@dataclass
class OpDescription__READ(DataClassJsonMixin):
    asyncOp: Literal[AsyncOpsStrings.READ]
    READ: Optional[ReadArgs]


@dataclass
class OpDescription__WRITE(DataClassJsonMixin):
    asyncOp: Literal[AsyncOpsStrings.WRITE]
    WRITE: Optional[WriteArgs]


@dataclass
class OpDescription__COPY(DataClassJsonMixin):
    asyncOp: Literal[AsyncOpsStrings.COPY]
    COPY: Optional[CopyArgs]


@dataclass
class OpDescription__MOVE(DataClassJsonMixin):
    asyncOp: Literal[AsyncOpsStrings.MOVE]
    MOVE: Optional[MoveArgs]


@dataclass
class OpDescription__REMOVE(DataClassJsonMixin):
    asyncOp: Literal[AsyncOpsStrings.REMOVE]
    REMOVE: Optional[RemoveArgs]


@dataclass
class OpDescription__GET_REVISIONS(DataClassJsonMixin):
    asyncOp: Literal[AsyncOpsStrings.GET_REVISIONS]
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
class TeamDetails(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    members: TeamMembersDetails = field(metadata=config(field_name="members"))
    key_generation: PerTeamKeyGeneration = field(
        metadata=config(field_name="keyGeneration")
    )
    annotated_active_invites: Dict[str, AnnotatedTeamInvite] = field(
        metadata=config(field_name="annotatedActiveInvites")
    )
    settings: TeamSettings = field(metadata=config(field_name="settings"))
    showcase: TeamShowcase = field(metadata=config(field_name="showcase"))


@dataclass
class TeamData(DataClassJsonMixin):
    chain: TeamSigChainState = field(metadata=config(field_name="chain"))
    subversion: int = field(metadata=config(field_name="v"))
    tombstoned: bool = field(metadata=config(field_name="tombstoned"))
    secretless: bool = field(metadata=config(field_name="secretless"))
    name: TeamName = field(metadata=config(field_name="name"))
    frozen: bool = field(metadata=config(field_name="frozen"))
    per_team_key_seeds_unverified: Dict[str, PerTeamKeySeedItem] = field(
        metadata=config(field_name="perTeamKeySeedsUnverified")
    )
    reader_key_masks: Dict[str, Dict[str, MaskB64]] = field(
        metadata=config(field_name="readerKeyMasks")
    )
    latest_seqno_hint: Seqno = field(metadata=config(field_name="latestSeqnoHint"))
    cached_at: Time = field(metadata=config(field_name="cachedAt"))
    tlf_crypt_keys: Dict[str, Optional[List[CryptKey]]] = field(
        metadata=config(field_name="tlfCryptKeys")
    )


@dataclass
class AnnotatedTeamList(DataClassJsonMixin):
    annotated_active_invites: Dict[str, AnnotatedTeamInvite] = field(
        metadata=config(field_name="annotatedActiveInvites")
    )
    teams: Optional[List[AnnotatedMemberInfo]] = field(
        default=None, metadata=config(field_name="teams")
    )


@dataclass
class TeamDebugRes(DataClassJsonMixin):
    chain: TeamSigChainState = field(metadata=config(field_name="chain"))


@dataclass
class AnnotatedTeam(DataClassJsonMixin):
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    name: str = field(metadata=config(field_name="name"))
    transitive_subteams_unverified: SubteamListResult = field(
        metadata=config(field_name="transitiveSubteamsUnverified")
    )
    tars_disabled: bool = field(metadata=config(field_name="tarsDisabled"))
    settings: TeamSettings = field(metadata=config(field_name="settings"))
    showcase: TeamShowcase = field(metadata=config(field_name="showcase"))
    members: Optional[List[AnnotatedTeamMemberDetails]] = field(
        default=None, metadata=config(field_name="members")
    )
    invites: Optional[List[AnnotatedTeamInvite]] = field(
        default=None, metadata=config(field_name="invites")
    )
    join_requests: Optional[List[TeamJoinRequest]] = field(
        default=None, metadata=config(field_name="joinRequests")
    )


@dataclass
class PublicKeyV2__NACL(DataClassJsonMixin):
    keyType: Literal[KeyTypeStrings.NACL]
    NACL: Optional[PublicKeyV2NaCl]


@dataclass
class PublicKeyV2__PGP(DataClassJsonMixin):
    keyType: Literal[KeyTypeStrings.PGP]
    PGP: Optional[PublicKeyV2PGPSummary]


PublicKeyV2 = Union[PublicKeyV2__NACL, PublicKeyV2__PGP]


@dataclass
class UserPlusKeysV2(DataClassJsonMixin):
    device_keys: Dict[str, PublicKeyV2NaCl] = field(
        metadata=config(field_name="deviceKeys")
    )
    uid: UID = field(metadata=config(field_name="uid"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    status: StatusCode = field(metadata=config(field_name="status"))
    remote_tracks: Dict[str, RemoteTrack] = field(
        metadata=config(field_name="remoteTracks")
    )
    username: str = field(metadata=config(field_name="username"))
    pgp_keys: Dict[str, PublicKeyV2PGPSummary] = field(
        metadata=config(field_name="pgpKeys")
    )
    unstubbed: bool = field(metadata=config(field_name="unstubbed"))
    stellar_account_id: Optional[str] = field(
        default=None, metadata=config(field_name="stellarAccountID")
    )
    per_user_keys: Optional[List[PerUserKey]] = field(
        default=None, metadata=config(field_name="perUserKeys")
    )
    reset: Optional[ResetSummary] = field(
        default=None, metadata=config(field_name="reset")
    )


@dataclass
class UPKLiteV1(DataClassJsonMixin):
    uid: UID = field(metadata=config(field_name="uid"))
    username: str = field(metadata=config(field_name="username"))
    eldest_seqno: Seqno = field(metadata=config(field_name="eldestSeqno"))
    status: StatusCode = field(metadata=config(field_name="status"))
    device_keys: Dict[str, PublicKeyV2NaCl] = field(
        metadata=config(field_name="deviceKeys")
    )
    reset: Optional[ResetSummary] = field(
        default=None, metadata=config(field_name="reset")
    )


@dataclass
class Folder(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    private: bool = field(metadata=config(field_name="private"))
    created: bool = field(metadata=config(field_name="created"))
    folder_type: FolderType = field(metadata=config(field_name="folderType"))
    team_id: Optional[TeamID] = field(
        default=None, metadata=config(field_name="team_id")
    )
    reset_members: Optional[List[User]] = field(
        default=None, metadata=config(field_name="reset_members")
    )
    mtime: Optional[Time] = field(default=None, metadata=config(field_name="mtime"))
    conflict_state: Optional[ConflictState] = field(
        default=None, metadata=config(field_name="conflictState")
    )
    sync_config: Optional[FolderSyncConfig] = field(
        default=None, metadata=config(field_name="syncConfig")
    )


@dataclass
class HomeScreenItem(DataClassJsonMixin):
    badged: bool = field(metadata=config(field_name="badged"))
    data: HomeScreenItemData = field(metadata=config(field_name="data"))
    data_ext: HomeScreenItemDataExt = field(metadata=config(field_name="dataExt"))


@dataclass
class Identify2Res(DataClassJsonMixin):
    upk: UserPlusKeys = field(metadata=config(field_name="upk"))
    identified_at: Time = field(metadata=config(field_name="identifiedAt"))
    track_breaks: Optional[IdentifyTrackBreaks] = field(
        default=None, metadata=config(field_name="trackBreaks")
    )


@dataclass
class IdentifyLiteRes(DataClassJsonMixin):
    ul: UserOrTeamLite = field(metadata=config(field_name="ul"))
    track_breaks: Optional[IdentifyTrackBreaks] = field(
        default=None, metadata=config(field_name="trackBreaks")
    )


@dataclass
class ResolveIdentifyImplicitTeamRes(DataClassJsonMixin):
    display_name: str = field(metadata=config(field_name="displayName"))
    team_id: TeamID = field(metadata=config(field_name="teamID"))
    track_breaks: Dict[str, IdentifyTrackBreaks] = field(
        metadata=config(field_name="trackBreaks")
    )
    folder_id: TLFID = field(metadata=config(field_name="folderID"))
    writers: Optional[List[UserVersion]] = field(
        default=None, metadata=config(field_name="writers")
    )


@dataclass
class TLFIdentifyFailure(DataClassJsonMixin):
    user: User = field(metadata=config(field_name="user"))
    breaks: Optional[IdentifyTrackBreaks] = field(
        default=None, metadata=config(field_name="breaks")
    )


@dataclass
class UserPlusKeysV2AllIncarnations(DataClassJsonMixin):
    current: UserPlusKeysV2 = field(metadata=config(field_name="current"))
    uvv: UserVersionVector = field(metadata=config(field_name="uvv"))
    seqno_link_i_ds: Dict[str, LinkID] = field(
        metadata=config(field_name="seqnoLinkIDs")
    )
    minor_version: UPK2MinorVersion = field(metadata=config(field_name="minorVersion"))
    stale: bool = field(metadata=config(field_name="stale"))
    past_incarnations: Optional[List[UserPlusKeysV2]] = field(
        default=None, metadata=config(field_name="pastIncarnations")
    )


@dataclass
class UPKLiteV1AllIncarnations(DataClassJsonMixin):
    current: UPKLiteV1 = field(metadata=config(field_name="current"))
    seqno_link_i_ds: Dict[str, LinkID] = field(
        metadata=config(field_name="seqnoLinkIDs")
    )
    minor_version: UPKLiteMinorVersion = field(
        metadata=config(field_name="minorVersion")
    )
    past_incarnations: Optional[List[UPKLiteV1]] = field(
        default=None, metadata=config(field_name="pastIncarnations")
    )


@dataclass
class FavoritesResult(DataClassJsonMixin):
    favorite_folders: Optional[List[Folder]] = field(
        default=None, metadata=config(field_name="favoriteFolders")
    )
    ignored_folders: Optional[List[Folder]] = field(
        default=None, metadata=config(field_name="ignoredFolders")
    )
    new_folders: Optional[List[Folder]] = field(
        default=None, metadata=config(field_name="newFolders")
    )


@dataclass
class HomeScreen(DataClassJsonMixin):
    last_viewed: Time = field(metadata=config(field_name="lastViewed"))
    version: int = field(metadata=config(field_name="version"))
    visits: int = field(metadata=config(field_name="visits"))
    announcements_version: int = field(
        metadata=config(field_name="announcementsVersion")
    )
    items: Optional[List[HomeScreenItem]] = field(
        default=None, metadata=config(field_name="items")
    )
    follow_suggestions: Optional[List[HomeUserSummary]] = field(
        default=None, metadata=config(field_name="followSuggestions")
    )


@dataclass
class Identify2ResUPK2(DataClassJsonMixin):
    upk: UserPlusKeysV2AllIncarnations = field(metadata=config(field_name="upk"))
    identified_at: Time = field(metadata=config(field_name="identifiedAt"))
    track_breaks: Optional[IdentifyTrackBreaks] = field(
        default=None, metadata=config(field_name="trackBreaks")
    )


@dataclass
class FSEditListRequest(DataClassJsonMixin):
    folder: Folder = field(metadata=config(field_name="folder"))
    request_id: int = field(metadata=config(field_name="requestID"))


@dataclass
class FSFolderEditHistory(DataClassJsonMixin):
    folder: Folder = field(metadata=config(field_name="folder"))
    server_time: Time = field(metadata=config(field_name="serverTime"))
    history: Optional[List[FSFolderWriterEditHistory]] = field(
        default=None, metadata=config(field_name="history")
    )


@dataclass
class FolderSyncConfigAndStatusWithFolder(DataClassJsonMixin):
    folder: Folder = field(metadata=config(field_name="folder"))
    config_: FolderSyncConfig = field(metadata=config(field_name="config"))
    status: FolderSyncStatus = field(metadata=config(field_name="status"))


@dataclass
class FolderWithFavFlags(DataClassJsonMixin):
    folder: Folder = field(metadata=config(field_name="folder"))
    is_favorite: bool = field(metadata=config(field_name="isFavorite"))
    is_ignored: bool = field(metadata=config(field_name="isIgnored"))
    is_new: bool = field(metadata=config(field_name="isNew"))


@dataclass
class SimpleFSIndexProgress(DataClassJsonMixin):
    overall_progress: IndexProgressRecord = field(
        metadata=config(field_name="overallProgress")
    )
    curr_folder: Folder = field(metadata=config(field_name="currFolder"))
    curr_progress: IndexProgressRecord = field(
        metadata=config(field_name="currProgress")
    )
    folders_left: Optional[List[Folder]] = field(
        default=None, metadata=config(field_name="foldersLeft")
    )


@dataclass
class TLFBreak(DataClassJsonMixin):
    breaks: Optional[List[TLFIdentifyFailure]] = field(
        default=None, metadata=config(field_name="breaks")
    )


@dataclass
class UPAKVersioned__V1(DataClassJsonMixin):
    v: Literal[UPAKVersionStrings.V1]
    V1: Optional[UserPlusAllKeys]


@dataclass
class UPAKVersioned__V2(DataClassJsonMixin):
    v: Literal[UPAKVersionStrings.V2]
    V2: Optional[UserPlusKeysV2AllIncarnations]


UPAKVersioned = Union[UPAKVersioned__V1, UPAKVersioned__V2]


@dataclass
class SyncConfigAndStatusRes(DataClassJsonMixin):
    overall_status: FolderSyncStatus = field(
        metadata=config(field_name="overallStatus")
    )
    folders: Optional[List[FolderSyncConfigAndStatusWithFolder]] = field(
        default=None, metadata=config(field_name="folders")
    )


@dataclass
class CanonicalTLFNameAndIDWithBreaks(DataClassJsonMixin):
    tlf_id: TLFID = field(metadata=config(field_name="tlfID"))
    canonical_name: CanonicalTlfName = field(
        metadata=config(field_name="CanonicalName")
    )
    breaks: TLFBreak = field(metadata=config(field_name="breaks"))


@dataclass
class GetTLFCryptKeysRes(DataClassJsonMixin):
    name_id_breaks: CanonicalTLFNameAndIDWithBreaks = field(
        metadata=config(field_name="nameIDBreaks")
    )
    crypt_keys: Optional[List[CryptKey]] = field(
        default=None, metadata=config(field_name="CryptKeys")
    )
