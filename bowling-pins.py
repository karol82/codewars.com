# Did you ever play Bowling? Short: You have to throw a bowl into 10 Pins arranged like this:
#
#
# I I I I  # each Pin has a Number:    7 8 9 10
#  I I I                                4 5 6
#   I I                                  2 3
#    I                                    1
#
# You will get an Array with Numbers, e.g.: [3,5,9] and remove them from the field like this:
#
#
# I I   I
#  I   I
#   I
#    I


def bowling_pins(arr):
    answer = ''
    for i in range(1,11):
        if i == 1:
            answer += '   ' + i + '   '
        elif 1 < i > 4:
            answer =
    print(answer)


print(bowling_pins([2,3]))
print("I I I  \n I I I \n    I  \n       ")