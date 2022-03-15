# Jesper Lundberg
# TEINF20
# Caesar

def encrypt(text, key):
    """Caesarchifferskryptering
    
    Args:
        text (_str_): Den text som ska krypteras.
        key (_int_): Hur många steg ska vi skifta?
    """

    encrypted = ""
    # loop through the message char by char
    for char in text:
        # check if it's an upper case letter
        if char.isupper():
            char_index = ord(char) - ord('A')

            # shift the current character by key positinos
            char_shifted = (char_index + key) % 26 + ord('A')
            char_new = chr(char_shifted)
            encrypted += char_new

        elif char.islower():
            char_index = ord(char) - ord('a')

            #shift the current character by key positions
            char_shifted = (char_index + key) % 26 + ord('a')
            char_new = chr(char_shifted)
            encrypted += char_new

        elif char.isdigit():
            # if it's a number, shift it's value
            char_new = (int(char)+ key) % 10
            encrypted += str(char_new)

        else:
            # if it's neither a letter or a number, leave as is
            encrypted += char

    return encrypted


def main():

    what_to_do = input("Input or output encrypted message? (i/o):")

    if "i" in what_to_do:
        message = input("Input message to encrypt:")
        encrypted_message = encrypt(message, 1)
        print(f"Message: {message}")
        print(f"Encrypted message with 1 shift: {encrypted_message}")

    elif "o" in what_to_do:
        message = input("Input message to encrypt:")
        decrypted_message = encrypt(message, -1)
        print(f"Message: {message}")
        print(f"Decrypted message with 1 shift: {decrypted_message}")

if __name__ == "__main__":
    main()