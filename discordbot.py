import discord
import random
import asyncio
import pickle
import os
import requests
import json
from nsfc import *
from vk_integ import *
from imgur_integ import *
from wolfram_integ import *
from google_integ import *
from games import *
from config import discord_token
from datetime import datetime
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
 

@client.event
async def on_message(message):
  time=str(datetime.now())
  if message.content.startswith('!goals'):
   try:
      f=open('discordbot/goals.txt','r')
      mp=f.read();
      f.close
      await client.send_message(message.channel,mp)
   except:
      f=open('discordbot/logs.txt','a')
      f.write(time+' Ошибка работы с командой !goals')
      f.close
 
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
  
  elif message.content.startswith('!rgoals'):
       goals_list=[] 
       username = message.author.name
       f=open('discordbot/goals.txt','a')
       goals_list.append(message.content[8:])
       print('Пользователь ' + username + ' добавил цель:\n- ' + goals_list[0] + ' -')
       f.write('- '+goals_list[0]+'\n-----------------------\n')
       f.close
       if message.server.name== 'Lamp Night':
        main=message.server.get_channel('425280734614519830')
       elif message.server.name== 'Bots':
        main=message.server.get_channel('434344740096442368')
       #print(main.get_channel('434344740096442368'))
       await client.send_message(message.channel, 'OK')
       await client.send_message(main,'Добавлена цель:\n' + goals_list[0],tts=True)

  elif message.content.startswith('!randvk'):
       if message.content.startswith('!randvk bntu'):
        mem=Random_BNTU_Mem()
       if message.content.startswith('!randvk it'):
        mem=Random_IT_Mem()
       else:
        mem=Random_VkMem()
        print(message.channel.name)
        print(message.channel.id)
        print(message.author.id)
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

  elif message.content.startswith('!google'):
       message=message.content[8:]
       res=Google_Search(message)
       print(res)

  elif message.content.startswith('!dice'):
       cube1, cube2 = Dice()
       name=message.author.name
       await client.send_message(message.channel, name+': выпало '+cube1+' и '+cube2)

  elif message.content.startswith('!wolf'):
       question=str(message.content[6:])
       if message.content.startswith('!wolf plot'):
           answer=Plot(question)
       elif message.content.startswith('!wolf solve'):
           answer=Solve(question)
       else: answer = Question(question)
       await client.send_message(message.channel,answer)
  
  elif message.content.startswith('!flip'):
       if random.randint(0,1000)<=453 : ans = 'Орёл'
       else: ans = 'Решка'
       await client.send_message(message.channel,'Выпало: '+ans)

  elif message.author.id=='377142726962970634' and message.content.startswith('Я спать'):
       await client.send_message(message.channel,'Тогда и я пойду')
  
  elif message.content.startswith('%nsf'):
       tag=str(message.content[5:])
       pic=Search_pic(tag)
       await client.send_message(message.channel,pic)
 
client.run(discord_token)
