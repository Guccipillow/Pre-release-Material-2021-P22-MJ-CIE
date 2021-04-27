# 1. Changes index (from least to most recent)

- [1. Changes index (from least to most recent)](#1-changes-index-from-least-to-most-recent)
  - [1.1. Correction of Minor Mistakes](#11-correction-of-minor-mistakes)
  - [1.2. Updated Task 1, More efficient now](#12-updated-task-1-more-efficient-now)
  - [1.3. Error corrected in UpTrip validation loop Task 2](#13-error-corrected-in-uptrip-validation-loop-task-2)
  - [1.4. Correction of Keyword error in FOR loop in TASK 3](#14-correction-of-keyword-error-in-for-loop-in-task-3)
  - [1.5. Datatype changed for 2 variables in TASK 3](#15-datatype-changed-for-2-variables-in-task-3)
  - [1.6. Keywords correction (No changes to the algorithm)](#16-keywords-correction-no-changes-to-the-algorithm)
  - [1.7. Big Update (Small change to the Algorithm and Prompts changes)](#17-big-update-small-change-to-the-algorithm-and-prompts-changes)
    - [1.7.1. "Train No: " changed to "Journey No: "](#171-train-no--changed-to-journey-no-)
    - [1.7.2. Prompts Updated](#172-prompts-updated)
    - [1.7.3. Array starting index changed](#173-array-starting-index-changed)
    - [1.7.4. New Print statement added](#174-new-print-statement-added)
    - [1.7.5. Python File Updated](#175-python-file-updated)

## 1.1. Correction of Minor Mistakes

DATE: 18/04/2021

commit [204d2ef](https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/204d2efe0fb520c519fd40f0f57ecb04c3d9e7da)

Author: [**@Dunroxiz**](https://github.com/Dunroxiz)

**Explanation:**

Updated the pseudocode files because they had some minor mistakes. There are no changes to the Algorithms itself.
There was a mistake in the last FOR loop.
Sorry for the inconvenience.

All pseudocode files have been updated

___
___

## 1.2. Updated Task 1, More efficient now

Date: 19/04/2021

commit [b6f69d8](https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/b6f69d8a032417965916cb14851d00ff5e7799b0)

Author: [**@Dunroxiz**](https://github.com/Dunroxiz)

**Explanation:**

Before, The task 1 *Train Journey Display* algorithm had an **IF** statement in the **FOR** loop to check if the tickets were available or not. If tickets were not available it would **PRINT** that the Train for that hour is closed.

```pseudocode
FOR index <- 0 TO 3
    IF UpSeats[index] != 0
        THEN
            PRINT ("Train No: ", index, "| Train Departure Hour: ", UpTime[index], "| Remaining Tickets: ", UpSeats[index])
        ELSE
            PRINT ("Train No: ", index, "| Train Departure Hour: ", UpTime[index], "| Closed!")
    ENDIF

    IF DownSeats[index] != 0
        THEN
            PRINT ("Train No: ", index, "| Train Return Hour: ", DownTime[index], "| Remaining Tickets: ", DownSeats[index])
        ELSE
            PRINT ("Train No: ", index, "| Train Return Hour: ", DownTime[index], "| Closed!")
    ENDIF
NEXT index
```

But knowing that this is the first time the *Train Journey Display* is being shown, and there had not been any bookings. We can remove the IF statements and the print statement for showing the Train is closed from the task 1 because there is no way that a train is going to be closed when the program has just started.

The improved algorithm for task 1 looks like this:

```pseudocode
FOR index <- 0 TO 3
    PRINT ("Train No: ", index, "| Train Departure Hour: ", UpTime[index], "| Remaining Tickets: ", UpSeats[index])
    PRINT ("Train No: ", index, "| Train Return Hour: ", DownTime[index], "| Remaining Tickets: ", DownSeats[index])
    PRINT "---------"
NEXT index
```

*Train Journey Display* algorithm in Task 2 remain unchanged.

All pseudocode files have been updated!

___
___

## 1.3. Error corrected in UpTrip validation loop Task 2

Date: 25/04/2021

commit [f5d2ab5](https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/f5d2ab564ecea3137405f5503fbee94eb70066b6)

Author: [**@Dunroxiz**](https://github.com/Dunroxiz)

**Explanation:**

There was a mistake in the condition of the WHILE loop that was being used as a validation for UpTrip.
**AND** have been changed to **OR**

All the files have been corrected and updated.

Before

```pseudocode
WHILE choice = True DO
    PRINT "Enter Train number corresponding to your departure hour: "
    INPUT UpTrip
    WHILE UpTrip < 0 AND UpTrip > 3 DO
        PRINT "Error! Enter train number from (0, 1, 2, 3): "
        INPUT UpTrip
    ENDWHILE
```

After:

```pseudocode
WHILE choice = True DO
    PRINT "Enter Train number corresponding to your departure hour: "
    INPUT UpTrip
    WHILE UpTrip < 0 OR UpTrip > 3 DO
        PRINT "Error! Enter train number from (0, 1, 2, 3): "
        INPUT UpTrip
    ENDWHILE
```

___
___

## 1.4. Correction of Keyword error in FOR loop in TASK 3

Date: 25/04/2021

Author: [**@Dunroxiz**](https://github.com/Dunroxiz)

commit [6e12d7b](https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/6e12d7b0405348dd31041a089fbb79076cd644b8)

**Explanation:**

Keyword error in **FOR** loop corrected in Task 3

Before:

```pseudocode
FOR index <- 0 TO 3
    TotalPassengers <- TotalPassengers + UpPassengers[index]
    TotalAmount <- TotalAmount + (UpMoneyTotal[index] * 2)
ENDIF
```

After:

```pseudocode
FOR index <- 0 TO 3
    TotalPassengers <- TotalPassengers + UpPassengers[index]
    TotalAmount <- TotalAmount + (UpMoneyTotal[index] * 2)
NEXT index
```

All pseudocode files have been updated
___
___

## 1.5. Datatype changed for 2 variables in TASK 3

Date: 25/04/2021

Author: [**@Dunroxiz**](https://github.com/Dunroxiz)

commit [2ff0acb](https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/2ff0acba2346d949552de0a579d7b8af60f42d8d)

**Explanation:**

Datatype changed for 2 variables in Task 3<br>
Datatype changed from **REAL** to **INTEGER** for **TotalPassengers, MostPassengers**.

Before:
`DECLARE TotalPassengers, MostPassengers <- 0 : REAL`

After:
`DECLARE TotalPassengers, MostPassengers <- 0 : INTEGER`

**All pseudocode files have been updated**

___
___

### 1.6. Keywords correction (No changes to the algorithm)

Date: 26/04/2021

Author: [**@Dunroxiz**](https://github.com/Dunroxiz)

commit [2b6748b](https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/2b6748b4bc0acef7c4f179f988b967f73d080e8d)

**Explanation:**<br>

Check commit to see the changes

Before:

`WHILE DownTrip < UpTrip OR DownTrip > 3:`<br>
`WHILE NumOfPassengers <= 0:`

After:

`WHILE DownTrip < UpTrip OR DownTrip > 3 DO`<br>
`WHILE NumOfPassengers <= 0 DO`

All pseudocode files have been updated!

___
___

## 1.7. Big Update (Small change to the Algorithm and Prompts changes)

Date: 27/04/2021

Author: [**@Dunroxiz**](https://github.com/Dunroxiz)

commit: [105483a](https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/105483a0d3aacab153cb734e191089685d52d57d)

**Explanation:**

### 1.7.1. "Train No: " changed to "Journey No: "

In this update, I have updated some prompts. In the previous solution, we asked the user to input Train Number but after reading the pre-release material again.
There it says, there is only one train that makes 4 return trips. So we shouldnt use "Train No: " in prompts and also shouldn't ask the user for "Train No" as an input.
To overcome this problem, I have changed the prompt "Train No: " to "Journey No: ". For example:

Before:

1. `PRINT ("Train No: ", index, "| Train Departure Hour: ", UpTime[index], "| Remaining Tickets: ", UpSeats[index])`

2. `PRINT "Enter Train number corresponding to your departure hour: "`

After:

1. `PRINT ("Journey No: ", index, "| Departure Hour: ", UpTime[index], "| Tickets available: ", UpSeats[index])`

2. `PRINT "Enter Journey number for your chosen departure hour: "`

___

### 1.7.2. Prompts Updated

The prompts that were too long or had unnecessary words have been updated as well and made short and understandable.<br>
For example:

Before:

1. `PRINT "Do you want to buy ticket(s)? 'True' for yes and 'False' for no"`

2. `PRINT "Enter 'True' for yes and 'False' for no: "`

3. `PRINT "Enter Train number corresponding to your departure hour: "`

After:

1. `PRINT "Do you want to buy ticket(s)? Enter True or False: "`

2. `"Invalid Input! Enter True or False: "`

3. `PRINT "Enter Journey number for your chosen departure hour: "`

___

### 1.7.3. Array starting index changed

Another update is, I have changed the starting index of the Arrays from 0 to 1. This is done because printing/saying "Journey No: 0" doesn't feel right and it would be easy for user to understand the counting starting from 1.<br>
For example:

Before it would print:

```pseudocode
PRINT ">>>>>    TRAIN JOURNEY DISPLAY    <<<<<"
FOR index <- 0 TO 3
    PRINT ("Journey No: ", index, "| Departure Hour: ", UpTime[index], "| Tickets available: ", UpSeats[index])
    PRINT ("Journey No: ", index, "| Return Hour: ", DownTime[index], "| Tickets available: ", DownSeats[index])
    PRINT "---------"
NEXT index


OUTPUT would be

Journey No: 0 | Departure Hour: 09:00 | Tickets available: 480
Journey No: 0 | Return Hour: 10:00 | Tickets available: 480
.......
```

After update it would now print:

```pseudocode
PRINT ">>>>>    TRAIN JOURNEY DISPLAY    <<<<<"
FOR index <- 1 TO 4
    PRINT ("Journey No: ", index, "| Departure Hour: ", UpTime[index], "| Tickets available: ", UpSeats[index])
    PRINT ("Journey No: ", index, "| Return Hour: ", DownTime[index], "| Tickets available: ", DownSeats[index])
    PRINT "---------"
NEXT index


OUTPUT would be

Journey No: 1 | Departure Hour: 09:00 | Tickets available: 480
Journey No: 1 | Return Hour: 10:00 | Tickets available: 480
Journey No: 2 | Departure Hour: 11:00 | Tickets available: 480
Journey No: 2 | Return Hour: 12:00 | Tickets available: 480
.......

```

The declarations have been updated also. For example:

Before:

```pseudocode
DECLARE UpTime : ARRAY[0:3] OF STRING 
DECLARE UpSeats : ARRAY[0:3] OF INTEGER
DECLARE UpPassengers : ARRAY[0:3] OF INTEGER 
DECLARE UpMoneyTotal : ARRAY[0:3] OF REAL 

DECLARE DownTime : ARRAY[0:3] OF STRING 
DECLARE DownSeats : ARRAY[0:3] OF INTEGER
DECLARE DownPassengers : ARRAY[0:3] OF INTEGER 
DECLARE DownMoneyTotal : ARRAY[0:3] OF REAL 
```

After:

```pseudocode
DECLARE UpTime : ARRAY[1:4] OF STRING 
DECLARE UpSeats : ARRAY[1:4] OF INTEGER
DECLARE UpPassengers : ARRAY[1:4] OF INTEGER 
DECLARE UpMoneyTotal : ARRAY[1:4] OF REAL 

DECLARE DownTime : ARRAY[1:4] OF STRING 
DECLARE DownSeats : ARRAY[1:4] OF INTEGER
DECLARE DownPassengers : ARRAY[1:4] OF INTEGER 
DECLARE DownMoneyTotal : ARRAY[1:4] OF REAL 
```

All the FOR loops, WHILE loops and prompts have also been updated according to the new Array indexes. For example:

Before:

1. `FOR index <- 0 TO 3`

2. `WHILE UpTrip < 0 OR UpTrip > 3 DO`

3. `PRINT "Error! Enter Journey number from (0, 1, 2, 3): "`

4. `WHILE DownTrip < UpTrip OR DownTrip > 3 DO`

After:  

1. `FOR index <- 1 TO 4`

2. `WHILE UpTrip < 1 OR UpTrip > 4 DO`

3. `PRINT "Error! Enter Journey number from (1, 2, 3, 4): "`

4. `WHILE DownTrip < UpTrip OR DownTrip > 4 DO`

___

### 1.7.4. New Print statement added

commit [New Print Statement](https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/105483a0d3aacab153cb734e191089685d52d57d#diff-c2f12e88103331fd46bc7501fba871121983c7f88653fe13704ce89b48c55572R95)

A new print statement has been added that prints out the price of the two-way journey that user has booked for.<br>
it only prints this if the seats have been booked.

`PRINT "Total price for two-way journey: $", OneWayCost * 2,`

___

### 1.7.5. Python File Updated

commit: [e4740c0](https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/e4740c0fcbd4425a20a66a269e2a7055d7cbc34b)

In python file all the changes mentioned above have been applied except Array index starting from 1.<br>
Instead, I have done this:

I add 1 to the index in print statement so where it should be printing "Journey No: 0" it would now print "Journey No: 1".<br>
This addition to the index in print statement does not effect the index variable being used in the loop.

```pseudocode
for index in range(0, 4):
    if UpSeats[index] != 0:
        print("Journey No:", index + 1, "| Departure Hour:", UpTime[index], "\t| Tickets available:", UpSeats[index], )
    else:
        print("Journey No:", index + 1, "| Departure Hour:", UpTime[index], "| Closed!",)

    if DownSeats[index] != 0:
        print("Journey No:", index + 1, "| Return Hour:", DownTime[index], "\t| Tickets available:", DownSeats[index],)
    else:
        print("Journey No:", index + 1, "| Return Hour:", DownTime[index], "| Closed!")
```

Plus, regarding the input from user. The user is shown the counting starting from 1.<br>
When he is asked for input he will enter a number from 1 to 4 but 1 will be subtracted from that number upon assigning it to the variable.<br>
The validation also remains the same because of this.
For Example:

Ex#1

```pseudocode
UpTrip = int(input("Enter Journey number for your chosen departure hour: ")) - 1
while UpTrip not in range(0, 4):
    UpTrip = int(input("Error! Enter Journey number from (1, 2, 3, 4): ")) - 1
```

Ex#2

```pseudocode
DownTrip = int(input("Enter Journey number for your chosen Return hour: ")) - 1
while DownTrip < UpTrip or DownTrip > 3:
    DownTrip = int(input("Error! Enter Journey number from the given list above: ")) - 1
```

***All files have been updated!***

___
___
