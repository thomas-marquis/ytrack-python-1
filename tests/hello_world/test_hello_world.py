import main


def test_should_say_hello_world():
    res = main.say_hello()
    assert res == 'Hello World'
