from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from config import UserConfig,CustomUserConfig
import time



class DataCollector:

    def __init__(self,config):
        self.options = Options()
        self.options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=self.options)
        
        self.config = config
        self.driver.set_page_load_timeout(self.config.timeout)

        self.outputBuffer = []
    # connect the web driver to the url
    def connect(self):
        try:
            self.driver.get(self.config.url)
            print("Page Loaded")
        except Exception as e:
            print("Page Loading failed: ",e)
            self.driver.close()
            raise
    
    # remove intro popup
    def popup(self):
        try:
            popupButton = WebDriverWait(self.driver, self.config.timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"button[{self.config.popupButtonAttr}={self.config.popupButtonValue}]")))
            popupButton.click()
            self.popup = True
            print("Popup detected and successfully removed")
        except Exception as e:
            print("Popup unsuccessfully detected/removed: ",e)
            # don't reraise, The popup might not exist (which is fine).
    

    # filters by the number of ticket
    # this is necessary as it impacts the tickets shown
    def filter(self):
        # Get the filter if possible
        try:
            dropdown = self.driver.find_element(By.CSS_SELECTOR, f"select[id={self.config.ticketDropdownId}]")
            select = Select(dropdown)
            select.select_by_visible_text(self.config.ticketDesiredAmountFilter)
            print("Successfully filter tickets by seat count")
        except NoSuchElementException as e:
            # improper value
            # default to one
            print(f"Could not filter by {self.config.ticketDesiredAmountFilter}")
            try:
                select.select_by_visible_text("1 Ticket")
            except:
                print("Could not filter by 1 ticket")
                raise
        except Exception as e:
            print("Unable to find the filter option")
            raise
        
    # performs the collection job
    def collect(self):
        try:
            ticketList = WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,f"li[role={self.config.ticketEntryRole}]")))
            for ticketEntry in ticketList:
                price = ticketEntry.get_attribute("data-price")
                seat = None
                if price is not None:
                    try:
                        span  = ticketEntry.find_element(By.CSS_SELECTOR, "span")
                        seat = span.text
                        self.outputBuffer.append((seat,price))
                    except:
                        # can't find the corresponding entry
                        # log this issue but continue scanning
                        print("Unable to collect corresponding seatname to entry")
                        pass
        except:
            print("Could not collect tickets")
            raise
    
    # main entrypoint to the collection process
    def run(self):
        try:
            self.connect()
            self.popup()
            self.filter()
            self.collect()
            print(self.outputBuffer)
        except:
            # unable to finish the collection process
            print("Error: The DataCollector is unable to collect the tickets")
        finally:
            self.driver.close()
        

if __name__ =='__main__':
    collector = DataCollector(UserConfig)
    collector.run()





# # set up the webdriver 
# options= Options()
# options.add_argument("--headless=new")
# driver = webdriver.Chrome(options=options)

# try:
#     driver.get(UserConfig.url)
#     print("Page Loaded")
# except Exception as e:
#     print("Page Loading failed")

# popupButton = None
# # click through the popup
# try:
#     popupButton = driver.find_element(By.CSS_SELECTOR, f"button[{UserConfig.popupButtonAttr}={UserConfig.popupButtonValue}]").click()
#     print("Button Clicked")
# except:
#     # TODO: error handle this
#     # should probably keep track of this in case the popup doesn't show up
#     print("LOL SHOULDN't Happen :3")


# # filter by the number of tickets 
# select = None
# try:
#     dropdown = driver.find_element(By.CSS_SELECTOR, f"select[id={UserConfig.ticketDropdownId}]")
#     print(dropdown.text)
#     select = Select(dropdown)
    
# except:
#     print("FAILED TO FILTER")


# # Try to filter if possible
# if select is not None:
#     try:
#         select.select_by_visible_text(UserConfig.ticketDesiredAmountFilter)
#     except:
#         print("Failed to filter by specified amount")

        

# # Collect all of the entries
# currentSeats = []
# ticketList = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,f"li[role={UserConfig.ticketEntryRole}]")))
# for ticketEntry in ticketList:
#     price = ticketEntry.get_attribute("data-price")
#     seat = None
#     if price is not None:
#         span  = ticketEntry.find_element(By.CSS_SELECTOR, "span")
#         seat = span.text
#         currentSeats.append((seat,price))
