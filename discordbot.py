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


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

    
def get_data(message):
    command = message.content
    data_table = {
        '/members': message.guild.members,
        '/roles': message.guild.roles,
        '/text_channels': message.guild.text_channels,
        '/voice_channels': message.guild.voice_channels,
        '/category_channels': message.guild.categories,
    }
    return data_table.get(command, 'not command')



@bot.event
async def on_message(message):
    if message.content == "/roles":
        await message.channel.send(message.guild.roles)


bot.run(token)
