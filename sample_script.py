from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

# setting up driver as chrome_driver and waits
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.wait = WebDriverWait(driver, 10)


# open the url
driver.get("https://www.amazon.com/wholefoodsdeals")

element = driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-action-type = 'DISMISS']")))
element.click()

elements = driver.find_elements(By.CSS_SELECTOR, "#wfm-pmd_deals_section [class *= 'regular-price' ]")
elements2 = driver.find_elements(By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")
for elem, elem2 in zip(elements, elements2):
    print(elem.text)
    print(elem2.text)
