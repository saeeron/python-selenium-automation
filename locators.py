from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/')  # browsing amazon.com
driver.find_element(By.ID ,"nav-link-accountList").click()  # going to sign-in page

driver.find_element(By.XPATH, "//span[@class = 'a-expander-prompt']").click()  #  dropping "Need help" options
driver.find_element(By.XPATH, "//i[@class = 'a-icon a-icon-logo']")   #  finding AMAZON logo
driver.find_element(By.ID, 'ap_email').clear()  # locating e-mail field
driver.find_element(By.ID, 'continue')  # locating continue button
driver.find_element(By.XPATH, "//span[@class = 'a-expander-prompt']") # need help link
driver.find_element(By.ID, "auth-fpp-link-bottom")   # forgot your password link
driver.find_element(By.ID, "ap-other-signin-issues-link") # other issues with Sign-In link
driver.find_element(By.ID, "createAccountSubmit")  # create you Amazon account
driver.find_element(By.XPATH, "//div[@id = 'legalTextRow']/a[contains(@href ,  'condition')]") # conditions of use
driver.find_element(By.XPATH, "//div[@id = 'legalTextRow']/a[contains(@href ,  'privacy')]")  # privacy notice

sleep(5)

driver.quit()
