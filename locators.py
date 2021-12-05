from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/')  # browsing amazon.com
driver.find_element(By.ID, "nav-link-accountList").click()  # going to sign-in page

driver.find_element(By.ID, "createAccountSubmit").click()  # browsing "create account" page
driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")  # this is the logo
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")  # "create account" header
driver.find_element(By.ID, "ap_customer_name")   # "name" field
driver.find_element(By.ID, "ap_email")     # email field
driver.find_element(By.ID, "ap_password")   # password field
driver.find_element(By.ID, "ap_password_check")   # confirm password field
driver.find_element(By.ID, "continue") # continue button
driver.find_element(By.CSS_SELECTOR, "[href *= 'condition']") # condition of use
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href *= 'privacy']")   # privacy notice
driver.find_element(By.CSS_SELECTOR, "[href *= 'signin']")    # sign-in page

driver.quit()
