from pdfminer.high_level import extract_text
import re
import os
from csv import DictWriter


#mainlist, an empty list for each Rptstring to go. 
mainlist = []
pdffolder = str(input('Which c:/ folder has your PDFs?. Make sure it only contains PDFs: '))

#pdffolder gives the user input and specifies the directory for the input PDFs



#for each pdf, run pdfminer Extract_Text on that PDF, search for any text between ZZstart and ZZend
#append that text (which is the Rptstring from the BillReq page) to the mainlist,
#giving a list of each Rptstring from each PDF
for item in os.listdir(pdffolder):

    text = extract_text(pdffolder+'/'+item)

    prize = re.search(('ZZStart-(.*)ZZEnd'), text)

    mainlist.append(prize.group(1))





#create list that describes dictionary names or fields
#create an empty list for dictionaries to go
names = ['SVC', 'MONTH', 'PARTICIPANT', 'AUTH', 'TOTAL', 'COUNTY', 'UOS']
dictlist = []


#For each Rptstring in the list, split it wherever you see '-', then create a 'Dictionary'
#Where the first entry comes from the Names list above, and the second entry is the split values
#From the Rptstring
for i in mainlist:
    entry = i.split('-')
    firstdict = dict(zip(names, entry))
    dictlist.append(firstdict)





#Specifies filename.csv, 'W' for Write. Specifies the column headers (must match the namelist above)
#Writes the headers to the file, and finally writes the Dictlist (compiled Rptstrings) to the rows. 
with open ('heyyy.csv', 'w', newline='') as outfile:
    writer = DictWriter(outfile, ('SVC', 'MONTH', 'PARTICIPANT', 'AUTH', 'TOTAL', 'COUNTY', 'UOS'))
    writer.writeheader()
    writer.writerows(dictlist)

print('Finished, go find your file')
 
