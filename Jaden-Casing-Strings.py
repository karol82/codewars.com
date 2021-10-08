quote = "How can mirrors be real if our eyes aren't real"

def to_jaden_case(quote):
    text = quote
    splited = text.split()
    temp = ''
    for idx, each in enumerate(splited):
        lenght = len(splited)
        temp += each.capitalize()
        if idx != lenght-1:
            temp += ' '

    print(temp)
to_jaden_case(quote)