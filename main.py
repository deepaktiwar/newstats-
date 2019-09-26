import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType

client = Bot(description="DarkBot Bot is best", command_prefix="d!", pm_help = True)
client.remove_command('help')


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(type=1,name='with ⎝⧹𝗗𝗿. BOSS™╱⎠'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name="With No girl friend"))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='DREAM WORLD TRIVIA',type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name=' your love and affection'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name=f'{len(client.servers)} servers'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name=f'with {len(set(client.get_all_members()))}users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(type=1,name='with your mom and sister!'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='PUGE  MOBILE',type=2))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='UNITED KINGDOM TRIVIA',type=3))
        await asyncio.sleep(5)


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('ansh arya')
    print('Created by ansh arya')
    client.loop.create_task(status_task())



client.run("NTMxMzUzMjgxMTU5NDk1Njgx.XYwtKQ.kRQStC2TGRTv9At_0XohFUInwgY", bot=False)
