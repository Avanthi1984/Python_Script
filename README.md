# vandelay_v1_assessment

## Language used
Python

## Libraries used
tkinter,re,json,csv,datetime

# Run the files
Make sure Python is installed in the machine, browse to the files located in local machine.
## command line 
python CsvtoJson.py

# Running the unittests 
## command line
python -m unittest test_CsvtoJson.py

# GUI Design:
*Note: I have chosen Python as am confortable writing it. I am yet to explore Ruby and other programming laguages for frontend*

I have desinged a GUI using Python's tkinter library (runs in a Single loop/thread)
Which has 3 buttons
- import CSV
- Convert to Json
- exit the application

## 1.Import CSV 
helps to load the CSV files depends on the user choice

## 2.convert to Json
- requires the file location and name to be for the json output file
- to clean the csv data and converts to json

## 3.Exit application 
- Terminates the application

# Application Design

The python file reads the csv data into dictionary.

reads through the rows and
1. Formats the phone numbers columns (1,2 ,3) to (XXX)-XXX-XXXX and update row

2. Validates the license number
- empty and valid digits and encoding of the lincense number checked
- records found in the process which are to be removed are added to the temporary dictionary
- duplicate license numbers checked and old records to be removed are added to the temporary dictionary
- compiled data added to the Dictionary

3. Records to identified as wrong are stored in a separate file with time stamp for review.
4. Throws warning to the user with the no. of records removed and the file name they saved

# Limitations

1.Since the application developed in Python, unfortunately it was not the fastest solution for me to design front-end using React or any other with the available time.

Django/Flask are the possible solutions to design the application for front-end.

2.Unittests were not covered the tkinter and CSV file parsing

3.with Docker its possible to run the python files but the PC am developing has Windows 10 Home version. Installing the docker is an issue.
