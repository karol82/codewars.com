# test.assert_equals(narcissistic(7), True, '7 is narcissistic');
# test.assert_equals(narcissistic(371), True, '371 is narcissistic');
# test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
# test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')

def narcissistic(number):
    how_many_numbers = len(str(number))
    list_of_numbers = list(str(number))
    sum = 0
    for each in list_of_numbers:
        sum += int(each) ** int(how_many_numbers)
    return number == sum

print(narcissistic(153))

#
# BEST
# def narcissistic(value):
#     return value == sum(int(x) ** len(str(value)) for x in str(value))