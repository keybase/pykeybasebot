"""stellar.1

Auto-generated to Python types by avdl-compiler v1.4.4 (https://github.com/keybase/node-avdl-compiler)
Input files:
 - ../../go/src/github.com/keybase/client/protocol/avdl/stellar1/bundle.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/stellar1/common.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/stellar1/gregor.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/stellar1/local.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/stellar1/notify.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/stellar1/remote.avdl
 - ../../go/src/github.com/keybase/client/protocol/avdl/stellar1/ui.avdl
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Union

from dataclasses_json import DataClassJsonMixin, config
from typing_extensions import Literal

import pykeybasebot.types.keybase1 as keybase1

BundleRevision = int


@dataclass
class EncryptedBundle(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    e: str = field(metadata=config(field_name="e"))
    n: keybase1.BoxNonce = field(metadata=config(field_name="n"))
    gen: keybase1.PerUserKeyGeneration = field(metadata=config(field_name="gen"))


class BundleVersion(Enum):
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


class BundleVersionStrings(Enum):
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
class BundleSecretUnsupported(DataClassJsonMixin):
    pass


@dataclass
class EncryptedAccountBundle(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    e: str = field(metadata=config(field_name="e"))
    n: keybase1.BoxNonce = field(metadata=config(field_name="n"))
    gen: keybase1.PerUserKeyGeneration = field(metadata=config(field_name="gen"))


class AccountBundleVersion(Enum):
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


class AccountBundleVersionStrings(Enum):
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
class AccountBundleSecretUnsupported(DataClassJsonMixin):
    pass


AccountID = str
SecretKey = str
TransactionID = str
PaymentID = str
KeybaseTransactionID = str
TimeMs = int
Hash = str
KeybaseRequestID = str
AssetCode = str


@dataclass
class Asset(DataClassJsonMixin):
    type: str = field(metadata=config(field_name="type"))
    code: str = field(metadata=config(field_name="code"))
    issuer: str = field(metadata=config(field_name="issuer"))
    verified_domain: str = field(metadata=config(field_name="verifiedDomain"))
    issuer_name: str = field(metadata=config(field_name="issuerName"))
    desc: str = field(metadata=config(field_name="desc"))
    info_url: str = field(metadata=config(field_name="infoUrl"))
    info_url_text: str = field(metadata=config(field_name="infoUrlText"))
    show_deposit_button: bool = field(metadata=config(field_name="showDepositButton"))
    deposit_button_text: str = field(metadata=config(field_name="depositButtonText"))
    show_withdraw_button: bool = field(metadata=config(field_name="showWithdrawButton"))
    withdraw_button_text: str = field(metadata=config(field_name="withdrawButtonText"))
    withdraw_type: str = field(metadata=config(field_name="withdrawType"))
    transfer_server: str = field(metadata=config(field_name="transferServer"))
    auth_endpoint: str = field(metadata=config(field_name="authEndpoint"))


@dataclass
class AccountReserve(DataClassJsonMixin):
    amount: str = field(metadata=config(field_name="amount"))
    description: str = field(metadata=config(field_name="description"))


class TransactionStatus(Enum):
    NONE = 0
    PENDING = 1
    SUCCESS = 2
    ERROR_TRANSIENT = 3
    ERROR_PERMANENT = 4


class TransactionStatusStrings(Enum):
    NONE = "none"
    PENDING = "pending"
    SUCCESS = "success"
    ERROR_TRANSIENT = "error_transient"
    ERROR_PERMANENT = "error_permanent"


class RequestStatus(Enum):
    OK = 0
    CANCELED = 1
    DONE = 2


class RequestStatusStrings(Enum):
    OK = "ok"
    CANCELED = "canceled"
    DONE = "done"


class PaymentStrategy(Enum):
    NONE = 0
    DIRECT = 1
    RELAY = 2


class PaymentStrategyStrings(Enum):
    NONE = "none"
    DIRECT = "direct"
    RELAY = "relay"


class RelayDirection(Enum):
    CLAIM = 0
    YANK = 1


class RelayDirectionStrings(Enum):
    CLAIM = "claim"
    YANK = "yank"


@dataclass
class NoteRecipient(DataClassJsonMixin):
    user: keybase1.UserVersion = field(metadata=config(field_name="user"))
    puk_gen: keybase1.PerUserKeyGeneration = field(metadata=config(field_name="pukGen"))


@dataclass
class EncryptedRelaySecret(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    e: str = field(metadata=config(field_name="e"))
    n: keybase1.BoxNonce = field(metadata=config(field_name="n"))
    gen: keybase1.PerTeamKeyGeneration = field(metadata=config(field_name="gen"))


OutsideCurrencyCode = str


@dataclass
class CurrencySymbol(DataClassJsonMixin):
    symbol: str = field(metadata=config(field_name="str"))
    ambigious: bool = field(metadata=config(field_name="ambigious"))
    postfix: bool = field(metadata=config(field_name="postfix"))


@dataclass
class PageCursor(DataClassJsonMixin):
    horizon_cursor: str = field(metadata=config(field_name="horizonCursor"))
    direct_cursor: str = field(metadata=config(field_name="directCursor"))
    relay_cursor: str = field(metadata=config(field_name="relayCursor"))


class AccountMode(Enum):
    NONE = 0
    USER = 1
    MOBILE = 2


class AccountModeStrings(Enum):
    NONE = "none"
    USER = "user"
    MOBILE = "mobile"


class BalanceDelta(Enum):
    NONE = 0
    INCREASE = 1
    DECREASE = 2


class BalanceDeltaStrings(Enum):
    NONE = "none"
    INCREASE = "increase"
    DECREASE = "decrease"


class PaymentStatus(Enum):
    NONE = 0
    PENDING = 1
    CLAIMABLE = 2
    COMPLETED = 3
    ERROR = 4
    UNKNOWN = 5
    CANCELED = 6


class PaymentStatusStrings(Enum):
    NONE = "none"
    PENDING = "pending"
    CLAIMABLE = "claimable"
    COMPLETED = "completed"
    ERROR = "error"
    UNKNOWN = "unknown"
    CANCELED = "canceled"


class ParticipantType(Enum):
    NONE = 0
    KEYBASE = 1
    STELLAR = 2
    SBS = 3
    OWNACCOUNT = 4


class ParticipantTypeStrings(Enum):
    NONE = "none"
    KEYBASE = "keybase"
    STELLAR = "stellar"
    SBS = "sbs"
    OWNACCOUNT = "ownaccount"


BuildPaymentID = str


class AdvancedBanner(Enum):
    NO_BANNER = 0
    SENDER_BANNER = 1
    RECEIVER_BANNER = 2


class AdvancedBannerStrings(Enum):
    NO_BANNER = "no_banner"
    SENDER_BANNER = "sender_banner"
    RECEIVER_BANNER = "receiver_banner"


InflationDestinationTag = str


@dataclass
class AirdropDetails(DataClassJsonMixin):
    is_promoted: bool = field(metadata=config(field_name="isPromoted"))
    details: str = field(metadata=config(field_name="details"))
    disclaimer: str = field(metadata=config(field_name="disclaimer"))


AirdropState = str


@dataclass
class AirdropQualification(DataClassJsonMixin):
    title: str = field(metadata=config(field_name="title"))
    subtitle: str = field(metadata=config(field_name="subtitle"))
    valid: bool = field(metadata=config(field_name="valid"))


@dataclass
class AssetActionResultLocal(DataClassJsonMixin):
    external_url: Optional[str] = field(
        default=None, metadata=config(field_name="externalUrl")
    )
    message_from_anchor: Optional[str] = field(
        default=None, metadata=config(field_name="messageFromAnchor")
    )


@dataclass
class BatchPaymentError(DataClassJsonMixin):
    message: str = field(metadata=config(field_name="message"))
    code: int = field(metadata=config(field_name="code"))


@dataclass
class BatchPaymentArg(DataClassJsonMixin):
    recipient: str = field(metadata=config(field_name="recipient"))
    amount: str = field(metadata=config(field_name="amount"))
    message: str = field(metadata=config(field_name="message"))


@dataclass
class PartnerUrl(DataClassJsonMixin):
    url: str = field(metadata=config(field_name="url"))
    title: str = field(metadata=config(field_name="title"))
    description: str = field(metadata=config(field_name="description"))
    icon_filename: str = field(metadata=config(field_name="icon_filename"))
    admin_only: bool = field(metadata=config(field_name="admin_only"))
    extra: str = field(metadata=config(field_name="extra"))


@dataclass
class StaticConfig(DataClassJsonMixin):
    payment_note_max_length: int = field(
        metadata=config(field_name="paymentNoteMaxLength")
    )
    request_note_max_length: int = field(
        metadata=config(field_name="requestNoteMaxLength")
    )
    public_memo_max_length: int = field(
        metadata=config(field_name="publicMemoMaxLength")
    )


ChatConversationID = str


@dataclass
class DirectOp(DataClassJsonMixin):
    note_b_64: str = field(metadata=config(field_name="noteB64"))


class PaymentSummaryType(Enum):
    NONE = 0
    STELLAR = 1
    DIRECT = 2
    RELAY = 3


class PaymentSummaryTypeStrings(Enum):
    NONE = "none"
    STELLAR = "stellar"
    DIRECT = "direct"
    RELAY = "relay"


@dataclass
class TimeboundsRecommendation(DataClassJsonMixin):
    time_now: keybase1.UnixTime = field(metadata=config(field_name="time_now"))
    timeout: int = field(metadata=config(field_name="timeout"))


@dataclass
class NetworkOptions(DataClassJsonMixin):
    base_fee: int = field(metadata=config(field_name="baseFee"))


@dataclass
class BundleVisibleEntryV2(DataClassJsonMixin):
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    mode: AccountMode = field(metadata=config(field_name="mode"))
    is_primary: bool = field(metadata=config(field_name="isPrimary"))
    acct_bundle_revision: BundleRevision = field(
        metadata=config(field_name="acctBundleRevision")
    )
    enc_acct_bundle_hash: Hash = field(metadata=config(field_name="encAcctBundleHash"))


@dataclass
class BundleSecretEntryV2(DataClassJsonMixin):
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    name: str = field(metadata=config(field_name="name"))


@dataclass
class AccountBundleSecretV1(DataClassJsonMixin):
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    signers: Optional[Optional[List[SecretKey]]] = field(
        default=None, metadata=config(field_name="signers")
    )


@dataclass
class BundleEntry(DataClassJsonMixin):
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    mode: AccountMode = field(metadata=config(field_name="mode"))
    is_primary: bool = field(metadata=config(field_name="isPrimary"))
    name: str = field(metadata=config(field_name="name"))
    acct_bundle_revision: BundleRevision = field(
        metadata=config(field_name="acctBundleRevision")
    )
    enc_acct_bundle_hash: Hash = field(metadata=config(field_name="encAcctBundleHash"))


@dataclass
class AccountBundle(DataClassJsonMixin):
    prev: Hash = field(metadata=config(field_name="prev"))
    own_hash: Hash = field(metadata=config(field_name="ownHash"))
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    signers: Optional[Optional[List[SecretKey]]] = field(
        default=None, metadata=config(field_name="signers")
    )


@dataclass
class AssetListResult(DataClassJsonMixin):
    total_count: int = field(metadata=config(field_name="totalCount"))
    assets: Optional[Optional[List[Asset]]] = field(
        default=None, metadata=config(field_name="assets")
    )


@dataclass
class Balance(DataClassJsonMixin):
    asset: Asset = field(metadata=config(field_name="asset"))
    amount: str = field(metadata=config(field_name="amount"))
    limit: str = field(metadata=config(field_name="limit"))
    is_authorized: bool = field(metadata=config(field_name="isAuthorized"))


@dataclass
class PaymentResult(DataClassJsonMixin):
    sender_account_id: AccountID = field(metadata=config(field_name="senderAccountID"))
    keybase_id: KeybaseTransactionID = field(metadata=config(field_name="keybaseID"))
    stellar_id: TransactionID = field(metadata=config(field_name="stellarID"))
    pending: bool = field(metadata=config(field_name="pending"))


@dataclass
class RelayClaimResult(DataClassJsonMixin):
    claim_stellar_id: TransactionID = field(
        metadata=config(field_name="claimStellarID")
    )


@dataclass
class EncryptedNote(DataClassJsonMixin):
    v: int = field(metadata=config(field_name="v"))
    e: str = field(metadata=config(field_name="e"))
    n: keybase1.BoxNonce = field(metadata=config(field_name="n"))
    sender: NoteRecipient = field(metadata=config(field_name="sender"))
    recipient: Optional[NoteRecipient] = field(
        default=None, metadata=config(field_name="recipient")
    )


@dataclass
class NoteContents(DataClassJsonMixin):
    note: str = field(metadata=config(field_name="note"))
    stellar_id: TransactionID = field(metadata=config(field_name="stellarID"))


@dataclass
class RelayContents(DataClassJsonMixin):
    stellar_id: TransactionID = field(metadata=config(field_name="stellarID"))
    sk: SecretKey = field(metadata=config(field_name="sk"))
    note: str = field(metadata=config(field_name="note"))


@dataclass
class OutsideExchangeRate(DataClassJsonMixin):
    currency: OutsideCurrencyCode = field(metadata=config(field_name="currency"))
    rate: str = field(metadata=config(field_name="rate"))


@dataclass
class OutsideCurrencyDefinition(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    symbol: CurrencySymbol = field(metadata=config(field_name="symbol"))


@dataclass
class Trustline(DataClassJsonMixin):
    asset_code: AssetCode = field(metadata=config(field_name="assetCode"))
    issuer: AccountID = field(metadata=config(field_name="issuer"))


@dataclass
class PaymentPath(DataClassJsonMixin):
    source_amount: str = field(metadata=config(field_name="sourceAmount"))
    source_amount_max: str = field(metadata=config(field_name="sourceAmountMax"))
    source_asset: Asset = field(metadata=config(field_name="sourceAsset"))
    destination_amount: str = field(metadata=config(field_name="destinationAmount"))
    destination_asset: Asset = field(metadata=config(field_name="destinationAsset"))
    source_insufficient_balance: str = field(
        metadata=config(field_name="sourceInsufficientBalance")
    )
    path: Optional[Optional[List[Asset]]] = field(
        default=None, metadata=config(field_name="path")
    )


@dataclass
class PaymentStatusMsg(DataClassJsonMixin):
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    kb_tx_id: KeybaseTransactionID = field(metadata=config(field_name="kbTxID"))
    tx_id: TransactionID = field(metadata=config(field_name="txID"))


@dataclass
class RequestStatusMsg(DataClassJsonMixin):
    req_id: KeybaseRequestID = field(metadata=config(field_name="reqID"))


@dataclass
class PaymentNotificationMsg(DataClassJsonMixin):
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    payment_id: PaymentID = field(metadata=config(field_name="paymentID"))


@dataclass
class AccountAssetLocal(DataClassJsonMixin):
    name: str = field(metadata=config(field_name="name"))
    asset_code: str = field(metadata=config(field_name="assetCode"))
    issuer_name: str = field(metadata=config(field_name="issuerName"))
    issuer_account_id: str = field(metadata=config(field_name="issuerAccountID"))
    issuer_verified_domain: str = field(
        metadata=config(field_name="issuerVerifiedDomain")
    )
    balance_total: str = field(metadata=config(field_name="balanceTotal"))
    balance_available_to_send: str = field(
        metadata=config(field_name="balanceAvailableToSend")
    )
    worth_currency: str = field(metadata=config(field_name="worthCurrency"))
    worth: str = field(metadata=config(field_name="worth"))
    available_to_send_worth: str = field(
        metadata=config(field_name="availableToSendWorth")
    )
    desc: str = field(metadata=config(field_name="desc"))
    info_url: str = field(metadata=config(field_name="infoUrl"))
    info_url_text: str = field(metadata=config(field_name="infoUrlText"))
    show_deposit_button: bool = field(metadata=config(field_name="showDepositButton"))
    deposit_button_text: str = field(metadata=config(field_name="depositButtonText"))
    show_withdraw_button: bool = field(metadata=config(field_name="showWithdrawButton"))
    withdraw_button_text: str = field(metadata=config(field_name="withdrawButtonText"))
    reserves: Optional[Optional[List[AccountReserve]]] = field(
        default=None, metadata=config(field_name="reserves")
    )


@dataclass
class PaymentDetailsOnlyLocal(DataClassJsonMixin):
    public_note: str = field(metadata=config(field_name="publicNote"))
    public_note_type: str = field(metadata=config(field_name="publicNoteType"))
    external_tx_url: str = field(metadata=config(field_name="externalTxURL"))
    fee_charged_description: str = field(
        metadata=config(field_name="feeChargedDescription")
    )
    path_intermediate: Optional[Optional[List[Asset]]] = field(
        default=None, metadata=config(field_name="pathIntermediate")
    )


@dataclass
class PaymentTrustlineLocal(DataClassJsonMixin):
    asset: Asset = field(metadata=config(field_name="asset"))
    remove: bool = field(metadata=config(field_name="remove"))


@dataclass
class CurrencyLocal(DataClassJsonMixin):
    description: str = field(metadata=config(field_name="description"))
    code: OutsideCurrencyCode = field(metadata=config(field_name="code"))
    symbol: str = field(metadata=config(field_name="symbol"))
    name: str = field(metadata=config(field_name="name"))


@dataclass
class SendAssetChoiceLocal(DataClassJsonMixin):
    asset: Asset = field(metadata=config(field_name="asset"))
    enabled: bool = field(metadata=config(field_name="enabled"))
    left: str = field(metadata=config(field_name="left"))
    right: str = field(metadata=config(field_name="right"))
    subtext: str = field(metadata=config(field_name="subtext"))


@dataclass
class SendBannerLocal(DataClassJsonMixin):
    level: str = field(metadata=config(field_name="level"))
    message: str = field(metadata=config(field_name="message"))
    proofs_changed: bool = field(metadata=config(field_name="proofsChanged"))
    offer_advanced_send_form: AdvancedBanner = field(
        metadata=config(field_name="offerAdvancedSendForm")
    )


@dataclass
class SendPaymentResLocal(DataClassJsonMixin):
    kb_tx_id: KeybaseTransactionID = field(metadata=config(field_name="kbTxID"))
    pending: bool = field(metadata=config(field_name="pending"))
    jump_to_chat: str = field(metadata=config(field_name="jumpToChat"))


@dataclass
class RequestDetailsLocal(DataClassJsonMixin):
    id: KeybaseRequestID = field(metadata=config(field_name="id"))
    from_assertion: str = field(metadata=config(field_name="fromAssertion"))
    from_current_user: bool = field(metadata=config(field_name="fromCurrentUser"))
    to_user_type: ParticipantType = field(metadata=config(field_name="toUserType"))
    to_assertion: str = field(metadata=config(field_name="toAssertion"))
    amount: str = field(metadata=config(field_name="amount"))
    amount_description: str = field(metadata=config(field_name="amountDescription"))
    worth_at_request_time: str = field(metadata=config(field_name="worthAtRequestTime"))
    status: RequestStatus = field(metadata=config(field_name="status"))
    asset: Optional[Asset] = field(default=None, metadata=config(field_name="asset"))
    currency: Optional[OutsideCurrencyCode] = field(
        default=None, metadata=config(field_name="currency")
    )


@dataclass
class PredefinedInflationDestination(DataClassJsonMixin):
    tag: InflationDestinationTag = field(metadata=config(field_name="tag"))
    name: str = field(metadata=config(field_name="name"))
    recommended: bool = field(metadata=config(field_name="recommended"))
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    url: str = field(metadata=config(field_name="url"))


@dataclass
class AirdropStatus(DataClassJsonMixin):
    state: AirdropState = field(metadata=config(field_name="state"))
    rows: Optional[Optional[List[AirdropQualification]]] = field(
        default=None, metadata=config(field_name="rows")
    )


@dataclass
class SendResultCLILocal(DataClassJsonMixin):
    kb_tx_id: KeybaseTransactionID = field(metadata=config(field_name="kbTxID"))
    tx_id: TransactionID = field(metadata=config(field_name="txID"))


@dataclass
class PaymentCLILocal(DataClassJsonMixin):
    tx_id: TransactionID = field(metadata=config(field_name="txID"))
    time: TimeMs = field(metadata=config(field_name="time"))
    status: str = field(metadata=config(field_name="status"))
    status_detail: str = field(metadata=config(field_name="statusDetail"))
    amount: str = field(metadata=config(field_name="amount"))
    asset: Asset = field(metadata=config(field_name="asset"))
    source_amount_max: str = field(metadata=config(field_name="sourceAmountMax"))
    source_amount_actual: str = field(metadata=config(field_name="sourceAmountActual"))
    source_asset: Asset = field(metadata=config(field_name="sourceAsset"))
    is_advanced: bool = field(metadata=config(field_name="isAdvanced"))
    summary_advanced: str = field(metadata=config(field_name="summaryAdvanced"))
    from_stellar: AccountID = field(metadata=config(field_name="fromStellar"))
    note: str = field(metadata=config(field_name="note"))
    note_err: str = field(metadata=config(field_name="noteErr"))
    unread: bool = field(metadata=config(field_name="unread"))
    public_note: str = field(metadata=config(field_name="publicNote"))
    public_note_type: str = field(metadata=config(field_name="publicNoteType"))
    fee_charged_description: str = field(
        metadata=config(field_name="feeChargedDescription")
    )
    display_amount: Optional[str] = field(
        default=None, metadata=config(field_name="displayAmount")
    )
    display_currency: Optional[str] = field(
        default=None, metadata=config(field_name="displayCurrency")
    )
    operations: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="operations")
    )
    to_stellar: Optional[AccountID] = field(
        default=None, metadata=config(field_name="toStellar")
    )
    from_username: Optional[str] = field(
        default=None, metadata=config(field_name="fromUsername")
    )
    to_username: Optional[str] = field(
        default=None, metadata=config(field_name="toUsername")
    )
    to_assertion: Optional[str] = field(
        default=None, metadata=config(field_name="toAssertion")
    )


@dataclass
class LookupResultCLILocal(DataClassJsonMixin):
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    username: Optional[str] = field(
        default=None, metadata=config(field_name="username")
    )


@dataclass
class BatchPaymentResult(DataClassJsonMixin):
    username: str = field(metadata=config(field_name="username"))
    start_time: TimeMs = field(metadata=config(field_name="startTime"))
    submitted_time: TimeMs = field(metadata=config(field_name="submittedTime"))
    end_time: TimeMs = field(metadata=config(field_name="endTime"))
    tx_id: TransactionID = field(metadata=config(field_name="txID"))
    status: PaymentStatus = field(metadata=config(field_name="status"))
    status_description: str = field(metadata=config(field_name="statusDescription"))
    error: Optional[BatchPaymentError] = field(
        default=None, metadata=config(field_name="error")
    )


@dataclass
class TxDisplaySummary(DataClassJsonMixin):
    source: AccountID = field(metadata=config(field_name="source"))
    fee: int = field(metadata=config(field_name="fee"))
    memo: str = field(metadata=config(field_name="memo"))
    memo_type: str = field(metadata=config(field_name="memoType"))
    operations: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="operations")
    )


@dataclass
class SignXdrResult(DataClassJsonMixin):
    singed_tx: str = field(metadata=config(field_name="singedTx"))
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    submit_err: Optional[str] = field(
        default=None, metadata=config(field_name="submitErr")
    )
    submit_tx_id: Optional[TransactionID] = field(
        default=None, metadata=config(field_name="submitTxID")
    )


@dataclass
class PaymentDirectPost(DataClassJsonMixin):
    from_device_id: keybase1.DeviceID = field(
        metadata=config(field_name="fromDeviceID")
    )
    display_amount: str = field(metadata=config(field_name="displayAmount"))
    display_currency: str = field(metadata=config(field_name="displayCurrency"))
    note_b_64: str = field(metadata=config(field_name="noteB64"))
    signed_transaction: str = field(metadata=config(field_name="signedTransaction"))
    quick_return: bool = field(metadata=config(field_name="quickReturn"))
    batch_id: str = field(metadata=config(field_name="batchID"))
    to: Optional[keybase1.UserVersion] = field(
        default=None, metadata=config(field_name="to")
    )
    chat_conversation_id: Optional[ChatConversationID] = field(
        default=None, metadata=config(field_name="chatConversationID")
    )


@dataclass
class PaymentRelayPost(DataClassJsonMixin):
    from_device_id: keybase1.DeviceID = field(
        metadata=config(field_name="fromDeviceID")
    )
    to_assertion: str = field(metadata=config(field_name="toAssertion"))
    relay_account: AccountID = field(metadata=config(field_name="relayAccount"))
    team_id: keybase1.TeamID = field(metadata=config(field_name="teamID"))
    display_amount: str = field(metadata=config(field_name="displayAmount"))
    display_currency: str = field(metadata=config(field_name="displayCurrency"))
    box_b_64: str = field(metadata=config(field_name="boxB64"))
    signed_transaction: str = field(metadata=config(field_name="signedTransaction"))
    quick_return: bool = field(metadata=config(field_name="quickReturn"))
    batch_id: str = field(metadata=config(field_name="batchID"))
    to: Optional[keybase1.UserVersion] = field(
        default=None, metadata=config(field_name="to")
    )
    chat_conversation_id: Optional[ChatConversationID] = field(
        default=None, metadata=config(field_name="chatConversationID")
    )


@dataclass
class RelayClaimPost(DataClassJsonMixin):
    keybase_id: KeybaseTransactionID = field(metadata=config(field_name="keybaseID"))
    dir: RelayDirection = field(metadata=config(field_name="dir"))
    signed_transaction: str = field(metadata=config(field_name="signedTransaction"))
    auto_claim_token: Optional[str] = field(
        default=None, metadata=config(field_name="autoClaimToken")
    )


@dataclass
class PathPaymentPost(DataClassJsonMixin):
    from_device_id: keybase1.DeviceID = field(
        metadata=config(field_name="fromDeviceID")
    )
    note_b_64: str = field(metadata=config(field_name="noteB64"))
    signed_transaction: str = field(metadata=config(field_name="signedTransaction"))
    quick_return: bool = field(metadata=config(field_name="quickReturn"))
    to: Optional[keybase1.UserVersion] = field(
        default=None, metadata=config(field_name="to")
    )
    chat_conversation_id: Optional[ChatConversationID] = field(
        default=None, metadata=config(field_name="chatConversationID")
    )


@dataclass
class RelayOp(DataClassJsonMixin):
    to_assertion: str = field(metadata=config(field_name="toAssertion"))
    relay_account: AccountID = field(metadata=config(field_name="relayAccount"))
    team_id: keybase1.TeamID = field(metadata=config(field_name="teamID"))
    box_b_64: str = field(metadata=config(field_name="boxB64"))


@dataclass
class PaymentSummaryDirect(DataClassJsonMixin):
    kb_tx_id: KeybaseTransactionID = field(metadata=config(field_name="kbTxID"))
    tx_id: TransactionID = field(metadata=config(field_name="txID"))
    tx_status: TransactionStatus = field(metadata=config(field_name="txStatus"))
    tx_err_msg: str = field(metadata=config(field_name="txErrMsg"))
    from_stellar: AccountID = field(metadata=config(field_name="fromStellar"))
    from_: keybase1.UserVersion = field(metadata=config(field_name="from"))
    from_device_id: keybase1.DeviceID = field(
        metadata=config(field_name="fromDeviceID")
    )
    to_stellar: AccountID = field(metadata=config(field_name="toStellar"))
    amount: str = field(metadata=config(field_name="amount"))
    asset: Asset = field(metadata=config(field_name="asset"))
    note_b_64: str = field(metadata=config(field_name="noteB64"))
    from_display_amount: str = field(metadata=config(field_name="fromDisplayAmount"))
    from_display_currency: str = field(
        metadata=config(field_name="fromDisplayCurrency")
    )
    to_display_amount: str = field(metadata=config(field_name="toDisplayAmount"))
    to_display_currency: str = field(metadata=config(field_name="toDisplayCurrency"))
    ctime: TimeMs = field(metadata=config(field_name="ctime"))
    rtime: TimeMs = field(metadata=config(field_name="rtime"))
    cursor_token: str = field(metadata=config(field_name="cursorToken"))
    unread: bool = field(metadata=config(field_name="unread"))
    from_primary: bool = field(metadata=config(field_name="fromPrimary"))
    batch_id: str = field(metadata=config(field_name="batchID"))
    from_airdrop: bool = field(metadata=config(field_name="fromAirdrop"))
    source_amount_max: str = field(metadata=config(field_name="sourceAmountMax"))
    source_amount_actual: str = field(metadata=config(field_name="sourceAmountActual"))
    source_asset: Asset = field(metadata=config(field_name="sourceAsset"))
    to: Optional[keybase1.UserVersion] = field(
        default=None, metadata=config(field_name="to")
    )
    display_amount: Optional[str] = field(
        default=None, metadata=config(field_name="displayAmount")
    )
    display_currency: Optional[str] = field(
        default=None, metadata=config(field_name="displayCurrency")
    )


@dataclass
class ClaimSummary(DataClassJsonMixin):
    tx_id: TransactionID = field(metadata=config(field_name="txID"))
    tx_status: TransactionStatus = field(metadata=config(field_name="txStatus"))
    tx_err_msg: str = field(metadata=config(field_name="txErrMsg"))
    dir: RelayDirection = field(metadata=config(field_name="dir"))
    to_stellar: AccountID = field(metadata=config(field_name="toStellar"))
    to: keybase1.UserVersion = field(metadata=config(field_name="to"))


@dataclass
class SubmitMultiRes(DataClassJsonMixin):
    tx_id: TransactionID = field(metadata=config(field_name="txID"))


@dataclass
class AutoClaim(DataClassJsonMixin):
    kb_tx_id: KeybaseTransactionID = field(metadata=config(field_name="kbTxID"))


@dataclass
class RequestPost(DataClassJsonMixin):
    to_assertion: str = field(metadata=config(field_name="toAssertion"))
    amount: str = field(metadata=config(field_name="amount"))
    to_user: Optional[keybase1.UserVersion] = field(
        default=None, metadata=config(field_name="toUser")
    )
    asset: Optional[Asset] = field(default=None, metadata=config(field_name="asset"))
    currency: Optional[OutsideCurrencyCode] = field(
        default=None, metadata=config(field_name="currency")
    )


@dataclass
class RequestDetails(DataClassJsonMixin):
    id: KeybaseRequestID = field(metadata=config(field_name="id"))
    from_user: keybase1.UserVersion = field(metadata=config(field_name="fromUser"))
    to_assertion: str = field(metadata=config(field_name="toAssertion"))
    amount: str = field(metadata=config(field_name="amount"))
    from_display_amount: str = field(metadata=config(field_name="fromDisplayAmount"))
    from_display_currency: str = field(
        metadata=config(field_name="fromDisplayCurrency")
    )
    to_display_amount: str = field(metadata=config(field_name="toDisplayAmount"))
    to_display_currency: str = field(metadata=config(field_name="toDisplayCurrency"))
    funding_kb_tx_id: KeybaseTransactionID = field(
        metadata=config(field_name="fundingKbTxID")
    )
    status: RequestStatus = field(metadata=config(field_name="status"))
    to_user: Optional[keybase1.UserVersion] = field(
        default=None, metadata=config(field_name="toUser")
    )
    asset: Optional[Asset] = field(default=None, metadata=config(field_name="asset"))
    currency: Optional[OutsideCurrencyCode] = field(
        default=None, metadata=config(field_name="currency")
    )


@dataclass
class PaymentPathQuery(DataClassJsonMixin):
    source: AccountID = field(metadata=config(field_name="source"))
    destination: AccountID = field(metadata=config(field_name="destination"))
    source_asset: Asset = field(metadata=config(field_name="sourceAsset"))
    destination_asset: Asset = field(metadata=config(field_name="destinationAsset"))
    amount: str = field(metadata=config(field_name="amount"))


@dataclass
class BundleVisibleV2(DataClassJsonMixin):
    revision: BundleRevision = field(metadata=config(field_name="revision"))
    prev: Hash = field(metadata=config(field_name="prev"))
    accounts: Optional[Optional[List[BundleVisibleEntryV2]]] = field(
        default=None, metadata=config(field_name="accounts")
    )


@dataclass
class BundleSecretV2(DataClassJsonMixin):
    visible_hash: Hash = field(metadata=config(field_name="visibleHash"))
    accounts: Optional[Optional[List[BundleSecretEntryV2]]] = field(
        default=None, metadata=config(field_name="accounts")
    )


@dataclass
class AccountBundleSecretVersioned__V1(DataClassJsonMixin):
    version: Literal[AccountBundleVersionStrings.V1]
    V1: Optional[AccountBundleSecretV1]


@dataclass
class AccountBundleSecretVersioned__V2(DataClassJsonMixin):
    version: Literal[AccountBundleVersionStrings.V2]
    V2: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V3(DataClassJsonMixin):
    version: Literal[AccountBundleVersionStrings.V3]
    V3: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V4(DataClassJsonMixin):
    version: Literal[AccountBundleVersionStrings.V4]
    V4: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V5(DataClassJsonMixin):
    version: Literal[AccountBundleVersionStrings.V5]
    V5: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V6(DataClassJsonMixin):
    version: Literal[AccountBundleVersionStrings.V6]
    V6: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V7(DataClassJsonMixin):
    version: Literal[AccountBundleVersionStrings.V7]
    V7: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V8(DataClassJsonMixin):
    version: Literal[AccountBundleVersionStrings.V8]
    V8: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V9(DataClassJsonMixin):
    version: Literal[AccountBundleVersionStrings.V9]
    V9: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V10(DataClassJsonMixin):
    version: Literal[AccountBundleVersionStrings.V10]
    V10: Optional[AccountBundleSecretUnsupported]


AccountBundleSecretVersioned = Union[
    AccountBundleSecretVersioned__V1,
    AccountBundleSecretVersioned__V2,
    AccountBundleSecretVersioned__V3,
    AccountBundleSecretVersioned__V4,
    AccountBundleSecretVersioned__V5,
    AccountBundleSecretVersioned__V6,
    AccountBundleSecretVersioned__V7,
    AccountBundleSecretVersioned__V8,
    AccountBundleSecretVersioned__V9,
    AccountBundleSecretVersioned__V10,
]


@dataclass
class Bundle(DataClassJsonMixin):
    revision: BundleRevision = field(metadata=config(field_name="revision"))
    prev: Hash = field(metadata=config(field_name="prev"))
    own_hash: Hash = field(metadata=config(field_name="ownHash"))
    account_bundles: Dict[str, AccountBundle] = field(
        metadata=config(field_name="accountBundles")
    )
    accounts: Optional[Optional[List[BundleEntry]]] = field(
        default=None, metadata=config(field_name="accounts")
    )


@dataclass
class StellarServerDefinitions(DataClassJsonMixin):
    revision: int = field(metadata=config(field_name="revision"))
    currencies: Dict[str, OutsideCurrencyDefinition] = field(
        metadata=config(field_name="currencies")
    )


@dataclass
class WalletAccountLocal(DataClassJsonMixin):
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    is_default: bool = field(metadata=config(field_name="isDefault"))
    name: str = field(metadata=config(field_name="name"))
    balance_description: str = field(metadata=config(field_name="balanceDescription"))
    seqno: str = field(metadata=config(field_name="seqno"))
    currency_local: CurrencyLocal = field(metadata=config(field_name="currencyLocal"))
    account_mode: AccountMode = field(metadata=config(field_name="accountMode"))
    account_mode_editable: bool = field(
        metadata=config(field_name="accountModeEditable")
    )
    device_read_only: bool = field(metadata=config(field_name="deviceReadOnly"))
    is_funded: bool = field(metadata=config(field_name="isFunded"))
    can_submit_tx: bool = field(metadata=config(field_name="canSubmitTx"))
    can_add_trustline: bool = field(metadata=config(field_name="canAddTrustline"))


@dataclass
class PaymentLocal(DataClassJsonMixin):
    id: PaymentID = field(metadata=config(field_name="id"))
    tx_id: TransactionID = field(metadata=config(field_name="txID"))
    time: TimeMs = field(metadata=config(field_name="time"))
    status_simplified: PaymentStatus = field(
        metadata=config(field_name="statusSimplified")
    )
    status_description: str = field(metadata=config(field_name="statusDescription"))
    status_detail: str = field(metadata=config(field_name="statusDetail"))
    show_cancel: bool = field(metadata=config(field_name="showCancel"))
    amount_description: str = field(metadata=config(field_name="amountDescription"))
    delta: BalanceDelta = field(metadata=config(field_name="delta"))
    worth: str = field(metadata=config(field_name="worth"))
    worth_at_send_time: str = field(metadata=config(field_name="worthAtSendTime"))
    issuer_description: str = field(metadata=config(field_name="issuerDescription"))
    from_type: ParticipantType = field(metadata=config(field_name="fromType"))
    to_type: ParticipantType = field(metadata=config(field_name="toType"))
    asset_code: str = field(metadata=config(field_name="assetCode"))
    from_account_id: AccountID = field(metadata=config(field_name="fromAccountID"))
    from_account_name: str = field(metadata=config(field_name="fromAccountName"))
    from_username: str = field(metadata=config(field_name="fromUsername"))
    to_account_name: str = field(metadata=config(field_name="toAccountName"))
    to_username: str = field(metadata=config(field_name="toUsername"))
    to_assertion: str = field(metadata=config(field_name="toAssertion"))
    original_to_assertion: str = field(
        metadata=config(field_name="originalToAssertion")
    )
    note: str = field(metadata=config(field_name="note"))
    note_err: str = field(metadata=config(field_name="noteErr"))
    source_amount_max: str = field(metadata=config(field_name="sourceAmountMax"))
    source_amount_actual: str = field(metadata=config(field_name="sourceAmountActual"))
    source_asset: Asset = field(metadata=config(field_name="sourceAsset"))
    source_conv_rate: str = field(metadata=config(field_name="sourceConvRate"))
    is_advanced: bool = field(metadata=config(field_name="isAdvanced"))
    summary_advanced: str = field(metadata=config(field_name="summaryAdvanced"))
    unread: bool = field(metadata=config(field_name="unread"))
    batch_id: str = field(metadata=config(field_name="batchID"))
    from_airdrop: bool = field(metadata=config(field_name="fromAirdrop"))
    is_inflation: bool = field(metadata=config(field_name="isInflation"))
    issuer_account_id: Optional[AccountID] = field(
        default=None, metadata=config(field_name="issuerAccountID")
    )
    to_account_id: Optional[AccountID] = field(
        default=None, metadata=config(field_name="toAccountID")
    )
    operations: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="operations")
    )
    inflation_source: Optional[str] = field(
        default=None, metadata=config(field_name="inflationSource")
    )
    trustline: Optional[PaymentTrustlineLocal] = field(
        default=None, metadata=config(field_name="trustline")
    )


@dataclass
class BuildPaymentResLocal(DataClassJsonMixin):
    ready_to_review: bool = field(metadata=config(field_name="readyToReview"))
    from_: AccountID = field(metadata=config(field_name="from"))
    to_err_msg: str = field(metadata=config(field_name="toErrMsg"))
    amount_err_msg: str = field(metadata=config(field_name="amountErrMsg"))
    secret_note_err_msg: str = field(metadata=config(field_name="secretNoteErrMsg"))
    public_memo_err_msg: str = field(metadata=config(field_name="publicMemoErrMsg"))
    public_memo_override: str = field(metadata=config(field_name="publicMemoOverride"))
    worth_description: str = field(metadata=config(field_name="worthDescription"))
    worth_info: str = field(metadata=config(field_name="worthInfo"))
    worth_amount: str = field(metadata=config(field_name="worthAmount"))
    worth_currency: str = field(metadata=config(field_name="worthCurrency"))
    display_amount_xlm: str = field(metadata=config(field_name="displayAmountXLM"))
    display_amount_fiat: str = field(metadata=config(field_name="displayAmountFiat"))
    sending_intention_xlm: bool = field(
        metadata=config(field_name="sendingIntentionXLM")
    )
    amount_available: str = field(metadata=config(field_name="amountAvailable"))
    banners: Optional[Optional[List[SendBannerLocal]]] = field(
        default=None, metadata=config(field_name="banners")
    )


@dataclass
class BuildRequestResLocal(DataClassJsonMixin):
    ready_to_request: bool = field(metadata=config(field_name="readyToRequest"))
    to_err_msg: str = field(metadata=config(field_name="toErrMsg"))
    amount_err_msg: str = field(metadata=config(field_name="amountErrMsg"))
    secret_note_err_msg: str = field(metadata=config(field_name="secretNoteErrMsg"))
    worth_description: str = field(metadata=config(field_name="worthDescription"))
    worth_info: str = field(metadata=config(field_name="worthInfo"))
    display_amount_xlm: str = field(metadata=config(field_name="displayAmountXLM"))
    display_amount_fiat: str = field(metadata=config(field_name="displayAmountFiat"))
    sending_intention_xlm: bool = field(
        metadata=config(field_name="sendingIntentionXLM")
    )
    banners: Optional[Optional[List[SendBannerLocal]]] = field(
        default=None, metadata=config(field_name="banners")
    )


@dataclass
class InflationDestinationResultLocal(DataClassJsonMixin):
    self_: bool = field(metadata=config(field_name="self"))
    destination: Optional[AccountID] = field(
        default=None, metadata=config(field_name="destination")
    )
    known_destination: Optional[PredefinedInflationDestination] = field(
        default=None, metadata=config(field_name="knownDestination")
    )


@dataclass
class RecipientTrustlinesLocal(DataClassJsonMixin):
    recipient_type: ParticipantType = field(metadata=config(field_name="recipientType"))
    trustlines: Optional[Optional[List[Balance]]] = field(
        default=None, metadata=config(field_name="trustlines")
    )


@dataclass
class PaymentPathLocal(DataClassJsonMixin):
    source_display: str = field(metadata=config(field_name="sourceDisplay"))
    source_max_display: str = field(metadata=config(field_name="sourceMaxDisplay"))
    destination_display: str = field(metadata=config(field_name="destinationDisplay"))
    exchange_rate: str = field(metadata=config(field_name="exchangeRate"))
    amount_error: str = field(metadata=config(field_name="amountError"))
    destination_account: AccountID = field(
        metadata=config(field_name="destinationAccount")
    )
    full_path: PaymentPath = field(metadata=config(field_name="fullPath"))


@dataclass
class PaymentOrErrorCLILocal(DataClassJsonMixin):
    payment: Optional[PaymentCLILocal] = field(
        default=None, metadata=config(field_name="payment")
    )
    err: Optional[str] = field(default=None, metadata=config(field_name="err"))


@dataclass
class OwnAccountCLILocal(DataClassJsonMixin):
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    is_primary: bool = field(metadata=config(field_name="isPrimary"))
    name: str = field(metadata=config(field_name="name"))
    account_mode: AccountMode = field(metadata=config(field_name="accountMode"))
    balance: Optional[Optional[List[Balance]]] = field(
        default=None, metadata=config(field_name="balance")
    )
    exchange_rate: Optional[OutsideExchangeRate] = field(
        default=None, metadata=config(field_name="exchangeRate")
    )


@dataclass
class BatchResultLocal(DataClassJsonMixin):
    start_time: TimeMs = field(metadata=config(field_name="startTime"))
    prepared_time: TimeMs = field(metadata=config(field_name="preparedTime"))
    all_submitted_time: TimeMs = field(metadata=config(field_name="allSubmittedTime"))
    all_complete_time: TimeMs = field(metadata=config(field_name="allCompleteTime"))
    end_time: TimeMs = field(metadata=config(field_name="endTime"))
    overall_duration_ms: TimeMs = field(metadata=config(field_name="overallDurationMs"))
    prepare_duration_ms: TimeMs = field(metadata=config(field_name="prepareDurationMs"))
    submit_duration_ms: TimeMs = field(metadata=config(field_name="submitDurationMs"))
    wait_payments_duration_ms: TimeMs = field(
        metadata=config(field_name="waitPaymentsDurationMs")
    )
    wait_chat_duration_ms: TimeMs = field(
        metadata=config(field_name="waitChatDurationMs")
    )
    count_success: int = field(metadata=config(field_name="countSuccess"))
    count_direct: int = field(metadata=config(field_name="countDirect"))
    count_relay: int = field(metadata=config(field_name="countRelay"))
    count_error: int = field(metadata=config(field_name="countError"))
    count_pending: int = field(metadata=config(field_name="countPending"))
    avg_duration_ms: TimeMs = field(metadata=config(field_name="avgDurationMs"))
    avg_success_duration_ms: TimeMs = field(
        metadata=config(field_name="avgSuccessDurationMs")
    )
    avg_direct_duration_ms: TimeMs = field(
        metadata=config(field_name="avgDirectDurationMs")
    )
    avg_relay_duration_ms: TimeMs = field(
        metadata=config(field_name="avgRelayDurationMs")
    )
    avg_error_duration_ms: TimeMs = field(
        metadata=config(field_name="avgErrorDurationMs")
    )
    payments: Optional[Optional[List[BatchPaymentResult]]] = field(
        default=None, metadata=config(field_name="payments")
    )


@dataclass
class ValidateStellarURIResultLocal(DataClassJsonMixin):
    operation: str = field(metadata=config(field_name="operation"))
    origin_domain: str = field(metadata=config(field_name="originDomain"))
    message: str = field(metadata=config(field_name="message"))
    callback_url: str = field(metadata=config(field_name="callbackURL"))
    xdr: str = field(metadata=config(field_name="xdr"))
    summary: TxDisplaySummary = field(metadata=config(field_name="summary"))
    recipient: str = field(metadata=config(field_name="recipient"))
    amount: str = field(metadata=config(field_name="amount"))
    asset_code: str = field(metadata=config(field_name="assetCode"))
    asset_issuer: str = field(metadata=config(field_name="assetIssuer"))
    memo: str = field(metadata=config(field_name="memo"))
    memo_type: str = field(metadata=config(field_name="memoType"))
    display_amount_fiat: str = field(metadata=config(field_name="displayAmountFiat"))
    available_to_send_native: str = field(
        metadata=config(field_name="availableToSendNative")
    )
    available_to_send_fiat: str = field(
        metadata=config(field_name="availableToSendFiat")
    )
    signed: bool = field(metadata=config(field_name="signed"))


@dataclass
class PaymentOp(DataClassJsonMixin):
    to: Optional[keybase1.UserVersion] = field(
        default=None, metadata=config(field_name="to")
    )
    direct: Optional[DirectOp] = field(
        default=None, metadata=config(field_name="direct")
    )
    relay: Optional[RelayOp] = field(default=None, metadata=config(field_name="relay"))


@dataclass
class PaymentSummaryStellar(DataClassJsonMixin):
    tx_id: TransactionID = field(metadata=config(field_name="txID"))
    from_: AccountID = field(metadata=config(field_name="from"))
    to: AccountID = field(metadata=config(field_name="to"))
    amount: str = field(metadata=config(field_name="amount"))
    asset: Asset = field(metadata=config(field_name="asset"))
    ctime: TimeMs = field(metadata=config(field_name="ctime"))
    cursor_token: str = field(metadata=config(field_name="cursorToken"))
    unread: bool = field(metadata=config(field_name="unread"))
    is_inflation: bool = field(metadata=config(field_name="isInflation"))
    source_amount_max: str = field(metadata=config(field_name="sourceAmountMax"))
    source_amount_actual: str = field(metadata=config(field_name="sourceAmountActual"))
    source_asset: Asset = field(metadata=config(field_name="sourceAsset"))
    is_advanced: bool = field(metadata=config(field_name="isAdvanced"))
    summary_advanced: str = field(metadata=config(field_name="summaryAdvanced"))
    inflation_source: Optional[str] = field(
        default=None, metadata=config(field_name="inflationSource")
    )
    operations: Optional[Optional[List[str]]] = field(
        default=None, metadata=config(field_name="operations")
    )
    trustline: Optional[PaymentTrustlineLocal] = field(
        default=None, metadata=config(field_name="trustline")
    )


@dataclass
class PaymentSummaryRelay(DataClassJsonMixin):
    kb_tx_id: KeybaseTransactionID = field(metadata=config(field_name="kbTxID"))
    tx_id: TransactionID = field(metadata=config(field_name="txID"))
    tx_status: TransactionStatus = field(metadata=config(field_name="txStatus"))
    tx_err_msg: str = field(metadata=config(field_name="txErrMsg"))
    from_stellar: AccountID = field(metadata=config(field_name="fromStellar"))
    from_: keybase1.UserVersion = field(metadata=config(field_name="from"))
    from_device_id: keybase1.DeviceID = field(
        metadata=config(field_name="fromDeviceID")
    )
    to_assertion: str = field(metadata=config(field_name="toAssertion"))
    relay_account: AccountID = field(metadata=config(field_name="relayAccount"))
    amount: str = field(metadata=config(field_name="amount"))
    ctime: TimeMs = field(metadata=config(field_name="ctime"))
    rtime: TimeMs = field(metadata=config(field_name="rtime"))
    box_b_64: str = field(metadata=config(field_name="boxB64"))
    team_id: keybase1.TeamID = field(metadata=config(field_name="teamID"))
    cursor_token: str = field(metadata=config(field_name="cursorToken"))
    batch_id: str = field(metadata=config(field_name="batchID"))
    from_airdrop: bool = field(metadata=config(field_name="fromAirdrop"))
    to: Optional[keybase1.UserVersion] = field(
        default=None, metadata=config(field_name="to")
    )
    display_amount: Optional[str] = field(
        default=None, metadata=config(field_name="displayAmount")
    )
    display_currency: Optional[str] = field(
        default=None, metadata=config(field_name="displayCurrency")
    )
    claim: Optional[ClaimSummary] = field(
        default=None, metadata=config(field_name="claim")
    )


@dataclass
class AccountDetails(DataClassJsonMixin):
    account_id: AccountID = field(metadata=config(field_name="accountID"))
    seqno: str = field(metadata=config(field_name="seqno"))
    subentry_count: int = field(metadata=config(field_name="subentryCount"))
    available: str = field(metadata=config(field_name="available"))
    unread_payments: int = field(metadata=config(field_name="unreadPayments"))
    display_currency: str = field(metadata=config(field_name="displayCurrency"))
    balances: Optional[Optional[List[Balance]]] = field(
        default=None, metadata=config(field_name="balances")
    )
    reserves: Optional[Optional[List[AccountReserve]]] = field(
        default=None, metadata=config(field_name="reserves")
    )
    read_transaction_id: Optional[TransactionID] = field(
        default=None, metadata=config(field_name="readTransactionID")
    )
    inflation_destination: Optional[AccountID] = field(
        default=None, metadata=config(field_name="inflationDestination")
    )


@dataclass
class UIPaymentReviewed(DataClassJsonMixin):
    bid: BuildPaymentID = field(metadata=config(field_name="bid"))
    review_id: int = field(metadata=config(field_name="reviewID"))
    seqno: int = field(metadata=config(field_name="seqno"))
    next_button: str = field(metadata=config(field_name="nextButton"))
    banners: Optional[Optional[List[SendBannerLocal]]] = field(
        default=None, metadata=config(field_name="banners")
    )


@dataclass
class BundleSecretVersioned__V1(DataClassJsonMixin):
    version: Literal[BundleVersionStrings.V1]
    V1: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V2(DataClassJsonMixin):
    version: Literal[BundleVersionStrings.V2]
    V2: Optional[BundleSecretV2]


@dataclass
class BundleSecretVersioned__V3(DataClassJsonMixin):
    version: Literal[BundleVersionStrings.V3]
    V3: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V4(DataClassJsonMixin):
    version: Literal[BundleVersionStrings.V4]
    V4: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V5(DataClassJsonMixin):
    version: Literal[BundleVersionStrings.V5]
    V5: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V6(DataClassJsonMixin):
    version: Literal[BundleVersionStrings.V6]
    V6: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V7(DataClassJsonMixin):
    version: Literal[BundleVersionStrings.V7]
    V7: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V8(DataClassJsonMixin):
    version: Literal[BundleVersionStrings.V8]
    V8: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V9(DataClassJsonMixin):
    version: Literal[BundleVersionStrings.V9]
    V9: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V10(DataClassJsonMixin):
    version: Literal[BundleVersionStrings.V10]
    V10: Optional[BundleSecretUnsupported]


BundleSecretVersioned = Union[
    BundleSecretVersioned__V1,
    BundleSecretVersioned__V2,
    BundleSecretVersioned__V3,
    BundleSecretVersioned__V4,
    BundleSecretVersioned__V5,
    BundleSecretVersioned__V6,
    BundleSecretVersioned__V7,
    BundleSecretVersioned__V8,
    BundleSecretVersioned__V9,
    BundleSecretVersioned__V10,
]


@dataclass
class PaymentOrErrorLocal(DataClassJsonMixin):
    payment: Optional[PaymentLocal] = field(
        default=None, metadata=config(field_name="payment")
    )
    err: Optional[str] = field(default=None, metadata=config(field_name="err"))


@dataclass
class PaymentDetailsLocal(DataClassJsonMixin):
    summary: PaymentLocal = field(metadata=config(field_name="summary"))
    details: PaymentDetailsOnlyLocal = field(metadata=config(field_name="details"))


@dataclass
class PaymentMultiPost(DataClassJsonMixin):
    from_device_id: keybase1.DeviceID = field(
        metadata=config(field_name="fromDeviceID")
    )
    signed_transaction: str = field(metadata=config(field_name="signedTransaction"))
    batch_id: str = field(metadata=config(field_name="batchID"))
    operations: Optional[Optional[List[PaymentOp]]] = field(
        default=None, metadata=config(field_name="operations")
    )


@dataclass
class PaymentSummary__STELLAR(DataClassJsonMixin):
    typ: Literal[PaymentSummaryTypeStrings.STELLAR]
    STELLAR: Optional[PaymentSummaryStellar]


@dataclass
class PaymentSummary__DIRECT(DataClassJsonMixin):
    typ: Literal[PaymentSummaryTypeStrings.DIRECT]
    DIRECT: Optional[PaymentSummaryDirect]


@dataclass
class PaymentSummary__RELAY(DataClassJsonMixin):
    typ: Literal[PaymentSummaryTypeStrings.RELAY]
    RELAY: Optional[PaymentSummaryRelay]


PaymentSummary = Union[
    PaymentSummary__STELLAR, PaymentSummary__DIRECT, PaymentSummary__RELAY
]


@dataclass
class PaymentsPageLocal(DataClassJsonMixin):
    payments: Optional[Optional[List[PaymentOrErrorLocal]]] = field(
        default=None, metadata=config(field_name="payments")
    )
    cursor: Optional[PageCursor] = field(
        default=None, metadata=config(field_name="cursor")
    )
    oldest_unread: Optional[PaymentID] = field(
        default=None, metadata=config(field_name="oldestUnread")
    )


@dataclass
class PaymentDetails(DataClassJsonMixin):
    summary: PaymentSummary = field(metadata=config(field_name="summary"))
    memo: str = field(metadata=config(field_name="memo"))
    memo_type: str = field(metadata=config(field_name="memoType"))
    external_tx_url: str = field(metadata=config(field_name="externalTxURL"))
    fee_charged: str = field(metadata=config(field_name="feeCharged"))
    path_intermediate: Optional[Optional[List[Asset]]] = field(
        default=None, metadata=config(field_name="pathIntermediate")
    )


@dataclass
class PaymentsPage(DataClassJsonMixin):
    payments: Optional[Optional[List[PaymentSummary]]] = field(
        default=None, metadata=config(field_name="payments")
    )
    cursor: Optional[PageCursor] = field(
        default=None, metadata=config(field_name="cursor")
    )
    oldest_unread: Optional[TransactionID] = field(
        default=None, metadata=config(field_name="oldestUnread")
    )


@dataclass
class DetailsPlusPayments(DataClassJsonMixin):
    details: AccountDetails = field(metadata=config(field_name="details"))
    recent_payments: PaymentsPage = field(metadata=config(field_name="recentPayments"))
    pending_payments: Optional[Optional[List[PaymentSummary]]] = field(
        default=None, metadata=config(field_name="pendingPayments")
    )
