# Config file detailing the variables needed by the scraper at different stages
# contains the url to scrap from

class CommonConfig(object):
    url = "https://www.ticketmaster.com/hans-zimmer-live-austin-texas-01-31-2025/event/3A00616BCA113C1E" # Change to evaluate a different page
    
    # used to identify the accept and continue popup
    popupButtonText = "Accept & Continue"
    popupButtonAttr = "data-bdd"
    popupButtonValue = "accept-modal-accept-button"
class TestConfig(CommonConfig):
    url = "meme.txt"
