from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import UserConfig
import time

# Gathers the data

# set up the webdriver 
options= Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
# TODO add check to ensure that the url is proper
driver.get(UserConfig.url)

# let the page elements to load
time.sleep(5)



popupButton = None
# click through the popup
try:
    popupButton = driver.find_element(By.CSS_SELECTOR, f"button[{UserConfig.popupButtonAttr}={UserConfig.popupButtonValue}]").click()
    print("Button Clicked")
except:
    # TODO: error handle this
    # should probably keep track of this in case the popup doesn't show up
    print("LOL SHOULDN't Happen :3")


# filter by the number of tickets 

select = None
try:
    dropdown = driver.find_element(By.CSS_SELECTOR, f"select[id={UserConfig.ticketDropdownId}]")
    print(dropdown.text)
    select = Select(dropdown)
    
except:
    print("FAILED TO FILTER")


# Try to filter if possible
if select is not None:
    try:
        select.select_by_visible_text(UserConfig.ticketDesiredAmountFilter)
    except:
        print("Failed to filter by specified amount")

        

# Collect all of the entries
currentSeats = []
ticketList = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,f"li[role={UserConfig.ticketEntryRole}]")))
for ticketEntry in ticketList:
    price = ticketEntry.get_attribute("data-price")
    seat = None
    if price is not None:
        span  = ticketEntry.find_element(By.CSS_SELECTOR, "span")
        seat = span.text
        currentSeats.append((seat,price))
print(currentSeats)
