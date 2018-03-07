#! python3
# toHotmailFirefox.py - Automatically opens your Hotmail using Firefox

from selenium import webdriver
import time

#Opening the Outlook webpage
browser = webdriver.Firefox()
browser.get("https://outlook.live.com/owa/?authRedirect=true")
browser.find_element_by_xpath('/html/body/section/div/div[2]/div[2]/div/div').click()
time.sleep(2)

#Introducing the email
emailElement = browser.find_element_by_xpath('//*[@id="i0116"]')
emailElement.send_keys("example@hotmail.com")
browser.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(2)

#Introducing the password
passElement = browser.find_element_by_xpath('//*[@id="i0118"]')
passElement.send_keys("example_password")
browser.find_element_by_xpath('//*[@id="idSIButton9"]').click()
