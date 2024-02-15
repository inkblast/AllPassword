import db
import string
import random
import db
def generatePassword():
    psw_length = 8 #int(input("Enter the password length you want(8-15): "))

    symbols =list(string.punctuation)
    numbers =list(string.digits)
    sim_char =list(string.ascii_lowercase)
    cap_char = list(string.ascii_uppercase)


    characters = [symbols,numbers,sim_char,cap_char]

    gen_pass = ""

    char_count = [0,0,0,0]

    for i in range(psw_length):
        character = random.choice(random.choice(characters))

        gen_pass += character

        if ( character in symbols):
            char_count[0] += 1
        elif (character in numbers):
            char_count[1] += 1

        elif (character in sim_char):
            char_count[2] += 1
        elif (character in cap_char):
            char_count[3] += 1
        #print(gen_pass)

    '''print(char_count)
    if (0 in char_count):
        generatePassword()


    else:'''
    return gen_pass

def CreatePassword():
    print("1.add your own password.\n2.generate new password.")
    choice = int(input("Enter your choice"))

    if choice ==1:
        new_password = input("Enter new password:")

    else:
        new_password = generatePassword()
        print(f"your password is {new_password}")


    email = input("please provide email: ")
    username = input("please provide username: ")
    url =  input("please provide url:")
    appname = input("please provide appname: ")


    db.insertToDb(new_password,email,username,url,appname)

def showDetails(email):
    db.selectFromDb(2,email)

def showPassword(appname):
    db.selectFromDb(3,appname)