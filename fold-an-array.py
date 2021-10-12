# In this kata you have to write a method that folds a given array of integers by the middle x-times.
# An example says more than thousand words:
# Fold 1-times:
# [1,2,3,4,5] -> [6,6,3]
# A little visualization (NOT for the algorithm but for the idea of folding):
#
#  Step 1         Step 2        Step 3       Step 4       Step5
#                      5/           5|         5\
#                     4/            4|          4\
# 1 2 3 4 5      1 2 3/         1 2 3|       1 2 3\       6 6 3
# ----*----      ----*          ----*        ----*        ----*
#
# Fold 2-times:
# [1,2,3,4,5] -> [9,6]
# As you see, if the count of numbers is odd, the middle number will stay. Otherwise the fold-point is between the middle-numbers, so all numbers would be added in a way.
# The array will always contain numbers and will never be null. The parameter runs will always be a positive integer greater than 0 and says how many runs of folding your method has to do.
# If an array with one element is folded, it stays as the same array.
# The input array should not be modified!
# Have fun coding it and please don't forget to vote and rank this kata! :-)
# I have created other katas. Have a look if you like coding and challenges.

def fold_array(array, runs):
    result = []
    print(array, runs)
    for i in range(runs):
        if int(i) > 0:
            array = result
        lenght = int(len(array))
        center = int(len(array) / 2)
        result = []
        for index, each in enumerate(array):
            if index < center:
                result.append(array[index] + array[lenght - index - 1])
            elif index == center and not int(len(array)) % 2 == 0:
                result.append(array[index])
    return result


print(fold_array([-9, 9, -8, 8, 66, 23], 1))
print(fold_array([1,2,3,4,5], 2))
#
# BEST
# def fold_array(array, runs):
#     nums = list(array)
#     for _ in xrange(runs):
#         for a in xrange(len(nums) // 2):
#             nums[a] += nums.pop()
#     return nums