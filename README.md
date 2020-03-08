# vandelay_v1_assessment

Laguage used: Python
Libraries used: tkinter,re,json,csv,datetime

Build and run the files:

Make sure Python is installed in the machine.
browse to the files located in local machine.

command line-> python CsvtoJson.py

running the unittests :

command line-> python -m unittest test_CsvtoJson.py

GUI Design:

Note: I have chosen Python as am confortable writing it. I am yet to explore Ruby and other programming laguages for frontend.

I have desinged a GUI using Python's tkinter library (runs in a Single loop/thread)
Which has 3 buttons
1- import CSV
2- Convert to Json
3- exit the application

Import CSV --> helps to load the CSV files depends on the user choice

convert to Json -->
1 -> requires the file location and name to be for the json output file
2 -> to clean the csv data and converts to json

Exit application --> Terminates the application

Application Design:

The python file reads the csv data into dictionary.

reads through the rows and
1 -> formats the phone numbers columns (1,2 ,3) to (XXX)-XXX-XXXX and update row

2 -> Validates the license number
a----> empty and valid digits and encoding of the lincense number checked
b----> records found in the process which are to be removed are added to the temporary dictionary
c----> duplicate license numbers checked and old records to be removed are added to the temporary dictionary
d----> compiled data added to the Dictionary

3 -> records to identified as wrong are stored in a separate file with time stamp for review.
4 -> throws warning to the user with the no. of records removed and the file name they saved

Limitations:

1 --> Since the application developed in Python, unfortunately it was not the fastest solution for me to design front-end using React or any other with the available time.

Django/Flask are the possible solutions to design the application for front-end.

2 --> Unittests were not covered the tkinter and CSV file parsing

3 --> with Docker its possible to run the python files but the PC am developing has Windows 10 Home version. Installing the docker is an issue.
