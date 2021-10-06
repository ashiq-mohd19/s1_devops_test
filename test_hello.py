from application import app


def test_hello():
    response = app.test_client().get('/')
    print('Response from test: {}'.format(response))

    assert response.status_code == 200
    assert response.data == b'This is Devops Assignment - Bits Pilani!'
