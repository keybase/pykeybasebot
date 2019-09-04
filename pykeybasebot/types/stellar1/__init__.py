"""stellar.1

Auto-generated to Python types by avdl-compiler v1.4.1 (https://github.com/keybase/node-avdl-compiler)
Input files:
 - ../client/protocol/avdl/stellar1/bundle.avdl
 - ../client/protocol/avdl/stellar1/common.avdl
 - ../client/protocol/avdl/stellar1/gregor.avdl
 - ../client/protocol/avdl/stellar1/local.avdl
 - ../client/protocol/avdl/stellar1/notify.avdl
 - ../client/protocol/avdl/stellar1/remote.avdl
 - ../client/protocol/avdl/stellar1/ui.avdl
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union

from mashumaro import DataClassJSONMixin
from typing_extensions import Literal

import keybase1

BundleRevision = int


@dataclass
class EncryptedBundle(DataClassJSONMixin):
    v: int
    e: bytes
    n: keybase1.BoxNonce
    gen: keybase1.PerUserKeyGeneration


class BundleVersion(Enum):
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
class BundleSecretUnsupported(DataClassJSONMixin):
    pass


@dataclass
class EncryptedAccountBundle(DataClassJSONMixin):
    v: int
    e: bytes
    n: keybase1.BoxNonce
    gen: keybase1.PerUserKeyGeneration


class AccountBundleVersion(Enum):
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
class AccountBundleSecretUnsupported(DataClassJSONMixin):
    pass


AccountID = str
SecretKey = str
TransactionID = str
PaymentID = str
KeybaseTransactionID = str
TimeMs = int
Hash = bytes
KeybaseRequestID = str
AssetCode = str


@dataclass
class Asset(DataClassJSONMixin):
    type: str
    code: str
    issuer: str
    verified_domain: str
    issuer_name: str
    desc: str
    info_url: str
    info_url_text: str
    show_deposit_button: bool
    deposit_button_text: str
    show_withdraw_button: bool
    withdraw_button_text: str
    withdraw_type: str
    transfer_server: str
    auth_endpoint: str


@dataclass
class AccountReserve(DataClassJSONMixin):
    amount: str
    description: str


class TransactionStatus(Enum):
    NONE = "none"
    PENDING = "pending"
    SUCCESS = "success"
    ERROR_TRANSIENT = "error_transient"
    ERROR_PERMANENT = "error_permanent"


class RequestStatus(Enum):
    OK = "ok"
    CANCELED = "canceled"
    DONE = "done"


class PaymentStrategy(Enum):
    NONE = "none"
    DIRECT = "direct"
    RELAY = "relay"


class RelayDirection(Enum):
    CLAIM = "claim"
    YANK = "yank"


@dataclass
class NoteRecipient(DataClassJSONMixin):
    user: keybase1.UserVersion
    puk_gen: keybase1.PerUserKeyGeneration


@dataclass
class EncryptedRelaySecret(DataClassJSONMixin):
    v: int
    e: bytes
    n: keybase1.BoxNonce
    gen: keybase1.PerTeamKeyGeneration


OutsideCurrencyCode = str


@dataclass
class CurrencySymbol(DataClassJSONMixin):
    str: str
    ambigious: bool
    postfix: bool


@dataclass
class PageCursor(DataClassJSONMixin):
    horizon_cursor: str
    direct_cursor: str
    relay_cursor: str


class AccountMode(Enum):
    NONE = "none"
    USER = "user"
    MOBILE = "mobile"


class BalanceDelta(Enum):
    NONE = "none"
    INCREASE = "increase"
    DECREASE = "decrease"


class PaymentStatus(Enum):
    NONE = "none"
    PENDING = "pending"
    CLAIMABLE = "claimable"
    COMPLETED = "completed"
    ERROR = "error"
    UNKNOWN = "unknown"
    CANCELED = "canceled"


class ParticipantType(Enum):
    NONE = "none"
    KEYBASE = "keybase"
    STELLAR = "stellar"
    SBS = "sbs"
    OWNACCOUNT = "ownaccount"


BuildPaymentID = str


class AdvancedBanner(Enum):
    NO_BANNER = "no_banner"
    SENDER_BANNER = "sender_banner"
    RECEIVER_BANNER = "receiver_banner"


InflationDestinationTag = str


@dataclass
class AirdropDetails(DataClassJSONMixin):
    is_promoted: bool
    details: str
    disclaimer: str


AirdropState = str


@dataclass
class AirdropQualification(DataClassJSONMixin):
    title: str
    subtitle: str
    valid: bool


@dataclass
class AssetActionResultLocal(DataClassJSONMixin):
    external_url: Optional[str]
    message_from_anchor: Optional[str]


@dataclass
class BatchPaymentError(DataClassJSONMixin):
    message: str
    code: int


@dataclass
class BatchPaymentArg(DataClassJSONMixin):
    recipient: str
    amount: str
    message: str


@dataclass
class PartnerUrl(DataClassJSONMixin):
    url: str
    title: str
    description: str
    icon_filename: str
    admin_only: bool
    extra: str


@dataclass
class StaticConfig(DataClassJSONMixin):
    payment_note_max_length: int
    request_note_max_length: int
    public_memo_max_length: int


ChatConversationID = str


@dataclass
class DirectOp(DataClassJSONMixin):
    note_b_64: str


class PaymentSummaryType(Enum):
    NONE = "none"
    STELLAR = "stellar"
    DIRECT = "direct"
    RELAY = "relay"


@dataclass
class TimeboundsRecommendation(DataClassJSONMixin):
    time_now: keybase1.UnixTime
    timeout: int


@dataclass
class NetworkOptions(DataClassJSONMixin):
    base_fee: int


@dataclass
class BundleVisibleEntryV2(DataClassJSONMixin):
    account_id: AccountID
    mode: AccountMode
    is_primary: bool
    acct_bundle_revision: BundleRevision
    enc_acct_bundle_hash: Hash


@dataclass
class BundleSecretEntryV2(DataClassJSONMixin):
    account_id: AccountID
    name: str


@dataclass
class AccountBundleSecretV1(DataClassJSONMixin):
    account_id: AccountID
    signers: List[SecretKey]


@dataclass
class BundleEntry(DataClassJSONMixin):
    account_id: AccountID
    mode: AccountMode
    is_primary: bool
    name: str
    acct_bundle_revision: BundleRevision
    enc_acct_bundle_hash: Hash


@dataclass
class AccountBundle(DataClassJSONMixin):
    prev: Hash
    own_hash: Hash
    account_id: AccountID
    signers: List[SecretKey]


@dataclass
class AssetListResult(DataClassJSONMixin):
    assets: List[Asset]
    total_count: int


@dataclass
class Balance(DataClassJSONMixin):
    asset: Asset
    amount: str
    limit: str
    is_authorized: bool


@dataclass
class PaymentResult(DataClassJSONMixin):
    sender_account_id: AccountID
    keybase_id: KeybaseTransactionID
    stellar_id: TransactionID
    pending: bool


@dataclass
class RelayClaimResult(DataClassJSONMixin):
    claim_stellar_id: TransactionID


@dataclass
class EncryptedNote(DataClassJSONMixin):
    v: int
    e: bytes
    n: keybase1.BoxNonce
    sender: NoteRecipient
    recipient: Optional[NoteRecipient]


@dataclass
class NoteContents(DataClassJSONMixin):
    note: str
    stellar_id: TransactionID


@dataclass
class RelayContents(DataClassJSONMixin):
    stellar_id: TransactionID
    sk: SecretKey
    note: str


@dataclass
class OutsideExchangeRate(DataClassJSONMixin):
    currency: OutsideCurrencyCode
    rate: str


@dataclass
class OutsideCurrencyDefinition(DataClassJSONMixin):
    name: str
    symbol: CurrencySymbol


@dataclass
class Trustline(DataClassJSONMixin):
    asset_code: AssetCode
    issuer: AccountID


@dataclass
class PaymentPath(DataClassJSONMixin):
    source_amount: str
    source_amount_max: str
    source_asset: Asset
    path: List[Asset]
    destination_amount: str
    destination_asset: Asset
    source_insufficient_balance: str


@dataclass
class PaymentStatusMsg(DataClassJSONMixin):
    account_id: AccountID
    kb_tx_id: KeybaseTransactionID
    tx_id: TransactionID


@dataclass
class RequestStatusMsg(DataClassJSONMixin):
    req_id: KeybaseRequestID


@dataclass
class PaymentNotificationMsg(DataClassJSONMixin):
    account_id: AccountID
    payment_id: PaymentID


@dataclass
class AccountAssetLocal(DataClassJSONMixin):
    name: str
    asset_code: str
    issuer_name: str
    issuer_account_id: str
    issuer_verified_domain: str
    balance_total: str
    balance_available_to_send: str
    worth_currency: str
    worth: str
    available_to_send_worth: str
    reserves: List[AccountReserve]
    desc: str
    info_url: str
    info_url_text: str
    show_deposit_button: bool
    deposit_button_text: str
    show_withdraw_button: bool
    withdraw_button_text: str


@dataclass
class PaymentDetailsOnlyLocal(DataClassJSONMixin):
    public_note: str
    public_note_type: str
    external_tx_url: str
    fee_charged_description: str
    path_intermediate: List[Asset]


@dataclass
class PaymentTrustlineLocal(DataClassJSONMixin):
    asset: Asset
    remove: bool


@dataclass
class CurrencyLocal(DataClassJSONMixin):
    description: str
    code: OutsideCurrencyCode
    symbol: str
    name: str


@dataclass
class SendAssetChoiceLocal(DataClassJSONMixin):
    asset: Asset
    enabled: bool
    left: str
    right: str
    subtext: str


@dataclass
class SendBannerLocal(DataClassJSONMixin):
    level: str
    message: str
    proofs_changed: bool
    offer_advanced_send_form: AdvancedBanner


@dataclass
class SendPaymentResLocal(DataClassJSONMixin):
    kb_tx_id: KeybaseTransactionID
    pending: bool
    jump_to_chat: str


@dataclass
class RequestDetailsLocal(DataClassJSONMixin):
    id: KeybaseRequestID
    from_assertion: str
    from_current_user: bool
    to_user_type: ParticipantType
    to_assertion: str
    amount: str
    asset: Optional[Asset]
    currency: Optional[OutsideCurrencyCode]
    amount_description: str
    worth_at_request_time: str
    status: RequestStatus


@dataclass
class PredefinedInflationDestination(DataClassJSONMixin):
    tag: InflationDestinationTag
    name: str
    recommended: bool
    account_id: AccountID
    url: str


@dataclass
class AirdropStatus(DataClassJSONMixin):
    state: AirdropState
    rows: List[AirdropQualification]


@dataclass
class SendResultCLILocal(DataClassJSONMixin):
    kb_tx_id: KeybaseTransactionID
    tx_id: TransactionID


@dataclass
class PaymentCLILocal(DataClassJSONMixin):
    tx_id: TransactionID
    time: TimeMs
    status: str
    status_detail: str
    amount: str
    asset: Asset
    display_amount: Optional[str]
    display_currency: Optional[str]
    source_amount_max: str
    source_amount_actual: str
    source_asset: Asset
    is_advanced: bool
    summary_advanced: str
    operations: List[str]
    from_stellar: AccountID
    to_stellar: Optional[AccountID]
    from_username: Optional[str]
    to_username: Optional[str]
    to_assertion: Optional[str]
    note: str
    note_err: str
    unread: bool
    public_note: str
    public_note_type: str
    fee_charged_description: str


@dataclass
class LookupResultCLILocal(DataClassJSONMixin):
    account_id: AccountID
    username: Optional[str]


@dataclass
class BatchPaymentResult(DataClassJSONMixin):
    username: str
    start_time: TimeMs
    submitted_time: TimeMs
    end_time: TimeMs
    tx_id: TransactionID
    status: PaymentStatus
    status_description: str
    error: Optional[BatchPaymentError]


@dataclass
class TxDisplaySummary(DataClassJSONMixin):
    source: AccountID
    fee: int
    memo: str
    memo_type: str
    operations: List[str]


@dataclass
class SignXdrResult(DataClassJSONMixin):
    singed_tx: str
    account_id: AccountID
    submit_err: Optional[str]
    submit_tx_id: Optional[TransactionID]


@dataclass
class PaymentDirectPost(DataClassJSONMixin):
    from_device_id: keybase1.DeviceID
    to: Optional[keybase1.UserVersion]
    display_amount: str
    display_currency: str
    note_b_64: str
    signed_transaction: str
    quick_return: bool
    chat_conversation_id: Optional[ChatConversationID]
    batch_id: str


@dataclass
class PaymentRelayPost(DataClassJSONMixin):
    from_device_id: keybase1.DeviceID
    to: Optional[keybase1.UserVersion]
    to_assertion: str
    relay_account: AccountID
    team_id: keybase1.TeamID
    display_amount: str
    display_currency: str
    box_b_64: str
    signed_transaction: str
    quick_return: bool
    chat_conversation_id: Optional[ChatConversationID]
    batch_id: str


@dataclass
class RelayClaimPost(DataClassJSONMixin):
    keybase_id: KeybaseTransactionID
    dir: RelayDirection
    signed_transaction: str
    auto_claim_token: Optional[str]


@dataclass
class PathPaymentPost(DataClassJSONMixin):
    from_device_id: keybase1.DeviceID
    to: Optional[keybase1.UserVersion]
    note_b_64: str
    signed_transaction: str
    quick_return: bool
    chat_conversation_id: Optional[ChatConversationID]


@dataclass
class RelayOp(DataClassJSONMixin):
    to_assertion: str
    relay_account: AccountID
    team_id: keybase1.TeamID
    box_b_64: str


@dataclass
class PaymentSummaryDirect(DataClassJSONMixin):
    kb_tx_id: KeybaseTransactionID
    tx_id: TransactionID
    tx_status: TransactionStatus
    tx_err_msg: str
    from_stellar: AccountID
    from_: keybase1.UserVersion
    from_device_id: keybase1.DeviceID
    to_stellar: AccountID
    to: Optional[keybase1.UserVersion]
    amount: str
    asset: Asset
    display_amount: Optional[str]
    display_currency: Optional[str]
    note_b_64: str
    from_display_amount: str
    from_display_currency: str
    to_display_amount: str
    to_display_currency: str
    ctime: TimeMs
    rtime: TimeMs
    cursor_token: str
    unread: bool
    from_primary: bool
    batch_id: str
    from_airdrop: bool
    source_amount_max: str
    source_amount_actual: str
    source_asset: Asset


@dataclass
class ClaimSummary(DataClassJSONMixin):
    tx_id: TransactionID
    tx_status: TransactionStatus
    tx_err_msg: str
    dir: RelayDirection
    to_stellar: AccountID
    to: keybase1.UserVersion


@dataclass
class SubmitMultiRes(DataClassJSONMixin):
    tx_id: TransactionID


@dataclass
class AutoClaim(DataClassJSONMixin):
    kb_tx_id: KeybaseTransactionID


@dataclass
class RequestPost(DataClassJSONMixin):
    to_user: Optional[keybase1.UserVersion]
    to_assertion: str
    amount: str
    asset: Optional[Asset]
    currency: Optional[OutsideCurrencyCode]


@dataclass
class RequestDetails(DataClassJSONMixin):
    id: KeybaseRequestID
    from_user: keybase1.UserVersion
    to_user: Optional[keybase1.UserVersion]
    to_assertion: str
    amount: str
    asset: Optional[Asset]
    currency: Optional[OutsideCurrencyCode]
    from_display_amount: str
    from_display_currency: str
    to_display_amount: str
    to_display_currency: str
    funding_kb_tx_id: KeybaseTransactionID
    status: RequestStatus


@dataclass
class PaymentPathQuery(DataClassJSONMixin):
    source: AccountID
    destination: AccountID
    source_asset: Asset
    destination_asset: Asset
    amount: str


@dataclass
class BundleVisibleV2(DataClassJSONMixin):
    revision: BundleRevision
    prev: Hash
    accounts: List[BundleVisibleEntryV2]


@dataclass
class BundleSecretV2(DataClassJSONMixin):
    visible_hash: Hash
    accounts: List[BundleSecretEntryV2]


@dataclass
class AccountBundleSecretVersioned__V1:
    version: Literal[AccountBundleVersion.V1]
    V1: Optional[AccountBundleSecretV1]


@dataclass
class AccountBundleSecretVersioned__V2:
    version: Literal[AccountBundleVersion.V2]
    V2: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V3:
    version: Literal[AccountBundleVersion.V3]
    V3: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V4:
    version: Literal[AccountBundleVersion.V4]
    V4: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V5:
    version: Literal[AccountBundleVersion.V5]
    V5: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V6:
    version: Literal[AccountBundleVersion.V6]
    V6: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V7:
    version: Literal[AccountBundleVersion.V7]
    V7: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V8:
    version: Literal[AccountBundleVersion.V8]
    V8: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V9:
    version: Literal[AccountBundleVersion.V9]
    V9: Optional[AccountBundleSecretUnsupported]


@dataclass
class AccountBundleSecretVersioned__V10:
    version: Literal[AccountBundleVersion.V10]
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
class Bundle(DataClassJSONMixin):
    revision: BundleRevision
    prev: Hash
    own_hash: Hash
    accounts: List[BundleEntry]
    account_bundles: Dict[str, AccountBundle]


@dataclass
class StellarServerDefinitions(DataClassJSONMixin):
    revision: int
    currencies: Dict[str, OutsideCurrencyDefinition]


@dataclass
class WalletAccountLocal(DataClassJSONMixin):
    account_id: AccountID
    is_default: bool
    name: str
    balance_description: str
    seqno: str
    currency_local: CurrencyLocal
    account_mode: AccountMode
    account_mode_editable: bool
    device_read_only: bool
    is_funded: bool
    can_submit_tx: bool
    can_add_trustline: bool


@dataclass
class PaymentLocal(DataClassJSONMixin):
    id: PaymentID
    tx_id: TransactionID
    time: TimeMs
    status_simplified: PaymentStatus
    status_description: str
    status_detail: str
    show_cancel: bool
    amount_description: str
    delta: BalanceDelta
    worth: str
    worth_at_send_time: str
    issuer_description: str
    issuer_account_id: Optional[AccountID]
    from_type: ParticipantType
    to_type: ParticipantType
    asset_code: str
    from_account_id: AccountID
    from_account_name: str
    from_username: str
    to_account_id: Optional[AccountID]
    to_account_name: str
    to_username: str
    to_assertion: str
    original_to_assertion: str
    note: str
    note_err: str
    source_amount_max: str
    source_amount_actual: str
    source_asset: Asset
    source_conv_rate: str
    is_advanced: bool
    summary_advanced: str
    operations: List[str]
    unread: bool
    batch_id: str
    from_airdrop: bool
    is_inflation: bool
    inflation_source: Optional[str]
    trustline: Optional[PaymentTrustlineLocal]


@dataclass
class BuildPaymentResLocal(DataClassJSONMixin):
    ready_to_review: bool
    from_: AccountID
    to_err_msg: str
    amount_err_msg: str
    secret_note_err_msg: str
    public_memo_err_msg: str
    worth_description: str
    worth_info: str
    worth_amount: str
    worth_currency: str
    display_amount_xlm: str
    display_amount_fiat: str
    sending_intention_xlm: bool
    amount_available: str
    banners: List[SendBannerLocal]


@dataclass
class BuildRequestResLocal(DataClassJSONMixin):
    ready_to_request: bool
    to_err_msg: str
    amount_err_msg: str
    secret_note_err_msg: str
    worth_description: str
    worth_info: str
    display_amount_xlm: str
    display_amount_fiat: str
    sending_intention_xlm: bool
    banners: List[SendBannerLocal]


@dataclass
class InflationDestinationResultLocal(DataClassJSONMixin):
    destination: Optional[AccountID]
    known_destination: Optional[PredefinedInflationDestination]
    self_: bool


@dataclass
class RecipientTrustlinesLocal(DataClassJSONMixin):
    trustlines: List[Balance]
    recipient_type: ParticipantType


@dataclass
class PaymentPathLocal(DataClassJSONMixin):
    source_display: str
    source_max_display: str
    destination_display: str
    exchange_rate: str
    amount_error: str
    destination_account: AccountID
    full_path: PaymentPath


@dataclass
class PaymentOrErrorCLILocal(DataClassJSONMixin):
    payment: Optional[PaymentCLILocal]
    err: Optional[str]


@dataclass
class OwnAccountCLILocal(DataClassJSONMixin):
    account_id: AccountID
    is_primary: bool
    name: str
    balance: List[Balance]
    exchange_rate: Optional[OutsideExchangeRate]
    account_mode: AccountMode


@dataclass
class BatchResultLocal(DataClassJSONMixin):
    start_time: TimeMs
    prepared_time: TimeMs
    all_submitted_time: TimeMs
    all_complete_time: TimeMs
    end_time: TimeMs
    payments: List[BatchPaymentResult]
    overall_duration_ms: TimeMs
    prepare_duration_ms: TimeMs
    submit_duration_ms: TimeMs
    wait_payments_duration_ms: TimeMs
    wait_chat_duration_ms: TimeMs
    count_success: int
    count_direct: int
    count_relay: int
    count_error: int
    count_pending: int
    avg_duration_ms: TimeMs
    avg_success_duration_ms: TimeMs
    avg_direct_duration_ms: TimeMs
    avg_relay_duration_ms: TimeMs
    avg_error_duration_ms: TimeMs


@dataclass
class ValidateStellarURIResultLocal(DataClassJSONMixin):
    operation: str
    origin_domain: str
    message: str
    callback_url: str
    xdr: str
    summary: TxDisplaySummary
    recipient: str
    amount: str
    asset_code: str
    asset_issuer: str
    memo: str
    memo_type: str
    display_amount_fiat: str
    available_to_send_native: str
    available_to_send_fiat: str
    signed: bool


@dataclass
class PaymentOp(DataClassJSONMixin):
    to: Optional[keybase1.UserVersion]
    direct: Optional[DirectOp]
    relay: Optional[RelayOp]


@dataclass
class PaymentSummaryStellar(DataClassJSONMixin):
    tx_id: TransactionID
    from_: AccountID
    to: AccountID
    amount: str
    asset: Asset
    ctime: TimeMs
    cursor_token: str
    unread: bool
    is_inflation: bool
    inflation_source: Optional[str]
    source_amount_max: str
    source_amount_actual: str
    source_asset: Asset
    is_advanced: bool
    summary_advanced: str
    operations: List[str]
    trustline: Optional[PaymentTrustlineLocal]


@dataclass
class PaymentSummaryRelay(DataClassJSONMixin):
    kb_tx_id: KeybaseTransactionID
    tx_id: TransactionID
    tx_status: TransactionStatus
    tx_err_msg: str
    from_stellar: AccountID
    from_: keybase1.UserVersion
    from_device_id: keybase1.DeviceID
    to: Optional[keybase1.UserVersion]
    to_assertion: str
    relay_account: AccountID
    amount: str
    display_amount: Optional[str]
    display_currency: Optional[str]
    ctime: TimeMs
    rtime: TimeMs
    box_b_64: str
    team_id: keybase1.TeamID
    claim: Optional[ClaimSummary]
    cursor_token: str
    batch_id: str
    from_airdrop: bool


@dataclass
class AccountDetails(DataClassJSONMixin):
    account_id: AccountID
    seqno: str
    balances: List[Balance]
    subentry_count: int
    available: str
    reserves: List[AccountReserve]
    read_transaction_id: Optional[TransactionID]
    unread_payments: int
    display_currency: str
    inflation_destination: Optional[AccountID]


@dataclass
class UIPaymentReviewed(DataClassJSONMixin):
    bid: BuildPaymentID
    review_id: int
    seqno: int
    banners: List[SendBannerLocal]
    next_button: str


@dataclass
class BundleSecretVersioned__V1:
    version: Literal[BundleVersion.V1]
    V1: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V2:
    version: Literal[BundleVersion.V2]
    V2: Optional[BundleSecretV2]


@dataclass
class BundleSecretVersioned__V3:
    version: Literal[BundleVersion.V3]
    V3: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V4:
    version: Literal[BundleVersion.V4]
    V4: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V5:
    version: Literal[BundleVersion.V5]
    V5: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V6:
    version: Literal[BundleVersion.V6]
    V6: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V7:
    version: Literal[BundleVersion.V7]
    V7: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V8:
    version: Literal[BundleVersion.V8]
    V8: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V9:
    version: Literal[BundleVersion.V9]
    V9: Optional[BundleSecretUnsupported]


@dataclass
class BundleSecretVersioned__V10:
    version: Literal[BundleVersion.V10]
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
class PaymentOrErrorLocal(DataClassJSONMixin):
    payment: Optional[PaymentLocal]
    err: Optional[str]


@dataclass
class PaymentDetailsLocal(DataClassJSONMixin):
    summary: PaymentLocal
    details: PaymentDetailsOnlyLocal


@dataclass
class PaymentMultiPost(DataClassJSONMixin):
    from_device_id: keybase1.DeviceID
    signed_transaction: str
    operations: List[PaymentOp]
    batch_id: str


@dataclass
class PaymentSummary__STELLAR:
    typ: Literal[PaymentSummaryType.STELLAR]
    STELLAR: Optional[PaymentSummaryStellar]


@dataclass
class PaymentSummary__DIRECT:
    typ: Literal[PaymentSummaryType.DIRECT]
    DIRECT: Optional[PaymentSummaryDirect]


@dataclass
class PaymentSummary__RELAY:
    typ: Literal[PaymentSummaryType.RELAY]
    RELAY: Optional[PaymentSummaryRelay]


PaymentSummary = Union[
    PaymentSummary__STELLAR, PaymentSummary__DIRECT, PaymentSummary__RELAY
]


@dataclass
class PaymentsPageLocal(DataClassJSONMixin):
    payments: List[PaymentOrErrorLocal]
    cursor: Optional[PageCursor]
    oldest_unread: Optional[PaymentID]


@dataclass
class PaymentDetails(DataClassJSONMixin):
    summary: PaymentSummary
    memo: str
    memo_type: str
    external_tx_url: str
    fee_charged: str
    path_intermediate: List[Asset]


@dataclass
class PaymentsPage(DataClassJSONMixin):
    payments: List[PaymentSummary]
    cursor: Optional[PageCursor]
    oldest_unread: Optional[TransactionID]


@dataclass
class DetailsPlusPayments(DataClassJSONMixin):
    details: AccountDetails
    recent_payments: PaymentsPage
    pending_payments: List[PaymentSummary]
