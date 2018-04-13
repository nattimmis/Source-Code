# CA PROJECT 1
userMonth = 0
userDay = 0
status = ""

import os
import pickle
import time
import calendar
import pyodbc

#DATABASE
databaseFile = "userDataCAA"
driver = "{Microsoft Access Driver (*.mdb)}"
connectionString = "DRIVER=" + driver + ";DBQ=" + databaseFile
connection = pyodbc.connect(connectionString, autocommit=True)
cursor = connection.cursor()

#sqlString = "INSERT INTO users (users) values ('TestUser')"
#cursor.execute(sqlString)

#sqlString = "SELECT * FROM users"
#cursor.execute(sqlString)
#print(list(cursor))

# Display welcome message

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
import time
print("Current Date and Time: ")
print(time.strftime("%d/%m/%y"))
print(time.strftime("%I:%M"))

day = time.strftime("%d")
month = time.strftime("%m")
year = time.strftime("%y")



def userMonth():
    global monthInput
    monthInput = int(input("Enter a month: "))
    while True:
        if monthInput >= int(month) and monthInput < 13:
            break
        print("Please choose a correct month")
        monthInput = int(input("Enter a month: "))
    return monthInput



def userDay():
    global dayInput
    dayInput = int(input("Enter a day: "))
    while True:
        if dayInput >= int(day) and dayInput < 32:
            break
        else:
            dayInput = int(input("Enter a day: "))
    return dayInput

def userRoom():
    global roomInput
    roomInput = int(input("Enter a room number (0-10): "))
    while True:
        if roomInput >= 0 and roomInput <= 10:
            break
        else:
            roomInput = int(input("Enter a room number (0-10): "))
    return roomInput
    #print("not done")

#main()


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

    sqlString = "SELECT * FROM users WHERE users.username = '%s'"% loginName
    print(cursor.execute(sqlString))

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
    if userFirstMenu() == True: break
    pickle.dump(users, open("CANamesX.p", "wb"))


def HotelInfo():
    print("")
    print("Bates Motel, developed by James Richardson. 2017")
    print("")
    print("******************************************************")
    # goBack()




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
                                "4. Display Hotel Rooms, "
                                "5. Display your current bookings: "))

        if mainMenuSub == "1":
            HotelInfo()
            break
        elif mainMenuSub == "2":
            selectedMonth = userMonth()
            selectedDay = userDay()
            selectedRoom = userRoom()
            break
        elif mainMenuSub == "3":
            exit()
        elif mainMenuSub == "4":
            print("unfinished")
        elif mainMenuSub == "5":
            print("unfinished")
        else:
            print("Please select a number presented on screen: ")


MainMenu()

def checker():
    for booking in list(cursor):
        if booking[2] == int(monthInput):
            if booking[3] == int(dayInput):
                if booking[4] == int(roomInput):
                    print(booking)
                    print("This room is already booked ")
                    return False
    return True


sqlString = "SELECT * FROM bookings"
cursor.execute(sqlString)
#print(list(cursor))

if checker() == True:
    sqlString = "INSERT INTO bookings (month, day, room) values ("+str(monthInput)+","+str(dayInput)+","+str(roomInput)+") "
    cursor.execute(sqlString)

#sqlString = "Select * from bookings "
#sqlString = "INSERT INTO bookings (bookings) values ('Mr Morrey')"
#cursor.execute(sqlString)
#print(list(cursor))

