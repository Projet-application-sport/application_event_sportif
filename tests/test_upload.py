def test_upload(client):
    import json
    from flask import url_for

    #mimetype = 'application/json'
                

    # import pdb ; pdb.set_trace()
    response = client.get('/chat')
    #print(response)

    assert response.status_code == 500
    
