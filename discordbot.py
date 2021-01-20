from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(
    command_prefix='/'
)
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_message(message):
    # メッセージの送信者がbotだった場合は無視する
    if message.author.bot:
        return
    # 狂人on
    elif message.content == "/mad":
        if message.author.voice is None:
            await message.channel.send(f"ボイスチャンネルに接続してからコマンドを入力してください")
            return
        else:
            # コマンド入力者の接続しているボイスチャンネルのmember_listを取得する
            await message.channel.send(f"チャンネル名:{message.author.voice.channel.name}")
            await message.channel.send(f"参加人数:{len(message.author.voice.channel.members)}名")
            # member_listからランダムな1ユーザを選択し、DMを送信する
            dm = await random.choice(message.author.voice.channel.members).create_dm()
            await dm.send(f"あなたは狂人に選ばれました")
            await message.channel.send(f"DMを送信しました")
            
    # てるてるon
    elif message.content == "/teru":
        if message.author.voice is None:
            await message.channel.send(f"ボイスチャンネルに接続してからコマンドを入力してください")
            return
        else:
            # コマンド入力者の接続しているボイスチャンネルのmember_listを取得する
            await message.channel.send(f"チャンネル名:{message.author.voice.channel.name}")
            await message.channel.send(f"参加人数:{len(message.author.voice.channel.members)}名")
            # member_listからランダムな1ユーザを選択し、DMを送信する
            dm = await random.choice(message.author.voice.channel.members).create_dm()
            await dm.send(f"あなたはてるてるに選ばれました")
            await message.channel.send(f"DMを送信しました")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    

bot.run(token)
