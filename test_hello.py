from application import app


def test_hello():
    response = app.test_client().get('/')
    print('*** Response from unit test: {}'.format(response))

    assert response.status_code == 200
    assert response.data == b'This is Devops Assignment - Bits Pilani! by Group 64"'

def test_1():
    pass

def test_2():
    pass

def test_3():
    pass

def test_4():
    pass

def test_5():
    pass

def test_ashiq():
    pass

def test_pardeep():
    pass

def test_demo():
    pass


