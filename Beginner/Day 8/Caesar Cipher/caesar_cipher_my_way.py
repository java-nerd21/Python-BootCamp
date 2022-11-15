from art import logo
print(logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(cipher_direction, start_text, shift):

    length_alphabet = len(alphabet)

    if(cipher_direction == "decode"):
        shift *= -1

    end_text = ""
    
    for letter in start_text:

        if letter not in alphabet:
            end_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position > length_alphabet - 1:
                new_position = new_position - length_alphabet
                end_text += alphabet[new_position]
            else:
                end_text += alphabet[new_position]

    print(f"The {cipher_direction}d text is {end_text}")


start_or_stop = "yes"

while(start_or_stop == "yes"):

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text_input = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    shift_amount = shift_amount % 26

    caesar(cipher_direction=direction,start_text=text_input,shift=shift_amount)

    start_or_stop = input("Do you want to restart cipher program? type 'yes' if you want to go again, otherwise type 'no'.\n")

print("Good Bye")



