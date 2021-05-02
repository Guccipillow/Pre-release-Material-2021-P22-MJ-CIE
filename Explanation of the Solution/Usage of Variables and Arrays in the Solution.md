# PURPOSE OF EACH VARIABLE & ARRAY IN THE SOLUTION

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Task 1: Usage of Variables & Arrays](#task-1-usage-of-variables-arrays)
- [Task 2: Usage of Variables](#task-2-usage-of-variables)
- [Task 3: Usage of Variables](#task-3-usage-of-variables)
- [Expected Questions](#expected-questions)

<!-- /code_chunk_output -->

---

## Task 1: Usage of Variables & Arrays

1. `UpTime : ARRAY[1:4] OF STRING`<br>
: *Used to store each train journey’s departure hour (leaving the foot of the mountain hour).*

2. `UpSeats : ARRAY[1:4] OF INTEGER`<br>
: *Used to store the total number of tickets available for each train journey going up the mountain (leaving the foot of the mountain).*

3. `UpPassengers : ARRAY[1:4] OF INTEGER`<br>
: *Used to store the total number of passengers travelled on each train journey going up the mountain (leaving the foot of the mountain).*

4. `UpMoneyTotal : ARRAY[1:4] OF REAL`<br>
: *Used to store the total money taken for each train journey going up (leaving the foot of the mountain).*

5. `DownTime : ARRAY[1:4] OF STRING`<br>
: *Used to store each train journey’s return hour (going down to the foot of mountain hour).*

6. `DownSeats : ARRAY[1:4] OF INTEGER`<br>
: *Used to store the total number of tickets available for each train journey going down (returning to the foot of mountain).*

7. `DownPassengers : ARRAY[1:4] OF INTEGER`<br>
: *Used to store the total number of passengers travelled on each train journey going down (returning to the foot of mountain).*

8. `DownMoneyTotal : ARRAY[1:4] OF REAL`<br>
: *Used to store the total money taken for each train journey going down (returning to the foot of mountain).*

9. `index`<br>
: *Used for FOR…TO…NEXT loop.*

---

## Task 2: Usage of Variables

1. `FreeTickets <- 0 : INTEGER`<br>
: *Used to store the calculated number of free tickets awarded/given to the user for the trip.*

2. `OneWayTicket <- 25.0 : CONSTANT REAL`<br>
: *Used to store the fixed price of one ticket. This variable is a constant.*

3. `OneWayCost <- 0.0 : REAL`<br>
: *Used to store the calculated one-way journey price for the trip.*

4. `choice : BOOLEAN`<br>
: *Used to store the user input when asked if wants to buy ticket(s) or not.*

5. `NumOfPassengers : INTEGER`<br>
: *To store the user input when asked for the number of passengers going on the trip.*

6. `UpTrip : INTEGER`<br>
: *To store user input when asked for the Journey number corresponding to chosen departure hour (leaving the foot of the mountain hour).*

7. `DownTrip : INTEGER`<br>
: *To store user input when asked for the Journey number corresponding to chosen return hour.*

8. `index : INTEGER`<br>
: *Used for FOR…TO…NEXT loop.*

---

## Task 3: Usage of Variables

1. `TotalAmount <- 0.0 : REAL`<br>
: *Used to store the calculated total amount of money taken in a single day.*

2. `TotalPassengers <- 0 : INTEGER`<br>
: *Used to store the total number of passengers travelled in a single day.*

3. `MostPassengers <- 0 : INTEGER`<br>
: *Used to store the greatest number of passengers travelled on a journey to help find the Journey hour with the greatest number of passengers.*

4. `MaxTrain : STRING`<br>
: *Used to store the Journey hour with the greatest number of passengers.*

5. `index : INTEGER`<br>
: *Used for FOR…TO…NEXT loop.*

---

## Expected Questions

For Expected Questions that can come in your Exam for Paper 22<br>
Check out this Document created by [Zafar Ali Khan](https://github.com/zakonweb):<br> :point_down: :point_down: :point_down:
> **[MJ 2021 PRM - Expected Questions - Variant 22.pdf](<https://github.com/zakonweb/Pre-release-Materials/blob/bb6aefaca06c9abca5e0da50ae8fdd1f2c813b7a/June-2021/OL/Variant%2022/Expected%20Questions/MJ%202021%20PRM%20-%20Expected%20Questions%20-%20Variant%2022.pdf>)<br>**

if the link doesn't work, copy and paste this URL in your browser:<br>
`https://github.com/zakonweb/Pre-release-Materials/blob/bb6aefaca06c9abca5e0da50ae8fdd1f2c813b7a/June-2021/OL/Variant%2022/Expected%20Questions/MJ%202021%20PRM%20-%20Expected%20Questions%20-%20Variant%2022.pdf`
