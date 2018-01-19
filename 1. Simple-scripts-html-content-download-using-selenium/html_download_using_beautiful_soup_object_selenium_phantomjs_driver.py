'''
This is a simple script which create a beautiful soup object and displays the html content of http://python.org fetched by selenium using phantomjs driver
'''

from selenium import webdriver
from bs4 import BeautifulSoup

# Specify the path of selenium phantomjs exe to load the driver
driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# Get the mentioned html page using the selenium phantomjs
driver.get('http://python.org')

# Store the page source i.e html in the html_doc variable.
html_doc  = driver.page_source

# Beautiful soup takes to params 1st html document and 2nd the parser
soup = BeautifulSoup(html_doc, 'lxml')

# Print the html content in pretty format.
print soup.prettify()

# Quit the driver
driver.quit()