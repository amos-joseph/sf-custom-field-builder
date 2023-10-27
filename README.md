# sf-custom-field-builder
Creates the XML metadata files for custom fields in Salesforce based on a CSV file for input.

Step 1: Retreive the metadata for your object using SFDX.  In this example we're pulling the Member__c custom object from the Example Salesforce Org.

    sfdx force:source:retrieve -m CustomObject:Member__c -u Example

Step 2: Fill out the CSV with the additional fields you want to add.

Step 3: Run the python script to generate your XML files and import commands.  Make sure to add the correct object name and Salesforg Org to the command line arguments.

    python3 create-metadata.py Member__c Example Field_Template.csv

Step 4: Copy the XML files that were created in the metadata directory into the fields folder that was generated in Step 1.

Step 5: Run the sfdx commands from the commands.txt file that was generated in Step 3.

Step 6: Profit.

If you need to edit field permissions in bulk you can use the following commands to pull field permissions for specific profiles:

sfdx force:source:retrieve -m Profile:Coach,CustomObject:Member__c

Once you've editited the permission metadata you can then re-deploy:

sfdx force:source:deploy -m Profile:Coach  
