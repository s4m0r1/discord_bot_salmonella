import os
import requests
import discord
from os.path import join, dirname
from dotenv import load_dotenv

#環境変数読み込み
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ.get("TOKEN")

client = discord.Client()

log_channel_id = 632817156022730782
ueki_channel_id = 632987047350501377

@client.event
async def on_ready():
    channel_id = 632987047350501377
    channel = client.get_channel(channel_id)
    await channel.send('うえきちゃんが起動しました')
    # await client.send_messege


@client.event
async def on_message(message):
    print(message)
    if message.author.bot:
        return
    if message.content == '/ueki':
        await message.channel.send('うえきちゃんです')
    elif message.content == '/chinpo':
        await message.channel.send('チンポ～～～～～～～～～～')

    

@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel(log_channel_id)

    # afterの中身がNoneであれば退室、afterのチャンネルネームとbeforeのチャンネルネームが同じであればミュート判定
    if after.channel == None:
        await channel.send(member.name + " が死にました")
    elif after.channel == before.channel:
        if after.self_mute:
            await channel.send(member.name + " がミュートしました")
        elif after.self_mute == False:
            await channel.send(member.name + " がミュートを解除しました")
        return
    else: 
        await channel.send(member.name + " が" + after.channel.name + " に入室しました")

client.run(TOKEN)

