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

def sentiment(keyword):

        text = TextAnalysisAPI.ApiClient('1f67147b09804f90a1be856eaf11f89f')


        dat = scraper('https://www.google.com/search?q=' + keyword)


        total = 0
        elements = 0
        for x in range(len(dat)):
                r = text.get_sentiment(dat[x])
                retval = (ast.literal_eval(r.text))['documents']
                if(retval):
                        total += (retval[0])['score']
                        elements += 1
        retstring = 'The sentiment of: ' +  keyword + ' is ' + str(total/elements)
        return retstring

print(sentiment('Trump'))