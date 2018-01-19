
'''
This is a simple python script to login to linked-in via user credentials.

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Load the selenium chrome driver
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

#Get the linkedin signin page
driver.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')


#Maximize the chrome instance window opened by selenium driver
driver.maximize_window()

#Specify the userid in the xpath of the username input box
email = driver.find_element_by_xpath('//*[@id="session_key-login"]')
email.send_keys('abc@gmail.com')

time.sleep(3)

#Specify the password in the xpath of the password input box
password = driver.find_element_by_xpath('//*[@id="session_password-login"]')
password.send_keys('s-p*_GY.ECn\G8k:')

time.sleep(3)

#Get the xpath of the login button and do click action
login = driver.find_element_by_xpath('//*[@id="btn-primary"]')
login.click()

time.sleep(5)

driver.quit()



