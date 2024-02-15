import db
import functions
import hashpass

choise = None
def display():
    print("======AllPasswords======")
    print("*** Main Menu ***")
    print("1.Create New Password\n2.Find all sites and apps connected to email\n3.Find password for site of app\nQ.Exit")

def MainMenu():
    global choise
    display()
    choise = input("Enter your choice: ")

    if(choise=='1'):
        functions.CreatePassword()
    elif(choise=='2'):
        email = input("Please provide the email: ")
        functions.showDetails(email)
    elif(choise=='3'):
        appname = input("Please provide the app name: ")
        functions.showPassword(appname)

    elif(choise=='Q'):
        exit()




if __name__ == '__main__':
    yn = input("do you already have an account(y/n): ")

    if(yn=='y'):
        key = input("Enter your super key: ")

        hashedkey = hashpass.hashPass(key)

        if(db.checkKey(hashedkey.hexdigest())):
            print('ok')
            while(choise !='Q'):
                MainMenu()

        else:
            key = input("Enter your super key: ")

    else:
        setKey = input("please provide key: ")
        db.insertKey(setKey)
        key = input("Enter your super key: ")
