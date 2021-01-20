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
            if 10 >= len(message.author.voice.channel.members) > 0:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名")
                # member_listからランダムな1ユーザを選択し、DMを送信する
                dm = await random.choice(message.author.voice.channel.members).create_dm()
                await dm.send(f"あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、狂人はいないことになります\n【勝利条件】インポスター陣営の勝利\n【敗北条件】クルー陣営の勝利")
                await message.channel.send(f"狂人に選ばれた方にDMを送信しました")
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nボイスチャンネルの参加人数が不適切です")
                return
            
    # てるてるon
    elif message.content == "/teru":
        if message.author.voice is None:
            await message.channel.send(f"ボイスチャンネルに接続してからコマンドを入力してください")
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 0:
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名")
                # member_listからランダムな1ユーザを選択し、DMを送信する
                dm = await random.choice(message.author.voice.channel.members).create_dm()
                await dm.send(f"あなたは「**てるてる**」に選ばれました\nあなたがインポスターの場合、てるてるはいないことになります\n【勝利条件】あなたが投票で吊られること\n【敗北条件】インポスターにキルされるor他陣営の勝利")
                await message.channel.send(f"てるてるに選ばれた方にDMを送信しました")
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nボイスチャンネルの参加人数が不適切です")
                return


bot.run(token)
