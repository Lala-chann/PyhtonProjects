import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
def random_person(name_list):
    selected = random.choice(name_list)
    return selected

whopays = random_person(friends)
print(f"the person who is paying is {whopays}")
