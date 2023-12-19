alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(start_text, shift_amount, code_direction):
    end_text = ""
    # Change shift based on direction
    if code_direction == "decode":
        shift_amount *= -1
    # Loop start text
    for character in start_text:

        # Check for alpha
        if character.isalpha():
            position = alphabet.index(character)

            # shift index by shift number
            new_position = position + shift_amount
            if new_position > 25:
                new_position -= 26
            elif new_position < 0:
                new_position += 26

            # use new index to append  letter in end_text
            end_text += alphabet[new_position]

        # append non alpha to end_text
        else:
            end_text += character

    print(end_text)


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, code_direction=direction)