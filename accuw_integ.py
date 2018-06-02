import requests
import json
from config import accuw_key

def Daily_Forecast():
    r=requests.get('http://dataservice.accuweather.com/forecasts/v1/daily/1day/28580', params={'apikey':accuw_key, 'lqnguage':'ru'})
    date=r.json()['Headline']['EffectiveDate']
    day={r.json().['DailyForecasts']
