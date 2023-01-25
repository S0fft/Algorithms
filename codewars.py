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
    result = []

    for index in range(0, len(my_list), 2):
        result.append(my_list[index])
    return result


remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep", "Remove", "Keep"])


def remove_every_other(my_list):
    return my_list[::2]


remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep", "Remove", "Keep"])


def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


sum_array([1, 2, 3, 4, 5, 6, 7])


def task(a, b):

    if a == b:
        return "{0} ({1} since both are same)".format(a, a)
    elif a < b:
        number = 0
        string = ""
        for i in range(a, b+1):
            number += i
            string += str(i) + " + "
        return "{0} ({1}= {2})".format(number, string[:-2], number)
    else:
        number = 0
        string = ""
        for i in range(b, a+1):
            number += i
            string += str(i) + " + "
        return "{0} ({1}= {2})".format(number, string[:-2], number)


task(1, 2)


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
