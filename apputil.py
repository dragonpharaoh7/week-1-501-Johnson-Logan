

# add code below ...

import re


def palindrome(word):
    """
    Check if a word is a palindrome.

    A palindrome is a word that reads the same backward as forward.

    Args:
        word (str): The word to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    # Normalize the word

    # first convert to lowercase

    lower_word = word.lower()

    # then remove spaces and strip leading/trailing whitespace
    lower_stripped_word = lower_word.replace(" ", "").strip()

    # use regex to remove any non-alphanumeric characters
    normalized_word = re.sub(r'[^a-zA-Z0-9]', '', lower_stripped_word)

    # Check if the normalized word is equal to its reverse

    return normalized_word == normalized_word[::-1]


# Test case 1

print(palindrome("racecar"))  # Expected output: True
print(palindrome("Nurses Run"))  # Expected output: True
print(palindrome("Sit on a potato pan, Otis"))  # Expected output: True
print(palindrome("Gibberish"))  # Expected output: False


def parentheses_checker(input_string):
    """
    Check if the parentheses in a string are balanced.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the parentheses are balanced, False otherwise.
    """

    opening_count = 0
    closing_count = 0

    # Rules: ( must be the opening parenthesis (first seen) and ) must
    # be the closing parenthesis (last seen)

    # iterate through the string, tracking the number of opening and
    # closing parentheses
    for char in input_string:
        if char != '(' and char != ')':
            continue  # Ignore non-parenthesis characters
        elif char == '(':
            # Increment the count of opening parentheses
            opening_count += 1
        elif char == ')':
            # Increment the count of closing parentheses
            closing_count += 1

        # If at any point the count of closing parentheses exceeds the
        # count of opening parentheses, return False
        if closing_count > opening_count:
            return False

    # order has been checked, now check if the counts of opening and
    # closing parentheses are equal
    return opening_count == closing_count


# Test Cases
print(parentheses_checker("((blah)()()())"))  # True
print(parentheses_checker("(((())blee))"))  # True
print(parentheses_checker("(()hello((())()))"))  # True
print(parentheses_checker("((((((())"))  # False
print(parentheses_checker("()))"))  # False
