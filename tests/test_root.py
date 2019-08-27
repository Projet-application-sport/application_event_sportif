def test_root_path(client):
    reponse = client.get('/', data=None, headers=None)
    # a = 1
    # b = 0

    # assert a == b
    # assert 1 == 0

    assert reponse.status_code == 200
    # assert reponse.body.content.match(regexp)

