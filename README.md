# 

# OpenUScheduler
A script that connects to your Google Calendar and schedules all the classes from a specific url of OpenU

## How To Use
1. Go to Google Calendar, enter the settings of the calendar you wish to edit, and copy the "Calendar ID".
2. Open the ```settings.json``` file and Replace ```<calendar_id>``` with your calendar id in the desired row. REMOVE THE ```<>```!
3. Replace ```<username>```,```<password>``` and ```<id>``` with the credentials of your account in OpenU
4. Generate a Credentials JSON File from the Google Calendar API:

    a. Enter https://console.developers.google.com/?pli=1

    b. Create a New Project

    c. Enable API And Services 

    d. Search for Google Calendar API and enable it.

    e. o to Credentials -> Create Credentials -> OAuth Client ID -> Other

    f. Download the file and put in the same folder as the script.

6. Run the script. 

First Argument: The name you wish to schedule the class as

Second Argument: Link to the class

Example: ```OpenUScheduler.py Calculus https://sheilta.apps.openu.ac.il/pls/dmyopt2/course_info_2.PIRTAIKVUTZA?p_kurs=20466&p_semester=2019b&p_MERKAZ_LIMUD=660&p_KVUTZAT_LIMUD=01&P_KOD_PEILUT_KURS=01 ```




© Dana Griff
