_________
_________

### CHANGE #1: Correction of Minor Mistakes

DATE: 18/04/2021

commit https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/204d2efe0fb520c519fd40f0f57ecb04c3d9e7da

Author: @Dunroxiz

**Explanation:**<br>
Updated the pseudocode files because they had some minor mistakes. There are no changes to the Algorithms itself.
There was a mistake in the last FOR loop.
Sorry for the inconvenience.

All pseudocode files have been updated

_________
_________

### CHANGE #2: Updated Task 1, More efficient now!

Date: 19/04/2021

commit https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/b6f69d8a032417965916cb14851d00ff5e7799b0

Author: @Dunroxiz

**Explanation:**<br>
Before, The task 1 *Train Journey Display* algorithm had an **IF** statement in the **FOR** loop to check if the tickets were available or not. If tickets were not available it would **PRINT** that the Train for that hour is closed. 
```
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

```
FOR index <- 0 TO 3
    PRINT ("Train No: ", index, "| Train Departure Hour: ", UpTime[index], "| Remaining Tickets: ", UpSeats[index])
    PRINT ("Train No: ", index, "| Train Return Hour: ", DownTime[index], "| Remaining Tickets: ", DownSeats[index])
    PRINT "---------"
NEXT index
```

*Train Journey Display* algorithm in Task 2 remain unchanged.

All pseudocode files have been updated!

_________
_________

### CHANGE #3: Error corrected in UpTrip validation loop Task 2!

Date: 25/04/2021

commit [f5d2ab5](https://github.com/Dunroxiz/Pre-release-Material-2021-P22-MJ-CIE/commit/f5d2ab564ecea3137405f5503fbee94eb70066b6)

Author: @Dunroxiz

**Explanation:**<br>

There was a mistake in the condition of the WHILE loop that was being used as a validation for UpTrip.
**AND** have been changed to **OR**

All the files have been corrected and updated.

Before
```
WHILE choice = True DO
    PRINT "Enter Train number corresponding to your departure hour: "
    INPUT UpTrip
    WHILE UpTrip < 0 AND UpTrip > 3 DO
        PRINT "Error! Enter train number from (0, 1, 2, 3): "
        INPUT UpTrip
    ENDWHILE
```
After:
```
WHILE choice = True DO
    PRINT "Enter Train number corresponding to your departure hour: "
    INPUT UpTrip
    WHILE UpTrip < 0 OR UpTrip > 3 DO
        PRINT "Error! Enter train number from (0, 1, 2, 3): "
        INPUT UpTrip
    ENDWHILE
```

_________
_________


