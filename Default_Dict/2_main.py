from collections import defaultdict
from timeit import timeit

animals = [('cat', 1), ('rabbit', 2), ('cat', 3), ('dog', 4), ('dog', 1)]
std_dict = dict()
def_dict = defaultdict(list)

def group_with_dict():
    for animal, count in animals:
        std_dict.setdefault(animal, []).append(count)
    return std_dict

def group_with_defaultdict():
    for animal, count in animals:
        def_dict[animal].append(count)
    return def_dict

print(f'dict.setdefault() takes {timeit(group_with_dict)} seconds.')
print(f'defaultdict takes {timeit(group_with_defaultdict)} seconds.')
