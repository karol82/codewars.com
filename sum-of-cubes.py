def sum_cubes(n):
    suma = 0
    for i in range(n):
        suma += (i+1)**3
    return suma

print(sum_cubes(4))



# BEST
# def sum_cubes(n):
#     return sum(i**3 for i in range(0,n+1))