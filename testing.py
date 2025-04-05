"""
CP1404/CP5632 Practical
Testing code using assert and doctest
Started 5/4/2015
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length  # Changed to >= from >


def format_sentence(phrase):
    """
    Format a phrase as a sentence starting with capital and ending with full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this works too!')
    'This works too.'
    """
    if not phrase:
        return ""
    formatted = phrase[0].upper() + phrase[1:]
    formatted = formatted.rstrip('.!?') + '.'  # Clean ending and add stop
    return formatted


def run_tests():
    """Run the tests on the functions."""
    # Fixed repeat_string test
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Test Car initialization
    test_car = Car("Test Car")
    assert test_car._odometer == 0, "Odometer not initialised to 0"

    # Test fuel initialization
    default_fuel_car = Car("Default Fuel Car")
    assert default_fuel_car.fuel == 0, "Default fuel not 0"

    custom_fuel_car = Car("Custom Fuel Car", fuel=10)
    assert custom_fuel_car.fuel == 10, "Fuel not set correctly"


run_tests()
doctest.testmod()