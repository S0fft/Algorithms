import math


def maskify(cc):
    if cc == "":
        return ""
    elif len(cc) < 4:
        return cc
    cc = str(cc)

    result = ""
    for num in str(cc[:-4]):
        result += "#"
    return result + cc[len(result):]


maskify("64607935616")


def remove_every_other(my_list):
    return my_list[::2]


remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep", "Remove", "Keep"])


def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


sum_array([1, 2, 3, 4, 5, 6, 7])


# -----------------------------------------------------------------------


def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]


sum_two_smallest_numbers([19, 5, 42, 2, 77])


def reverse_seq(n):
    m = 0
    list_n = [n]
    for i in range(n):
        m += 1
        list_n.append(n - m)
        i = i-1
    return list_n[:-1]


reverse_seq(5)


def quarter_of(month):
    for n in range(1, 3 + 1):
        if n == month:
            return 1
    for n in range(4, 6 + 1):
        if n == month:
            return 2
    for n in range(7, 9 + 1):
        if n == month:
            return 3
    for n in range(10, 12 + 1):
        if n == month:
            return 4


quarter_of(4)


def min_max(lst):
    return [min(lst), max(lst)]


min_max([1, 2, 3, 4, 5])


def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2


basic_op("-", 15, 18)


def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "red":
        return "green"
    else:
        return "red"


update_light("green")


def array_diff(a, b):
    for t in range(len(a + b)):
        for n in b:
            for i in a:
                if n == i:
                    a.remove(i)
    return a


array_diff([-17, -15, -18, 8, -9], [1, 17, -3, 5, -16, -17, -4, -15, -17, -6, 4])


def likes(names):
    num_names = len(names)

    if num_names == 0:
        return "no one likes this"
    elif num_names == 1:
        return f"{names[0]} liekes this"
    elif num_names == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_names == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif num_names >= 4:
        return f"{names[0]}, {names[1]} and {num_names - 2} others like this"


likes(["Alex", "Jacob", "Mark", "Max"])


def domain_name(url):
    symbols = ["/", "https", ":", "http", "www", "com"]

    for sym in symbols:
        if sym in url:
            url = url.replace(sym, "")

    dot_index = url.find(".")

    return url[:dot_index]


domain_name("https://github.com/carbonfive/raygun")


def add_binary(a, b):
    return f"{bin(a + b)}"[2:]


add_binary(1, 1)


def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 == 1 or flower1 % 2 == 1 and flower2 % 2 == 0:
        return True

    return False


lovefunc(1, 4)


def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))

    return signature[:n]


tribonacci([1, 1], 10)


def find_smallest_int(arr):
    return min(arr)


find_smallest_int([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0])


def find_average(numbers):
    return sum(numbers) / len(numbers)


find_average([1, 2, 3, 5, 6])


def fake_bin(x):
    result = ""

    for i in x:
        if int(i) >= 5:
            result += "1"
        else:
            result += "0"

    return result


fake_bin("800857237867")


def disemvowel(string):
    chartes = "aeiouAEIOU"

    for char in chartes:
        if char in string:
            string = string.replace(char, "")

    return string


disemvowel("This website is for losers LOL!")


def friend(x):
    result = [elem for elem in x if len(elem) == 4]

    return result


friend(["Ryan", "Kieran", "Mark",])


def set_alarm(employed, vacation):
    if employed is True and vacation is True:
        return False
    elif employed is False and vacation is True:
        return False
    elif employed is False and vacation is False:
        return False
    else:
        return True


set_alarm(True, False)


def find_uniq(arr):
    max_elem = max(arr)
    min_elem = min(arr)
    arr.remove(max_elem)
    arr.remove(min_elem)

    for i in arr:
        if i == max_elem:
            return min_elem

    return max_elem


find_uniq([2, 2, 2, 2, 2, 1])


def sum_array(a):
    return sum(a)


sum_array([1, 5.2, 4, 0, -1])


def descending_order(num):
    num = [int(i) for i in list((str(num)))]
    num.sort(reverse=True)
    num = [str(i) for i in num]
    num = "".join(num)

    return int(num)


descending_order(123456789)


def make_upper_case(s):
    return s.upper()


make_upper_case("big")


def find_short(s):
    s = [len(i) for i in list(s.split(" "))]

    return min(s)


find_short("bitcoin take over the world maybe who knows perhaps")


def feast(beast, dish):
    return beast[-1] == dish[-1] and beast[0] == dish[0]


