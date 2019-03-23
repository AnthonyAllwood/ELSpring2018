# Midterm: Motion Sensor Device

Midterm branch created!!!

Refer to the "Mid Term/ Practical Evaluation" post on Google Classroom for further/detailed explanation on this tutorial!


Modified python script to:

-Trigger two sensors to determine if a person is entering or exiting the room

-Write the sensor readings to the sqlite database

(Complete python script in midterm.py)


Motion Detection Circuit:

-Create motion detection circuit by utilizing a breadboard and the Raspberry Pi


Web page display:

-Establish a web page that graphically displays how many people are in the room that updates any time an entrance or exit occurs

-In the web page, also display a table with the past 10 timestamped entrances and exits


Tutorial Steps:

-----------------

Step 1: 

Create midterm branch using the following git commands:

-git branch midterm

-git checkout midterm

Create a directory called "midterm":

-All necessary files will be in this directory!

Step 2: 

-Create the Motion Detection circuit using a breadboard. Refer to the "GPIO Pinout Explained" on Google Classroom to properly connect pins

-Connect one motion sensor's +Power and GND to a vdd and ground pin on the Raspberry Pi. Connect it's output to pin 13 on the Raspberry Pi. This will be the "entrySensor"

-Connect the other motion sensor's +Power and GND to a vdd and ground pin on the Raspberry Pi. Connect it's output to pin 26 on the Raspberry Pi. This will be the "exitSensor"

Step 3:

(In the midterm directory): 

-Create/edit python script file called "midterm.py" that triggers two motion sensors. In the file, write code that prints the timestamp, whether the motion was "entrance" or "exit", and how many people are in the room:

	-Set "entrySensor" to GPIO pin 13 and "exitSensor" to GPIO pin 26.

	-Create a variable called peopleCount that keeps track of the amount of people in the room.
	
	-Write code that states: "If motion is detected from entrySensor to exitSensor, display the timestamp, "entrance", and increment the peopleCount variable by 1.

	-Write code that states: "If motion is detected from exitSensor to entrySensor, display the timestamp, "exit",  and decrement the peopleCount variable by 1.  

	-Make sure to install and import necessary libraries (i.e install python, time library, os library) and set important GPIO parameters at the top of the file.

	-Run the script. Wave your hand above both sensors to cause both of them to trigger. If your hand is waved from entrySensor to exitSensor, it should print the timestamp, "entrance", and "1" for the amount of people in
 the room. If your hand is waved from exitSensor to entrySensor, it should print the timestamp, "exit", and 0 for the amount of people in the room. 

	-Remember: "entrySensor to exitSensor" increments the peopleCount by 1. "exitSensor to entranceSensor" decrements by 1. 

Step 4:

(In the midterm directory):

-Create /log directory

-The database file created in the next few steps will be in this "log" directory 

Step 5:

-Install sqlite3 and follow the appropriate steps under the "AnSQLiteSession.pdf" file on Google Classroom with respect to the midterm.py file. 

-Sqlite will be used to create a table where the string for date timestamp, "entrance" or "exit" text, and the people count for each motion reading can be recorded.

-The information from this table will be stored in a database file.    

Step 6:

-Establish a web page that displays the information within the database file:

-There are many ways to establish a web server. So utilize whatever software that you are comfortable with (i.e Flask, Node.js, lightpd, etc...)

-Utilizing javascript, create file(s) that establish a chart or gauge for visualization. Have these charts read the information from your database file

	Recommended:

	-Create an "index.html" file that references these javascript files in order to create a web page that displays a chart/gauge showing the information within the database file. AGAIN...there are MANY ways to do this

	-Refer to online sources if necessary to help you establish a web server. Regardless of your method, make sure there is a way to display your Raspberry Pi's IP address and any port of your choosing to the console 
when you run your server 

- Run your server. Go to your preferred browser. Type in your Raspberry PI's IP address along with the port. It should be formatted as something like "0.0.0.1:5000" 
 
-The web page should display the chart/gauge that you created which graphically portrays how many people are in the room that updates any time an entrace or exit occurs. It should also display a table with the last few
entrances and exits. 
 

