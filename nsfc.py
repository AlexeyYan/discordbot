import requests
import random
from xml.etree import ElementTree

def Search_pic (tag):
 r=requests.get('https://rule34.xxx/index.php?page=dapi&s=post&q=index',params={'tags':tag})
 
 plist=[]
 
 root=ElementTree.fromstring(r.content)
 
 for child in root.iter('post'):
  plist.append(child.attrib['file_url'])
 
 url=random.choice(plist)
 return url
 
