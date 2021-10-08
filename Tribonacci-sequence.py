# test = ([1, 2, 3], 10) # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
# test = ([0.5, 0.5, 0.5], 30)
# test = ([300, 200, 100], 0)
test = ([14, 13, 1], 2)

def tribonacci(signature, n):
    print(signature, n)
    i = 3
    while i < 10:
        signature.append(signature[i-3] + signature [i-2] + signature[i-1])
        i += 1
    if n == 0:
        return []
    elif n <= 3:
        return signature[:n]
    else:
        return signature
print(tribonacci(test[0], test[1]))

