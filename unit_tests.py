import Arms

def test_correct_temperature():
    assert (15 <= Arms.get_temperature() <= 55) is True

def test_incorrect_temperature():
    assert (Arms.get_temperature() <= 0) is False

