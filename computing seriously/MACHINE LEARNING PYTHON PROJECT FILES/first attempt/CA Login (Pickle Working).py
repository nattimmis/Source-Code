#CA PROJECT 1
roomList = {'Room No.1':[],'2':[]}

status = ""

import os
import pickle
import time
import calendar


#Display welcome message

def main():
    print("******************************************************")
    print("Welcome to Bates Motel booking/reservation system!")
    print("******************************************************")

    def goBack():
        goBackX = input("To go back to the main menu press m: ")
        if goBackX == "m":
            MainMenu()
        else:
            print("Invalid")
            goBack()

    # First Main Menu Function

    users = {}
    ChooseRoomT = 0
main()

def userFirstMenu():
    status = input("Are you a registered user? y/n? Press q to quit: ")
    if status == "y":
        return oldUser()
    elif status == "n":
        return newUser()
    elif status == "q":
        exit()

def newUser():
    loginName = input("Create login name please: ")

    if loginName in users:
        print("\nLogin name already exists!\n")
    else:
        loginPass = input("Create a login password please: ")
        users[loginName] = loginPass
        print("\nUser Created!\n")



users = pickle.load(open("CANamesX.p", 'rb'))
pickle.dump(users, open("CANamesX.p", "wb"))

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
    pickle.dump(users, open("CANamesX.p", "wb"))


def HotelInfo():
    print("")
    print("Bates Motel, developed by James Richardson. 2017")
    print("")
    print("******************************************************")
    #goBack()


def BookRoom():
    room = ChooseRoom()
    month = ChooseMonth()
    day = ChooseDate()
    checkRoom(room,month,day)
    print(checkRoom)

def checkRoom(room, month, day):
    roomList.ChooseRoomT.append()

def ChooseMonth():
    flag = True
    while flag == True:
        try:
            userDateMonth = int(input("Please enter the month as a single figure: "))
            flag = False
        except:
            print("Incorrect, enter a valid figure")

        if userDateMonth > 12:
            print("Incorrect")
            ChooseMonth()
        elif userDateMonth > 0:
            print("******************************************************")
            month = userDateMonth
            return month
        else:
            print("Enter a valid month: ")
            ChooseMonth()

#def the_list():
    #data = ['data1', 'data2', 'data3 ', 'data4', 'data5']
    #for i in data:
        #print(i)
        #print(' would you like to add')
        #a = input()
        #if a == ('yes'):
            #b = input()
            #data.append(b)
            #print(data)
            #the_list()

def ChooseRoom():
    flag = True
    while flag == True:
        try:
            ChooseRoomT = int(input("Please choose a room from 1-9, all rooms are identical: "))
            flag = False
        except:
            print("Incorrect, enter a valid figure")


        if ChooseRoomT > 9:
            print("Incorrect")
            ChooseRoom()
        elif ChooseRoomT > 0:
            print("******************************************************")
            ChooseDate()
        else:
            print("Enter a valid room: ")
            flag = True
    if ChooseRoomT == 1:
        ChooseRoomT = 'Room No.1'

def ChooseDate():
    flag = True
    while flag == True:
        try:
            userDateDay = int(input("Please enter the day of the month as a single figure: "))
            flag = False
        except:
            print("Incorrect, enter a valid figure")


    if userDateDay > 31:
        print("Incorrect")
        ChooseDate()
    elif userDateDay > 0:
        print("******************************************************")
        return userDateDay
        ChooseDate()
    else:
        print("Incorrect: ")
        ChooseDate()

def roomDisplay():
    HOTEL_ROOM = {'Room No.1',
                  'Room No.2',
                  'Room No.3',
                  'Room No.4',
                  'Room No.5'}
    print(HOTEL_ROOM)
    print("")
    print("Fictional Hotel has eight identical rooms on one floor")
    print("")


def MainMenu():
    print("")
    print("Welcome to Bates Motel booking/reservation system! Choose a number displayed for selection")
    print("******************************************************")
    print("Current Date and Time: ")
    print(time.strftime("%d/%m/%y"))
    print(time.strftime("%I:%M"))
    print("******************************************************")
    while True:
        mainMenuSub = str(input("1. Display Hotel Information, "
                            "2. Book a Room,  "
                            "3. Logout and Exit, "
                            "4. Display Hotel Rooms: "))

        if mainMenuSub == "1":
            HotelInfo()
            break
        elif mainMenuSub == "2":
            BookRoom()
            break
            exit()
        elif mainMenuSub == "3":
            exit()
        else:
            print("Please select a number presented on screen: ")
MainMenu()

