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
