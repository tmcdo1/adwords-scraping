# Adwords-Scraping
Program scrapes Google Adwords for current ads displayed for certain keywords. Uses Python3

SETUP
--------------------------------------------------------------------
This program uses Selenium for scraping the webpage. Make sure that geckodriver is installed and is in PATH in order to work. **geckodriver** can be obtained from https://github.com/mozilla/geckodriver/releases

Options are contained in the config folder:

devices.txt contains the device ids used in the google adwords url.
    Everything before the ':' is a label and is used in the result filename

keywords.txt contains the keywords used in the search.
    Each search is done on a line. If multiple searches want to be done, put keywords on different lines

regions.txt contains the location ids used in the google adwords url.
    Everything before the ':' is a label and is used in the result filename

All outputted results are contained in the results folder

DEPENDENCIES
--------------------------------------------------------------------
- geckodriver

- selenium           (try: <code>pip install selenium</code>)

- beautifulsoup4     (try: <code>pip install beautifulsoup4</code>


RUNNING
--------------------------------------------------------------------
Make sure to install **geckodriver** and add to PATH

1) To run, go to the main directory (the one with scrape.py) in a terminal.
2) Type <code>python scrape.py</code>

