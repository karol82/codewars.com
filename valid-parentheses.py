# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
# The function should return true if the string is valid, and false if it's invalid.
#
# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

def valid_parentheses(string):
    print('string przed zmianą: ', string)
    string = [_ if _ == '(' or _ == ')' else '' for _ in str(string)]
    string = ''.join(string)
    print('string po zmianie: ', string)
    while True:
        lenght_before = len(string)
        # print(lenght_before, string)
        string = string.replace('()', '')
        lenght_after = len(string)
        # print(lenght_after, string)
        if lenght_before == lenght_after == 0:
            print('wynik:', string)
            return True
        elif lenght_after == lenght_before:
            print('wynik:', string)
            return False


test = "(())((()())())"
test2 = "   hi(hi)"
print(valid_parentheses(''))