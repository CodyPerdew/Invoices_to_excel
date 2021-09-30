from pdfminer.high_level import extract_text                        #breaks a PDF into raw text data
from pdfminer.high_level import extract_pages                       #used to determine number of pages
import re
import os
from csv import DictWriter                                          #from the CSV library, for writing dictionaries to CSV files



mainlist = []                                                       #mainlist, an empty list for each Billing Tag to go. 
pdffolder = str(input('Which c:/ folder has your PDFs?. Make sure it only contains PDFs: '))    #pdffolder asks user for PDF location.




for item in os.listdir(pdffolder):
                                                                    #for each pdf in the folder, run pdfminer Extract_Text on that PDF.
    text = extract_text(pdffolder+'/'+item)

    prize = re.findall(('ZZStart-(.*)ZZEnd'), text)                 #search for text between 'ZZstart' & 'ZZend'. Findall grabs each instance & adds them to a list called Prize.
    tags = len(prize)                                               #Tags is the number of tags found in that pdf. 
    pages = len(list(extract_pages(pdffolder+'/'+item)))            #Pages is the number of pages for that PDF, so we can find untagged invoices. 
    print('{} : {} pages :  {} tags'.format(item, pages, tags))     #Tells user how many pages vs tags found. User can inspect PDFs with missing tags for data entry. 

    if prize != None:                                               #If no tags are found there's nothing to append to the main list, this loop gets around that exception.
        for i in prize:                                             #for each item in each 'Prize' list
            mainlist.append(i)                                      #append that text (the billing tag from the invoice) to the MainList, giving a list with every billing tag.

    
    

names = ['SVC', 'MONTH', 'PARTICIPANT', 'AUTH', 'TOTAL', 'COUNTY', 'UOS']   #This list will be used to add the same 7 keys to several dictionaries, one for each billing tag.
dictlist = []                                                               #Dicitonaries will look like {SVC:Coaching, Month:Apr20, Participant:John,} etc. All dicts get added to a list. 



for i in mainlist:                                                  #For each billing tag in the Main List. 
    i=str(i)
    entry = i.split('-')                                            #split it wherever you see '-'. Tags are formatted as Svc-Month-Person-Authnumber-InvoiceTotal-County-BillableUnits
    
    firstdict = dict(zip(names, entry))                             #Create a dictionary for each tag, where the keys come from 'names' above, and values are split from the billing tag.
    
    dictlist.append(firstdict)                                      #Adds each dictionary to the dict list. Because the keys are always the same, they can be used for column headers later. 
    
   



with open ('heyyy.csv', 'w', newline='') as outfile:                #Creates a CSV file named 'heyyy' in the project folder. 'W' is for writeable 
    writer = DictWriter(outfile, ('SVC', 'MONTH', 'PARTICIPANT', 'AUTH', 'TOTAL', 'COUNTY', 'UOS')) #Writes the headers to the file. 
    writer.writeheader()
    writer.writerows(dictlist)                                      #finally writes the Dictlist (Billing Tags) to the rows.

print('Finished, go find your file')
 
