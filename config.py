# Config file detailing the variables needed by the scraper at different stages
# contains the url to scrap from

class CommonConfig(object):
    # Configs related to scraping the data
    # Change this if the scraping job is failing; should be general for most TM pages

    # used to identify the accept and continue popup
    popupButtonText = "Accept & Continue"
    popupButtonAttr = "data-bdd"
    popupButtonValue = "accept-modal-accept-button"


    # used to filter by number of tickets
    ticketDropdownId = "filter-bar-quantity"

    # used to process ticket entries
    ticketEntryRole = "menuitem"
    ticketEntryTitle = "Section Description"
    

class UserConfig(CommonConfig):
    # Configs based on the user's preference
    # Change this if you are looking for different elements
    url = "https://www.ticketmaster.com/post-malone-presents-the-big-ass-salt-lake-city-utah-04-29-2025/event/1E00616FD6842BE7" # Change to evaluate a different page
    ticketDesiredAmount = 1



    ticketDesiredAmountFilter = "1 Ticket" if ticketDesiredAmount == 1 else f"{ticketDesiredAmount} Tickets"

    