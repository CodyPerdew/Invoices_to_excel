from pdfminer.high_level import extract_text
import re
import os
from csv import DictWriter



#Rptstring format is 'ZZstart-Service-Month(MMMYY)-Name-Authnumber-Total-County-ZZend'

mainlist = []                           #an empty list for each Rptstring to go. 
pdffolder = str(input('Which c:/ folder has your PDFs?. Make sure it only contains PDFs: '))    #specifies where PDFs are located





for item in os.listdir(pdffolder):          #for each PDF

    text = extract_text(pdffolder+'/'+item)     #extract the OCR text

    prize = re.search(('ZZStart-(.*)ZZEnd'), text)      #locate the string between ZZstart/End

    mainlist.append(prize.group(1))                 #add that string to the mainlist





#create list that describes dictionary keys
#create an empty list for dictionaries to go
names = ['SVC', 'MONTH', 'PARTICIPANT', 'AUTH', 'TOTAL', 'COUNTY', 'UOS']
dictlist = []



for i in mainlist:                          #for all strings in the list
    entry = i.split('-')                    #split on the -
    firstdict = dict(zip(names, entry))     #create a dict using the names specified, and the string values
    dictlist.append(firstdict)              #add that dict to a list







with open ('heyyy.csv', 'w', newline='') as outfile:        #Specify the CSV filename, Write, don't create a new blank line each time
    writer = DictWriter(outfile, ('SVC', 'MONTH', 'PARTICIPANT', 'AUTH', 'TOTAL', 'COUNTY', 'UOS')) #use dictwriter to write each dict to CSV
    writer.writeheader()
    writer.writerows(dictlist)

print('Finished, go find your file')        #currently CSV is placed in the py projects folder
 
