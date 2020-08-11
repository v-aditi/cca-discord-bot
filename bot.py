from discord.ext import commands
import portfolios

bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    print('Logged on as', bot.user)

@bot.command()
async def publications(ctx):
    await ctx.send(portfolios.PUBLICATIONS)

@bot.command()
async def sponsorship(ctx):
    await ctx.send(portfolios.SPONSORSHIP)

@bot.command()
async def marketing(ctx):
    await ctx.send(portfolios.MARKETING)

@bot.command()
async def technology(ctx):
    await ctx.send(portfolios.TECHNOLOGY)

@bot.command()
async def admin(ctx):
    await ctx.send(portfolios.ADMIN)

@bot.command()
async def events(ctx):
    await ctx.send(portfolios.EVENTS)

bot.run(TOKEN)