feast("great blue heron", "garlic naan")


def better_than_average(class_points, your_points):
    return sum(class_points) / len(class_points) < your_points


better_than_average([5, 6, 7, 8, 9], 10)


def abbrev_name(name):
    name = name.split()

    return f"{name[0][0].upper()}.{name[1][0].upper()}"


abbrev_name("Sam Harris")


def to_jaden_case(string):
    string = [leter[0:1].upper() + leter[1:].lower() for leter in string.split()]
    string = " ".join(string)

    return string


to_jaden_case("How can mirrors be real if our eyes aren't real")


def minimum(arr):
    return min(arr)


minimum([1, 2, 3, 4, 5])


def maximum(arr):
    return max(arr)


maximum([1, 2, 3, 4, 5])


def greet(name):
    return f"Hello, {name} how are you doing today?"


greet("Jack")


def no_space(x):
    return x.replace(" ", "")


no_space("Fixed Tests")


def count_by(x, n):
    return [i for i in range(x, n*x+1, x)]


count_by(100, 5)


def century(year):
    return math.ceil(year / 100)


century(1901)


def points(games):
    result = 0

    for s in games:
        s = list(s)
        del s[1]
        s = [int(i) for i in s]
        if s[0] > s[1]:
            result += 3
        elif s[0] == s[1]:
            result += 1

    return result


points(['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4'])


def litres(time):
    return math.floor(time * 0.5)


litres(3)


def get_grade(s1, s2, s3):
    if 90 <= (s1 + s2 + s3) / 3 <= 100:
        return "A"

    if 80 <= (s1 + s2 + s3) / 3 < 90:
        return "B"

    if 70 <= (s1 + s2 + s3) / 3 < 80:
        return "C"

    if 60 <= (s1 + s2 + s3) / 3 < 70:
        return "D"

    return "F"


get_grade(90, 100, 95)


def check(seq, elem):
    return True if elem in seq else False


check([1, 2, 3, 4, 5], 3)


def count_sheeps(sheep):
    return sheep.count(True)


count_sheeps([True, True, True])


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


zero_fuel(100, 50, 1)


def square_sum(numbers):
    return sum([i**2 for i in numbers])


square_sum([1, 2])


def square_digits(num):
    num = [str(int(i)**2) for i in list(str(num))]

    return int("".join(num))


square_digits(9119)


def filter_list(l):
    new = []

    for i in l:
        if type(i) is int:
            new.append(i)

    return new


filter_list([1, 2, 'a', 'b'])


def get_sum(a, b):
    if a > b:
        return sum(list(range(b, a+1)))
    elif a == b:
        return a

    return sum(list(range(a, b+1)))


get_sum(22, 1)


def duplicate_count(text):
    dup_list = []
    lst = []

    for x in text.lower():
        if x not in lst:
            lst.append(x)
        else:
            dup_list.append(x)

    return len(set(dup_list))


duplicate_count("Indivisibilities")


def duplicate_encode(word):
    new_str = ""
    word = word.lower()

    for i in word:
        if word.count(i) > 1:
            new_str += ")"
        else:
            new_str += "("

    return new_str


duplicate_encode("Success")


def check_password(pasw):
    pasw = list(pasw)
    points_list = []

    if len(pasw) >= 6:
        points_list.append(True)
        for i in pasw:
            if i.isupper():
                points_list.append(True)
                if i.islower():
                    points_list.append(True)

    return len(points_list) == 3 and any(i.isdigit() for i in pasw) and "".join(pasw).isalnum()


check_password('fjd3IR9dd')


def tower_builder(n_floors):
    lst = []
    spaces = ""

    for n in range(1, n_floors*2, 2)[::-1]:
        lst.append(spaces + "*" * n)
        spaces += " "

    lst.reverse()

    for e in lst:
        # print(e)
        pass

    return lst


tower_builder(6)


def cakes(recipe, available):
    count = []

    if len(available) < len(recipe):
        return 0

    for recipe_key, recipe_value in recipe.items():
        for available_key, available_value in available.items():
            if recipe_key == available_key:
                if available_value >= recipe_value:
                    if math.floor(available_value / recipe_value) >= 1:
                        count.append(math.floor(available_value / recipe_value))

    return min(count)


cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000})


def is_isogram(string):
    if len(string.lower()) == len(set(string.lower())):
        return True
    else:
        return False


(is_isogram("abA"))
