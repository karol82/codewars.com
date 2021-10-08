
def alphabet_position(text):
    alphabet = {}
    wynik = ''
    for i in range(26):
        alphabet[chr(i+97)] = i+1
    print(alphabet)
    list_of_strings = list(text.lower())
    for each in list_of_strings:
        if each in alphabet:
            wynik += str(alphabet[each]) + ' '
    return print(wynik.strip())

alphabet_position("YXiBYvGQsMJiCeSrooixlZAsiRJEtCdbJDnbEbVsamrcZCFrAUJsHbgIFLcGsgAEQEeNJuiyZiCfAXQuWybHoQZVhTtuwnrxuHQt")