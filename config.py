# Config file detailing the variables needed by the scraper at different stages
# contains the url to scrap from

class CommonConfig(object):
    # Configs related to scraping the data
    # Change this if the scraping job is failing

    # used to identify the accept and continue popup
    popupButtonText = "Accept & Continue"
    popupButtonAttr = "data-bdd"
    popupButtonValue = "accept-modal-accept-button"


    # used to filter by number of tickets
    ticketDropdownId = "filter-bar-quantity"
    
    

class UserConfig(CommonConfig):
    # Configs based on the user's preference
    # Change this if you are looking for different elements
    url = "https://www.ticketmaster.com/hans-zimmer-live-austin-texas-01-31-2025/event/3A00616BCA113C1E" # Change to evaluate a different page
    ticketDesiredAmount = 1
    
    ticketDesiredAmountFilter = "1 Ticket" if ticketDesiredAmount == 1 else f"{ticketDesiredAmount} Tickets"
