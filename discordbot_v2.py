import discord
import asyncio
import pickle
import os
import requests
import json
from discord.ext import commands
from datetime import datetime

discription = 'LOL'
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
 print('Logged on')
 print(bot.user.name)
 print(bot.user.id)
 print("-------------")

@bot.command()
async def add(left: int, right: int):
  """Сложить два числа"""
  await bot.say(left+right)
@bot.command 
async def goals():
 """Открывает список текущих целей"""
 try:
      f=open('discordbot/goals.txt','r')
      mp=f.read();
      f.close
      await client.send_message(message.channel,mp)
 except:
      f=open('discordbot/logs.txt','a')
      f.write(time+' Ошибка работы с командой !goals')
      f.close

bot.run('NDI1Njk5NDM5NTk3MDYwMDk2.DZVeoA.ErWcwG-mu7w6a9IfaJCPUOSyOwo')

