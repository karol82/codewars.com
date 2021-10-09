# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

list0 = []
list1 = ["Peter"]
list2 = ["Jacob", "Alex"]
list3 = ["Max", "John", "Mark"]
list4 = ["Alex", "Jacob", "Mark", "Max"]


def likes(names):
    lenght = len(names)

    # result = 0 if lenght == 0 else 0

    if lenght == 0:
        result = "no one likes this"
    elif lenght == 1:
        result = f"{names[0]} likes this"
    elif lenght == 2:
        result = f"{names[0]} and {names[1]} like this"
    elif lenght == 3:
        result = f"{names[0]}, {names[1]} and {names[2]} like this"
    elif lenght >= 4:
        result = f"{names[0]}, {names[1]} and {lenght - 2} others like this"
    return result


print(likes(list0))
print(likes(list1))
print(likes(list2))
print(likes(list3))
print(likes(list4))
