from collections import defaultdict

base = {0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"}

mult_10 = {1: "ten", 2: "twenty", 3: "thirty", 4: "fourty",
           5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
           9: "ninety"}

teens = {10:"ten", 11: "eleven", 12:"twelve", 13:"thirteen",
         14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",
         18:"eighteen", 19:"nineteen"}

# 0 = 1s place, 1: 10s place, 2: hund place, 3: thousands place
power = {0: defaultdict(lambda:""),
         1: {},
         2: {},
         3: defaultdict(lambda:"thousand")}


def to_english(value):
    """
    Input: An integer value between 1 and 1000
    Output: The english version of the number
    """
    english = ""

    # if it contains a thousands place
    if value // 1000 > 0:
        english = english + f"{base[value // 1000]}thousand"
        value = value - (1000 * (value // 1000))

    # contains 100s
    if value // 100 != 0:
        english = english + f"{base[value // 100]}hundred"
        value = value - (100 * (value // 100))

    # if last two digits need "and"
    if value != 0:
        if len(english) > 0:
            english += f"and"
    else:
        return english

    if value >= 20:
        english += f"{mult_10[value // 10]}{base[value % 10]}"
    elif value >= 10:
        english += f"{teens[value]}"
    else:
        english += f"{base[value]}"

    return english

def pv(value):
    print(to_english(value))

# ones
for i in range(11):
    pv(i)

# teens
for i in range(10,20):
    pv(i)

# less that 100

count = 0
for i in range(1001):
    count += len(to_english(i))
