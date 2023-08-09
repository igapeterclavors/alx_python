"""
    Write a function that returns a tuple with the length of a string and its first character.
    Create afunction multiple_returns(sentence) with string sentance

    Declare variable first_character

    return:
        Length of sentance
        first_character
"""


def multiple_returns(sentence):
    if len(sentence) == 0:
        first_character  = None
    else:
        first_character  = sentence[0]
    return len(sentence), first_character 


# sentence = "At Holberton school, I learnt C!"
# length, first = multiple_returns(sentence)
# print("Length: {:d} - First character: {}".format(length, first))

