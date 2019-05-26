from selenium import webdriver
from selenium.webdriver.support.expected_conditions import url_matches
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup

import json
import sys
import os
import datetime
import time
import urllib.parse

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file as my_file
from oauth2client import client, tools

SCOPES = 'https://www.googleapis.com/auth/calendar'

def calendar_service():
    store = my_file.Storage(full_path('token.json'))
    creds = store.get()
    print(creds)
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(full_path('credentials.json'), SCOPES)
        creds = tools.run_flow(flow, store)
    return build('calendar',
                 'v3',
                 http=creds.authorize(Http()))
                 
def full_path(file_name):
    if getattr( sys, 'frozen', False ): # running in a bundle
        dir_path = os.path.dirname(sys.executable)
        return os.path.join(dir_path, file_name)
    else : # running live
        dir_path = os.path.dirname(__file__)
        return os.path.join(dir_path, file_name)


def retrieve_settings():
    with open(full_path('settings.json')) as settings_file:
        try:
            json_data = json.load(settings_file)
            return json_data
        except ValueError:
            print('The JSON File is corrupted, modify the setting file and re-run the script')
            sys.exit()



def main(data,name,url):
    counter = 0
    url = 'https://sheilta.apps.openu.ac.il/pls/dmyopt2/course_info_2.PIRTAIKVUTZA?p_kurs=20466&p_semester=2019b&p_MERKAZ_LIMUD=660&p_KVUTZAT_LIMUD=01&P_KOD_PEILUT_KURS=01'
    
    browser = webdriver.Chrome(r"C:\Users\Dana\bin\chromedriver.exe")
    browser.get(url)

    username = browser.find_element_by_css_selector('#p_user')
    username.send_keys(data["username"])
    
    password = browser.find_element_by_css_selector('#p_sisma')
    password.send_keys(data["password"])
    
    id = browser.find_element_by_css_selector('#p_mis_student')
    id.send_keys(data["id"])
    
    button = browser.find_element_by_css_selector('input[type=submit]')
    button.click()
    
    WebDriverWait(browser, 90).until(
        url_matches('https://sheilta.apps.openu.ac.il/pls/dmyopt2/myop.myop_screen')
    )
    
    browser.get(url)

    html = browser.find_element_by_css_selector('body').get_attribute('innerHTML')
    
    bs = BeautifulSoup(html,features="html.parser")
    table = bs.select('table > tbody > tr:nth-child(6) > td > table > tbody')[0]
    
    eventDateTimesStart = []
    eventDateTimesEnd = []
    
    for row in table.find_all('tr')[1:-1]:
        tds = row.find_all('td')
        date = tds[4].text.strip().split('.')
        time = tds[3].text.strip().split(' - ')
        eventDateTimesStart.append(date[2] + '-' + date[1] + '-' + date[0]+'T'+time[0]+':00')
   
        eventDateTimesEnd.append(date[2] + '-' + date[1] + '-' + date[0]+'T'+time[1]+':00')
    
    try:
        calendar_id = data["calender_id"]
    except KeyError:
        print('The calendar id setting is missing, modify the setting file and re-run the script')
        sys.exit()

    if calendar_id == '':
        print('The calendar id is empty, modify the setting file and re-run the script')
        sys.exit()

    service = calendar_service()
    
    i = 0 
    while i < len(eventDateTimesStart): 
        event = {
          'summary': name,
          'start': {
            'dateTime': eventDateTimesStart[i],
            'timeZone': 'Asia/Jerusalem',
          },
          'end': {
            'dateTime': eventDateTimesEnd[i],
            'timeZone': 'Asia/Jerusalem',
          }
        }
        event = service.events().insert(calendarId=calendar_id, body=event).execute()
        counter += 1
        i += 1
        
    print('{} {}'.format(counter,'Events were created successfully'))

if __name__=="__main__":
    data = retrieve_settings()
    print(sys.argv[2])
    
    main(data,sys.argv[1],sys.argv[2])
    
    
    #TODO: url not working as argument        
    
    
