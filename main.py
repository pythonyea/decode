# James Chau
def encode(password):
    result = ''
    for i in password:
        if i == '7':
            result += '0'
        elif i == '8':
            result += '1'
        elif i == '9':
            result += '2'
        else:
            result += str(int(i) + 3)
    return result

#Decode function by Abdullah Islam
def decode(password):
    encoded_num = ''
    for i in range(8):

        if str(int(password[i])) == '2':
            encoded_num += '9'
        elif str(int(password[i])) == '1':
            encoded_num += '8'
        elif str(int(password[i])) == '0':
            encoded_num += '7'
        else:
            encoded_num += str(int(password[i]) - 3)

    return encoded_num

program = True
while program:
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit\n""")
    option = int(input("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
        password = encode(password)
        print("Your password has been encoded and stored!\n")

    if option == 2:
        try:
            print(f"The encoded password is {password}, and the original password is {decode(password)}.\n")
        except NameError:
            print("No password stored!\n")

    if option == 3:
        exit()