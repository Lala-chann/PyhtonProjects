def finding_even_or_odd(num):
    if num % 2 == 0:
        return 1
    else:
        return 0

number = int(input("Enter the number: "))
find_number = finding_even_or_odd(number)
print(find_number)