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
    
    
    # 狂人1名固定on
    elif message.content == "/mad_1":
        if message.author.voice is None:
            await message.channel.send(f"ボイスチャンネルに接続してからコマンドを入力してください")
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 0:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名")
                # member_listからランダムな1ユーザを選択し、DMを送信する
                dm = await random.choice(message.author.voice.channel.members).create_dm()
                await dm.send(f"あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、無効試合となるので名乗り出てください\n【勝利条件】インポスターの勝利\n【敗北条件】クルーメイトの勝利")
                await message.channel.send(f"狂人に選ばれた方1名にDMを送信しました")
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です")
                return
            
            
    # 狂人2名固定on
    elif message.content == "/mad_2":
        if message.author.voice is None:
            await message.channel.send(f"ボイスチャンネルに接続してからコマンドを入力してください")
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 1:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名")
                # member_listからランダムな2ユーザを選択し、DMを2通送信する
                mad_list = random.sample(message.author.voice.channel.members, 2)
                for i in range(2):
                    dm = await mad_list[i-1].create_dm()
                    await dm.send(f"あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、狂人は1人欠けた状態となります\n【勝利条件】インポスターの勝利\n【敗北条件】クルーメイトの勝利")
                await message.channel.send(f"狂人に選ばれた方2名にDMを送信しました")
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です")
                return
            
            
    # 狂人1or2名on
    elif message.content == "/mad_randam":
        if message.author.voice is None:
            await message.channel.send(f"ボイスチャンネルに接続してからコマンドを入力してください")
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 1:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名")
                # 狂人の人数をランダムに選択する
                rnd = random.randint(1,2)
                # 狂人1名の場合
                if rnd == 1:
                    # member_listからランダムな1ユーザを選択し、DMを送信する
                    dm = await random.choice(message.author.voice.channel.members).create_dm()
                    await dm.send(f"あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、狂人は1人欠けた状態となります\n【勝利条件】インポスターの勝利\n【敗北条件】クルーメイトの勝利")
                    await asyncio.sleep(2)
                    await message.channel.send(f"狂人に選ばれた方にDMを送信しました")
                    return
                # 狂人2名の場合
                else:
                    # member_listからランダムな2ユーザを選択し、DMを2通送信する
                    mad_list = random.sample(message.author.voice.channel.members, 2)
                    for i in range(2):
                        dm = await mad_list[i-1].create_dm()
                        await dm.send(f"あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、狂人は1人欠けた状態となります\n【勝利条件】インポスターの勝利\n【敗北条件】クルーメイトの勝利")
                    await message.channel.send(f"狂人に選ばれた方にDMを送信しました")
                    return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f"channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です")
                return
            
            
    # てるてるon
    elif message.content == "/teru_1":
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
    elif message.content == "/dm_test":
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
    elif message.content == "/status":
        await message.channel.send(f"bot起動中です")
        await message.channel.send(message.author.channel)
        return
            
        
    # テキストチャットログ削除コマンド
    elif message.content == "/chat_delete":
        if message.author.voice is None:
            await message.channel.send(f"ボイスチャンネルに接続してからコマンドを入力してください")
            return
        else:
            if message.author.guild_permissions.administrator:
                await message.channel.purge()
                await message.channel.send("""【**AuteMutebotコマンド**】
    .au new : 起動
    .au e   : 終了

【**AmongUs-DMbotコマンド**】(DMbotは誰でも使用可能です)
    /mad_1       : 参加者から狂人1名をランダムに選択
    /mad_2       : 参加者から狂人2名をランダムに選択
    /mad_randam  : 参加者から狂人1or2名をランダムに選択
    /teru_1   : 参加者からてるてる1名をランダムに選択
    /dm_test     : 参加者全員にDMのテスト送信
    /status      : botの起動状態を確認
    /chat_delete : テキストチャットログを全て削除


【**狂人について**】
    プレイヤーの中からbotがランダムに選出します
    狂人の人数は入力したコマンドによって変動します
    /mad_1      : 狂人1名固定
    /mad_2      : 狂人2名固定（重複なし）
    /mad_randam : 狂人1名もしくは2名のランダム（重複なし）

    [勝利条件]
    インポスターの勝利（狂人の生死を問わず）
    
    [敗北条件]
    クルーメイトの勝利（狂人の生死を問わず）

    [備考]
    ・インポスターも狂人も互いに認知できない状態から始まります
    ・狂人は生存時にクルーメイト同様タスクをこなしますが、任意のショートタスクを一つ残しタスク勝利を妨害できます
    ・残したタスクは幽霊になったら必ず消化しなければなりません
    ・狂人に選ばれたプレイヤーがインポスターとなった場合、狂人1名欠けの状態となります
    
    
【**てるてるについて**】
    プレイヤーの中からbotがランダムに1名選出します

    [勝利条件]
    てるてるが「投票で吊られる」と試合が終了し、てるてるの1人勝ちとなる
    
    [敗北条件]
    ・インポスターにキルされてしまう
    ・投票で吊られずに「クルーメイトorインポスターが勝利する」と敗北

    [備考]
    ・てるてるは生存時にクルーメイト同様タスクをこなさなければなりません
    ・てるてるに選ばれたプレイヤーがインポスターとなった場合、てるてる欠けの状態となります""")
            else:
                await message.channel.send('コマンド入力者の権限が足りていません')
            return

            
bot.run(token)
