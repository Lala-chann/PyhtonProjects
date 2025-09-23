# TODO-1: Import and print the logo from art.py when the program starts.
from art import*
print(logo)


# TODO-2: What happens if the user enters a number/symbol/space?




# TODO-3: Can you figure out a way to restart the cipher program?
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(orginal_text, shifted_amount):
    result = ""
    for letter in orginal_text:
        if letter in alphabet:
            progress = alphabet.index(letter) + shifted_amount
            progress %= len(alphabet)
            result += alphabet[progress]
        else:
            result += letter

    print(f"Here we go!. {result} is your encode")
    return result

def decode(orginal_text, shifted_amount):
    result = ""
    for letter in orginal_text:
        if letter in alphabet:
            progress = alphabet.index(letter) - shifted_amount
            progress %= len(alphabet)
            result += alphabet[progress]
        else:
            result += letter

    print(f"Here we go! This is your {result} decode")
    return result

def casear(direc,orginal_text,shift):
    if direc == "encode":
        return encode(text,shift)
    else:
        return decode(text,shift)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    result = casear(direction,text,shift)

    restart = input("Do you want to play again: ")
    if restart != "yes":
        break
