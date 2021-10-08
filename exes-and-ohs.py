# test.expect(xo('xo'), 'True expected')
# test.expect(xo('xo0'), 'True expected')
# test.expect(not xo('xxxoo'), 'False expected')

test = 'xoxoxoxoo'

def xo(s):
    x, o = 0, 0
    s = s.lower()
    print(s)
    for each in s:
        if each == 'x':
            x += 1
    for e in s:
        if e == 'o':
            o += 1
    if x == o:
        return True
    else:
        return False


print(xo(test))

# BEST
# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')