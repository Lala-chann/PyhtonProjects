def ordering_pizza(order,pepperoni,extra_cheese):
    order_fee = 0
    if order == "s":
        order_fee += 15
    elif order == "m":
        order_fee += 20
    elif order == "l":
        order_fee += 25
    else:
        return 0

    if pepperoni == "y":
        if order == "s":
            order_fee +=2
        else:
            order_fee += 3

    if extra_cheese == "y":
        order_fee += 1

    return order_fee





asking_order = input("How would like to get order size: ")
pepperoni = input("Would you like to add pepperoni: ")
extra_cheese = input("Would you like to add extra_cheese: ")
bill = ordering_pizza(asking_order,pepperoni,extra_cheese)

print(f"Your bill is ${bill}")










