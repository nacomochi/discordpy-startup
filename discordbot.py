from discord.ext import commands
import os
import traceback
import random
import asyncio

bot = commands.Bot(
    command_prefix='/'
)
token = os.environ['DISCORD_BOT_TOKEN']

# @client.event
# activity = discord.Activity(name='Amongus', type=discord.ActivityType.watching)
# await client.change_presence(activity=activity)

# 接続に必要なオブジェクトを生成
# client = discord.Client()

# 起動時に動作する処理
# @client.event
# async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
#     await message.channel.send(f"ログインしました")
#     return


@bot.event
async def on_message(message):
    
    #説明文作成
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
    last_update : 2021/02/17"""
    
    
    # メッセージの送信者がbotだった場合は無視する
    if message.author.bot:
        return
    
            
    # bot動作確認コマンド
    elif message.content == "/status":
        await message.channel.send(f"bot起動中です")
        return
    

bot.run(token)
