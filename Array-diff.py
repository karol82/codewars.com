# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b keeping their order.
#
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]


def array_diff(a, b):
    print(a, b)
    copy = []
    if not b:       # jeżeli puste
        return a
    for i in a:
        print(copy, i)
        if i not in b:
            copy.append(i)
    return copy


print(array_diff([1,2,2,2,3],[1, 2]))