# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

def validBraces(string):
    dlugosc = len(string)
    for i in range(dlugosc):
        string = string.replace('()', '')
        string = string.replace('[]', '')
        string = string.replace('{}', '')
        # print(i, string)
    if len(string) > 0:
        return False
    else:
        return True


print(validBraces("([{}])"))

# BEST
# def validBraces(s):
#   while '{}' in s or '()' in s or '[]' in s:
#       s=s.replace('{}','')
#       s=s.replace('[]','')
#       s=s.replace('()','')
#   return s==''