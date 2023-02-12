from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re

driver_path = r"C:\Users\LENOVO\Documents\Python tutorial\Elan-Naveen programs\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.google.com")
assert "Google" in driver.title
element = driver.find_element(By.NAME,"q")
element.clear()
element.send_keys("cts email id")
element.send_keys(Keys.RETURN)
assert "No results found" not in driver.page_source
matches = driver.page_source

email_lists = []

# email_pattern = re.compile("^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$")
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
emails = re.findall(email_pattern,matches)
for email in emails:
        email_lists.append(email)


for i in range(2,6):
    xpath = '//*[@id="botstuff"]/div/div[2]/table/tbody/tr/td[' + str(i+1) + ']/a'
    element = driver.find_element(By.XPATH, xpath)
    matches = driver.page_source

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(email_pattern,matches)

    for email in emails:
        email_lists.append(email)

driver.close()

for email in email_lists:
    print(email)
