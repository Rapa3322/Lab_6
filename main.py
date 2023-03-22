def encode_password(password):
    """Encodes password by having the digit being shifted up by 3 numbers"""

    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode_password(encoded_password):
    """Encodes password by having the digit being shifted down by 3 numbers"""

    password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        password += decoded_digit
    return password


def main_menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")


def main():
    global decode, encode
    while True:
        main_menu()

        option = int(input("Please enter an option: "))

        if option == 1:
            code = input("Please enter your password to encode: ")
            decode = encode_password(code)
            encode = decode_password(decode)

            print("Your password has been encoded and stored!\n")

        if option == 2:
            print(f"The encoded password is {decode}, and the original password is {encode}.")

        if option == 3:
            break

if __name__ == "__main__":
    main()
