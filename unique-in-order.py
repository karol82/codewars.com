def unique_in_order(iterable):
    iterable = list(iterable)
    print(iterable)
    wynik = []
    for i, each in enumerate(iterable):
        if iterable[i] != iterable[i-1]:
            wynik.append(iterable[i])
        elif i == 0:
            wynik.append(iterable[i])
    return(wynik)




print(unique_in_order(['A', 'A']))