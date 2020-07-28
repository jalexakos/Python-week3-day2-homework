# Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters and empty space characters (“ “), return the length of the last word. Meaning, the word that appears far most to the right if we loop through the words.
# Example Input: “Hello World”
# Example Output: 5
# Example Input 2: “The brown loud cow plowed”
# Example Output 2: 6

# Questions to ask:
#   What EXACTLY do I want to return? Don't overthink, clarify!
#   Should we filter out punctuations? I did this using RegEx
#   Do I need to account for casing?

import re

def length_of_last_word(str1):
    str1 = str1.strip().lower()
    pattern_r = re.compile("[A-Za-z]+")
    str1 = pattern_r.findall(str1)
    return len(str1[-1])

print(length_of_last_word("Hello World"))
print(length_of_last_word("The brown loud cow plowed"))
print(length_of_last_word("CaN you bE SURE that this UNDoUBTEDLY?"))