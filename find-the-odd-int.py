# seq = [1,2,2,3,3,3,4,3,3,3,2,2,1]
seq = [0,1,0,1,0]

def find_it(seq):

    for each in seq:
        how_many_times = 0
        for i in seq:
            if each == i:
                how_many_times += 1
        if how_many_times % 2 == 1:
            return each
    return None


print(find_it(seq))
#
# BEST
# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i