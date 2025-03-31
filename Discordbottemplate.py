import discord
from discord.ext import commands

# Create a bot instance with a command prefix
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} and ready to go!")

@bot.command(name="sigma")
async def sigma(ctx):
    await ctx.send("sigma")  


bot.run('put your bot token here')
# have fun!!!!!! 
# much love, SleepyHarp :3