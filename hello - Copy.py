def login():

    print("[=] Attempting to Login")
    # Interact with login button on naukri.com
    login_button_xpath = '//*[@id="login_Layer"]'
    login_button = driver.find_element(By.XPATH, login_button_xpath)
    login_button.click()

    time.sleep(3)
    # Interact with enter email and password button
    email_input_button_xpath = '//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[2]/input'
    password_input_button_xpath = '//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[3]/input'

    print("[=] Attempting to Login: Entering username")
    time.sleep(3)
    # Enter email ID
    email_input_button = driver.find_element(By.XPATH, email_input_button_xpath)
    email_input_button.send_keys('******')

    time.sleep(5)
    # Enter password
    password_input_button = driver.find_element(By.XPATH, password_input_button_xpath)
    password_input_button.send_keys('*****')

    print("[=] Attempting to Login: Entering password")
    time.sleep(4)
    # Click login button
    login_button_to_click_xpath = '//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[6]/button'
    driver.find_element(By.XPATH, login_button_to_click_xpath).click()

    print("[=] Clicking the login button")
    print('\n')
    time.sleep(20)


def open_link(job_link):
    print("Link opened", job_link)
    # Open the URL for job search
    driver.get(job_link)
    print("Opened link")
    time.sleep(15)
    job_list = driver.find_elements(By.XPATH, '//*[@id="root"]/div[4]/div/div/section[2]/div[2]/article')
    print("Found the Job List")
    for job in job_list:
        #job.click()
        #print(job)

        job_name = job.text
        #print(job_name, job.get_attribute('a'))
        print('\n')
        display.display("[+] Trying For: ", job_name.partition('\n')[0])

        open_job_link(job)
        #driver.close()
        #apply()


def open_job_link(job):
    job.click()
    print("Opening the tab")
    # Sleep
    time.sleep(10)
    is_already_applied_question()
    print("Closing the tab")
    pyautogui.hotkey('ctrl', 'w')

"""
def is_already_applied_question():
    time.sleep(20)
    try:
        already_applied_xpath = '//*[@id="root"]/main/div[2]/div[1]/section[1]/div[2]/div[2]'
        already_applied = driver.find_element(By.XPATH, already_applied_xpath)
        print("Contained Text: ", already_applied.text)

        if (already_applied.text == 'Applied'):
            print("[-] Already Applied for this Job")
        elif ("Apply on company site" in already_applied.text):
            print("[++] Needs to be applied on company website")
            print("Use this: ", driver.current_url)
        else:
            print("[+] Haven't applied for this Job")
            click_apply_button()
    except:
        print('[=] Probably Not Applied')
"""

def is_already_applied_question():
    time.sleep(20)
    try:
        already_applied_xpath = '//*[@id="root"]/main/div[2]/div[1]/section[1]/div[2]/div[2]'
        already_applied = driver.find_element(By.XPATH, already_applied_xpath)
        print("Contained Text: ", already_applied.text)

        if (already_applied.text == 'Applied'):
            print("[-] Already Applied for this Job")
        elif ("Apply on company site" in already_applied.text):
            print("[++] Needs to be applied on company website")
            print("Use this: ", driver.current_url)
        else:
            print("[+] Haven't applied for this Job")
            click_apply_button()
    except:
        print('[=] Jumping Over Again')

def click_apply_button():
    apply_button_xpath = '//*[@id="root"]/main/div[2]/div[1]/section[1]/div[2]/div[2]/button[2]'
    apply_button = driver.find_element(By.XPATH, apply_button_xpath)

    # Since url changes when successfully applied, we will use it to compare if we applied or not
    # which means if previous_url == current_url then apply was unsuccessful
    # if not, then it probably means that apply was successful
    previous_url = driver.current_url
    # print(apply_button.text)
    apply_button.click()

    time.sleep(10)
    success_metric = driver.current_url
    print(success_metric)

    if (previous_url == success_metric):
        print("Failed to Apply for Job")
    else:
        print("Successfully Applied for Job")

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import pyautogui
from IPython import display

link_to_open = "http://www.naukri.com/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(link_to_open)

login()

job_link_1 = 'https://www.naukri.com/web-scraping-jobs-in-hyderabad-secunderabad?k=web%20scraping&l=hyderabad%20secunderabad&nignbevent_src=jobsearchDeskGNB'
job_link_2 = 'https://www.naukri.com/python-pandas-jobs-in-hyderabad-secunderabad?k=python%20pandas&l=hyderabad%20secunderabad&nignbevent_src=jobsearchDeskGNB'
job_link_3 = 'https://www.naukri.com/data-analyst-jobs-in-hyderabad-secunderabad?k=data%20analyst&l=hyderabad%20secunderabad&nignbevent_src=jobsearchDeskGNB'

open_link(job_link_1)

time.sleep(10)
driver.quit()