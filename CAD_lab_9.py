#Chase DuPre'
def encode(password):
    newPassword = ""

    # You can reverse this to decode the password
    encode = {"0":"3","1":"4","2":"5","3":"6","4":"7","5":"8","6":"9","7":"0","8":"1","9":"2"}
    for num in password:
        newPassword += encode[num]
    return newPassword

def decode(password):
    newerPassword = ""
    decode = {"3":"0","4":"1","5":"2","6":"3","7":"4","8":"5","9":"6","0":"7","1":"8","2":"9"}
    for num in password:
        newerPassword += decode[num]
    return newerPassword
def main():
    run = 1

    # This is the password variable
    password = ""

    while run == 1:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = input("Please enter an option: ")
        if choice == "1":
            passencode = input("Please enter your password to encode: ")
            password = encode(passencode)
            print("Your password has been encoded and stored!\n")
        elif choice == "2":
            decodedPass = decode(password)
            print(f"The encoded password is {password}, and the original password is {decodedPass}")
            pass
        elif choice =="3":
            run = 0
if __name__ == "__main__":
    main()