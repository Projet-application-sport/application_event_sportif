def test_upload(client):
 import json

 mimetype = 'application/json'
 headers = {
             'Content-Type': mimetype,
                                        'Accept': mimetype
                                            }
     data = {
                                    'msg': "Hello !",
                                            "author": "Glenn"
                                                }
                        url = '/chat'

                            # import pdb ; pdb.set_trace()
                                response = client.post(url, data=json.dumps(data), headers=headers)

                                    print(response)

                                        assert response.content_type == mimetype
                                            assert response.json['status'] == 'success'
