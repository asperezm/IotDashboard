import pytest
import app

def test_temperature():
    assert app.get_temperature() == "38729"