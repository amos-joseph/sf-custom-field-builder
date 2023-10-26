import csv
import sys

customObject = sys.argv[1]
sfOrg = sys.argv[2]
csvIn = sys.argv[3]

commandList = ""

with open(csvIn, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        file = '<?xml version="1.0" encoding="UTF-8"?> \n\
<CustomField xmlns="http://soap.sforce.com/2006/04/metadata"> \n\
    <fullName>'+row['Field_Name']+'</fullName> \n\
    <externalId>false</externalId> \n\
    <label>'+row['Label']+'</label> \n\
    <length>'+row['Length']+'</length> \n\
    <required>'+row['Required']+'</required> \n\
    <trackTrending>false</trackTrending> \n\
    <type>'+row['Type']+'</type> \n\
    <unique>'+row['Unique']+'</unique> \n\
</CustomField>'

        f = open('./metadata/'+row['Field_Name']+'.field-meta.xml', "w")
        f.write(file)
        f.close()
        commandList = commandList + 'sfdx force:source:deploy -m CustomField:'+customObject+'.'+row['Field_Name']+' -u '+sfOrg+'\n'

f = open('commands.txt', "w")
f.write(commandList)
f.close()
