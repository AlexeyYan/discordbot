from googleapiclient.discovery import build
from config import api_key, cse_id

def Google_Search(message):
 service = build("customsearch", "v1", api_key)
 res = service.cse().list(q=message,cx=cse_id,num=10).execute()
 return res
