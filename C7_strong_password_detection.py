"""
Program that uses regular expressions to make sure the password string it is passed is strong.

A strong password is defined as one that is at least eight characters long,
contains both uppercase and lowercase characters,
and has at least one digit.

"""

import re


def is_strong(password):
    """
    Function that uses regular expressions to make sure the password string it is passed is strong.

    :param password: The password that should be checked
    :return: True is password is strong, False otherwise
    """
    # at least eight characters long
    if len(password) < 8:
        return False

    # contains both uppercase and lowercase characters
    upper = re.compile(r"[A-Z]")
    up = upper.search(password)
    lower = re.compile(r"[a-z]")
    low = lower.search(password)

    # has at least one digit
    digit = re.compile(r'[0-9]')
    dig = digit.search(password)

    if up is None or low is None or dig is None:
        return False

    return True


print("Give a password: ")
password = input()
print("This password is strong: ")
print(is_strong(password))
