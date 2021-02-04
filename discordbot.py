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
                await dm.send(f"あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、無効試合となるので名乗り出てください\n【勝利条件】インポスター陣営の勝利\n【敗北条件】クルー陣営の勝利")
                await message.channel.send(f"狂人に選ばれた方にDMを送信しました")
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です")
                return
            
    # 狂人複数on
    elif message.content == "/mad_randam":
        if message.author.voice is None:
            await message.channel.send(f"ボイスチャンネルに接続してからコマンドを入力してください")
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 1:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名")
                # member_listからランダムな1ユーザを選択し、DMを送信する
                rnd = random.randint(1,2)
                await message.channel.send(rnd)
                rnd = 2
                if rnd == 1:
                    # member_listからランダムな1ユーザを選択し、DMを送信する
                    dm = await random.choice(message.author.voice.channel.members).create_dm()
                    await dm.send(f"あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、狂人は1人欠けた状態となります\n【勝利条件】インポスター陣営の勝利\n【敗北条件】クルー陣営の勝利")
                    await message.channel.send(f"狂人に選ばれた方にDMを送信しました")
                    return
                else:
                    mad_list = random.sample(message.author.voice.channel.members, 2)
                    for i in range(2):
                        dm = await mad_list[i-1].create_dm()
                        await dm.send(f"あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、狂人は1人欠けた状態となります\n【勝利条件】インポスター陣営の勝利\n【敗北条件】クルー陣営の勝利")
                    await message.channel.send(f"狂人に選ばれた方にDMを送信しました")
                    return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です")
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
                await dm.send(f"あなたは「**てるてる**」に選ばれました\nあなたがインポスターの場合、無効試合となるので名乗り出てください\n【勝利条件】あなたが投票で吊られること\n【敗北条件】インポスターにキルされるor他陣営の勝利")
                await message.channel.send(f"てるてるに選ばれた方にDMを送信しました")
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です")
                return

    # DMテストコマンド
    elif message.content == "/test":
        if message.author.voice is None:
            await message.channel.send(f"ボイスチャンネルに接続してからコマンドを入力してください")
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 0:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名")
                # ボイスチャンネル参加者全員にDMを送信する
                for i in message.author.voice.channel.members:
                    dm = await i.create_dm()
                    await dm.send(f"**これはDMのテスト送信です**\n役職に選ばれた場合、このようにDMが送信されます")
                await message.channel.send(f"ボイスチャンネル参加者全員にDMを送信しました")
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です")
                return
            
    # テキストチャットログ削除コマンド
    elif message.content == "/chat_delete":
        if message.author.voice is None:
            await message.channel.send(f"ボイスチャンネルに接続してからコマンドを入力してください")
            return
        else:
            await message.channel.send(f"res")
            # メッセージ取得
            msgs = [msg async for msg in client.logs_from(message.channel)]
            await client.delete_messages(msgs)
            await message.channel.send(f"res1")
            delmsg = await client.send_message(message.channel, '削除が完了しました')
            await sleep(5)
            await message.channel.send(f"res2")
            await client.delete_message(delmsg)
            return

            
bot.run(token)
