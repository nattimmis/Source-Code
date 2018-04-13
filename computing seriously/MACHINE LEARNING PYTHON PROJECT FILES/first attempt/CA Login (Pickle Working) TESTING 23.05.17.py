#CA PROJECT 1

import os
import pickle

#Display welcome message


print("Welcome to Fictional Hotel booking/reservation system!")
print("******************************************************")

# First Main Menu Function

users = {}
status = ""

def userFirstMenu():
    status = input("Are you a registered user? y/n? Press q to quit: ")
    if status == "y":
        return oldUser()
    elif status == "n":
        return newUser()

def newUser():
    loginName = input("Create login name please: ")

    if loginName in users:
        print("\nLogin name already exists!\n")
    else:
        loginPass = input("Create a login password please: ")
        users[loginName] = loginPass
        print("\nUser Created!\n")



users = pickle.load(open("CANames.p", 'rb'))
#pickle.dump(users, open("CANames.p", "wb"))

def oldUser():
    login = input("Enter your login name please: ")
    password = input("Enter your password please: ")

    if login in users and users[login] == password:
        print("\nLogin Successful!\n")
        return True
    else:
        print("\nIncorrect details.\n")
        return False

while status != "q":
    if userFirstMenu() == True:break
    pickle.dump(users, open("CANames.p", "wb"))


def HotelInfo():
    print("Fictional Hotel, developed by James Richardson. 2017")

def ChooseMonth():
    while True:
        userDateMonth = int(input("Please enter the month as a two digit figure: "))

        if userDateMonth > 12:
            print("Incorrect")
            ChooseDate()
        elif userDateMonth > 0:
            print("******************************************************")
            exit()
        else:
            print("Enter a valid month: ")
            ChooseDate()


def ChooseDate():
    while True:
        userDateDay = int(input("Please enter the day of the month as a two digit figure: "))

        if userDateDay > 31:
            print("Incorrect")
            ChooseDate()
        elif userDateDay > 0:
            ChooseMonth()
        else:
            print("Incorrect: ")
            ChooseDate()

def MainMenu():
    print("Welcome to Fictional Hotel booking/reservation system! Choose a number displayed for selection")
    while True:
        mainMenuSub = str(input("1. Display Hotel Information, "
                            "2. Choose A Date,  "
                            "3. Logout and Exit: "))

        if mainMenuSub == "1":
            HotelInfo()
            break
        elif mainMenuSub == "2":
            ChooseDate()
            break
        elif mainMenuSub == "3":
            exit()
        else:
            print("Please select a number presented on screen: ")
MainMenu()







