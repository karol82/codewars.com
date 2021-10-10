# Write a function that takes in a string of one or more words, and returns the same string,
# with all five or more letter words reversed (like the name of this kata).
#
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
# Examples:
#
# spinWords("Hey fellow warriors") => "Hey wollef sroirraw"
# spinWords("This is a test") => "This is a test"
# spinWords("This is another test") => "This is rehtona test"

test_string = "Hey fellow warriors"

def spin_words(test_string):
    test_string = test_string.split()
    temp_list = []
    for each in test_string:
        temp_list.append(each[::-1]) if len(each) >= 5 else temp_list.append(each)
    result = ' '.join(temp_list)
    return result

print(spin_words(test_string))