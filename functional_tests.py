from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"C:/Users/Owner/AppData/Local/Mozilla Firefox/firefox.exe"
browser = webdriver.Firefox(options=options, executable_path="C:/Users/Owner/Documents/WEB 2210/geckodriver.exe")
browser.get('http://localhost:8000')

assert 'Django' in browser.title
