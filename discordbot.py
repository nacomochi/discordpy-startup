from discord.ext import commands
import os
import traceback

bot = commands.Bot(
    command_prefix='/'
)
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_message(message):
    # メッセージの送信者がbotだった場合は無視する
    if message.author.bot:
        return
    elif message.content == "/roles":
        await message.channel.send(message.guild.roles)
    elif message.content == "/voice":
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        else:
            channel = discord.utils.get(guild.voice_channels, name="AmongUs")
            await message.channel.send(guild.voice_channels)
    elif message.content == "/dm":
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんは狂人に選ばれました")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')






bot.run(token)
