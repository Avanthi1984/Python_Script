import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import json
import csv
import re

from time import strftime, strptime
from datetime import datetime

# check the validity of the license
# check the encoding: sum the each of the 9 prior digits
# and then perform a modulus 10 operation on the sum.
# The result is the 10th digit.


def chkValidLicense(license_num):
    sum = 0
    # check no. of 10 digits, if not return false
    if not re.match("^[0-9]{10}$", license_num):
        return False
    # check if string is empty , if so return false
    if not license_num:
        return False
    # read and sum upto 9 characters in license string as integers
    for i in range(len(license_num)-1):
        digit = int(license_num[i])
        sum += digit
    # check modulous 10 of sum of 9 digits is equal to 10th digit
    if int(license_num[len(license_num)-1]) == (sum % 10):
        return True
    else:
        return False

# function to return the converted date


def convert_date(strdate):
    # two patterns added,
    # provision of more patters also test to be done for different patterns
    # ["%d-%m-%Y", "%Y-%m-%d", "%m/%d/%y", "%m/%d/%Y","%d/%m/%Y", "%d/%m/%y", "%y/%m/%d", "%Y/%m/%d", "%y/%d/%m", "%Y/%d/%m"]
    date_patterns = ["%Y-%m-%d", "%m/%d/%y"]

    for pattern in date_patterns:
        try:
            return datetime.strptime(strdate, pattern)
        except:
            pass
    return None


# remove the duplicate record with same license number


def makeNoteOfDuplicates(newRecord):
    for key in list(data):
        if data[key]["License number"] == newRecord['License number']:
            if max(convert_date(data[key]["Last update date"]),
                   convert_date(newRecord["Last update date"])) == convert_date(newRecord['License number']):
                makeNoteOfRecords[key] = data[key]
            else:
                makeNoteOfRecords[key] = newRecord


def cleanDataRecord():
    csvReader = csv.DictReader(csvFile)
    for csvRow in csvReader:
        first_name = csvRow['First name']
        # phone number formatting as (xxx)-xxx-xxxx using re
        csvRow['Phone 3 number'] = reg.sub(
            r'(\1)\2-\3', csvRow['Phone 3 number'])
        csvRow['Phone 2 number'] = reg.sub(
            r'(\1)\2-\3', csvRow['Phone 2 number'])
        csvRow['Phone 1 number'] = reg.sub(
            r'(\1)\2-\3', csvRow['Phone 1 number'])
        # print(csvRow['Phone 3 number'])
        # Validate license number
        # print(csvRow['License number'])

        if not chkValidLicense(csvRow['License number']):
            # make note of records for later deletion
            makeNoteOfRecords[first_name] = csvRow
        else:
            # this step is to record the licence no. of getting info of duplicates for valid licenses
            if csvRow['License number'] not in License_numbers:
                License_numbers.add(csvRow['License number'])
            else:
                # make note of records for later deletion
                makeNoteOfDuplicates(csvRow)

        # update cleaned record to dictionary
        data[first_name] = csvRow


def removeRecords(data):
    count = 0
    for key in makeNoteOfRecords:
        del data[key]
        count += 1

    RemovedRecords = datetime.now().strftime(
        'RemovedRecords-%Y-%m-%d-%H-%M-%S.json')
    # write to json file
    with open(RemovedRecords, 'w') as jsonFile:
        jsonFile.write(json.dumps(makeNoteOfRecords, indent=4))
    tk.messagebox.showwarning(
        'warning', message="{} Records identified wrong and saved to {} file for review".format(count, RemovedRecords), icon='warning')


def getCSV():
    global csvFile

    import_file_path = filedialog.askopenfilename()
    csvFile = open(import_file_path)


def convertToJSON():
    global csvFile

    export_file_path = filedialog.asksaveasfilename(defaultextension='.json')

    cleanDataRecord()
    removeRecords(data)

    # write to json file
    with open(export_file_path, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))

    data.clear()
    makeNoteOfRecords.clear()
    License_numbers.clear()


def exitApplication():
    MsgBox = tk.messagebox.askquestion(
        'Exit Application', 'Are you sure you want to exit the application', icon='warning')
    if MsgBox == 'yes':
        root.destroy()


# reading csv and adding data to dictionary
data = {}
makeNoteOfRecords = {}
License_numbers = set()
# regular expression for decoding the phone numbers
reg = re.compile(r'\d?[-.\s]?\(?(\d{3})\)?[ -.]?(\d{3})[ -.]?(\d{4})')

root = tk.Tk()
canvas1 = tk.Canvas(root, width=400, height=400,
                    bg='lightyellow3', relief='raised')
canvas1.pack()

label1 = tk.Label(
    root, text=' CSV to JSON Conversion ', bg='lightyellow3')
# label1.grid(column=0, row=1)
label1.config(font=('helvetica', 20))
canvas1.create_window(200, 60, window=label1)


browseButton_CSV = tk.Button(text="  Import CSV File ",
                             command=getCSV, bg='lightblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(200, 130, window=browseButton_CSV)

saveAsButton_JSON = tk.Button(text='Convert CSV to JSON', command=convertToJSON,
                              bg='lightblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(200, 180, window=saveAsButton_JSON)


exitButton = tk.Button(root, text='       Exit Application     ',
                       command=exitApplication, bg='thistle4', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(200, 230, window=exitButton)

root.mainloop()
