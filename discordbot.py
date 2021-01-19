from discord.ext import commands
import os
import traceback

bot = commands.Bot(
    command_prefix='/'
    activity=discord.Game("AmongUs")
)
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
async def on_message(message):
    if message.content == "/roles":
        await message.channel.send(message.guild.roles)
    elif message.content == "!dm":
        dm = await message.author.create_dm()
        await dm.send(f"{message.author.mention} to dm")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')






bot.run(token)
