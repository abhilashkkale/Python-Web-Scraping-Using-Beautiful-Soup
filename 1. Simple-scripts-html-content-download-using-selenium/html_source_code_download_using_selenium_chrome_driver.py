from selenium import webdriver

# Specify the path of selenium chrome driver exe to load the driver
driver = webdriver.Chrome(executable_path = r'C:\chromedriver_win32\chromedriver.exe')

# Get the mentioned html page using the selenium chrome driver
driver.get('http://python.org')

# Store the page source i.e html in the html_doc variable.
html_doc = driver.page_source

# Print source code
print html_doc