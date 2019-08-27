import json
import os
from pathlib import Path

import pytest

from pykeybasebot import (
    ContentType,
    EventType,
    KbEvent,
    PaymentStatusStr,
    Source,
    TeamMention,
)


@pytest.fixture()
def fixture_path():
    app_dir = Path().absolute()
    return os.path.join(app_dir, "tests/fixtures")


def test_teamchat(fixture_path):
    with open(f"{fixture_path}/teamchat.json") as json_file:
        data = json.load(json_file)

    event = KbEvent.from_dict(data)

    assert event.type == EventType.CHAT
    expected_team_mention = TeamMention(name="yourcompany.marketing", channel="general")
    assert event.msg.content.text.teamMentions == [expected_team_mention]
    reply_channel = event.msg.channel.replyable_dict()
    assert reply_channel == {
        "name": "yourcompany.marketing",
        "topic_name": "lunchtalk",
        "members_type": "team",
    }


def test_oneonone(fixture_path):
    with open(f"{fixture_path}/oneonone.json") as json_file:
        data = json.load(json_file)

    event = KbEvent.from_dict(data)

    assert event.type == EventType.CHAT
    assert event.msg.content.text.body == "hi"
    reply_channel = event.msg.channel.replyable_dict()
    assert reply_channel == {"name": "someoneelse,yourbot"}


def test_reaction(fixture_path):
    with open(f"{fixture_path}/reaction.json") as json_file:
        data = json.load(json_file)

    event = KbEvent.from_dict(data)

    assert event.msg.content.type == ContentType.REACTION
    assert event.msg.content.reaction.b == ":sunglasses:"
    reply_channel = event.msg.channel.replyable_dict()
    assert reply_channel == {"name": "someoneelse,yourbot"}


def test_payment(fixture_path):
    with open(f"{fixture_path}/payment.json") as json_file:
        data = json.load(json_file)

    event = KbEvent.from_dict(data)

    assert event.type == EventType.WALLET
    assert event.source == Source.PAYMENT
    assert event.notification.amountDescription == "12.3400000 XLM"
    assert event.notification.statusDescription == PaymentStatusStr.COMPLETED
