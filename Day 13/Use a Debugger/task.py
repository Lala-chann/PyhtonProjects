import random
import maths


def mutate(a_list):
    b_list = []
    for items in a_list:
        new_items = (items * 2) + random.randint(1,3)
        b_list.append(new_items)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
