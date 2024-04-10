def encode(password):
    encodedpassword = ''
    for i in password:
        i = int(i)
        i +=3
        encodedpassword += str(i)
    return encodedpassword

if __name__ == '__main__':
    userinput = '0'
    encodedpassword = ''
    while userinput != '3':
        print('Menu\n'
        '-------------\n'
        '1. Encode\n'
        '2. Decode\n'
        '3. Quit')
        userinput = input('Please enter an option: ')
        if userinput == '1':
            password = input('Please enter your password to encode:')
            encodedpassword = encode(password)
            print('Your password has been encoded and stored!')
        elif userinput == '2':
            print('The encoded password is',encodedpassword, ', and the original password is')


