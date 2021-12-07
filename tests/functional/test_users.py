def test_get_users(app_client):
    re = app_client.get("api/users")
    print("\nRESPONSE JSON: ", re.json)
    print("RESPONSE STATUS: ", re.status_code)
