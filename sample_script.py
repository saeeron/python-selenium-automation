from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome()

# open the url
driver.get("https://www.amazon.com/gp/help/customer/display.html")
driver.find_element(By.ID, "helpsearch").clear()
driver.find_element(By.ID, "helpsearch").send_keys("Cancel Order")
driver.find_element(By.ID, "helpsearch").send_keys(Keys.RETURN)

assert driver.find_element(By.XPATH, "//div/h1").text == "Cancel Items or Orders" ,"Error"

sleep(5)

driver.quit()