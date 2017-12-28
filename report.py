import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import datetime
import os

def create_data_frame():
    new_frame = pd.DataFrame()

def find_domain():
    re_domain = re.compile('(\w*)\.(\w*)')

def update_report(keyword, region):
    date = datetime.datetime
    report_filename = keyword+'_'+region+'_'+date.year+'-'+date.month
    
    os.path.isfile('./reports/'+report_filename)
    in_report = pd.read_excel('./reports/'+report_filename)

