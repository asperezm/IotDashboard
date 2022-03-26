import app

def test_correct_temperature():
    temperature = app.get_temperature()[1]
    assert (15 <= temperature <= 55) is True

def test_incorrect_temperature():
    temperature = app.get_temperature()[1]
    assert (temperature <= 0) is False

def test_correct_moisture():
    moisture = app.get_moisture()[1]
    assert (0 <= moisture <= 100) is True

def test_incorrect_moisture():
    moisture = app.get_moisture()[1]
    assert (moisture > 100) is False

def test_correct_humidity(): # %
    humidity = app.get_humidity()[1]
    assert (0 <= humidity <= 100) is True

def test_incorrect_humidity():
    humidity = app.get_humidity()[1]
    assert (humidity > 100) is False

def test_correct_light(): # nm
    light = app.get_light()[1]
    assert (300 <= light <= 1000) is True

def test_incorrect_light():
    light = app.get_light()[1]
    assert (light > 1000) is False