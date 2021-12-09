import pytest


def test_get_messages_to_recipient(app_client):
    re = app_client.get("api/messages?recipient_id=3")
    assert re.status_code == 200
    assert len(re.json) == 2
    for message in re.json:
        assert all(
            (message["id"], message["author_id"], message["recipient_id"], message["content"], message["created_date"])
        )


def test_get_messages_none_found(app_client):
    re = app_client.get("api/messages?recipient_id=5")
    assert re.status_code == 200
    assert re.json == []


def test_get_messages_150_found(app_client):
    re = app_client.get("api/messages?recipient_id=6&page=1")
    assert re.status_code == 200
    assert len(re.json) == 100
    re = app_client.get("api/messages?recipient_id=6&page=2")
    assert re.status_code == 200
    assert len(re.json) == 50


def test_get_messages_over_35_days_old(app_client):
    re = app_client.get("api/messages?recipient_id=2")
    assert re.status_code == 200
    assert re.json == []


def test_get_messages_to_recipient_from_author(app_client):
    re = app_client.get("api/messages?recipient_id=1&author_id=4")
    assert re.status_code == 200
    assert len(re.json) == 1


@pytest.mark.parametrize(
    "param, error",
    [
        ("?NO_RECIPIENT=1", "recipient_id Missing required parameter"),
        ("?recipient_id=INVALID", "recipient_id invalid literal for int"),
        ("?recipient_id=1&author_id=INVALID", "author_id invalid literal for int"),
    ],
)
def test_get_messages_invalid_param(app_client, param, error):
    re = app_client.get(f"api/messages{param}")
    assert re.status_code == 400
    assert error in str(list(re.json["errors"].values())[0])
    assert re.json["message"] == "Input payload validation failed"


def test_post_message(app_client):
    data = {"recipient_id": 1, "author_id": 1, "content": "lorem ipsum"}
    re = app_client.post("api/messages", json=data)
    assert re.status_code == 201
    for key, value in data.items():
        assert value == re.json[key]


@pytest.mark.parametrize(
    "override, error",
    [
        ({"recipient_id": 1, "content": "lorem ipsum"}, "validation_error"),
        ({"author_id": 1, "content": "lorem ipsum"}, "validation_error"),
        ({"author_id": 1, "recipient_id": 1}, "validation_error"),
    ],
)
def test_post_message_malformed_request(app_client, override, error):
    data = {"author_id": 1, "content": "lorem ipsum"}
    re = app_client.post("api/messages", json=data)
    assert re.status_code == 400
    assert re.json["message"] == error


@pytest.mark.parametrize(
    "override, error", [({"recipient_id": 999}, "resource_not_found"), ({"author_id": 999}, "resource_not_found")]
)
def test_post_message_invalid_param(app_client, override, error):
    data = {"recipient_id": 1, "author_id": 1, "content": "lorem ipsum"}
    data.update(override)
    re = app_client.post("api/messages", json=data)
    assert re.status_code == 404
    assert re.json["message"] == error
