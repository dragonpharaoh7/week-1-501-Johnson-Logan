import streamlit as st

from apputil import *


st.write(
'''
# Week x: [Title]

...
''')

# currently set for integer input
amount = st.number_input("Exercise Input: ", 
                         value=None, 
                         step=1, 
                         format="%d")

if amount is not None:
    st.write(f"The exercise input was {amount}.")
    
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
    #Normalize the word
    
    #first convert to lowercase
    
    lower_word = word.lower()
    
    #then remove spaces and strip leading/trailing whitespace
    lower_stripped_word = lower_word.replace(" ", "").strip()
    
    #use regex to remove any non-alphanumeric characters
    normalized_word = re.sub(r'[^a-zA-Z0-9]', '', lower_stripped_word)

    # Check if the normalized word is equal to its reverse
    
    return normalized_word == normalized_word[::-1]


#Test case 1

print(palindrome("racecar"))  # Expected output: True
print(palindrome("Nurses Run"))  # Expected output: True
print(palindrome("Sit on a potato pan, Otis"))  # Expected output: True
print(palindrome("Gibberish"))  # Expected output: False

