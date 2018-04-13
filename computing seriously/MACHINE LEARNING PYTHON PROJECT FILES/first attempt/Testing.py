import time
print("Current Date and Time: ")
print(time.strftime("%d/%m/%y"))
print(time.strftime("%I:%M"))

day = time.strftime("%d")
month = time.strftime("%m")
year = time.strftime("%y")



def userMonth():
    monthInput = int(input("Enter a month: "))
    while True:
        if monthInput >= int(month) and monthInput < 13:
            break
        print("Please choose a correct month")
        monthInput = int(input("Enter a month: "))
    return monthInput



def userDay():
    dayInput = int(input("Enter a day: "))
    while True:
        if dayInput >= int(day) and dayInput < 32 and int(month) == selectedMonth:
            break
        elif dayInput > 0 and dayInput < 32 and int(month) < selectedMonth:
            break
        else:
            dayInput = int(input("Enter a day: "))
    return dayInput


def userRoom():
    roomInput = int(input("Enter a room between 1 and 8: "))
    while True:
        if roomInput > 0 and roomInput <= 8:
            break
        else:
            roomInput = int(input("Enter a room between 1 and 8: "))
        return roomInput

    #dayInput = int(input("Enter day: "))
    #if m != int(month):
       #selectedDay = dayInput
       #print("Thank you")
    #else:
        #while dayInput < int(day):
            #print("INVALID")
            #dayInput = int(input("Enter day: "))
        #selectedDay = dayInput
        #print("Thank you")

selectedMonth = userMonth()
selectedDay = userDay()
selectedRoom = userRoom()

