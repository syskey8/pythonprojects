import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

print(art.logo)
def caesar(direction, original_text, shift_amount):
    new_text = ""
    if direction == "encode":
        new_text = ""
        for i in range(0, len(original_text)):
            if original_text[i] not in alphabet:
                new_text += original_text[i]
                continue
            if original_text[i] == " ":
                new_text += " "
            ogindex = alphabet.index(original_text[i])
            ogindex += shift_amount
            new_text += alphabet[ogindex]
        print(new_text)    
    elif direction == "decode":
        new_text = ""
        for i in range(0, len(original_text)):
            if original_text[i] not in alphabet:
                continue
            if original_text[i] == " ":
                new_text += " "
            ogindex = alphabet.index(original_text[i])
            ogindex -= shift_amount
            new_text += alphabet[ogindex]
        print(new_text)
    else:
        print("Wrong input")

while (True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number [0-25]:\n"))

    caesar(direction, text, shift)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if choice == "yes":
        continue
    else:
        break
