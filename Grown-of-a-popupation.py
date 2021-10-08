# test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
from math import ceil

def nb_year(p0, percent, aug, p):
    print(0, p0, percent, aug, p)
    result = p0 + (p0*percent/100) + aug
    result = round(result)
    print(1, result, (result*percent/100), aug, p)
    years = 1
    while p > result:
        result = round(result)
        result = (result) + (result*percent/100) + aug
        years += 1
        print(years, result, (result*percent/100), aug, p)


    return years


# nb_year(1500, 5, 100, 5000)
# nb_year(1500000, 0.25, 1000, 2000000)
# nb_year(1520000, 0.6, 0, 2000000)
nb_year(1000, 2, 50, 1214)
# nb_year(1500000, 0, 10000 ,2000000)


#  BEST
# def nb_year(p0, percent, aug, p, years = 0):
#     if p0 < p:
#         return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
#     return years