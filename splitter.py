# splitter.py
# splits the rows of CSV file and saves them as individual CSV files

# import libraries
import pandas as pd
import numpy as np
from datetime import date

# returns the current local date
today = date.today()

# split(): separates rows of data frame into individual CSV files
def split():
    print("Splitting files ...")
    i = 0
    while i < len(data):
        # isolate each row of data and save it as CSV based on the Name
        data.iloc[i].to_csv(str(today) + '_' + str(data.iloc[i]["Name"]) +'.csv') 
        i+=1
    print("Split complete.")

# startup message
print("Welcome to Splitter. \nDesigned by Anthony Nanfito. \nThis is a python script which splits the rows of CSV file and saves them as individual CSV files. Learn more at https://github.com/ananfito/splitter. \nFollow the instructions below to split your file.")

# user input: file path to CSV file
dataPath = input("Please type (or copy and paste) the file path to the CSV path your with to split: ")

# reads CSV file and creates data frame
data = pd.read_csv(dataPath).replace(np.nan, "MISSING")

split()
