from discord.ext import commands
import os
import traceback

bot = commands.Bot(
    command_prefix='/'
)
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_message(message):
    if message.content == "/roles":
        await message.channel.send(message.guild.roles)
    elif message.content == "/voice":
        await message.channel.send(discord.VoiceChannel.members)
    elif message.content == "/dm":
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention}さんは狂人に選ばれました")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')






bot.run(token)
