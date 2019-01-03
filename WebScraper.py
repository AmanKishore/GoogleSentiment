'''
Web Scraper:
    This file scrapes data from a website.
'''

import urllib.request
import requests
from bs4 import BeautifulSoup
import json

def scraper(webpage):
    data = requests.get(webpage)
    soup = BeautifulSoup(data.text, 'html.parser')    

    list_data = soup.find_all(class_='s')
    only_data = []
    for text in list_data:
        only_data.append(text.find(class_='st'))

    final_list = []
    for vals in only_data:
        if vals:
            for content in vals.contents:
                if str(content)[:2] != '<b':                
                    final_list.append(content)

    # textdat = tree.xpath('//*[@id="rso"]/div[3]/div/div[1]/div/div/div[2]/div/text()')
    return final_list