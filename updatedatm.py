
import random

database = {}

def init():
    print("Welcome to goldbank")

    haveAcc = int(input("Do you have account with us:\n 1:Yes \n 2:No \n"))

    if (haveAcc == 1):
        login()

    elif (haveAcc == 2):
        register()

    else:
        print("You have selected invalid option")

init()
def login():
    print(" Login")
    accountNumberGivenByUser = int(input("What is your account number? \n"))
      password = input("What is   your password \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberGivenByUser:
            if (userDetails[3] == password):
                bankOperation(userDetails)

    print('Invalid account or password')

    login()
def register():
    print("****** Register *******")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generateNewAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account Has been created")
    print("*****************************")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print("**************************")

    login()
def bankOperation(user):
    print("Welcome %s %s " % (user[0]))

    selectedOption = int(input("What would you like to do? \n 1:Deposit \n 2:Withdrawal \n 3:Logout \n 4:Exit \n"))

    if (selectedOption == 1):
        depositOperation()

    elif (selectedOption == 2):
        withdrawalOperation()

    elif (selectedOption == 3):
       transferOperation()

    elif (selectedOption == 4):
        logout()

    else:
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
        amount = float(input("How much would you like to withdrawal? \n")
        print("processing...\n " )
        print('take your cash \n ' )
          print("successful withdrawal of " &amount )
        print("Thank you for using this channel \n")

def depositOperation():
    deposit = float(input("How much would you like to deposit?")
    print(+deposit "Succefully been deposited")
    print("Thank you for using this channel")

def transferOperation():
    amount = float(input("How much would you like to transfer? \n ")
    transferAccount =int(input)("The account you want to transfer to: \n")
    print(+amount"has been successfully transferred to " &transferAccount)
    print("Thank you for using this channel")

def generateNewAccountNumber():
    return random.randrange(1111111111, 9999999999)


def logout():
    login()


#### ACTUAL BANKING SYSTEM #####

init()



