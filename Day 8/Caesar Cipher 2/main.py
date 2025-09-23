alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.


def decrypt(orginal_text, shifted_text):
    result = ""
    for letter in orginal_text:
        shifted_progress = alphabet.index(letter) - shifted_text
        shifted_progress %= len(alphabet)
        result += alphabet[shifted_progress]
    print(f"decryped text is {result}")

def encrypt(orginal_text, shifted_amount):
    result = ""
    for letter in orginal_text:
        shifted_progress = alphabet.index(letter) + shifted_amount
        shifted_progress %= len(alphabet)
        result += alphabet[shifted_progress]

    print(f"encrpt text is {result}")



# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(direction_text):
    if direction == "encode":
        encrypt(text,shift)
    else:
        decrypt(text, shift)

caesar(direction)


