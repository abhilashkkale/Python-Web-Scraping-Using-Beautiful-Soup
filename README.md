# Python-Web-Scraping-Using-Beautiful-Soup
This repository contains web scraping scripts and projects created using Python, Selenium and Beautiful Soup.

1. Simple-scripts-html-content-download-using-selenium folder contains python scripts to download html page using Selenium Chrome Driver and Phantom JS
2. Beautiful-soup-scripts-step-by-step folder contains python scripts for using different features of Beautiful Soup.
3. Projects-using-Beautiful soup folder contains web scraping projects created using Python, Selenium and Beautiful Soup.

Python Installation :

1] Python3: - Windows Users: - Visit https://www.python.org/ to download the latest Python 3.X. - Install Python 3.X - Linux Users (Debian): - Python is usually shipped with most of the Linux distributions. If it's not installed in your machine, you can use the following command: - sudo apt-get install python

2] Set up environment paths: - Windows Users: - Open the Control Panel (easy way: click in the Windows search on your task bar and type ?Control Panel? then click the icon). - In the Control Panel, search for Environment; click Edit the System Environment Variables. Then click the Environment Variables button. - In the User Variables section, we will need to either edit an existing PATH variable or create one. If you are creating one, make PATH the variable name and add the following directories to the variable values section as shown, separated by a semicolon. If you?re editing an existing PATH, the values are presented on separate lines in the edit dialog. Click New and add one directory per line. - C:\Python35-32;C:\Python35-32\Lib\site-packages\;C:\Python35-32\Scripts\ - (Replace 35-32 with installed version (Check C: drive to know the installed exact version) - Linux Users (Debian): - No need to setup environment paths.

3] To manage software packages for Python, install using following command: - pip sudo apt-get install -y python3-pip

4] To check pip version installed : - pip --version

5] Packages: (Administrator rights might be needed for installation): - Windows Users: - Go to C:\python x.x folder (where x.x is the version of installed Python) - Hold down shift and right click inside the folder then click on open command window here - Enter python and see which version you are running - Quick Tip: Folder name indicates the version. - Go to scripts folder, Hold down shift and right click inside the folder, then click on "Open Command Window Here", and then type - pip3 install requests openpyxl lxml scrapy - Linux Users (Debian): - Use the following command to install the required packages: - sudo -H pip3 install requests openpyxl lxml scrapy