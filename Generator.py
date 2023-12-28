from Number import replacewithnumber
from Special import specialcharacter
from Upper import replacewithuppercaseletter
import random

def generatePassword(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = [] 

    for i in pwlength:
        
        password = "" 
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        
        password = replacewithnumber(password)
        password = replacewithuppercaseletter(password)
        password = specialcharacter(password)
        passwords.append(password) 
    
    return passwords

def main():
    
    numPasswords = int(input("How many passwords do you want to generate? "))
    
    print("Generating " +str(numPasswords)+" passwords")
    
    passwordLengths = []

    print("Minimum length of password should be 5")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length<5:
            length = 5
        passwordLengths.append(length)
    
    
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Password #"+str(i+1)+" = " + Password[i])



main()