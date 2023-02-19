# splitter.py
# splits the rows of CSV file and saves them as individual CSV files

# import libraries
import pandas as pd
from datetime import date

# returns the current local date
today = date.today()

# reads CSV file and creates data frame
data = pd.read_csv("data.csv")

# separates rows of data frame into individual CSV files
i = 0
while i < len(data):
    # isolate each row of data and save it as CSV based on the Name
    data.iloc[i].to_csv(str(today) + '_' + str(data.iloc[i]["Name"]) +'.csv') 
    i+=1
