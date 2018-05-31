import discord
import asyncio
import apiai, json

aitoken = 'e1100c6da4484ff1bf84812b5d0fec7a'
client = discord.Client()

@client.event
async def on_ready():
 print('Logged on')
 print(client.user.name)
 print(client.user.id)
 print("-------------")

@client.event
async def on_message(message):
 if(message.author.name==client.user.name):
  return
 else:
   request=apiai.ApiAI(aitoken).text_request()
   request.lang='ru'
   request.session_id='MyVKbot'
   request.query=message.content

   responseJson=json.loads(request.getresponse().read().decode('utf-8'))
   response=responseJson['result']['fulfillment']['speech']
   if response :
      await client.send_message(message.channel, response)
   else: 
      await client.send_message(message.channel, 'Прости,не понял тебя...')


client.run('NDI1Njk5NDM5NTk3MDYwMDk2.DZVeoA.ErWcwG-mu7w6a9IfaJCPUOSyOwo')
