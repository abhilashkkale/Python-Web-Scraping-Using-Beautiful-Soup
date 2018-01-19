from selenium import webdriver

# Specify the path of selenium phantomjs exe to load the driver
driver = webdriver.Chrome(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# Get the mentioned html page using the selenium phantomjs
driver.get('http://python.org')

# Store the page source i.e html in the html_doc variable.
html_doc = driver.page_source

# Print source code
print html_doc