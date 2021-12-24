from logging import error
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

driver = webdriver.Chrome()

def login():

    url = "https://businesscentral.dynamics.com/?company=AMD%20Medicom%20Inc&page=7335&dc=0&bookmark=35%3bmBwAAAJ7%2f0EATQBEAC0AUwBIADAAMAAwADQAMQA0"
    driver.get(url)


def ship_lines():
        
        url = "https://businesscentral.dynamics.com/?company=AMD%20Medicom%20Inc&page=7335&dc=0&bookmark=35%3bmBwAAAJ7%2f0EATQBEAC0AUwBIADAAMAAwADQAMQA0"
        driver.get(url)

        time.sleep(1)

def sweep_run():
    frame = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(frame)
        
    for x in range(0, 5000):
        try:
            time.sleep(1)

            process = driver.find_element_by_xpath("//span[@aria-label='Process']")
            process.click()

            time.sleep(0.5)

            create_pick = driver.find_element_by_xpath("//span[@aria-label='Create Pick...']")
            create_pick.click()

            time.sleep(1)

            first_verification = driver.find_element_by_xpath("//body/div/div/form[@role='dialog']/div/div/div/button[1]")
            first_verification.click()

            time.sleep(1)

            second_verification = driver.find_element_by_xpath("//span[normalize-space()='OK']")
            second_verification.click()

            time.sleep(1.5)

            next_shipline = driver.find_element_by_xpath("//i[contains(text(),'')]")
            next_shipline.click()

        except:
            pass    
