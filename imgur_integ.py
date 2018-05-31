from imgurpython import ImgurClient
from config import client_id, client_secret
import random

def Random_Pic():

 client = ImgurClient(client_id, client_secret)

 items = client.gallery()
 num=random.randint(0,len(items))
 return items[num].link

def Search_Pic():

 pass
 
 
 
