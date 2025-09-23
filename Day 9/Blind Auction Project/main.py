# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import*
print(logo)


def adding_dict(dictionary,dict_name,dict_bid):
    dictionary[dict_name] = dict_bid


def max_items(dictionary):
    max_bid = 0
    max_name = ""
    for items, number in dictionary.items():
        if number > max_bid:
            max_bid = number
            max_name = items
    print(f"The winner is {max_name} with a bid of ${max_bid}")



while True:
    name = input("What is your name?: ")  # Key
    bid = int(input("What is your bid?: $"))  # Value
    my_dict = {}

    adding_dict(my_dict,name,bid)

    new_users = input("Are there any other bidders? Type 'yes or 'no'.")

    if new_users == "yes":
        adding_dict(my_dict,name,bid)
        print("\n" * 50)
    else:
        max_items(my_dict)
        break











