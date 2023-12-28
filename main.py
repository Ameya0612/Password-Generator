from Generator import generatePassword
def main():
    numPassword = int(input("How many passwords you want Generate? "))
    print("Generating" +str(numPassword)+ 'Passwords')

    passwordLength = []
    print("Minimum password legth should be 3")

    for i in range(passwordLength):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length < 3:
            length = 3
            passwordLength.append(length)

    password = generatePassword(passwordLength)

    for i in range(numPassword):
        print('Password #'+str(i+1)+" = "+ password+[i])