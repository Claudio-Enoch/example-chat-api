def test_get_messages(app_client):
    re = app_client.get("api/messages")
    print("\nRESPONSE JSON: ", re.json)
    print("RESPONSE STATUS: ", re.status_code)
    assert re.status_code == 200
