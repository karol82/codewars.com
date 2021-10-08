def solution(number):
    sum = 0
    if number < 0: return 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# ujemne = zeruj

print(solution(0))

#
# BEST
# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)