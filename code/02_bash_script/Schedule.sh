#!/bin/bash

#This script generates today's date and displays a decription with respect to the date.

	echo "Anthony's Schedule"
	echo "Anthony Allwood, 2019"
	echo "Embedded Linux"

	echo
	echo


	number=$1

	TODAY_DATE=$(date +%m-%d-%Y)
	MONTH_CALENDAR=$(cal)

	case $number in

	1) echo "$TODAY_DATE"

	   if [ "$TODAY_DATE" == "02-20-2019" ]
	   then
		echo "Your Embedded Linux assignment 2 was due yesterday."
		echo "You have VLSI Lab today at 11:00 am."
		echo "You have a test tomorrow in OOP design."
	   fi

	   if [ "$TODAY_DATE" == "02-21-2019" ]
	   then
		echo "You have a test today at 9:30 am in OOP."
		echo "You have OOP, Functional Verification, VLSI lecture, and Embedded Linux today."
		echo "Patricia coming today!!!"
	   fi

	   if [ "$TODAYS_DATE" == "02-22-2019" ]
	   then
		echo "NO CLASS TODAY!!!!"
		echo "Work tonight at 11:45!!"
	   fi

	;;

	2) echo "$MONTH_CALENDAR"
	;;
	esac
