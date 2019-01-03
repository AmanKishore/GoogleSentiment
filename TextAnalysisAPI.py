import requests
import json
import datetime
from WebScraper import scraper

class ApiClient:

    # date = datetime.date + dateutil.relativedelta.relativedelta(months=-6)

    def __init__(self, api_key):
        self.base_url = 'https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
        self.api_key = api_key

    def get_sentiment(self, website):
        txt = {}
        txt['language'] = 'en'
        txt['id'] = 1
        txt['text'] = website
        diction = {}
        diction['documents'] = [txt]
        # var = (dict(zip([x for x in range(len(website))], website)))

        headers = {'Ocp-Apim-Subscription-Key' : self.api_key, 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

        data = requests.post(self.base_url, data=json.dumps(diction), headers=headers)
        if(data.ok):
            return data
        else:
            print("Unsuccesful: " + str(data.status_code))
            return None