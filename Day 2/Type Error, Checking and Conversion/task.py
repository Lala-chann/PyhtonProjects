#first one
def finding_int(s):
    count = 0
    for number in str(s):
        count += 1
    return count

my_integer = 1234567890
length = finding_int(my_integer)
print(length)
print(type(my_integer))

#second one

length_of_size = len(str(123345))
print(length_of_size)

