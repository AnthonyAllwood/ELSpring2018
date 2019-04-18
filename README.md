# Midterm: Soil Moisture Sensor

Moisture_sensor branch created!!!


Created and modified python script to:

-Make a YL-69 Soil Moisture Sensor constantly read the moisture content value within the soil of a plant
and log that value within a SQLite database table, along with each reading's timestamp, and a message string
stating whether or not the plant is dry or watered.

-Send an email informing the user whether or not the plant is dry and how long it has been since the plant 
was watered. 

SQLite database:

-Utilize the Sqlite3 database program in order to create a table that can take in certain varaibles from the 
python script and use them to make rows and columns.

Moisture Detection Circuit:

-Establish a moisture detection circuit by utilizing the YL_69 Soil Moisture Sensor, a breadboard, a HCP3008
Analog to Digital Converter, and the Raspberry Pi.

-------------------

Tutorial Steps: 

-------------------

Step 1:

Create moisture_sensor branch using the following git commands:

-git branch moisture_sensor

-git checkout moisture_sensor


Create a directory called "moisture_detection":

-All project files will be in the directory!


Step 2:

Create the moisture detection circuit using the breadboard. Make sure to understand the GPIO Pinout on the
Raspeberry Pi before making the circuit:

-Connect the VCC and Gnd ports on the YL-69 Sensor to the 5V pin and a GND pin on the Raspberry Pi. The light will
pop up on the sensor indicating that it is receiving power.

-Connect the D0 (digital) port on the YL-69 Sensor to pin 27 on the Raspberry Pi. This will be assigned to the sensorPin 
varaible within the python script

-An MCP3008 Analog to Digital Converter will be used to take the analog signals containing the moisture content values from the YL-69
and turn in into a digital signal that the Raspeberry Pi can detect and utilize. (This is because the Raspberry Pi does not
have any analog pins. Sending an analog signal directly into the Pi's digital pins can cause major problems). Connect
the A0 (analog) port from the YL-69 sensor to port 0 on the MCP3008. Click on the link below to see how to connect the other
necessary ports on the MCP3008 ADC to the Raspberry Pi. 

[a link] (Enter Link Here) 


Step 3:

Create python file in "moisture_detection" directory:

-Import necessary libraries

-Initialize GPIO

-Create varaiables:

	-sensorPin: pin 27 which is responsible for digital input from sensor

	-thresholdValue: Will be used to trigger events based on moisture content value. 

	-SMTP: certain variables will need to be assigned in order to utilize smtp. SMTP is responsible for sending emails to user.
	Click on the link below to learn how to set up SMTP to send emails to user. 
	[a link] (https://raspberry-projects.com/pi/software_utilities/email/ssmtp-to-send-emails)

-Create functions:

	-Create a function that sends emails using the smtp library and objects. The link above can assist with this. 

	-Create a function that determine whether or not the sensor is on or off. Use the sensorPin variable for this. 

	-Create a function that reads the moisture content value and sends an email notifying if moisture content is 
	low or stable. 

-Setup SQLite:

	-Under the "moisture_detection" directory, create a directory called "log"

	-In the log directory, create a database file

	-Type "sqlite3" on the command line and create a table for holding your timestamp, moisture content value, and (watered?) message. 
 
	-In the python script, log the timestamp, moisture content value, and a (watered?) message to the database table.

	
-Create a way to save the time when the plant was last watered:

	-Save this time within a variable.

	-Send this variable along with the email to notify the user when the last time the plant was watered. 


Step 4:

Create your try block that will run your functions and other important code within yuor script to your specifications. 

-Set time intervals betwwen your functions to correctly analyze and monitor what is going on while the script is running.

-RUN THE SCRIPT!!!!!  
