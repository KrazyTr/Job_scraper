from selenium import webdriver
import time
# import pandas as pd
# import os

# from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
url1 = "https://in.linkedin.com/jobs/python-developer-jobs?keywords=Python%20Developer&location=India&locationId=&geoId=102713980&f_TPR=r604800&f_E=2&original_referer=https%3A%2F%2Fin.linkedin.com%2Fjobs%2Fpython-developer-jobs%3Fkeywords%3DPython%2520Developer%26location%3DIndia%26locationId%3D%26geoId%3D102713980%26f_TPR%3D%26f_E%3D2%26position%3D1%26pageNum%3D0&position=1&pageNum=0"

driver = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"), options=options)

driver.get(url1)
driver.implicitly_wait(15)

def is_see_more_button_present():
    try:
        driver.find_element(By.CSS_SELECTOR, "button.infinite-scroller__show-more-button")
        return True
    except NoSuchElementException:
        return False

# Click the "See more jobs" button repeatedly until it is no longer visible
click_count = 0
while is_see_more_button_present() and click_count < 5:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  

    # Scroll up a bit
    driver.execute_script("window.scrollBy(0, -100);")
    time.sleep(3)  
    # Scroll down to the bottom of the page to make the button visible
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    driver.execute_script("window.scrollBy(0, -100);")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except ElementNotInteractableException:
        print("ElementNotInteractableException: Element is not interactable.")
        break

    
    see_more_button = driver.find_element(By.CSS_SELECTOR, "button.infinite-scroller__show-more-button")
    see_more_button.click()
    click_count += 1
    time.sleep(2)  


company_list = []
job_titles = WebDriverWait(driver, 60).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "base-search-card__subtitle"))
)
for job_title in job_titles:
    company_list.append(job_title.text)

print(company_list)

# Close the browser
driver.quit()