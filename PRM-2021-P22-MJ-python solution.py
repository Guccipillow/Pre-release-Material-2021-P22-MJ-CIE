# ------ TASK 1 ------

# DECLARE index : INTEGER //for FOR loop
UpTime = ["09:00", "11:00", "13:00", "15:00"]  # ARRAY STRING
UpSeats = [480, 480, 480, 480]  # ARRAY INTEGER
UpPassengers = [0, 0, 0, 0]  # ARRAY INTEGER
UpMoneyTotal = [0.0, 0.0, 0.0, 0.0]  # ARRAY REAL

DownTime = ["10:00", "12:00", "14:00", "16:00"]  # ARRAY STRING
DownSeats = [480, 480, 480, 640]  # ARRAY INTEGER
DownPassengers = [0, 0, 0, 0]  # ARRAY INTEGER
DownMoneyTotal = [0.0, 0.0, 0.0, 0.0]  # ARRAY REAL


def ScreenDisplay():  # DECLARING PROCEDURE
    print("\n\t\t>>>>>>>     TRAIN JOURNEY DISPLAY     <<<<<<<\n")
    for index in range(0, 4):
        if UpSeats[index] != 0:
            print(
                "Train No:",
                index,
                "| Train Departure Hour:",
                UpTime[index],
                "\t| Remaining Tickets:",
                UpSeats[index],
            )
        else:
            print(
                "Train No:",
                index,
                "| Train Departure Hour:",
                UpTime[index],
                "| Closed!",
            )

        if DownSeats[index] != 0:
            print(
                "Train No:",
                index,
                "| Train Return Hour:",
                DownTime[index],
                "\t\t| Remaining Tickets:",
                DownSeats[index],
            )
        else:
            print(
                "Train No:", index, "| Train Return Hour:", DownTime[index], "| Closed!"
            )
        print()  # IGNORE
        print("-----------------------\n")  # IGNORE


# ENDPROCEDURE

ScreenDisplay()  # CALL

# ----------- TASK 2 -----------
NumOfPassengers = UpTrip = DownTrip = FreeTickets = 0  # INTEGER
OneWayTicket = 25.0  # CONSTANT
OneWayCost = 0.0  # REAL
# DECLARE num : INTEGER //for FOR loops


print("Do you want to buy ticket? 'True' for yes and 'False' for no")
choice = input()
while choice != "True" and choice != "False":
    choice = input("Enter 'True' for yes and 'False' for no: ")

while choice != "False":
    print("\n-----------------------\n")  # IGNORE
    #
    UpTrip = int(input("Enter Train number corresponding to your departure hour: "))
    while UpTrip not in range(0, 4):
        UpTrip = int(input("Error! Enter train number from (0, 1, 2, 3): "))
    #
    print("\n----- Return Hours Available -----\n")
    for num in range(UpTrip, 4):
        print(
            "Train No:",
            num,
            " | Return Hour:",
            DownTime[num],
            " | Remaining Tickets:",
            DownSeats[num],
        )
    print()  # IGNORE
    DownTrip = int(input("Enter Train number corresponding to your Return hour: "))
    while DownTrip < UpTrip or DownTrip > 3:
        DownTrip = int(input("Error! Enter Train number from the given list above: "))
    #
    print()  # IGNORE
    NumOfPassengers = int(input("Enter number of passengers for trip: "))
    while NumOfPassengers <= 0:
        NumOfPassengers = int(input("Error! Enter number greater than 0: "))

    if NumOfPassengers > UpSeats[UpTrip] or NumOfPassengers > DownSeats[DownTrip]:
        print("\n####################\n")  # IGNORE
        print("Seats not available for chosen hours")
        print("Please check the display below for available Seats =>")

    else:
        print("//// Seats Booked ////")
        if NumOfPassengers >= 10 and NumOfPassengers <= 80:
            FreeTickets = NumOfPassengers // 10
        else:
            FreeTickets = 0
        OneWayCost = (NumOfPassengers - FreeTickets) * OneWayTicket
        #
        UpPassengers[UpTrip] = UpPassengers[UpTrip] + NumOfPassengers
        UpSeats[UpTrip] = UpSeats[UpTrip] - NumOfPassengers
        UpMoneyTotal[UpTrip] = UpMoneyTotal[UpTrip] + OneWayCost
        #
        DownPassengers[DownTrip] = DownPassengers[DownTrip] + NumOfPassengers
        DownSeats[DownTrip] = DownSeats[DownTrip] - NumOfPassengers
        DownMoneyTotal[DownTrip] = DownMoneyTotal[DownTrip] + OneWayCost

    ScreenDisplay()
    print("Do you want to buy ticket(s)? 'True' for yes and 'False' for no")
    choice = input()
    while choice != "True" and choice != "False":
        choice = input("Enter 'True' for yes and 'False' for no: ")

# ----------- TASK 3 -----------
TotalAmount = 0.0  # INTEGER (FOR TASK 3)
TotalPassengers = 0  # INTEGER
MaxTrain = ""  # STRING (Empty)
MostPassengers = 0  # INTEGER
# DECLARE count : INTEGER //for FOR loops

print("\n")  # IGNORE
print(" ------ END OF THE DAY ------ ")
print("\n")  # IGNORE
for counti in range(0, 4):
    print(
        "Train No:",
        counti,
        "| Train Departure Hour:",
        UpTime[counti],
        "\t| Number of passengers:",
        UpPassengers[counti],
        "\t| Total money:",
        UpMoneyTotal[counti],
    )
    print(
        "Train No:",
        counti,
        "| Train Return Hour:",
        DownTime[counti],
        "\t\t| Number of passengers:",
        DownPassengers[counti],
        "\t| Total money:",
        DownMoneyTotal[counti],
    )
    print("\n-----------------------\n")  # IGNORE

for index in range(0, 4):
    TotalPassengers = TotalPassengers + UpPassengers[index]
    TotalAmount = TotalAmount + (UpMoneyTotal[index] * 2)
for count in range(0, 4):
    if UpPassengers[count] > MostPassengers:
        MostPassengers = UpPassengers[count]
        MaxTrain = UpTime[count]
    if DownPassengers[count] > MostPassengers:
        MostPassengers = DownPassengers[count]
        MaxTrain = DownTime[count]


print("Total money earned today:", TotalAmount)
print("Total passengers travelled today:", TotalPassengers)
print("The train journey with the highest number of passengers today:", MaxTrain)
input("Press Enter to Exit!")  # IGNORE

