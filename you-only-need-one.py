# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

def check(seq, elem):
    for each in seq:
        if each == elem:
            return True
    return False

test_list = ['a', 1, 2, 3]
print(check(test_list, 'a'))

# BEST
# def check(seq, elem):
#     return elem in seq