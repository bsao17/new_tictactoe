from game_core.game_functions import Messages


def test_messages():
    my_message = Messages("test", "test")
    assert my_message.title == "test"
    assert my_message.message == "test"


