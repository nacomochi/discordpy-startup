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
    elif message.content == "/voice":
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません")
            return
        else:
            # コマンド入力者の接続しているボイスチャンネルのmember_listを取得する
            await message.channel.send(message.author.voice.channel.name)
            member_list = await message.author.voice.channel.members
            await message.channel.send(member_list)
            # member_listからランダムな1ユーザを選択し、DMを送信する
            dm = await random.choice(member_list).create_dm()
            await dm.send(f"{message.author.mention}さんは狂人に選ばれました")
            await message.channel.send("DMを送信しました")
    elif message.content == "/dm":
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんは狂人に選ばれました")
        await message.channel.send("DMを送信しました")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    

bot.run(token)
