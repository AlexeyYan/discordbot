import requests
import json
from config import accuw_key

def Daily_Forecast():
    r=requests.get('http://dataservice.accuweather.com/forecasts/v1/daily/5day/28580', params={'apikey':accuw_key, 'language':'ru'})
    date=r.json()['Headline']['EffectiveDate']
    day=r.json()['DailyForecasts'][1]
    temperature=str(day['Temperature']['Minimum']['Value'])+' - '+str(day['Temperature']['Maximum']['Value'])
    dayw=day['Day']['IconPhrase']
    nightw=day['Night']['IconPhrase']
    result=str(date)+'```\n'+'Днём: '+dayw+'\n'+'Ночью: '+nightw+'\n'+'Температура в течении суток: '+temperature+'\n```'
    return result
