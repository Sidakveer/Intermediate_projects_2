# Intermediate_projects_2
Using various modules such as **smtplib, pandas, datetime and more.** to build interesting projects and using various **API's** (get, put, post methods) to work with different sets of data. 
 ## Birthday_Wisher
This project contains a program which automates the process of sending out emails to people in our .csv file on their birthdays. The program uses **pandas** 
to work with the csv file and **smtplib** module to build a connection with the email servers and send out emails from the users email address. The **datetime** module helps to keep a track of the current 
day and month to check if anyone from the guest list has a birthday or not.
## iss_tracker
This project uses the **requests** module to use different **API's** to get a hold of the iss satellite's current position which revolves the earth continously and get the times for the sunrise and sunsets each day to compare them with the current time. If it is night time and the satellite is crossing over us the program then sends us an email to "look up" towards the sky to spot the satellite.
## Quiz_game
In this project we use **object oreinted programming** concepts to create different classes using **tkinter and requests module** to build a UI for the user. The question are generated from the API added and the program displays it for the user to select their answer which is either right or wrong. Based on their answer the score on the screen is updated and the next question appears.
