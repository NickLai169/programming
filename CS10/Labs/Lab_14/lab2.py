# Exercise 1
def push_first_odd_back(lst):
    for i in range(len(lst)):
        if lst[i]%2 != 0:
            lst.append(lst.pop(i))
            return

# Exercise 2
def flatten(lst):
    new_lst = []
    for i in lst:
        new_lst += i
    return new_lst

# Exercise 3.1
def squares_of_evens(lst):
    return [i**2 for i in lst if i%2 == 0]

# Exercise 3.2
def nth_power_of_evens(lst, n):
    return [i**n for i in lst if i%2 == 0]

# Exercise 4
def substitute_base(string, old, new):
    def tr_substitue_base(char):
        if char == old:
            return new
        else:
            return char
    return ''.join([tr_substitue_base(i) for i in string])

# Exercise 5
def combine(lst):
    if len(lst) == []:
        return lst
    else:
        return lst[0] + combine(lst[1:])

# Exercise 6
def base_freq(string):
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

# Exercise 7.1
def substitute_chars(string, replacements):
    new_str = ''
    for i in string:
        if i in replacements:
            new_str += replacements[i]
        else:
            new_str += i
    return new_str

# Exercise 7.2
def invert_dict(original):
    new_dict = {}
    for i in original:
        new_dict[original[i]] = i
    return new_dict
