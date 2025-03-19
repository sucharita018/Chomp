import pytest
import random
import numpy as np
from project import toss, chocolate_change, next_chocolate, display_chocolate
from unittest.mock import patch
import emoji


cookie = emoji.emojize(":cookie:")  #🍪
poison = emoji.emojize(":skull:")   #💀
chocolate = np.full((2, 12), cookie, dtype=object)
chocolate[1, 0] = poison
changed_chocolate = chocolate
changed_chocolate[:1, 5:] = " "

def reset_chocolate():
    chocolate = np.full((2, 12), cookie, dtype=object)
    chocolate[1, 0] = poison
    return chocolate



@pytest.mark.parametrize("input_choice, random_choice, expected", [
    ("h", "h", True),
    ("t", "t", True),
    ("h", "t", False),
    ("t", "h", False),
])

def test_toss(input_choice, random_choice, expected):
    with patch("random.choice", return_value = random_choice):
        assert toss(input_choice) == expected

def test_chocolate_change():
    assert np.array_equal(chocolate_change(0,5), changed_chocolate)

def test_next_chocolate():
    with patch("random.choice", return_value=(0, 5)):
        assert np.array_equal(chocolate_change(0,5), next_chocolate())

chocolate = reset_chocolate()

def test_display_chocolate(capsys):
    display_chocolate(chocolate)
    captured = capsys.readouterr().out.strip()
    expected_output = (
        "🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪\n"
        "💀 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪 🍪"
    )
    print(captured)
    print(expected_output)
    assert captured == expected_output