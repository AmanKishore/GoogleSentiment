import requests
import json
import numpy as np
import pandas as pd
import sklearn
import matplotlib
import seaborn
import scipy
from pandas.io.json import json_normalize
import datetime
from pytrends.request import TrendReq
import TextAnalysisAPI
import ast
from WebScraper import scraper

text = TextAnalysisAPI.ApiClient('1f67147b09804f90a1be856eaf11f89f')

dat = scraper('https://www.google.com/search?q=facebook&rlz=1C1CHBF_enUS823US824&oq=facebook&aqs=chrome..69i57j69i60j0l4.4870j0j4&sourceid=chrome&ie=UTF-8')


total = 0
elements = 0
for x in range(len(dat)):
        r = text.get_sentiment(dat[x])
        retval = (ast.literal_eval(r.text))['documents']
        if(retval):
                total += (retval[0])['score']
                elements += 1
print(total/elements)