from application import app


def test_hello():
    response = app.test_client().get('/')
    print('Response from unit test: {}'.format(response))

    assert response.status_code == 200
    assert response.data == b'This is Devops Assignment - Bits Pilani!'

def test1():
    pass

def test2():
    pass

def test3():
    pass
