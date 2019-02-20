#!/bin/bash

#This script generates today's date and displays a decription with respect to the date.

	echo "Anthony's Schedule"
	echo "Anthony Allwood, 2019"
	echo "Embedded Linux"

	echo
	echo


	number=$1

	TODAY_DATE=$(date +%m-%d-%Y)

	case $number in

	1) echo "$TODAY_DATE"

	;;
	esac
