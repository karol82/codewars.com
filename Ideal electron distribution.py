# You are a khmmadkhm scientist and you decided to play with electron distribution among atom's shells. You know that
# basic idea of electron distribution is that electrons should fill a shell untill it's holding the maximum number of
# electrons.
# test.assert_equals(atomic_number(1),[1])
# test.assert_equals(atomic_number(10),[2, 8])
# test.assert_equals(atomic_number(11),[2, 8, 1])
# test.assert_equals(atomic_number(22),[2, 8, 12])
# test.assert_equals(atomic_number(23),[2, 8, 13])
# test.assert_equals(atomic_number(47),[2, 8, 18, 19])
# test.assert_equals(atomic_number(50),[2, 8, 18, 22])
# test.assert_equals(atomic_number(52),[2, 8, 18, 24])
# test.assert_equals(atomic_number(60),[2, 8, 18, 32])
# test.assert_equals(atomic_number(61),[2, 8, 18, 32, 1])
# 3rd shield is 2*3^2 = 18.

def atomic_number(electrons):
    list_of_results = []
    if electrons == 1: return [1]
    for i in range(1, electrons):
        definition = 2 * i ** 2

        if sum(list_of_results) + definition < electrons:

            list_of_results.append(definition)
            continue
        else:
            list_of_results.append(electrons-sum(list_of_results))
            break

    return list_of_results


print(atomic_number(61))