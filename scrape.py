import datetime
import re
import time
import os
import random
from selenium import webdriver
from bs4 import BeautifulSoup

keyword_list = []

region_codes = []
region_labels = []

device_codes = []
device_labels=[]

date = datetime.datetime

#regex definitions
label_re = re.compile('(.*):')
code_re = re.compile(':(.*)')

#selenium browser driver
driver = webdriver.Firefox()

with open('./config/keywords.txt') as kwd_file:
    for line in kwd_file:
        line = line.replace(' ', '+')
        line = str.strip(line)
        keyword_list.append(line)

with open('./config/regions.txt') as reg_file:
    for line in reg_file:
        region_labels.append(label_re.search(line).group(1))
        region_codes.append(code_re.search(line).group(1))

with open('./config/devices.txt') as dev_file:
    for line in dev_file:
        device_labels.append(label_re.search(line).group(1))
        device_codes.append(code_re.search(line).group(1))

for d_ind in range(0, len(device_codes)):
    for r_ind in range(0, len(region_codes)):
        for k_ind in range(0, len(keyword_list)):
            adwords_url = 'https://adwords.google.com/anon/AdPreview?lang=en&loc='+region_codes[r_ind]+'&device='+device_codes[d_ind]+'&st='+keyword_list[k_ind]
            driver.get(adwords_url)
            time.sleep(random.randint(10,20))

            adwords_html = BeautifulSoup(driver.page_source, 'html.parser')
            iframe = adwords_html.find("iframe", class_='iframe-preview')
            src_url = iframe['src']

            driver.get(src_url)
            search_results = BeautifulSoup(driver.page_source, 'html.parser')
            ads = search_results.find_all(class_="ads-ad")

            time_str = date.now().strftime('%H-%M')
            date_str = date.now().strftime('%m-%d-%y')

            file_path = './results/'+date_str+'/'+region_labels[r_ind]+'-'+keyword_list[k_ind]+'-'+device_labels[d_ind]+'_'+time_str+'.html'

            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(file_path,'w',encoding='UTF-8') as out_file:
                out_file.write(str(ads))
            time.sleep(random.randint(10,20)) #For putting a delay between requests to not be as suspicious as a bot

driver.close()
