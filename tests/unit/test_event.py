import json
import os
from pathlib import Path

import pytest

import pykeybasebot.types.chat1 as chat1
import pykeybasebot.types.stellar1 as stellar1
from pykeybasebot import EventType, KbEvent, Source


@pytest.fixture()
def fixture_path():
    app_dir = Path().absolute()
    return os.path.join(app_dir, "tests/unit/fixtures")


def get_result(path: str):
    with open(path) as json_file:
        data = json.load(json_file)
    return data["result"]


def test_list(fixture_path):
    result = get_result(f"{fixture_path}/list_result.json")
    chat_list = chat1.ChatList.from_dict(result)
    assert chat_list == chat1.ChatList(
        offline=False,
        conversations=[
            chat1.ConvSummary(
                id="0000d5ba71470610a40b4d32af53a52775cc561589525d7b21bad9ec057b6aac",
                channel=chat1.ChatChannel(
                    name="keybasefriends",
                    members_type="team",
                    topic_type="chat",
                    topic_name="general",
                ),
                unread=True,
                is_default_conv=True,
                active_at=1_572_402_097,
                active_at_ms=1_572_402_097_456,
                member_status="active",
            )
        ],
    )


def test_read(fixture_path):
    result = get_result(f"{fixture_path}/read_result.json")
    thread = chat1.Thread.from_dict(result)
    assert thread == chat1.Thread(
        messages=[
            chat1.Message(
                msg=chat1.MsgSummary(
                    id=3,
                    conv_id="00001bca4f13b0a7b81bfbc2acd7f8cf829bf53845ac87cdd8b62617d5aaa084",
                    channel=chat1.ChatChannel(
                        name="alice,bob",
                        members_type="impteamnative",
                        topic_type="chat",
                    ),
                    sender=chat1.MsgSender(
                        uid="8440bf65b0e77107c12e0350fc905e19",
                        username="alice",
                        device_id="011e2994f419d748d751a449ae17e218",
                        device_name="alice's phone",
                    ),
                    sent_at=1_544_140_065,
                    sent_at_ms=1_544_140_065_815,
                    content=chat1.MsgContent(
                        type_name="text",
                        text=chat1.MessageText(
                            body="hello",
                            payments=None,
                            user_mentions=None,
                            team_mentions=None,
                        ),
                    ),
                    prev=[
                        chat1.MessagePreviousPointer(
                            id=2, hash="A40VOjV7PVK7KcGZwOL/BOhPvn/a0jWg1JUltv7OLaQ="
                        )
                    ],
                    unread=False,
                    channel_mention="none",
                )
            )
        ],
        pagination=chat1.Pagination(
            num=469, next="AQ==", previous="zQHV", last=True, force_first_page=None
        ),
    )


def test_teamchat(fixture_path):
    with open(f"{fixture_path}/teamchat.json") as json_file:
        data = json.load(json_file)

    event = KbEvent.from_dict(data)

    assert event.type == EventType.CHAT
    expected_team_mention = chat1.KnownTeamMention(
        name="yourcompany.marketing", channel="general"
    )
    assert event.msg.content.text.team_mentions == [expected_team_mention]
    reply_channel = event.msg.channel.to_dict()
    assert reply_channel == {
        "name": "yourcompany.marketing",
        "topic_name": "lunchtalk",
        "members_type": "team",
        "topic_type": "chat",
        "public": False,
    }


def test_oneonone(fixture_path):
    with open(f"{fixture_path}/oneonone.json") as json_file:
        data = json.load(json_file)

    event = KbEvent.from_dict(data)

    assert event.type == EventType.CHAT
    assert event.msg.content.text.body == "hi"
    reply_channel = event.msg.channel.to_dict()
    assert reply_channel == {
        "name": "someoneelse,yourbot",
        "members_type": "impteamnative",
        "public": False,
        "topic_name": None,
        "topic_type": "chat",
    }


def test_reaction(fixture_path):
    with open(f"{fixture_path}/reaction.json") as json_file:
        data = json.load(json_file)

    event = KbEvent.from_dict(data)

    assert event.msg.content.type_name == chat1.MessageTypeStrings.REACTION.value
    assert event.msg.content.reaction.body == ":sunglasses:"
    reply_channel = event.msg.channel.to_dict()
    assert reply_channel == {
        "name": "someoneelse,yourbot",
        "members_type": "impteamnative",
        "public": False,
        "topic_name": None,
        "topic_type": "chat",
    }


def test_payment(fixture_path):
    with open(f"{fixture_path}/payment.json") as json_file:
        data = json.load(json_file)

    event = KbEvent.from_dict(data)

    assert event.type == EventType.WALLET
    assert event.source == Source.PAYMENT_STATUS
    assert event.notification.summary.amount_description == "1 XLM"
    assert (
        event.notification.summary.status_description
        == stellar1.PaymentStatusStrings.PENDING.value
    )


def test_chat_conv(fixture_path):
    with open(f"{fixture_path}/chat_conv.json") as json_file:
        data = json.load(json_file)

    event = KbEvent.from_dict(data)
    print(event)
    assert event.type == EventType.CHAT_CONV
    assert not event.conv.unread
    assert event.conv.creator_info.username == "yourbot"
    channel = event.conv.channel.to_dict()
    assert channel == {
        "name": "yourcompany.marketing",
        "topic_name": "general",
        "members_type": "team",
        "topic_type": "chat",
        "public": None,
    }
