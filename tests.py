import pytest
import Arms

def test_temperature():
    assert Arms.get_temperature() == "38729"