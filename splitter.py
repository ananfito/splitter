# splitter.py
# splits the rows of CSV file and saves them as individual CSV files

# import libraries
import pandas as pd
from datetime import date

# returns the current local date
today = date.today()

# FUNCTIONS
# split(): separates rows of data frame into individual CSV files
def split():
    print("Splitting files ...")
    i = 0
    while i < len(data):
        # isolate each row of data and save it as CSV based on the Name
        data.iloc[i].to_csv(str(today) + '_' + str(data.iloc[i]["Name"]) +'.csv') 
        i+=1
    print("Split complete.")

# missingAssignmentReport(): generates list of missing assignments for each student
def missingAssignmentReport():
    print("Generating missing assignment reports ...")

    i = 0
    columnTitles = list(data) # creates array of column names
    studentsMissingWork = {} # empty dictionary to store missing assignments

    # loop through the rows and columns of the dataframe for any 'nan' entries
    # 'nan' entries are missing assignments that students need to complete
    # student names and list of missing assignment are stored in studentsMissingWork dictionary
    while i < len(data):
        j = 1
        while j < len(columnTitles) - 1:
            if data.iloc[i][columnTitles[j]].astype(str) == 'nan':
                if data.iloc[i][columnTitles[0]] not in studentsMissingWork.keys():
                    studentsMissingWork.update({data.iloc[i][columnTitles[0]]: [columnTitles[j]]})
                else:
                    studentsMissingWork.get(data.iloc[i][columnTitles[0]]).append(columnTitles[j])
            j+=1
        i+=1
    
    # iterate through the dictionary to create individual filees for students' missing work
    for student in studentsMissingWork:
        file = open('%s_%s.txt' % (today, student), 'w')
        file.write('Below is a list of the assignment(s) you are missing. Please complete for credit, then email me me your list of completed assignment(s) with their new scores. Thank you. \n%s' % studentsMissingWork[student])
        file.close()
    
    print("Reports generated.")

# startup message
print("Welcome to Splitter. \nDesigned by Anthony Nanfito. \nThis is a python script which splits the rows of CSV file and saves them as individual CSV files. Learn more at https://github.com/ananfito/splitter. \nFollow the instructions below to split your file.")

# user input: file path to CSV file
dataPath = input("Please type (or copy and paste) the file path to the CSV path your with to split: ")

# reads CSV file and creates data frame
data = pd.read_csv(dataPath)

# user input: how do you want to manipulate this file?
command = input("How do you want to manipulate this file? \nPlease select the option you want by typing the correspond number followed by the 'Enter' key:\n 1: Split each of selected file into individual files.\n 2: Generate missing assignment report\n 0: Quit program\n")

if command == '0':
    quit()
elif command == '1':
    split()
elif command == '2':
    missingAssignmentReport()
