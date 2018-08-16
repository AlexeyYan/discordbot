import discord
import random
import asyncio
import pickle
import os
import requests
import json
import logging
import time
from vk_integ import *
from imgur_integ import *
from wolfram_integ import *
from funs import *
#from google_integ import *
from accuw_integ import *
from games import *
from config import discord_token

logging.basicConfig(filename="log.txt", level=logging.INFO)
try:
 commands=''
 comand_list = ['\n!help - показать список команд','\n!goals - показать список текущих целей','\n!rasp - расписание пар на завтра','\n!rgoals - добавить цель','\n!randvk - случайный мем из вк (могут быть аморальные)','\n!randpic - случайная картинка','\n!joke - случайный анекдот','\n!wolf - запрос к wolframalpha']
 for i in range (len(comand_list)):
  commands = commands+comand_list[i]

 client = discord.Client()
 @client.event
 async def on_ready():
  print('Logged on')
  print(client.user.name)
  print(client.user.id)
  print("-------------")
  logging.info("Bot started")

 @client.event
 async def on_message(message):
   if message.content.startswith('!goals'):
       f=open('discordbot/goals.txt','r')
       mp=f.read();
       f.close
       logging.info(time.ctime(time.time())+"Call the command !goals")
       await client.send_message(message.channel,mp)
  
   elif message.content.startswith('!ping'):
          await client.send_message(message.channel, 'pong')
 
   elif message.content.startswith('!help'):
          await  client.send_message(message.channel,'```Спискок команд:' + commands + ' ```')
   
   elif message.content.startswith('!isalexcool'):
          await client.send_message(message.channel,'Of course!')
  
   elif message.content.startswith('!rasp'):
          r=requests.get('https://students.bsuir.by/api/v1/studentGroup/schedule?studentGroup=740401')
          week=requests.get('http://students.bsuir.by/api/v1/week').json()
          leng=len(r.json()['tomorrowSchedules'])
          i=0
          if r.json()['tomorrowSchedules']!=[]:
             while i<leng:
               if week in r.json()['tomorrowSchedules'][i]['weekNumber'] or r.json()['tomorrowSchedules']!=None:
                  time=('Время: ' + r.json()['tomorrowSchedules'][i]['lessonTime'])
                  sub=('Предмет: ' + r.json()['tomorrowSchedules'][i]['subject']+' ('+r.json()['tomorrowSchedules'][i]['lessonType']+')')
                  aud=('Аудитория: ' + r.json()['tomorrowSchedules'][i]['auditory'][0])
                  await client.send_message(message.channel,time + '\n' + sub + '\n' + aud +'\n'+'----------------\n')
                  i+=1
          else: await client.send_message(message.channel,'Завтра пар нет, гуляем)')
  
   elif message.content.startswith('!randvk'):
        if message.content.startswith('!randvk bntu'):
         mem=Random_BNTU_Mem()
        else:
          if message.content.startswith('!randvk it'):
           mem=Random_IT_Mem()
          else:
           mem=Random_VkMem()
        await client.send_message(message.channel,mem)

   elif message.content.startswith('!randpic'):
        pic = Random_Pic()
        await client.send_message(message.channel,pic)

   elif message.content.startswith('!joke'):
        joke = Random_Joke()
        await client.send_message(message.channel,joke)
 
   elif message.content.startswith('!wolf'):
        question=str(message.content[6:])
        answer = Question(question)
        await client.send_message(message.channel,answer)
 
  # elif message.content.startswith('!google'):
   #     message=message.content[8:]
    #    res=Google_Search(message)
     #   print(res)
 
   elif message.content.startswith('!dice'):
        cube1, cube2 = Dice()
        name=message.author.name
        await client.send_message(message.channel, name+': выпало '+cube1+' и '+cube2)
 
   #elif message.content.startswith('!wolf'):
    #    question=str(message.content[6:])
     #   if message.content.startswith('!wolf plot'):
      #      answer=Plot(question)
       # elif message.content.startswith('!wolf solve'):
        #    answer=Solve(question)
        #else: answer = Question(question)
       # await client.send_message(message.channel,answer)
   
   elif message.content.startswith('!flip'):
        if random.randint(0,1000)<=453 : ans = 'Орёл'
        else: ans = 'Решка'
        await client.send_message(message.channel,'Выпало: '+ans)
 
   elif message.content.startswith('!weather'):
        result=Daily_Forecast()
        await client.send_message(message.channel,result)
 
   elif message.content.startswith('!curs'):
        if message.content[6:]=='all':
           curs=Curs_All()
        else: 
           if message.content[6:]=='btc':
              curs=Curs_BTC()
           else:
              curs=Curs()
        await client.send_message(message.channel, curs)
   
   elif message.content.startswith('!test'):
       await client.send_message(message.channel,':sunny:')
 client.run(discord_token)
except Exception:
 print('Fatal error!')
 ErrorAlarm()
