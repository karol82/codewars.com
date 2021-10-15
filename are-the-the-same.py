# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same"
# elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
#
# Examples
# Valid arrays
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361
# the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

def comp(*args):
    array1 = args[0]
    if len(args) < 2 or type(args[1]) == 'NoneType':
        return False
    array2 = args[1]
    print(array1)
    print(array2)
    array1 = [_ * _ for _ in array1]
    array1.sort()
    array2.sort()
    if array1 == array2:
        return True
    else:
        return False



# print(comp([2, 3, 4], [16, 4, 9]))
print(comp([]))