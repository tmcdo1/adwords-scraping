# Adwords-Scraping
Program scrapes Google Adwords for current ads displayed for certain keywords.

This program uses Selenium for scraping the webpage. Make sure that geckodriver is installed and is in PATH in order to work. geckodriver can be obtained from https://github.com/mozilla/geckodriver/releases

Options are contained in the config folder:

devices.txt contains the device ids used in the google adwords url.
    Everything before the ':' is a label and is used in the result filename

keywords.txt contains the keywords used in the search.
    Each search is done on a line. If multiple searches want to be done, put keywords on different lines

regions.txt contains the location ids used in the google adwords url.
    Everything before the ':' is a label and is used in the result filename

All outputted results are contained in the results folder
