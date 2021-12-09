def test_get_users(app_client):
    re = app_client.get("api/users")
    assert re.status_code == 200
    assert re.json == [
        {"id": 1, "username": "DefaultUser"},
        {"id": 2, "username": "OutdatedMessages"},
        {"id": 3, "username": "OnlyRecipient"},
        {"id": 4, "username": "OnlyAuthor"},
        {"id": 5, "username": "NoMessagesReceived"},
        {"id": 6, "username": "150MessagesReceived"},
    ]


def test_post_user(app_client):
    data = {"username": "NewUser"}
    re = app_client.post("api/users", json=data)
    assert re.status_code == 201
    assert re.json["username"] == "NewUser"
    assert re.json["id"]


def test_post_duplicate_user(app_client):
    data = {"username": "NewUser"}
    app_client.post("api/users", json=data)
    re = app_client.post("api/users", json=data)
    assert re.status_code == 400
    assert re.json["message"] == "duplicate_error"


def test_post_users_invalid_param(app_client):
    data = {"INVALID_PARAM": "NewUser"}
    re = app_client.post("api/users", json=data)
    assert re.status_code == 400
    assert re.json["message"] == "validation_error"


def test_post_users_missing_param(app_client):
    data = {}
    re = app_client.post("api/users", json=data)
    assert re.status_code == 400
    assert re.json["message"] == "validation_error"


def test_get_user(app_client):
    re = app_client.get("api/users/1")
    assert re.status_code == 200
    assert re.json == {"id": 1, "username": "DefaultUser"}


def test_get_user_invalid_user_id(app_client):
    re = app_client.get("api/users/999")
    assert re.status_code == 404
    assert re.json["message"] == "resource_not_found"


def test_get_user_malformed_user_id(app_client):
    re = app_client.get("api/users/BAD_ID")
    assert re.status_code == 404
    assert not re.json
