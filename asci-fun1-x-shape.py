# You will get an odd integer n (>= 3) and your task is to draw an X. Each line is separated with \n.
#
# Use the following characters: ■ □ For Ruby, Crystal and PHP: whitespace and o
#
# Examples
#
#                                      ■□□□■
#             ■□■                      □■□■□
#   x(3) =>   □■□             x(5) =>  □□■□□
#             ■□■                      □■□■□
#                                      ■□□□■


# -*- coding: utf-8 -*-
def x(n):
    result = ''
    char0 = '□'
    char1 = '■'
    for i in range(n):
        for j in range(n):
            if i == j or n - i == j + 1:
                result = result + ''.join(char1)
            else:
                result = result + ''.join(char0)
        if i + 1 == n:
            pass
        else:
            result = result + '\n'
    return result


print(x(5))