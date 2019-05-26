from selenium import webdriver
from selenium.webdriver.support.expected_conditions import url_matches
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time


def main():
    url = 'https://sheilta.apps.openu.ac.il/pls/dmyopt2/course_info_2.PIRTAIKVUTZA?p_kurs=20466&p_semester=2019b&p_MERKAZ_LIMUD=660&p_KVUTZAT_LIMUD=01&P_KOD_PEILUT_KURS=01'

    browser = webdriver.Chrome(r"C:\Users\Dana\bin\chromedriver.exe")
    browser.get(url)

    username = browser.find_element_by_css_selector('#p_user')
    username.send_keys('GRDANA24')
    
    password = browser.find_element_by_css_selector('#p_sisma')
    password.send_keys('Florence250615')
    
    id = browser.find_element_by_css_selector('#p_mis_student')
    id.send_keys('312486707')
    
    button = browser.find_element_by_css_selector('input[type=submit]')
    button.click()
    
    WebDriverWait(browser, 90).until(
        url_matches('https://sheilta.apps.openu.ac.il/pls/dmyopt2/myop.myop_screen')
    )
    
    browser.get(url)

    html = browser.find_element_by_css_selector('body').get_attribute('innerHTML')
    
    bs = BeautifulSoup(html)
    table = bs.select('table > tbody > tr:nth-child(6) > td > table > tbody')[0]
    for row in table.find_all('tr')[1:-1]:
        tds = row.find_all('td')
        
        print('{} -- {} -- {}'.format(tds[4].text.strip(), tds[3].text.strip(), tds[0].text.strip()))
    
    
    time.sleep(5)
    browser.quit()

if __name__=="__main__":
    main()
    
    
    
    
