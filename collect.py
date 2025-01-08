from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from config import CommonConfig
import time

# Gathers the data

# set up the webdriver 
options= Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get(CommonConfig.url)

# load the page
time.sleep(5)

# elements = driver.find_elements(By.TAG_NAME,"button")
# for e in elements:
#     if e.text == CommonConfig.popupButtonText:
#         print(e.get_attribute(CommonConfig.popupButtonAttr))
    # popupButtonAttr = "data-bdd"
    # popupButtonValue = "accept-modal-accept-button"
element = driver.find_element(By.CSS_SELECTOR, f"button[{CommonConfig.popupButtonAttr}={CommonConfig.popupButtonValue}]")
print(element.text)
# with open("temp.txt", "w", encoding="utf-8") as f:
#     f.write(driver.page_source)
driver.close()
