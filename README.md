# Assignment 3: Temp Sensor

Assignment 3 branch created!!!

Complete python script in blinkTemp_a3.py

Modified python script to:

-Read the sensor once a minute instead of when the button switch is pressed

-Write the sensor reading to the sqlite database

-Clear the console and print the table each time the sensor takes a reading


Tutorial Steps:

-----------------

Step 1: 

Create assignment3 branch using the following git commands:

-git branch assignment3

-git checkout assignment3

Step 2: 

-Create the temperature sensor circuit using a breadboard. Refer to the "Logging GPIO data with Python" file. 

Step 3: 

-Create/edit python script that reads a temperature sensor once a minute and prints the temperature to the screen in Fahrenheits. 

-Make sure to install and import necessary libraries (i.e install python, time library, os library) and set important GPIO parameters.

Step 4:

-Create /log directory

-Create assignment3.csv file and an assignment3.db file. 

Step 5:

-Modify the python script so that it prints out the date and time in string format along with the temperature reading. 

-Also modify it so that the string is written to the assignment.csv file each time it prints.

Step 6:

-Install sqlite3 and follow the appropriate steps under the "AnSQLiteSession.pdf" file. 

-Sqlite will be used to create a database and a table where the string for date, time, and temperature for each reading can be recorded.

-While the python script executes, the previous readings will appear in a table-like format.   

 

 

