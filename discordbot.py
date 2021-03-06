import discord
import os
import traceback
import random
import asyncio
from discord.ext import commands
from discord.ext import tasks

bot = commands.Bot(
    command_prefix='/'
)

token = os.environ['DISCORD_BOT_TOKEN']

    
# 接続に必要なオブジェクトを生成
client = discord.Client()


# 指定間隔(60秒に1回)で実行
@tasks.loop(seconds=60)
async def change_activity():
    # botのステータスを変更
    activity = discord.Activity(name='セキュリティカメラ', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)    
    
    
# tasks.loop の開始直前に実行
@change_activity.before_loop
async def before_change_activity():
    # botがログインするまで(on_readyが発火するまで）待機
    await client.wait_until_ready()


# tasks.loop を開始
change_activity.start()



# コマンド受信時に動作する処理
@client.event
async def on_message(message):

    # 説明文作成
    read_me = """【**AmongUs-DMbotコマンド**】
    /mad_1  :  参加者から狂人1名をランダムに選択
    /mad_2  :  参加者から狂人2名をランダムに選択
    /mad_randam  :  参加者から狂人1or2名をランダムに選択
    /mad_3  :  参加者から狂人3名をランダムに選択
    /teru_1  :  参加者からてるてる1名をランダムに選択
    /dm_test  :  参加者全員にDMのテスト送信を行う
    /chat_delete  :  amongus-dmbotテキストチャットのログを全て削除
    /status  :  botの起動状態を確認
    /command  :  botのコマンドリストを表示
    /read_me  :  botの説明文を表示

    [備考]
    **月550時間までしか稼働できないためBOTがオフラインの場合があります**
    ゲーム内に干渉するMODとは別物で、ゲーム自体には一切干渉しません
    コマンド実行者のロールに関わらず使用可能です
    DM送信時にbotから表示された参加人数がボイスチャンネル内の人数と一致しない場合、
    チャンネル内の全員が一度通話に入りなおすことで解消されます


【**使用方法**】
    1. ボイスチャンネルに参加する(2~10人以内であること)
    2. テキストチャンネルに使用したいコマンドを入力する
    3. 役職に選ばれたユーザにのみbotからDMが送信される


【**狂人について**】
    ボイスチャンネル参加者の中からbotがランダムに選出します
    狂人の人数は入力したコマンドによって変動します
    /mad_1  :  狂人1名固定
    /mad_2  :  狂人2名固定（重複なし）
    /mad_randam  :  狂人1名もしくは2名のランダム（重複なし）
    /mad_3  :  狂人3名固定（重複なし）

    [勝利条件]
    インポスターの勝利（狂人の生死を問わず）
    
    [敗北条件]
    クルーメイトの勝利（狂人の生死を問わず）

    [備考]
    ・インポスターも狂人も互いを認知できない状態から始まります
    ・狂人は生存時にクルーメイト同様タスクをこなしますが、任意のショートタスクを1つ残しタスク勝利を妨害できます
    ・狂人が幽霊になった場合、残したタスクを必ず消化しなければなりません
    ・狂人に選ばれたプレイヤーがインポスターとなった場合、狂人欠けの状態となります
    ・狂人のCO（カミングアウト）やPP（パワープレイ）は問題ありません
    ・クルーメイトによる狂人騙りも問題ありません
    ・狂人2名以上のルールの場合、明らかな吊り日に狂人がスキップに投票することはできません（無投票は可）
    
    
【**てるてるについて**】
    ボイスチャンネル参加者の中からbotがランダムに1名選出します

    [勝利条件]
    てるてるが「投票で吊られる」と試合が終了し、てるてるの1人勝ちとなります
    
    [敗北条件]
    ・てるてるがインポスターにキルされる
    ・投票で吊られずに「クルーメイトorインポスターが勝利する」と敗北

    [備考]
    ・てるてるの勝利画面が存在しないため使用は推奨しません
    ・てるてるは生存時にクルーメイト同様タスクをこなさなければなりません
    ・てるてるに選ばれたプレイヤーがインポスターとなった場合、てるてる欠けの状態となります
    ・てるてるのCO(カミングアウト)は問題ありません
    ・クルーメイトによるてるてる騙りも問題ありません
    
    
【**Credit**】
    bot制作 : なこもち (TwiiterID : nacomochio)
    last_update : 2021/02/27"""


    # メッセージの送信者がbotだった場合は無視する
    if message.author.bot:
        return


    # 狂人1名固定on
    elif message.content == '/mad_1':
        if message.author.voice is None:
            await message.channel.send(f'ボイスチャンネルに接続した状態でコマンドを入力してください')
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 0:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名')
                # member_listからランダムな1ユーザを選択し、DMを送信する
                dm = await random.choice(message.author.voice.channel.members).create_dm()
                await dm.send(f'あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、無効試合となるので名乗り出てください\n【勝利条件】インポスターの勝利\n【敗北条件】クルーメイトの勝利\n- - - - -')
                await message.channel.send(f'狂人に選ばれた方1名にDMを送信しました')
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です\n1~10人の状態でコマンドを実行してください')
                return


    # 狂人2名固定on
    elif message.content == '/mad_2':
        if message.author.voice is None:
            await message.channel.send(f'ボイスチャンネルに接続した状態でコマンドを入力してください')
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 1:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名')
                # member_listからランダムな2ユーザを選択し、DMを2通送信する
                mad_list = random.sample(message.author.voice.channel.members, 2)
                for i in range(2):
                    dm = await mad_list[i-1].create_dm()
                    await dm.send(f'あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、狂人は1人欠けた状態となります\n【勝利条件】インポスターの勝利\n【敗北条件】クルーメイトの勝利\n- - - - -')
                await message.channel.send(f'狂人に選ばれた方2名にDMを送信しました')
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です\n2~10人の状態でコマンドを実行してください')
                return


    # 狂人1or2名on
    elif message.content == '/mad_randam':
        if message.author.voice is None:
            await message.channel.send(f'ボイスチャンネルに接続した状態でコマンドを入力してください')
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 1:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名')
                # 狂人の人数をランダムに選択する
                rnd = random.randint(1,2)
                # 狂人1名の場合
                if rnd == 1:
                    # member_listからランダムな1ユーザを選択し、DMを送信する
                    dm = await random.choice(message.author.voice.channel.members).create_dm()
                    await dm.send(f'あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、狂人は1人欠けた状態となります\n【勝利条件】インポスターの勝利\n【敗北条件】クルーメイトの勝利\n- - - - -')
                    # 処理時間で人数が推測できないように処理を遅延
                    await asyncio.sleep(2)
                    await message.channel.send(f'狂人に選ばれた方にDMを送信しました')
                    return
                # 狂人2名の場合
                else:
                    # member_listからランダムな2ユーザを選択し、DMを2通送信する
                    mad_list = random.sample(message.author.voice.channel.members, 2)
                    # デバック用mad_list表示
                    # await message.channel.send(mad_list)
                    for i in range(2):
                        dm = await mad_list[i-1].create_dm()
                        await dm.send(f'あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、狂人は1人欠けた状態となります\n【勝利条件】インポスターの勝利\n【敗北条件】クルーメイトの勝利\n- - - - -')
                    # 処理時間で人数が推測できないように処理を遅延
                    await asyncio.sleep(1)
                    await message.channel.send(f'狂人に選ばれた方にDMを送信しました')
                    return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です\n2~10人の状態でコマンドを実行してください')
                return


    # 狂人3名固定on
    elif message.content == '/mad_3':
        if message.author.voice is None:
            await message.channel.send(f'ボイスチャンネルに接続した状態でコマンドを入力してください')
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 2:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名')
                # member_listからランダムな3ユーザを選択し、DMを2通送信する
                mad_list = random.sample(message.author.voice.channel.members, 3)
                for i in range(3):
                    dm = await mad_list[i-1].create_dm()
                    await dm.send(f'あなたは「**狂人**」に選ばれました\nあなたがインポスターの場合、狂人は1人欠けた状態となります\n【勝利条件】インポスターの勝利\n【敗北条件】クルーメイトの勝利\n- - - - -')
                await message.channel.send(f'狂人に選ばれた方3名にDMを送信しました')
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です\n3~10人の状態でコマンドを実行してください')
                return


    # てるてるon
    elif message.content == '/teru_1':
        if message.author.voice is None:
            await message.channel.send(f'ボイスチャンネルに接続した状態でコマンドを入力してください')
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 0:
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名')
                # member_listからランダムな1ユーザを選択し、DMを送信する
                dm = await random.choice(message.author.voice.channel.members).create_dm()
                await dm.send(f'あなたは「**てるてる**」に選ばれました\nあなたがインポスターの場合、てるてるは欠けた状態となります\n【勝利条件】あなたが投票で吊られること\n【敗北条件】インポスターにキルされるor他陣営の勝利\n- - - - -')
                await message.channel.send(f'てるてるに選ばれた方にDMを送信しました')
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です\n1~10人の状態でコマンドを実行してください')
                return


    # DMテストコマンド
    elif message.content == '/dm_test':
        if message.author.voice is None:
            await message.channel.send(f'ボイスチャンネルに接続した状態でコマンドを入力してください')
            return
        else:
            if 10 >= len(message.author.voice.channel.members) > 0:
                # コマンド入力者の接続しているボイスチャンネルのメンバーを取得する
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名')
                # ボイスチャンネル参加者全員にDMを送信する
                for i in message.author.voice.channel.members:
                    dm = await i.create_dm()
                    await dm.send(f'**これはDMのテスト送信です**\nあなたが役職に選ばれた場合、このようにbotからDMが届きます\n- - - - -')
                await message.channel.send(f'ボイスチャンネル参加者全員にDMをテスト送信しました')
                return
            else:
                # コマンド入力者の接続しているボイスチャンネルのメンバー数が規定値にない
                await message.channel.send(f'channel : {message.author.voice.channel.name}\n参加人数 : {len(message.author.voice.channel.members)}名\nDMを送信できませんでした。ボイスチャンネルの参加人数が不適切です\n1~10人の状態でコマンドを実行してください')
                return


    # bot動作確認コマンド
    elif message.content == '/status':
        await message.channel.send(f'bot起動中です')
        return


    # コマンドリスト表示
    elif message.content == '/command':
        await message.channel.send(f"""【**AmongUs-DMbotコマンド**】(ロールに関わらず使用可能です)
    /mad_1  :  参加者から狂人1名をランダムに選択
    /mad_2  :  参加者から狂人2名をランダムに選択
    /mad_randam  :  参加者から狂人1or2名をランダムに選択
    /mad_3  :  参加者から狂人3名をランダムに選択
    /teru_1  :  参加者からてるてる1名をランダムに選択
    /dm_test  :  参加者全員にDMのテスト送信を行う
    /chat_delete  :  amongus-dmbotテキストチャットのログを全て削除
    /status  :  botの起動状態を確認
    /command  :  botのコマンドリストを表示
    /read_me  :  botの説明文を表示""")
        return


    # readme表示
    elif message.content == '/read_me':
        await message.channel.send(read_me)
        return


    # 隠しコマンド
    elif message.content == 'よしおちゃん天才って言って':
        rnd = random.randint(1,3)
        if rnd == 1:
            await message.channel.send(f'ﾖｼｵﾁｬﾝﾃﾝｻｲﾔｯﾀｰ!!!<:aupurple:787851727821996042>')
        elif rnd == 2:
            await asyncio.sleep(1)
            await message.channel.send(f'こ ろ す ぞ <:aupurple:787851727821996042>')
        else:
            await message.channel.send(f'Yoshio is an Impostor.<:aupurpledead:787851743399641091>')
        return


    # 隠しコマンド
    elif message.content == 'よしおさんに投票します':
        rnd = random.randint(1,3)
        if rnd == 1:
            await message.channel.send(f'<:aupurple:787851727821996042><じゃあ、なこもちに入れます')
        elif rnd == 2:
            await message.channel.send(f'Yoshio is an Impostor.<:aupurpledead:787851743399641091>')
        else:
            await message.channel.send(f'Yoshio is not an Impostor.<:aupurpledead:787851743399641091>')
        return


    # 隠しコマンド
    elif message.content == 'がめんさんに投票します':
        rnd = random.randint(1,3)
        if rnd == 1:
            await message.channel.send(f'Gamen is an old man.:older_man:')
        elif rnd == 2:
            await message.channel.send(f'<:auwhite:787851726308376606><Nuts to you!')
        else:
            await message.channel.send(f'<:auwhitedead:787851742577688597>')
        return


    # 隠しコマンド
    elif message.content == 'ばななさんに投票します':
        rnd = random.randint(1,3)
        if rnd == 1:
            await message.channel.send(f'<:aupink:787851721182543922><えぇ～わからんーーー:sob:')
        elif rnd == 2:
            await message.channel.send(f'<:aupink:787851721182543922><ﾋﾟｰ!ﾋﾟﾋﾟﾋﾟｰ!!!:scream:')
        else:
            await message.channel.send(f'<:aupinkdead:787851737360629800><ﾋﾟｰ...ﾋﾟｰ...:pensive:')
        return


    # テキストチャットログ削除コマンド
    elif message.content == '/chat_delete':
        if message.channel.name != 'amongus-dmbot':
            await message.channel.send(f'テキストチャンネル名がamongus-dmbotではありません')
            return
        else:
            await message.channel.send(f'このテキストチャンネルのログを全て削除します')
            await asyncio.sleep(5)
            await message.channel.purge()
            await message.channel.send(read_me)
            return


client.run(token)
