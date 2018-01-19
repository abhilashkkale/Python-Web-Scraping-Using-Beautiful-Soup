'''
This is a simple python script to login to linked-in via user credentials and search for people based on specific skill. Then scrape the details of the search result i.e prints the links to specific individual on search page. This scraping is for only the first page.

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

'''
This function returns the driver object of selenium  which has the html page of search result
'''

def login_and_search():	
	
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

	# driver.quit()

	return driver



'''
This function scrapes and prints the search result based on the css class as 'result-image' found in html of search result provided by driver object of selenium of login_and_search() function.

'''
def get_detail_link(driver):

	soup = BeautifulSoup(driver.page_source, 'lxml')	

	for a in soup.find_all('a', class_ = 'result-image'):
		print a['href']
	
	driver.quit()

# Call get_detail_link() function and pass the driver object.
get_detail_link( login_and_search() )