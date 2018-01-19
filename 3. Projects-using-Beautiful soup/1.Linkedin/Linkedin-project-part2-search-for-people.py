
'''
This is a simple python script to login to linked-in via user credentials and search for people based on specific skill.

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

#Load the selenium chrome driver
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

#Get the linkedin signin page
driver.get('https://www.linkedin.com/uas/login?goback=&trk=hb_signin')

#Maximize the chrome instance window opened by selenium driver
driver.maximize_window()

#Specify the userid in the xpath of the username input box
email = driver.find_element_by_xpath('//*[@id="session_key-login"]')
email.send_keys('tomhankss500@gmail.com')

time.sleep(3)

#Specify the password in the xpath of the password input box
password = driver.find_element_by_xpath('//*[@id="session_password-login"]')
password.send_keys('s-p*_GY.ECn\G8k:')

time.sleep(3)

#Get the xpath of the login button and do click action
login = driver.find_element_by_xpath('//*[@id="btn-primary"]')
login.click()

time.sleep(3)

#Get the xpath of the search input and provide input as 'python programmer' 
search = driver.find_element_by_xpath('//*[@id="main-search-box"]')
search.send_keys('python programmer')

time.sleep(3)


# Do click action for search icon
button = driver.find_element_by_xpath('//*[@id="global-search"]/fieldset/button')
button.click()

time.sleep(3)

# Get the xpath of the 'People' label and  do click action on it
people = driver.find_element_by_xpath('//*[@id="search-types"]/div/ul/li[2]/a')
people.click()

time.sleep(10)

driver.quit()